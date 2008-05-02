Summary: Common Unix Printing System
Name: cups
Version: 1.2.12
Release: 1ev
License: GPL
Group: System Environment/Daemons
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
Url: http://www.cups.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: gcc-g++, make >= 3.80, libjpeg, libpng, libtiff, libpam,
BuildRequires: pkg-config, aspell, pcre, perl, dbus >= 0.60, openslp
BuildRequires: openldap-libs
Requires: dbus >= 0.60, libjpeg, libtiff, libpng, libpam, perl
Provides: /usr/bin/lpq, /usr/bin/lpr, /usr/bin/lp, /usr/bin/cancel 
Provides: /usr/bin/lprm, /usr/bin/lpstat
Provides: lpd lpr LPRng = 3.8.15-3
Conflicts: foomatic < 3.0.2-33.3
Conflicts: hplip < 0.9.9-5.1
Obsoletes: lpd lpr LPRng <= 3.8.15-3

%description
The Common UNIX Printing System provides a portable printing layer for 
UNIX® operating systems. It has been developed by Easy Software Products 
to promote a standard printing solution for all UNIX vendors and users. 
CUPS provides the System V and Berkeley command-line interfaces. 


%prep
%setup -q -n %{name}-%{version}
%patch2 -p1 -b .no-gzip-man
%patch3 -p1 -b .system-auth
%patch5 -p1 -b .ext
%patch6 -p1 -b .includeifexists
%patch7 -p1 -b .banners
%patch8 -p1 -b .logfileperm
%patch9 -p1 -b .rcp
%patch10 -p1 -b .ppdsdat
%patch12 -p1 -b .locale
%patch13 -p1 -b .CAN-2005-0064
%patch17 -p1 -b .serverbin-compat
%patch18 -p1 -b .language
# %patch20 -p1 -b .direct-usb
%patch22 -p1 -b .dest-cache-v2
%patch24 -p1 -b .maxlogsize
%patch28 -p1 -b .no-propagate-ipp-port
%patch32 -p1 -b .pid
%patch41 -p1 -b .relro
perl -pi -e 's,^#(Printcap\s+/etc/printcap),$1,' conf/cupsd.conf.in
aclocal -I config-scripts
autoconf

# Let's look at the compilation command lines.
perl -pi -e "s,^.SILENT:,," Makedefs.in


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
	--enable-pam \
	--enable-threads \
	--with-optim="$RPM_OPT_FLAGS $CFLAGS" \
	--with-perl
make %{_smp_mflags}


%install
[ "$RPM_BUILD_ROOT" != '/' ] && rm -rf "$RPM_BUILD_ROOT"
mkdir -p $RPM_BUILD_ROOT%{initdir}

make BUILDROOT="$RPM_BUILD_ROOT" install 

# Install init file

mkdir -p "$RPM_BUILD_ROOT"/etc/initng/daemon
cat %{SOURCE1} | \
	sed -e 's,@cupsd@,%{_sbindir}/cupsd,g' \
	> "$RPM_BUILD_ROOT"/etc/initng/daemon/cupsd.i

# Gzip PPDs:
find "$RPM_BUILD_ROOT"/usr/share/cups/model -name "*.ppd" |xargs gzip -n9f

install -c -m 644 %{SOURCE13} $RPM_BUILD_ROOT%{_sysconfdir}/cups/pdftops.conf
ln -s ../doc/%{name}-%{version} $RPM_BUILD_ROOT%{_datadir}/%{name}/doc


# Deal with users trying to access the admin tool at
# /usr/share/doc/cups-%{version}/index.html rather than the
# correct http://localhost:631/

for i in admin classes jobs printers
do
	mkdir -p "$RPM_BUILD_ROOT"/"%{_datadir}"/doc/"%{name}"/"$i"

	cat  << __EOF__ > "$RPM_BUILD_ROOT"/"%{_datadir}"/doc/"%{name}"/"$i"/index.html
<?xml version="1.0"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/transitional.dtd">
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="refresh" content="2; URL=http://localhost:631/$i" />
	<title>CUPS $i</title>
</head>
<body bgcolor="#cccc99" text="#000000" link="#0000ff" vlink="#ff00ff">
	<p>You are trying to access the CUPS admin frontend through reading the files.
	The correct way to access the CUPS admin frontend is pointing your browser at
	<a href="http://localhost:631/">http://localhost:631/</a>.</p>
	<p>You should be automatically redirected to the correct URL in 2 seconds.
	If your browser does not support redirection, please use
	<a href="http://localhost:631/$i">this link</a>.</p>
</body>
</html>
__EOF__

done

cat > "$RPM_BUILD_ROOT"/"%{_sysconfdir}"/cups/snmp.conf <<"EOF"
#Address @LOCAL
#Community public
#DebugLevel 0
#HostNameLookups off
EOF

# Ship a generic postscript PPD file (#73061)
install -c -m 644 "%{SOURCE8}" "$RPM_BUILD_ROOT"/"%{_datadir}"/cups/model


# Ship a printers.conf file, and a client.conf file.  That way, they get
# their SELinux file contexts set correctly.
touch "$RPM_BUILD_ROOT"/"%{_sysconfdir}"/cups/printers.conf
touch "$RPM_BUILD_ROOT"/"%{_sysconfdir}"/cups/client.conf


# Remove unshipped files.

rm -rf "$RPM_BUILD_ROOT"/"%{_mandir}"/cat? "$RPM_BUILD_ROOT"/"%{_mandir}"/*/cat?
rm -f "$RPM_BUILD_ROOT"/"%{_datadir}"/applications/cups.desktop
rm -rf "$RPM_BUILD_ROOT"/"%{_datadir}"/icons
rm -rf "$RPM_BUILD_ROOT"/etc/{init.d,rc?.d}


%post
/sbin/ldconfig
if ngc -s | grep 'daemon/cupsd' > /dev/null 2>&1
then
	ngc -r daemon/cupsd ||: > /dev/null 2>&1
fi

%preun
if [ "$1" = "0" ]
then
	/sbin/ngc -d cupsd > /dev/null 2>&1
	/sbin/ng-update del daemon/cupsd > /dev/null 2>&1
fi

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != '/' ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-,root,root)
%doc *.txt
/etc/initng/daemon/cupsd.i
/etc/dbus-1/system.d/cups.conf
%config(noreplace) /etc/pam.d/cups
%dir %attr(0755, root, lp) /etc/cups
%dir %attr(0755, root, lp) /var/run/cups
%dir %attr(0511, lp, sys) /var/run/cups/certs
%config(noreplace) %attr(0640, root, lp) /etc/cups/cupsd.conf
%attr(0640, root, lp) /etc/cups/cupsd.conf.default
%config(noreplace) %attr(0644, root, lp) /etc/cups/client.conf
%config(noreplace) %attr(0600, root, lp) /etc/cups/printers.conf
%config(noreplace) %attr(0644, root, lp) /etc/cups/pdftops.conf
%config(noreplace) %attr(0644, root, lp) /etc/cups/snmp.conf
%config(noreplace) /etc/cups/mime.types
%config(noreplace) /etc/cups/mime.convs
%dir %attr(0755, root, lp) /etc/cups/ppd
%dir %attr(0700, root, lp) /etc/cups/ssl
/etc/cups/interfaces
%{_bindir}/cups*
%{_bindir}/cancel*
%{_bindir}/lp*
%{_sbindir}/*
%{_libdir}/*.so*
%{_libdir}/cups/
%{_includedir}/cups
%{_mandir}/man?/*
%dir %{_datadir}/cups
%dir %{_datadir}/cups/banners
%config(noreplace) %{_datadir}/cups/banners/*
%{_datadir}/cups/charsets
%{_datadir}/cups/charmaps
%{_datadir}/cups/data
%{_datadir}/cups/doc
%{_datadir}/cups/fonts
%{_datadir}/cups/model
%{_datadir}/cups/templates
%{_datadir}/locale/*/*
%{_datadir}/doc/cups/
%dir %attr(1770, root, lp) /var/spool/cups/tmp
%dir %attr(0710, root, lp) /var/spool/cups
%dir %attr(0755, lp, sys) /var/log/cups

%changelog
* Sun Aug 13 2006 Eric MSP Veith <eveith@wwweb-library.net> 1.2.2
- Modified SPEC file to make it fit MSP Slackware
