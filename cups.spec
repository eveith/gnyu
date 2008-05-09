Name: cups
Version: 1.3.7
Release: 3ev
Summary: Common Unix Printing System
URL: http://www.cups.org/
Group: System Environment/Daemons
License: GPL-2
Vendor: GNyU-Linux
Source0: ftp://ftp.easysw.com/pub/cups/%{version}/cups-%{version}-source.tar.bz2
Source1: cups-cupsd.i
Source8: postscript.ppd.gz
Source13: pdftops.conf
Patch2: cups-no-gzip-man.patch
Patch3: cups-1.1.16-system-auth.patch
Patch5: cups-ext.patch
Patch6: cups-includeifexists.patch
Patch7: cups-banners.patch
Patch8: cups-logfileperm.patch
Patch9: cups-1.1.17-rcp.patch
Patch10: cups-1.1.17-ppdsdat.patch
Patch12: cups-locale.patch
Patch13: cups-CAN-2005-0064.patch
Patch17: cups-serverbin-compat.patch
Patch18: cups-language.patch
Patch20: cups-direct-usb.patch
Patch22: cups-dest-cache-v2.patch
Patch24: cups-maxlogsize.patch
Patch28: cups-no-propagate-ipp-port.patch
Patch32: cups-pid.patch
Patch41: cups-relro.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: coreutils, grep, sed, make >= 3.80, gcc, gcc-g++, pkg-config
BuildRequires: libjpeg, libpng, libtiff, libpam, heimdal-libs, openldap-libs
BuildRequires: pcre, perl, dbus >= 0.60, openslp, gnutls, zlib
Requires: perl
Provides: %{_bindir}/lpq, /usr/bin/lpr, /usr/bin/lp, /usr/bin/cancel 
Provides: %{_bindir}/lprm, /usr/bin/lpstat
Provides: lpd, lpr, LPRng = 3.8.15-3
Conflicts: foomatic < 3.0.2-33.3
Conflicts: hplip < 0.9.9-5.1
Obsoletes: lpd, lpr, LPRng <= 3.8.15-3
%define _lp_uid 4
%define _lp_gid 7

%description
The Common UNIX Printing System provides a portable printing layer for 
UNIX® operating systems. It has been developed by Easy Software Products 
to promote a standard printing solution for all UNIX vendors and users. 
CUPS provides the System V and Berkeley command-line interfaces. 


%package libs
Version: %{version}
Summary: Libraries for the Common Unix Printing System
Group: System Environment/Libraries

%description libs
The Common UNIX Printing System provides a portable printing layer for
UNIX® operating systems like BSD lp or lprng. CUPS provides some
additional features. This package contains libraries needed by CUPS and
some other packages.



%prep
%setup -q -n %{name}-%{version}


%build
%configure \
	--with-cups-user=lp \
	--with-cups-group=lp \
	--with-logdir=/%{_var}/log/cups \
	--enable-dbus \
	--enable-jpeg \
	--enable-png \
	--enable-tiff \
	--enable-slp \
	--enable-ldap \
	--enable-openssl \
	--disable-gnutls \
	--enable-pam \
	--enable-threads \
	--disable-dnssd \
	--disable-launchd \
	--with-optim="${RPM_OPT_FLAGS} ${CFLAGS}" \
	--with-perl
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/initng/daemon'

# Install init file
%{__make_install} BUILDROOT='%{buildroot}'
%{__cat} %{SOURCE1} | \
	%{__sed} -e 's,@cupsd@,%{_sbindir}/cupsd,g' \
	> '%{buildroot}/etc/initng/daemon/cupsd.i'

%{__install} -c -m 0644 '%{SOURCE13}' \
	'%{buildroot}/%{_sysconfdir}/cups/pdftops.conf'

# Ship a generic postscript PPD file (#73061)
%{__install} -c -m 0644 '%{SOURCE8}' '%{buildroot}/%{_datadir}/cups/model'


# Ship a printers.conf file, and a client.conf file.  That way, they get
# their SELinux file contexts set correctly.
touch '%{buildroot}/%{_sysconfdir}/cups/printers.conf' \
	'%{buildroot}/%{_sysconfdir}/cups/client.conf'


# Remove unshipped files
%{__rm} -rf \
	'%{buildroot}/%{_mandir}'/cat? \
	'%{buildroot}/%{_mandir}'/*/cat? \
	'%{buildroot}/%{_datadir}/applications/cups.desktop' \
	'%{buildroot}/%{_datadir}/icons' \
	'%{buildroot}/etc'/{init.d,rc?.d}


%pre
{
	groupadd \
		-g '%{_lp_gid}' \
		lp
	useradd \
		-u '%{_lp_uid}' \
		-g '%{_lp_gid}' \
		-c 'Printer Spooler' \
		-d '%{_localstatedir}/spool/cups' \
		-s /sbin/nologin \
		lp
} > /dev/null 2>&1
exit 0

%preun
if [[ "${1}" -eq 0 ]]
then
	ngc -d cupsd
	ng-update del daemon/cupsd default
fi > /dev/null 2>&1
exit 0

%postun
if [[ "${1}" -eq 0 ]]
then
	userdel lp
	groupdel lp
fi > /dev/null 2>&1
exit 0

%post libs
/sbin/ldconfig

%postun libs
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-,root,root)
%doc *.txt
%{_sysconfdir}/initng/daemon/cupsd.i
%{_sysconfdir}/dbus-1/system.d/cups.conf
%config(noreplace) %{_sysconfdir}/pam.d/cups
%dir %attr(0755, root, lp) %{_sysconfdir}/cups
%dir %attr(0755, root, lp) %{_localstatedir}/run/cups
%dir %attr(0511, lp, sys) %{_localstatedir}/run/cups/certs
%config(noreplace) %attr(0640, root, lp) %{_sysconfdir}/cups/cupsd.conf
%attr(0640, root, lp) %{_sysconfdir}/cups/cupsd.conf.default
%config(noreplace) %attr(0644, root, lp) %{_sysconfdir}/cups/client.conf
%config(noreplace) %attr(0600, root, lp) %{_sysconfdir}/cups/printers.conf
%config(noreplace) %attr(0644, root, lp) %{_sysconfdir}/cups/pdftops.conf
%config(noreplace) %attr(0644, root, lp) %{_sysconfdir}/cups/snmp.conf
%config(noreplace) %{_sysconfdir}/cups/mime.types
%config(noreplace) %{_sysconfdir}/cups/mime.convs
%dir %attr(0755, root, lp) %{_sysconfdir}/cups/ppd
%dir %attr(0700, root, lp) %{_sysconfdir}/cups/ssl
%{_sysconfdir}/cups/interfaces
%{_bindir}/cups*
%{_bindir}/cancel*
%{_bindir}/lp*
%{_sbindir}/*
%{_libdir}/cups/
%{_includedir}/cups
%{_mandir}/man?/*
%dir %{_datadir}/cups
%dir %{_datadir}/cups/banners
%config(noreplace) %{_datadir}/cups/banners/*
%{_datadir}/cups/charsets
%{_datadir}/cups/charmaps
%{_datadir}/cups/data
%{_datadir}/cups/fonts
%{_datadir}/cups/model
%{_datadir}/cups/templates
%{_datadir}/locale/*/*
%{_datadir}/doc/cups/
%dir %attr(1770, root, lp) /var/spool/cups/tmp
%dir %attr(0710, root, lp) /var/spool/cups
%dir %attr(0755, lp, sys) /var/log/cups

%files libs
%{_libdir}/libcupsimage.*
%{_libdir}/libcups.*
