Name: eglibc
Summary: Standard Shared Libraries (from the GNU C Library)
%define svnrev 12839
Version: 2.13
Release: 6.0
Group: System Environment/Base
License: GPL-2, LGPL-2.1
URL: http://www.eglibc.org/
Source0: %{name}-%{version}.%{svnrev}.tar.bz2
Source1: nscd.ii
Source2: nsswitch.conf
Source3: bindresvport.blacklist
Provides: glibc = %{version}-%{release}
Obsoletes: glibc < %{version}-%{release}
Conflicts: glibc < %{version}-%{release}
#BuildRequires(prep): subversion
BuildRequires: make >= 3.80, gcc >= 4.1, gcc-g++ >= 4.1, binutils >= 2.20
BuildRequires: perl >= 5.8
BuildRequires: texinfo >= 3.12f, gawk >= 3.0, sed >= 3.02, bash >= 2.0
BuildRequires: bison, info, gettext-tools >= 0.17
%define kernel_version 2.6.27
BuildRequires: kernel-headers >= %{kernel_version}
%define run_testsuite 1

%description
The GNU C Library provides the most important standard libraries used
by nearly all programs: the standard C library, the standard math
library, and the POSIX thread library.	A system is not functional
without these libraries.


%package devel
Summary: Header files and tools needed for C development
Group: Development/Libraries
Requires: eglibc = %{version}-%{release}

%description devel
These header files, libraries and tools are needed as soon as one wants to
develop C programs or compile C sources.


%package info
Summary: Info Files for the GNU C Library
Group: Documentation
Requires: /sbin/install-info

%description info
This package contains the documentation for the GNU C library stored as
info files. Due to a lack of resources, this documentation is not
complete and is partially out of date.


%package html
Summary: HTML Documentation for the GNU C Library
Group: Documentation

%description html
This package contains the HTML documentation for the GNU C library. Due
to a lack of resources, this documentation is not complete and is
partially out of date.


%package i18ndata
Summary: Database Sources for 'locale'
Group: System Environment/Base

%description i18ndata
This package contains the data needed to build the locale data files to
use the internationalization features of the GNU libc. It is normally
not necessary to install this packages, the data files are already
created.


%package locale
Summary: Locale Data for Localized Programs
Group: System Environment/Base
Requires: glibc = %{version}

%description locale
Locale data for the internationalisation features of the GNU C library.


%package -n nscd
Summary: Name Service Caching Daemon
Group: System Environemnt/Daemons

%description -n nscd
Nscd caches name service lookups and can dramatically improve
performance with NIS, NIS+, and LDAP.


%package tzdata
Summary: Timezone descriptions
Group: System Environment/Base
Obsoletes: timezone
Requires: glibc = %{version}
Conflicts: glibc > %{version}, glibc < %{version}
AutoReq: on
AutoProv: on

%description tzdata
These are configuration files that describe available time zones. If you want
your clock to display the current time and date in your local time zone, you
have to install this package.
You can set your timezone by copying the apropriate file from
%{_datadir}/zoneinfo to /etc/localtime, e. g. by issuing "cp
/usr/share/zoneinfo/Europe/Berlin /etc/localtime".


%prep
#%setup -Tcq
#svn_branch_version=$(echo %{version} | tr . _)
#svn co "svn://svn.eglibc.org/branches/eglibc-${svn_branch_version}" src
%setup -q
%{__find} . -name 'configure' -exec %{__touch} '{}' \;
%{__mkdir} obj


%build
# Print out some information about the build process. Might be useful.
uname -a
uptime || :
ulimit -a
nice

# Adjust glibc version.h
echo '#define CONFHOST "%{_target_cpu}-gnyu-linux"' >> libc/version.h

# Glibc cares about the CFLAGS. Don't touch them; it might break the library.
unset CFLAGS CXXFLAGS

pushd obj
../libc/configure \
	--build='%{_target_platform}' \
	--host='%{_target_platform}' \
	--prefix='%{_prefix}' \
	--datadir='%{_datadir}' \
	--mandir='%{_mandir}' \
	--infodir='%{_infodir}' \
	--enable-add-ons='libidn,nptl' \
	--srcdir='../libc' \
	--enable-stackguard-randomization \
	--without-cvs \
	--without-selinux \
	--with-tls \
	--with-__thread \
	--enable-kernel='%{kernel_version}' \
	--with-cpu='%{_target_cpu}' \
	--enable-check-abi=warn \
	--with-bugurl='bugs+eglibc@gnyu.org'
%{__make} %{?_smp_mflags}
%{__make} html
popd


%check
pushd obj
%{__make} -k check check-abi ||:
popd


%install
# Make sure we will create the gconv-modules.cache

%{__mkdir_p} '%{buildroot}%{_libdir}/gconv'
%{__touch} '%{buildroot}%{_libdir}/gconv/gconv-modules.cache'

# Create ghost ld.so.cache file

%{__mkdir_p} '%{buildroot}%{_sysconfdir}'
%{__touch} '%{buildroot}%{_sysconfdir}/ld.so.cache'

# Do not install in parallel, timezone Makefile will fail
pushd obj
%{__make} install install_root='%{buildroot}'
%{__make} localedata/install-locales install_root='%{buildroot}'
popd

%find_lang libc

# Adjust /etc/localtime

%{__rm} -f '%{buildroot}/%{_sysconfdir}/localtime'
%{__cp} -f '%{buildroot}/%{_prefix}/share/zoneinfo/UTC' \
	'%{buildroot}/%{_sysconfdir}/localtime'

# Install nscd tools

%{__cp} libc/nscd/nscd.conf '%{buildroot}%{_sysconfdir}'
%{__mkdir_p} '%{buildroot}%{_localstatedir}/run/nscd'
%{__touch} '%{buildroot}%{_localstatedir}/run/nscd/'{passwd,group,hosts}
%{__touch} '%{buildroot}%{_localstatedir}/run/nscd/'{socket,nscd.pid}

# Install nscd startup file

%{__mkdir_p} '%{buildroot}%{_sysconfdir}/initng/daemon'
%{install_ifile '%{SOURCE0}' daemon/nscd.i}

# Install bindresvport.blacklist and default/nss

%{__install} -m 0644 '%{SOURCE2}' \
	'%{buildroot}%{_sysconfdir}/bindresvport.blacklist'
%{__mkdir_p} '%{buildroot}%{_sysconfdir}/default'
%{__install} -m 0644 libc/nis/nss '%{buildroot}%{_sysconfdir}/default'

# Create ld.so.conf
%{__cat} << __EOF > '%{buildroot}%{_sysconfdir}/ld.so.conf'
/%{_lib}
%{_libdir}
/usr/local/%{_lib}
/usr/i586-gnyu-linux/lib
/usr/i686-gnyu-linux/lib
/usr/i586-slackware-linux/lib
/usr/i686-slackware-linux/lib
include /etc/ld.so.conf.d/*
__EOF

%{__mkdir_p} '%{buildroot}%{_sysconfdir}/ld.so.conf.d'

# install nsswitch.conf
%{__install} -m 0644 '%{SOURCE1}' \
	'%{buildroot}%{_sysconfdir}/nsswitch.conf'

# Don't look at it! We don't wish a /bin/sh requires
# Or /usr/bin/perl, for that matter.

for i in '%{_bindir}/ldd' '%{_bindir}/catchsegv' '%{_bindir}/mtrace' \
		'%{_bindir}/xtrace'; do
	%{__chmod} 0644 "%{buildroot}${i}"
done

# Remove not needed files from BuildRoot
%{__rm_rf} '%{buildroot}%{_infodir}/dir'


%post -p <lua>
os.execute("/sbin/ldconfig")


%post info
update-info-dir ||:


%postun info
update-info-dir ||:


%post -n nscd
if [[ "${1}" -eq 0 ]]; then
	ng-update add daemon/nscd default
	ngc -u daemon/nscd
fi
exit 0


%preun -n nscd
if [[ "${1}" -eq 0 ]]; then
	ngc -d daemon/nscd
	ng-update del daemon/nscd default
fi > /dev/null 2>&1 
exit 0


%files
%defattr(-,root,root)
%doc libc/LICENSES libc/ChangeLog* libc/COPYING*
%doc libc/README* libc/CONFORMANCE* libc/FAQ libc/NEWS
%doc libc/NOTES libc/BUGS libc/CANCEL*
%config %attr(0644, root, root) %{_sysconfdir}/ld.so.conf
%dir %{_sysconfdir}/ld.so.conf.d
%attr(0644, root, root) %verify(not md5 size mtime) %ghost %config(missingok, noreplace) %{_sysconfdir}/ld.so.cache
%config(noreplace) %attr(0644, root, root) %{_sysconfdir}/rpc
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/nsswitch.conf
%config(noreplace) %{_sysconfdir}/bindresvport.blacklist
%config(noreplace) %{_sysconfdir}/default/nss
/%{_lib}/ld-%{version}*.so
%ifarch x86_64
/%{_lib}/ld-linux-x86-64.so.2
%else
/%{_lib}/ld-linux.so.2
%endif
/%{_lib}/libBrokenLocale-%{version}*.so
/%{_lib}/libBrokenLocale.so.1
/%{_lib}/libSegFault.so
/%{_lib}/libanl-%{version}*.so
/%{_lib}/libanl.so.1
/%{_lib}/libc-%{version}*.so
/%{_lib}/libc.so.6*
/%{_lib}/libcidn-%{version}*.so
/%{_lib}/libcidn.so.1
/%{_lib}/libcrypt-%{version}*.so
/%{_lib}/libcrypt.so.1
/%{_lib}/libdl-%{version}*.so
/%{_lib}/libdl.so.2*
/%{_lib}/libm-%{version}*.so
/%{_lib}/libm.so.6*
/%{_lib}/libmemusage.so
/%{_lib}/libnsl-%{version}*.so
/%{_lib}/libnsl.so.1
/%{_lib}/libnss_compat-%{version}*.so
/%{_lib}/libnss_compat.so.2
/%{_lib}/libnss_dns-%{version}*.so
/%{_lib}/libnss_dns.so.2
/%{_lib}/libnss_files-%{version}*.so
/%{_lib}/libnss_files.so.2
/%{_lib}/libnss_hesiod-%{version}*.so
/%{_lib}/libnss_hesiod.so.2
/%{_lib}/libnss_nis-%{version}*.so
/%{_lib}/libnss_nis.so.2
/%{_lib}/libnss_nisplus-%{version}*.so
/%{_lib}/libnss_nisplus.so.2
/%{_lib}/libpcprofile.so
/%{_lib}/libpthread-%{version}*.so
/%{_lib}/libpthread.so.0
/%{_lib}/libresolv-%{version}*.so
/%{_lib}/libresolv.so.2
/%{_lib}/librt-%{version}*.so
/%{_lib}/librt.so.1
/%{_lib}/libthread_db-1.0.so
/%{_lib}/libthread_db.so.1
/%{_lib}/libutil-%{version}*.so
/%{_lib}/libutil.so.1
%{__ldconfig}
%{_bindir}/gencat
%{_bindir}/getconf
%{_bindir}/getent
%{_bindir}/iconv
%attr(0755, root, root) %{_bindir}/ldd
%attr(0751, root, root) /sbin/sln
%ifarch %ix86 
%{_bindir}/lddlibc4
%endif
%attr(4711, root, root) %{_libexecdir}/pt_chown
%dir %attr(0755, root, root) %{_libexecdir}/getconf
%{_libexecdir}/getconf/*
%{_sbindir}/rpcinfo
%{_sbindir}/iconvconfig


%files devel
%defattr(-, root, root)
%doc libc/LICENSES libc/ChangeLog* libc/COPYING*
%doc libc/README* libc/CONFORMANCE* libc/FAQ libc/NEWS
%doc libc/NOTES libc/BUGS libc/CANCEL*
%attr(0751, root, root) %{_bindir}/?trace
%{_bindir}/rpcgen
%{_bindir}/sprof
%{_bindir}/pcprofiledump
%attr(0751, root, root) %{_bindir}/catchsegv
%{_libdir}/*.o
%{_libdir}/*.so
%{_libdir}/libBrokenLocale.a
%{_libdir}/libanl.a
%{_libdir}/libbsd-compat.a
%{_libdir}/libc.a
%{_libdir}/libc_nonshared.a
%{_libdir}/libcrypt.a
%{_libdir}/libdl.a
%{_libdir}/libg.a
%{_libdir}/libieee.a
%{_libdir}/libm.a
%{_libdir}/libmcheck.a
%{_libdir}/libnsl.a
%{_libdir}/libpthread.a
%{_libdir}/libpthread_nonshared.a
%{_libdir}/libresolv.a
%{_libdir}/librpcsvc.a
%{_libdir}/librt.a
%{_libdir}/libutil.a
%{_libdir}/libBrokenLocale_pic.a
%{_libdir}/libBrokenLocale_pic.map
%{_libdir}/libanl_pic.a
%{_libdir}/libanl_pic.map
%{_libdir}/libc_pic.a
%{_libdir}/libc_pic.map
%dir %{_libdir}/libc_pic
%{_libdir}/libc_pic/sofini.o
%{_libdir}/libc_pic/soinit.o
%{_libdir}/libcidn_pic.a
%{_libdir}/libcidn_pic.map
%{_libdir}/libcrypt_pic.a
%{_libdir}/libcrypt_pic.map
%{_libdir}/libdl_pic.a
%{_libdir}/libdl_pic.map
%{_libdir}/libm_pic.a
%{_libdir}/libm_pic.map
%{_libdir}/libnsl_pic.a
%{_libdir}/libnsl_pic.map
%{_libdir}/libnss_compat_pic.a
%{_libdir}/libnss_compat_pic.map
%{_libdir}/libnss_dns_pic.a
%{_libdir}/libnss_dns_pic.map
%{_libdir}/libnss_files_pic.a
%{_libdir}/libnss_files_pic.map
%{_libdir}/libnss_hesiod_pic.a
%{_libdir}/libnss_hesiod_pic.map
%{_libdir}/libnss_nis_pic.a
%{_libdir}/libnss_nis_pic.map
%{_libdir}/libnss_nisplus_pic.a
%{_libdir}/libnss_nisplus_pic.map
%{_libdir}/libresolv_pic.a
%{_libdir}/libresolv_pic.map
%{_libdir}/librt_pic.a
%{_libdir}/librt_pic.map
%{_libdir}/libthread_db_pic.a
%{_libdir}/libthread_db_pic.map
%{_libdir}/libutil_pic.a
%{_libdir}/libutil_pic.map
%{_includedir}/*


%files locale -f libc.lang
%defattr(-, root, root)
%{_bindir}/locale
%{_bindir}/localedef
%{_datadir}/locale/locale.alias
%{_libdir}/locale/
%{_libdir}/gconv/


%files info
%defattr(-, root, root)
%doc %{_infodir}/libc.info*


%files html
%defattr(-, root, root)
%doc libc/manual/libc/*.html


%files i18ndata
%defattr(-, root, root)
%{_datadir}/i18n/


%files -n nscd
%defattr(-, root, root)
%attr(0600, root, root) %config(noreplace) %{_sysconfdir}/nscd.conf
%attr(0700, root, root) %{_sysconfdir}/initng/daemon/nscd.i
%{_sbindir}/nscd
%dir %attr(0711, root, root) %{_localstatedir}/run/nscd
%attr(0600, root, root) %verify(not md5 size mtime) %ghost %config(missingok, noreplace) %{_localstatedir}/run/nscd/nscd.pid
%attr(0666, root, root) %verify(not md5 size mtime) %ghost %config(missingok, noreplace) %{_localstatedir}/run/nscd/socket
%attr(0600, root, root) %verify(not md5 size mtime) %ghost %config(missingok, noreplace) %{_localstatedir}/run/nscd/passwd
%attr(0600, root, root) %verify(not md5 size mtime) %ghost %config(missingok, noreplace) %{_localstatedir}/run/nscd/group
%attr(0600, root, root) %verify(not md5 size mtime) %ghost %config(missingok, noreplace) %{_localstatedir}/run/nscd/hosts


%files tzdata
%defattr(-, root, root)
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/localtime
%{_datadir}/zoneinfo/
%{_bindir}/tzselect
%{_sbindir}/zdump
%{_sbindir}/zic
