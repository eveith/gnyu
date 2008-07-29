Name: glibc
Summary: Standard Shared Libraries (from the GNU C Library)
Version: 2.7
Release: 2ev 
Group: System Environment/Base
License: GPL-2, LGPL-2.1
URL: http://www.gnu.org/software/libc/
Source0: http://ftp.gnu.org/gnu/glibc/glibc-%{version}.tar.bz2
Source1: http://ftp.gnu.org/gnu/glibc/glibc-libidn-%{version}.tar.bz2
Source2: %{name}-nscd.i
Source3: %{name}-noversion.tar.bz2
Source4: %{name}-manpages.tar.bz2
Source8: %{name}-nsswitch.conf
Source10: %{name}-bindresvport.blacklist
Patch1: glibc-2.3.90-noversion.diff
Patch3: resolv.dynamic.diff
Patch4: glibc-2.3.locales.diff.bz2
Patch10: glibc-2.3-regcomp.diff
Patch14: glibc-2.3.2.no_archive.diff
Patch17: glibc-2.3.90-bindresvport.blacklist.diff
Patch26: glibc-2.3.4-gb18030-big5hkscs.diff.bz2
Patch29: glibc-2.3.5-nscd-zeronegtimeout.diff
BuildRequires: coreutils, grep, sed, make, gcc, gcc-g++, libstdc++, libgcc_s
BuildRequires: findutils, gettext, gawk, perl, bison, autoconf
PreReq: fhs
BuildRoot: %{_tmppath}/%{name}-buildroot
%define run_testsuite 1
%define disable_assert 0
%define enable_stackguard_randomization 0

%description
The GNU C Library provides the most important standard libraries used
by nearly all programs: the standard C library, the standard math
library, and the POSIX thread library.	A system is not functional
without these libraries.


%package info
Summary: Info Files for the GNU C Library
Group: Documentation
Requires: /sbin/install-info
AutoReq: on
AutoProv: on

%description info
This package contains the documentation for the GNU C library stored as
info files. Due to a lack of resources, this documentation is not
complete and is partially out of date.


%package html
Summary: HTML Documentation for the GNU C Library
Group: Documentation
AutoReq: on
AutoProv: on

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


%package -n timezone
Summary: Timezone descriptions
Group: System Environment/Base
AutoReq: on
AutoProv: on

%description -n timezone
These are configuration files that describe available time zones. You
can select an appropriate time zone for your system with YaST.


%package profile
Summary: Libc Profiling and Debugging Versions
Group: Development/Libraries
Requires: glibc = %{version}
AutoReq: on
AutoProv: on

%description profile
This package contains special versions of the GNU C library which are
necessary for profiling and debugging.


%package obsolete
Summary: Obsolete Shared Libraries from the GNU C Library
Group: System Environment/Libraries
Requires: glibc = %{version}
AutoReq: on
AutoProv: on

%description obsolete
This package provides some old libraries from the GNU C Library which
are no longer supported. Additional it provides a compatibility library
for old binaries linked against glibc 2.0.
Install this package if you need one of this libraries to get old
binaries working, but since this libraries are not supported and there
is no gurantee that they work for you, you should try to get newer
versions of your software.


%prep
%setup -n 'glibc-%{version}' -q -a 1 -b 2 -a 3 -a 4
%{__mv} -v 'glibc-libidn-%{version}' libidn

# libNoVersion part is only active on ix86:
%ifarch %ix86
%patch1
%endif

%patch3
%patch4
%patch10
%patch14
%patch17
%patch26
%patch29


%build
# Print out some information about the build process. Might be useful.
if [[ -x /bin/uname.bin ]]
then
	/bin/uname.bin -a
else
	uname -a
fi
uptime || :
ulimit -a
nice

# Adjust glibc version.h
echo '#define CONFHOST "%{_target_cpu}-slackware-linux"' >> version.h

# Default CFLAGS and Compiler:
build_cflags=''
build_cc='%{_target_platform}-gcc'
build_cxx='%{_target_platform}-g++'
addons='libidn'


# Filter CFLAGS, because alot of them will cause problems.
for flag in ${RPM_OPT_FLAGS}
do
	if echo "${flag}" | egrep -q '(-m[0-9][0-9])|(-march)|(-O[0-9])'
	then
		build_cflags="${build_cflags} ${flag}"
	fi
done


# Now overwrite or modify CFLAGS for some architectures
%ifarch %ix86 %x86_64
build_cflags="${build_cflags} -mno-tls-direct-seg-refs"
%endif

# Add flags for all plattforms except AXP
%ifarch %ix86
addons="${addons},noversion"
%endif


# How we build it:
# A little helper function that may be called more than once.
	configure_and_build_glibc() {
	local cflags="${1}"
	local addons="${2}"
	shift 2
	CFLAGS="${cflags}" \
	CC="${build_cc}" \
	CXX="${build_cxx}" \
		../configure \
		--build='%{_target_platform}' \
		--host='%{_target_platform}' \
		--prefix='%{_prefix}' \
		--datadir='%{_datadir}' \
		--mandir='%{_mandir}' \
		--infodir='%{_infodir}' \
		--enable-profile \
	    --enable-add-ons="nptl,${addons}" \
		--srcdir=.. \
		--without-cvs \
		--without-selinux \
		--with-tls \
		--with-__thread \
		--enable-kernel=2.6.16 \
		${*} \
		--enable-bind-now

	%{__make} %{?_smp_mflags}
}


# Now build NPTL version
%{__mkdir_p} 'cc-nptl'
pushd 'cc-nptl'
configure_and_build_glibc "${build_cflags}" "${addons}"
popd


# Run testsuite, if appropriate.
%if %{run_testsuite}
# Increase timeout
export TIMEOUTFACTOR=16

%ifarch %ix86 %x86_64
# ix86: tst-cputimer? fails
# ia64: tst-timer4 fails
# ppc64: tst-pselect, ftwtest fails
# s390,s390x: tst-timer* fails
%{__make} -C cc-nptl -k check || echo %{__make} check failed
%else
%{__make} -C cc-nptl check
%endif
%endif
%{__make} -C cc-nptl check-abi || echo %{__make} check-abi failed


# Build html documentation
%{__make} -C cc-nptl html


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'

# We don't want to strip the .symtab from our libraries in
# find-debuginfo.sh, at least not from libpthread.so.* because it is used
# by libthread_db to find some non-exported symbols in order to detect if
# threading support should be enabled. These symbols are _not_ exported, 
# and we can't easily export them retroactively without changing the API.
# So we have to continue to "export" them via .symtab, instead of 
# .dynsym :-(
export STRIP_KEEP_SYMTAB=yes

# Make sure we will create the gconv-modules.cache
%{__mkdir} -p '%{buildroot}/%{_libdir}/gconv'
touch '%{buildroot}/%{_libdir}/gconv/gconv-modules.cache'

# Do not install in parallel, timezone Makefile will fail
%{__fakeroot} %{__make} -C cc-nptl install install_root='%{buildroot}'

# Install locales. Don't install in parallel!
pushd 'cc-nptl'
%{__fakeroot} %{__make} -C ../localedata install-locales \
	objdir="$(pwd)" \
	install_root='%{buildroot}' 
popd

# create file list for glibc-locale package
%find_lang libc

# Now the manpages
pushd 'manpages'
%{__make_install} \
	install_root='%{buildroot}' \
	MANSEC='%{buildroot}/%{_mandir}/man'
popd

# Obsolete libraries are stored extra:
%{__mkdir} -p '%{buildroot}/%{_lib}/obsolete'

# Install the mapv4v6* header files
%{__mkdir_p} '%{buildroot}/usr/include/resolv'
%{__install} -m 0644 resolv/mapv4v6addr.h '%{buildroot}/usr/include/resolv/'
%{__install} -m 0644 resolv/mapv4v6hostent.h \
	'%{buildroot}/usr/include/resolv/'

# Adjust /etc/localtime
%{__rm} -f '%{buildroot}/etc/localtime'
%{__cp} -f '%{buildroot}/%{_prefix}/share/zoneinfo/UTC' \
	'%{buildroot}/etc/localtime'

# Install nscd tools
%{__cp} nscd/nscd.conf '%{buildroot}/%{_sysconfdir}'
%{__mkdir_p} '%{buildroot}/var/run/nscd'
touch '%{buildroot}/var/run/nscd/'{passwd,group,hosts}
touch '%{buildroot}/var/run/nscd/'{socket,nscd.pid}

# Install nscd startup file
%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/initng/daemon'
%{__cat} < '%{SOURCE2}' | \
	%{__sed} -e 's,@nscd@,%{_sbindir}/nscd,g' \
	> '%{buildroot}/etc/initng/daemon/nscd.i'

# Install bindresvport.blacklist
%{__install} -m 0644 '%{SOURCE10}' \
	'%{buildroot}/%{_sysconfdir}/bindresvport.blacklist'

# Create ld.so.conf
%{__cat} << __EOF__ > '%{buildroot}/%{_sysconfdir}/ld.so.conf'
/lib
/usr/X11R6/lib/Xaw3d
/usr/X11R6/lib
%ifarch %ix86
/usr/i586-slackware-linux/lib
/usr/i686-slackware-linux/lib
%else
/usr/local/lib
%endif
%ifarch %x86_64
/lib64
/lib
/usr/lib64
/usr/lib
/usr/local/lib64
/opt/gnome/lib64
%endif
include /etc/ld.so.conf.d/*
__EOF__

%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/ld.so.conf.d'

# install nsswitch.conf
%{__install} -m 0644 '%{SOURCE8}' \
	'%{buildroot}/%{_sysconfdir}/nsswitch.conf'

%ifarch %ix86
# Remove static library and .so symlink, not needed
%{__rm} -f '%{buildroot}/%{_libdir}'/libNoVersion*

# Move to lib/obsolete
%{__mkdir_p} '%{buildroot}/%{_lib}/obsolete/noversion'
%{__mv} -v '%{buildroot}/%{_lib}'/libNoVersion* \
	'%{buildroot}/%{_lib}/obsolete/noversion/'
%endif

# Don't look at it! We don't wish a /bin/sh requires
%{__chmod} 0644 \
	'%{buildroot}/%{_bindir}/ldd' \
	'%{buildroot}/sbin/sln'

# Remove not needed files from BuildRoot
%{__rm} -f '%{buildroot}/%{_infodir}/dir'

# Now, finally, move the library files so that the system does not
# crash when we update glibc...
%{__mkdir_p} '%{buildroot}/%{_lib}/incoming'
find '%{buildroot}/%{_lib}' -maxdepth 1 -not -type d -and -not -type l \
	-exec %{__cp} -a '{}' '%{buildroot}/%{_lib}/incoming' \;


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%post 
post_install_glibc() {
	# This is the 'incoming' dir
	incoming_dir="${1}"
	cd "${incoming_dir}"

	for file in *.so
	do
		if [[ -f "${file}" ]]
		then
			%{__cp} -a "${file}" "../${file}.incoming"
		fi
	done

	cd ..
	/sbin/ldconfig -l *.incoming
	
	for incoming_file in *.incoming
	do
		basename=$(basename "${incoming_file}" .incoming)
		%{__rm} -f "${basename}"
		%{__cp} -a "${incoming_file}" "${basename}"
		/sbin/ldconfig -l "${basename}"
		%{__rm} -f "${incoming_file}"
	done
}
post_install_glibc '/%{_lib}/incoming'
/sbin/ldconfig

%postun
/sbin/ldconfig

%post info
update-info-dir

%postun info
update-info-dir

%preun -n nscd
if [[ "${1}" -eq 0 ]]
then
	ngc -d daemon/nscd
	ng-update del daemon/nscd default
fi > /dev/null 2>&1 
exit 0


%files
%defattr(-,root,root)
%doc LICENSES
%doc COPYING COPYING.LIB FAQ INSTALL NEWS NOTES README BUGS CONFORMANCE CANCEL*
%doc %{_mandir}/man1/catchsegv.1*
%doc %{_mandir}/man1/rpcgen.1*
%doc %{_mandir}/man1/sprof.1*
%doc %{_mandir}/man1/getconf.1*
%doc %{_mandir}/man1/getent.1*
%doc %{_mandir}/man1/localedef.1*
%doc %{_mandir}/man3/*
%doc %{_mandir}/man5/*
%doc %{_mandir}/man8/rpcinfo.8*
%config %{_sysconfdir}/ld.so.conf
%dir %{_sysconfdir}/ld.so.conf.d
%attr(0644, root, root) %verify(not md5 size mtime) %ghost %config(missingok, noreplace) %{_sysconfdir}/ld.so.cache
%config(noreplace) %{_sysconfdir}/rpc
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/nsswitch.conf
%config(noreplace) %{_sysconfdir}/bindresvport.blacklist
%ghost /%{_lib}/ld-%{version}.so
%ifarch x86_64
%ghost /%{_lib}/ld-linux-x86-64.so.2
%else
%ghost /%{_lib}/ld-linux.so.2
%endif
%ghost /%{_lib}/libBrokenLocale-%{version}.so
%ghost /%{_lib}/libBrokenLocale.so.1
%ghost /%{_lib}/libSegFault.so
%ghost /%{_lib}/libanl-%{version}.so
%ghost /%{_lib}/libanl.so.1
%ghost /%{_lib}/libc-%{version}.so
%ghost /%{_lib}/libc.so.6*
%ghost /%{_lib}/libcidn-%{version}.so
%ghost /%{_lib}/libcidn.so.1
%ghost /%{_lib}/libcrypt-%{version}.so
%ghost /%{_lib}/libcrypt.so.1
%ghost /%{_lib}/libdl-%{version}.so
%ghost /%{_lib}/libdl.so.2*
%ghost /%{_lib}/libm-%{version}.so
%ghost /%{_lib}/libm.so.6*
%ghost /%{_lib}/libmemusage.so
%ghost /%{_lib}/libnsl-%{version}.so
%ghost /%{_lib}/libnsl.so.1
%ghost /%{_lib}/libnss_compat-%{version}.so
%ghost /%{_lib}/libnss_compat.so.2
%ghost /%{_lib}/libnss_dns-%{version}.so
%ghost /%{_lib}/libnss_dns.so.2
%ghost /%{_lib}/libnss_files-%{version}.so
%ghost /%{_lib}/libnss_files.so.2
%ghost /%{_lib}/libnss_hesiod-%{version}.so
%ghost /%{_lib}/libnss_hesiod.so.2
%ghost /%{_lib}/libnss_nis-%{version}.so
%ghost /%{_lib}/libnss_nis.so.2
%ghost /%{_lib}/libnss_nisplus-%{version}.so
%ghost /%{_lib}/libnss_nisplus.so.2
%ghost /%{_lib}/libpcprofile.so
%ghost /%{_lib}/libpthread-%{version}.so
%ghost /%{_lib}/libpthread.so.0
%ghost /%{_lib}/libresolv-%{version}.so
%ghost /%{_lib}/libresolv.so.2
%ghost /%{_lib}/librt-%{version}.so
%ghost /%{_lib}/librt.so.1
%ghost /%{_lib}/libthread_db-1.0.so
%ghost /%{_lib}/libthread_db.so.1
%ghost /%{_lib}/libutil-%{version}.so
%ghost /%{_lib}/libutil.so.1
/%{_lib}/incoming/
/sbin/ldconfig
%{_bindir}/gencat
%{_bindir}/getconf
%{_bindir}/getent
%{_bindir}/iconv
%attr(0755, root, root) %{_bindir}/ldd
%attr(0755, root, root) /sbin/sln
%ifarch %ix86 
%{_bindir}/lddlibc4
%endif
%{_bindir}/locale
%{_bindir}/localedef
%attr(4755, root, root) %{_libexecdir}/pt_chown
%dir %attr(0755, root, root) %{_libexecdir}/getconf
%{_libexecdir}/getconf/*
%{_sbindir}/rpcinfo
%{_sbindir}/iconvconfig
%{_bindir}/catchsegv
%{_bindir}/mtrace
%{_bindir}/pcprofiledump
%{_bindir}/rpcgen
%{_bindir}/sprof
%{_bindir}/xtrace
%{_includedir}/*
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

%files obsolete
%defattr (0755, root, root, 0755)
%dir /%{_lib}/obsolete/
%ifarch %ix86
%dir /%{_lib}/obsolete/noversion
/%{_lib}/obsolete/noversion/libNoVersion-%{version}.so
/%{_lib}/obsolete/noversion/libNoVersion.so.1
%endif

%files locale -f libc.lang
%defattr(-,root,root)
%{_datadir}/locale/locale.alias
%{_datadir}/locale/
%{_libdir}/locale/
%{_libdir}/gconv

%files info
%defattr(-, root, root)
%{_infodir}/libc.info*

%files html
%defattr(-, root, root)
%doc manual/libc/*.html

%files i18ndata
%defattr(-, root, root)
%{_datadir}/i18n/

%files -n nscd
%defattr(-, root, root)
%config(noreplace) %{_sysconfdir}/nscd.conf
%{_sysconfdir}/initng/daemon/nscd.i
%{_sbindir}/nscd
%dir %attr(0755, root, root) %{_localstatedir}/run/nscd
%attr(0644, root, root) %verify(not md5 size mtime) %ghost %config(missingok, noreplace) %{_localstatedir}/run/nscd/nscd.pid
%attr(0666, root, root) %verify(not md5 size mtime) %ghost %config(missingok, noreplace) %{_localstatedir}/run/nscd/socket
%attr(0600, root, root) %verify(not md5 size mtime) %ghost %config(missingok, noreplace) %{_localstatedir}/run/nscd/passwd
%attr(0600, root, root) %verify(not md5 size mtime) %ghost %config(missingok, noreplace) %{_localstatedir}/run/nscd/group
%attr(0600, root, root) %verify(not md5 size mtime) %ghost %config(missingok, noreplace) %{_localstatedir}/run/nscd/hosts

%files -n timezone
%defattr(-, root, root)
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/localtime
%{_datadir}/zoneinfo/
%{_bindir}/tzselect
%{_sbindir}/zdump
%{_sbindir}/zic

%files profile
%defattr(-, root, root)
%{_libdir}/libc_p.a
%{_libdir}/libBrokenLocale_p.a
%{_libdir}/libanl_p.a
%{_libdir}/libm_p.a
%{_libdir}/libcrypt_p.a
%{_libdir}/libpthread_p.a
%{_libdir}/libresolv_p.a
%{_libdir}/libnsl_p.a
%{_libdir}/librt_p.a
%{_libdir}/librpcsvc_p.a
%{_libdir}/libutil_p.a
%{_libdir}/libdl_p.a
