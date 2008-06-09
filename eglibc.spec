Name: glibc
Summary: Standard Shared Libraries (from the GNU C Library)
Version: 2.4
Release: 1.1ev 
Group: System Environment/Base
License: GPL, LGPL
URL: http://www.gnu.org/software/libc/libc.html
BuildRequires: gcc-g++, libstdc++, gcc-core, make >= 3.79.1, findutils, sed,
BuildRequires: gettext, gawk, perl, bison
PreReq: fhs
BuildRoot: %{_tmppath}/%{name}-buildroot
%define snapshot_date 2006032009
Source0: http://ftp.gnu.org/gnu/glibc/glibc-%{version}.tar.bz2
Source1: http://ftp.gnu.org/gnu/glibc/glibc-libidn-%{version}.tar.bz2
#Source0: glibc-%{version}-%{snapshot_date}.tar.bz2
#Source1: glibc-nptl-%{version}-2006040312.tar.bz2
Source2: %{name}-nscd.i
Source3: noversion.tar.bz2
Source4: manpages.tar.bz2
Source5: http://www.openwall.com/crypt/crypt_blowfish-1.0.tar.gz
Source8: nsswitch.conf
Source10: bindresvport.blacklist
Source11: ctype_b.c
Patch1: glibc-2.3.90-noversion.diff
Patch2: glibc-2.3.90-fnmatch.diff
Patch3: resolv.dynamic.diff
Patch4: glibc-2.3.locales.diff.bz2
Patch5: crypt_blowfish-glibc-2.3.diff
Patch9: glibc-2.3.3-revert-only-euro.diff
Patch10: glibc-2.3-regcomp.diff
Patch11: glibc-2.3.2-revert_tcsetattr.diff
Patch12: glibc-2.3.1.localedef.diff
Patch14: glibc-2.3.2.no_archive.diff
Patch15: glibc-2.3.3-amd64-string.diff
Patch16: libm-x86-64.diff
Patch17: glibc-2.3.90-bindresvport.blacklist.diff
Patch19: glibc-2.3.90-no_NO.diff
Patch20: glibc-2.3.90-zic.diff
Patch21: glibc-2.3.90-ld.so-madvise.diff
Patch22: glibc-2.3.3-amd64-s_ceil.diff
Patch23: glibc-2.3.3-mdns-resolver.diff
Patch24: glibc-2.3.3-execstack.diff
Patch25: glibc-2.3.3-china.diff
Patch26: glibc-2.3.4-gb18030-big5hkscs.diff.bz2
Patch27: glibc-2.3.90-nscd.diff
Patch28: glibc-2.3.3-nscd-db-path.diff
Patch29: glibc-2.3.5-nscd-zeronegtimeout.diff
Patch31: glibc-2.3.90-pthread_kill-invalid-thread-id.diff
Patch32: glibc-2.3.90-langpackdir.diff
Patch33: glibc-2.3.90-clone-cfi.diff
Patch34: glibc-2.4-2006040312-CVS.diff
Patch35: glibc-2.4-readlink.diff
Patch36: glibc-nptl-2.4-nofixsyscallnr.diff
Patch38: glibc-2.4-nptl-negpid.diff
%define build_locales 1
%define run_testsuite 1
%define disable_assert 0
%define enable_stackguard_randomization 0

%description
The GNU C Library provides the most important standard libraries used
by nearly all programs: the standard C library, the standard math
library, and the POSIX thread library.	A system is not functional
without these libraries.


%package tlscompat
Summary: Compatibility package for old linuxthreads + nptl versions
Group: System Environment/Libraries
Requires: glibc = %{version}

%description tlscompat
Older package versions of the GNU C library came with to threading models:
Linuxthreads and NTPL, whereas the first one was included to be compatible
with 2.4 kernels. The NPTL version resistet in /lib/ntpl. Newer packages come
with the NPTL threading model only, because the 2.6 kernel version is now
standard. To avoid breaking old systems, this package has the old /lib/tls
directory structure, but holds the same libraries as the standard glibc
package.


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
AutoReq: on
AutoProv: on

%description i18ndata
This package contains the data needed to build the locale data files to
use the internationalization features of the GNU libc. It is normally
not necessary to install this packages, the data files are already
created.


%package locale
Summary: Locale Data for Localized Programs
Group: System Environment/Base
Requires: glibc = %{version}
AutoReq: on
AutoProv: on

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
# %setup -n glibc-2.4 -q -a 1 -b 2 -a 3 -a 4 -a 5
%setup -n glibc-2.4 -q -a 1 -b 2 -a 3 -a 4 -a 5
mv -v glibc-libidn-%{version} libidn

# libNoVersion part is only active on ix86:
%ifarch %ix86
%patch1
%endif

%patch2
%patch3
%patch4
%patch9
%patch10
# %patch11
%patch12
%patch14
%patch15
# strncmp is broken, let's delete it for now this way
rm sysdeps/x86_64/strncmp.S
%patch16 -E
# We have s_sincos.c in patch20, remove duplicate
rm sysdeps/x86_64/fpu/s_sincos.S
%patch17
%patch19
%patch20
%patch21
%patch22
%patch23
%patch24
%patch25
%patch26
%patch27
%patch28
%patch29
%patch31
%patch33
# %patch34 -p2
%patch35
# %patch36
%patch38


# Install blowfish crypt add-on

rm crypt_blowfish-*/crypt.h
cp -a crypt_blowfish-*/*.[ch] crypt
%patch5
find . -name configure | xargs touch


%build
if [ -x /bin/uname.bin ]
then
	/bin/uname.bin -a
else
	uname -a
fi
uptime || :
ulimit -a
nice


# Adjust glibc version.h

echo "#define CONFHOST \"%{_target_cpu}-slackware-linux\"" >> version.h
echo "#define CVSDATE \"`date -r ChangeLog +%Y%m%d`\"" >> version.h


# Default CFLAGS and Compiler:
BuildCFlags=
BuildCC="%{_target_platform}-gcc"
BuildCXX="%{_target_platform}-g++"
addons="libidn"


# Filter CFLAGS, because alot of them will cause problems.

for flag in $RPM_OPT_FLAGS
do
	if echo "$flag" | egrep -q '(-m[0-9][0-9])|(-march)|(-O[0-9])'
	then
		BuildCFlags="$BuildCFlags $flag"
	fi
done


# Now overwrite or modify CFLAGS for some architectures

%ifarch %ix86 %x86_64
BuildCFlags="$BuildCFlags -mno-tls-direct-seg-refs"
%endif
# Add flags for all plattforms except AXP
%ifarch %ix86
addons="${addons},noversion"
%endif


# How we build it: A little helper function that may be called more than once.

configure_and_build_glibc() {
	local cflags="$1"
	local addons="$2"
	shift 2
	CFLAGS="$cflags" \
	CC="$BuildCC" \
	CXX="$BuildCXX" \
	../configure \
		--build=%{_target_platform} \
		--host=%{_target_platform} \
		--prefix=%{_prefix} \
		--datadir=%{_datadir} \
		--mandir=%{_mandir} \
		--infodir=%{_infodir} \
        --enable-add-ons="nptl,${addons}" \
		--srcdir=.. \
		--without-cvs \
		--without-selinux \
		--with-tls \
		--with-__thread \
		--enable-kernel=2.6.16 \
		$* \
		--enable-bind-now
	
	make %{_smp_mflags}
}


# Now build NPTL version

mkdir cc-nptl
cd cc-nptl
configure_and_build_glibc "$BuildCFlags" "$addons"
cd ..


# Run testsuite, if appropriate.

%if %{run_testsuite}
	# Increase timeout
	export TIMEOUTFACTOR=16

	%ifarch %ix86 x86_64
		# ix86: tst-cputimer? fails
		# ia64: tst-timer4 fails
		# ppc64: tst-pselect, ftwtest fails
		# s390,s390x: tst-timer* fails
	   make -C cc-nptl -k check || echo make check failed
	%else
	   make -C cc-nptl check
	%endif
%endif
make -C cc-nptl check-abi || echo check-abi failed


# Build html documentation

make -C cc-nptl html


%install
[ "$RPM_BUILD_ROOT" != '/' ] && rm -rf "$RPM_BUILD_ROOT"

# We don't want to strip the .symtab from our libraries in find-debuginfo.sh,
# at least not from libpthread.so.* because it is used by libthread_db to find
# some non-exported symbols in order to detect if threading support
# should be enabled.  These symbols are _not_ exported, and we can't easily
# export them retroactively without changing the API.  So we have to
# continue to "export" them via .symtab, instead of .dynsym :-(
export STRIP_KEEP_SYMTAB=yes

# Make sure we will create the gconv-modules.cache
mkdir -p $RPM_BUILD_ROOT%{_libdir}/gconv
touch $RPM_BUILD_ROOT%{_libdir}/gconv/gconv-modules.cache

# Do not install in parallel, timezone Makefile will fail
make -C cc-nptl install_root="$RPM_BUILD_ROOT" install 

# Install locales if wanted.

%if %{build_locales}
# Do not install locales in parallel!
	cd cc-nptl
	make install_root=$RPM_BUILD_ROOT install-locales \
		-C ../localedata objdir=`pwd`
	cd ..
%endif

# create file list for glibc-locale package
%find_lang libc

# Now the manpages
cd manpages
make install \
	install_root="$RPM_BUILD_ROOT" \
	MANSEC="${RPM_BUILD_ROOT}/%{_mandir}/man" 
cd ..
#export RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_lib}/obsolete

# NPTL <bits/stdio-lock.h> is not usable outside of glibc, so include
# the generic one (RH#162634)
cp -av bits/stdio-lock.h $RPM_BUILD_ROOT%{_prefix}/include/bits/stdio-lock.h

# Install the mapv4v6* header files

mkdir -p "${RPM_BUILD_ROOT}/usr/include/resolv"
install -m 0644 resolv/mapv4v6addr.h "${RPM_BUILD_ROOT}/usr/include/resolv/"
install -m 0644 resolv/mapv4v6hostent.h "${RPM_BUILD_ROOT}/usr/include/resolv/"

# Adjust /etc/localtime

rm -f "${RPM_BUILD_ROOT}/etc/localtime"
cp -f "${RPM_BUILD_ROOT}/%{_prefix}/share/zoneinfo/UTC" \
	"${RPM_BUILD_ROOT}/etc/localtime"

# glibc documentation in HTML

mkdir -p "${RPM_BUILD_ROOT}/usr/share/doc/glibc"
cp -p manual/libc/*.html "${RPM_BUILD_ROOT}/usr/share/doc/glibc"
(cd "${RPM_BUILD_ROOT}/usr/share/doc/glibc"; ln -sf libc.html index.html)

# Install nscd tools

cp nscd/nscd.conf "${RPM_BUILD_ROOT}/etc"
mkdir -p "${RPM_BUILD_ROOT}/var/run/nscd"
touch "${RPM_BUILD_ROOT}/var/run/nscd/"{passwd,group,hosts}
touch "${RPM_BUILD_ROOT}/var/run/nscd/"{socket,nscd.pid}

# Install nscd startup file

mkdir -p "${RPM_BUILD_ROOT}/etc/initng/daemon"
cat < %{SOURCE2} | \
	sed -e 's,@nscd@,%{_sbindir}/nscd,g' \
	> ${RPM_BUILD_ROOT}/etc/initng/daemon/nscd.i

# Install bindresvport.blacklist
install -m 644 ${RPM_SOURCE_DIR}/bindresvport.blacklist "${RPM_BUILD_ROOT}/etc"


# Create ld.so.conf

cat << __EOF__ > "${RPM_BUILD_ROOT}/etc/ld.so.conf"
/lib/tls
/lib
/usr/X11R6/lib/Xaw3d
/usr/X11R6/lib
%ifarch %ix86
/usr/i486-linux-libc5/lib=libc5
%endif
%ifarch %x86
/usr/i586-slackware-linux/lib
/usr/i686-slackware-linux/lib
%else
/usr/$RPM_ARCH-suse-linux/lib
%endif
/usr/local/lib
%ifarch x86_64
/lib64
/lib
/usr/lib64
/usr/lib
/usr/local/lib64
/opt/gnome/lib64
%endif
include /etc/ld.so.conf.d/*
__EOF__

mkdir -p "${RPM_BUILD_ROOT}/etc/ld.so.conf.d"

# install nsswitch.conf
install -m 644 "${RPM_SOURCE_DIR}/nsswitch.conf" "${RPM_BUILD_ROOT}/etc"


%ifarch %ix86
# Remove static library and .so symlink, not needed
rm -f $RPM_BUILD_ROOT%{_libdir}/libNoVersion*

# Move to lib/obsolete

mkdir -p "${RPM_BUILD_ROOT}/%{_lib}/obsolete/noversion"
mv -v "$RPM_BUILD_ROOT"/%{_lib}/libNoVersion* \
	"$RPM_BUILD_ROOT"/%{_lib}/obsolete/noversion/
%endif

# Don't look at it! We don't wish a /bin/sh requires
chmod 644 \
	"${RPM_BUILD_ROOT}/usr/bin/ldd" \
	"${RPM_BUILD_ROOT}/sbin/sln"

# Remove not needed files from BuildRoot

rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"

# Now, finally, move the library files so that the system does not crash when
# we update glibc...

mkdir -p "${RPM_BUILD_ROOT}/%{_lib}/incoming"
mkdir -p "${RPM_BUILD_ROOT}/%{_lib}/tls/incoming"
find "${RPM_BUILD_ROOT}/%{_lib}" -maxdepth 1 -not -type d -and -not -type l \
	-exec cp -a "{}" "${RPM_BUILD_ROOT}/%{_lib}/incoming" \; \
	-exec cp -a "{}" "${RPM_BUILD_ROOT}/%{_lib}/tls/incoming" \;
find "${RPM_BUILD_ROOT}/%{_lib}" -maxdepth 1 -not -type d \
	-exec cp -a "{}" "${RPM_BUILD_ROOT}/%{_lib}/tls/" \;


%clean
[ "$RPM_BUILD_ROOT" != '/' ] && rm -rf "$RPM_BUILD_ROOT"


%post 
post_install_glibc() {
	# This is the 'incoming' dir
	incoming_dir="$1"
	shift

	pushd $incoming_dir

	for file in *.so
	do
		if [ -f "$file" ]
		then
			cp -a "$file" "../${file}.incoming"
		fi
	done

	cd ..
	/sbin/ldconfig -l *.incoming
	
	for file in *.incoming
	do
		basename=$(basename "$file" .incoming)
		rm -f "$basename"
		cp -a "$file" "$basename"
		/sbin/ldconfig -l "$basename"
		rm -f "$file"
	done

	popd
}
post_install_glibc /%{_lib}/incoming > /dev/null 2>&1
/sbin/ldconfig

%post tlscompat
post_install_glibc() {
	# This is the 'incoming' dir
	incoming_dir="$1"
	shift

	pushd $incoming_dir

	for file in *.so
	do
		if [ -f "$file" ]
		then
			cp -a "$file" "../${file}.incoming"
		fi
	done

	cd ..
	/sbin/ldconfig -l *.incoming
	
	for file in *.incoming
	do
		basename=$(basename "$file" .incoming)
		rm -f "$basename"
		cp -a "$file" "$basename"
		/sbin/ldconfig -l "$basename"
		rm -f "$file"
	done

	popd
}
# This is a hack for some old libc directory architecture with tls/ dir
post_install_glibc /%{_lib}/tls/incoming > /dev/null 2>&1
/sbin/ldconfig

%postun
/sbin/ldconfig

%postun tlscompat
/sbin/ldconfig

%post info
/sbin/install-info %{_infodir}/libc.info.gz %{_infodir}/dir

%postun info
/sbin/install-info --delete %{_infodir}/libc.info.gz %{_infodir}/dir

%preun -n nscd
/sbin/ngc -d daemon/nscd 2>/dev/null
/sbin/ng-update del daemon/nscd default 2>/dev/null
exit 0


%files
%defattr(-,root,root)
%doc LICENSES
%doc COPYING COPYING.LIB FAQ INSTALL NEWS NOTES README BUGS CONFORMANCE INTERFACE $RPM_SOURCE_DIR/ctype_b.c
%doc %{_mandir}/man1/catchsegv.1.gz
%doc %{_mandir}/man1/rpcgen.1.gz
%doc %{_mandir}/man1/sprof.1.gz
%doc %{_mandir}/man3/*
%dir /etc/ld.so.conf.d
%config(noreplace) /etc/bindresvport.blacklist
%config /etc/ld.so.conf
%attr(0644,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /etc/ld.so.cache
%config(noreplace) /etc/rpc
%verify(not md5 size mtime) %config(noreplace) /etc/nsswitch.conf
# %config(noreplace) /etc/default/nss
%doc %{_mandir}/man1/getconf.1.gz
%doc %{_mandir}/man1/getent.1.gz
%doc %{_mandir}/man1/localedef.1.gz
%doc %{_mandir}/man5/*
%doc %{_mandir}/man8/rpcinfo.8.gz
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
/usr/bin/gencat
/usr/bin/getconf
/usr/bin/getent
/usr/bin/iconv
%attr(755,root,root) /usr/bin/ldd
%attr(755,root,root) /sbin/sln
%ifarch %ix86 
/usr/bin/lddlibc4
%endif
/usr/bin/locale
/usr/bin/localedef
%attr(4755,root,root) %{_libexecdir}/pt_chown
%dir %attr(0755,root,root) %{_libexecdir}/getconf
%{_libexecdir}/getconf/*
%{_sbindir}/rpcinfo
/usr/sbin/iconvconfig
/usr/bin/catchsegv
/usr/bin/mtrace
/usr/bin/pcprofiledump
/usr/bin/rpcgen
/usr/bin/sprof
/usr/bin/xtrace
%{_prefix}/include/*
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

%files tlscompat
%defattr(-,root,root)
%doc LICENSES
%doc COPYING COPYING.LIB FAQ INSTALL NEWS NOTES README BUGS CONFORMANCE INTERFACE $RPM_SOURCE_DIR/ctype_b.c
%dir /%{_lib}/tls
%ghost /%{_lib}/tls/ld-%{version}.so
%ghost /%{_lib}/tls/ld-linux.so.2
%ghost /%{_lib}/tls/libBrokenLocale-%{version}.so
%ghost /%{_lib}/tls/libBrokenLocale.so.1
%ghost /%{_lib}/tls/libSegFault.so
%ghost /%{_lib}/tls/libanl-%{version}.so
%ghost /%{_lib}/tls/libanl.so.1
%ghost /%{_lib}/tls/libc-%{version}.so
%ghost /%{_lib}/tls/libc.so.6*
%ghost /%{_lib}/tls/libcidn-%{version}.so
%ghost /%{_lib}/tls/libcidn.so.1
%ghost /%{_lib}/tls/libcrypt-%{version}.so
%ghost /%{_lib}/tls/libcrypt.so.1
%ghost /%{_lib}/tls/libdl-%{version}.so
%ghost /%{_lib}/tls/libdl.so.2*
%ghost /%{_lib}/tls/libm-%{version}.so
%ghost /%{_lib}/tls/libm.so.6*
%ghost /%{_lib}/tls/libmemusage.so
%ghost /%{_lib}/tls/libnsl-%{version}.so
%ghost /%{_lib}/tls/libnsl.so.1
%ghost /%{_lib}/tls/libnss_compat-%{version}.so
%ghost /%{_lib}/tls/libnss_compat.so.2
%ghost /%{_lib}/tls/libnss_dns-%{version}.so
%ghost /%{_lib}/tls/libnss_dns.so.2
%ghost /%{_lib}/tls/libnss_files-%{version}.so
%ghost /%{_lib}/tls/libnss_files.so.2
%ghost /%{_lib}/tls/libnss_hesiod-%{version}.so
%ghost /%{_lib}/tls/libnss_hesiod.so.2
%ghost /%{_lib}/tls/libnss_nis-%{version}.so
%ghost /%{_lib}/tls/libnss_nis.so.2
%ghost /%{_lib}/tls/libnss_nisplus-%{version}.so
%ghost /%{_lib}/tls/libnss_nisplus.so.2
%ghost /%{_lib}/tls/libpcprofile.so
%ghost /%{_lib}/tls/libpthread-%{version}.so
%ghost /%{_lib}/tls/libpthread.so.0
%ghost /%{_lib}/tls/libresolv-%{version}.so
%ghost /%{_lib}/tls/libresolv.so.2
%ghost /%{_lib}/tls/librt-%{version}.so
%ghost /%{_lib}/tls/librt.so.1
%ghost /%{_lib}/tls/libthread_db-1.0.so
%ghost /%{_lib}/tls/libthread_db.so.1
%ghost /%{_lib}/tls/libutil-%{version}.so
%ghost /%{_lib}/tls/libutil.so.1
/%{_lib}/tls/incoming/

%files obsolete
%defattr (755,root,root,755)
%dir /%{_lib}/obsolete/
%ifarch %ix86
%dir /%{_lib}/obsolete/noversion
/%{_lib}/obsolete/noversion/libNoVersion-%{version}.so
/%{_lib}/obsolete/noversion/libNoVersion.so.1
%endif

%files locale -f libc.lang
%defattr(-,root,root)
/usr/share/locale/locale.alias
%if %{build_locales}
/usr/lib/locale
%endif
%{_libdir}/gconv

%files info
%defattr(-,root,root)
%doc %{_infodir}/libc.info.gz
%doc %{_infodir}/libc.info-?.gz
%doc %{_infodir}/libc.info-??.gz

%files html
%defattr(-,root,root)
%doc %{_prefix}/share/doc/glibc

%files i18ndata
%defattr(-,root,root)
%{_prefix}/share/i18n

%files -n nscd
%defattr(-,root,root)
%config(noreplace) /etc/nscd.conf
%config /etc/initng/daemon/nscd.i
/usr/sbin/nscd
%dir %attr(0755,root,root) /var/run/nscd
%attr(0644,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/run/nscd/nscd.pid
%attr(0666,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/run/nscd/socket
%attr(0600,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/run/nscd/passwd
%attr(0600,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/run/nscd/group
%attr(0600,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/run/nscd/hosts

%files -n timezone
%defattr(-,root,root)
%verify(not md5 size mtime) %config(noreplace) /etc/localtime
%{_prefix}/share/zoneinfo
%{_bindir}/tzselect
%{_sbindir}/zdump
%{_sbindir}/zic

%files profile
%defattr(-,root,root)
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
