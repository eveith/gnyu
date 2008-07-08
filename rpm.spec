Name: rpm
Version: 4.4.8
Release: 2ev
Summary: The RPM Package Manager 
URL: http://www.rpm.org/
Group: System Environment/Base
License: LGPL
Vendor: MSP Slackware
Source: http://rpm5.org/files/rpm/rpm-4.4/rpm-%{version}.tar.bz2
Patch0: rpm-4.4.6-brp-nobuildrootpath-exitcode.diff
Patch1: rpm-4.4.6-rpmv3-support.patch

# Correct some little mistake with header inclusion
Patch5: rpm-4.4.8-gelf_h.patch

# Add some undocumented feature to gendiff
Patch17: rpm-4.2-gendiff-improved.patch

# (gb) fix built-in zlib dependencies
Patch4: rpm-4.4.6-deps.patch

# (gb) use shared libraries
Patch2: rpm-4.4.6-no-static.patch

# (gb) force generation of PIC code for static libs that can be built into a
# DSO (zlib, file)
Patch3: rpm-4.4.6-pic.patch

# if %post of foo-2 fails,
# or if %preun of foo-1 fails,
# or if %postun of foo-1 fails,
# => foo-1 is not removed, so we end up with both packages in rpmdb
# this patch makes rpm ignore the error in those cases
# failing %pre must still make the rpm install fail (#23677)
#
# (nb: the exit code for pretrans/posttrans & trigger/triggerun/triggerpostun
#       scripts is ignored with or without this patch)
Patch22: rpm-4.4.6-non-pre-scripts-dont-fail.patch

# (fredl) add loging facilities through syslog
Patch31: rpm-4.4.3-syslog.patch

# Check amd64 vs x86_64, these arch are the same
Patch44: rpm-4.4.1-amd64.patch

# Backport from 4.2.1 provides becoming obsoletes bug (fpons)
Patch49: rpm-4.4.3-provides-obsoleted.patch

# Introduce new ppc32 arch. Fix ppc64 bi-arch builds. Fix ppc builds on newer
# CPUs.
Patch56: rpm-4.4.6-ppc32.patch

# ok for this
Patch63: rpm-4.4.6-dont-install-delta-rpms.patch

# This patch ask to read /usr/lib/rpm/vendor/rpmpopt too
Patch64: rpm-4.4.1-morepopt.patch

# Being able to read old rpm (build with rpm v3)
# See https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=127113#c12
Patch68: rpm-4.4.1-region_trailer.patch

# In original rpm, -bb --short-circuit does not work and run all stage
# From popular request, we allow to do this
# http://qa.mandriva.com/show_bug.cgi?id=15896
Patch70: rpm-4.4.1-bb-shortcircuit.patch

# http://www.redhat.com/archives/rpm-list/2005-April/msg00131.html
# http://www.redhat.com/archives/rpm-list/2005-April/msg00132.html
Patch71: rpm-4.4.4-ordererase.patch

# File conflicts when rpm -i
# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=151609
Patch72: rpm-4.4.1-fileconflicts.patch

# Allow to set %_srcdefattr for src.rpm
Patch77: rpm-source-defattr.patch

# Do not use futex, but fcntl
Patch78: rpm-4.4.6-fcntl.patch

Patch82: rpm-4.4.3-ordering.patch

# don't conflict for doc files from colored packages
# (to be able to install lib*-devel together with lib64*-devel even if they
# have conflicting manpages)
Patch83: rpm-4.2.3-no-doc-conflicts.patch

# Fix http://qa.mandriva.com/show_bug.cgi?id=19392
Patch84: rpm-4.4.4-rpmqv-ghost.patch

# Install perl module in vendor directory
Patch85: rpm-4.4.4-perldirs.patch

# Use temporary table for Depends DB (Olivier Thauvin upstream)
Patch86: rpm-4.4.6-depsdb.patch

# Currently we prefer to disable dependencies over parents directory
Patch87: rpm-4.4.6-no-dirnames-dep.patch

# rpm 4.4.6 killed SOURCEPACKAGE, but this was announce lately, and will
# break all older tools that was using it (mdv 2006, 2005) which need this
# tag to know it is possible to rebuild a src.rpm
# This patch readd the tag into src.rpm
Patch88: rpm-4.4.6-SOURCEPACKAGE.patch

# make rpmdb cpp compliant (sptutle)
# reported upstream, I hope to see this include
Patch89: rpm-4.4.6-rpmdb.h-cpp-fix.patch

# avoids taking into account duplicates in file list when checking
# for unpackaged files
Patch91: rpm-4.4.6-check-dupl-files.patch

# with tar >= 1.15.91, one needs the --wildcard option to list *.spec
# files (for rpm -ta)
Patch92: rpm-4.4.6-newtar.patch

# fix free on invalid pointer after displaying "Unable to open temp file"
Patch98: rpm-4.4.6-fix-free-on-bad-pointer.patch

# without this patch, when pkg rpm-build is not installed,
# using rpm -bs t.spec returns: "t.spec: No such file or directory"
Patch100: rpm-4.4.6-fix-error-message-rpmb-not-installed.patch

Patch108: rpm-4.4.6-use-dgettext-instead-of-gettext-to-allow-use-of-multilibs.patch

Patch109: rpm-build-expand-field-for-single-token.patch

Patch111: rpm-check-file-trim-double-slash-in-buildroot.patch

Patch112: rpm-dont-use-rpmio-to-read-file-for-script.patch

# Patch from cvs
# using _docdir_fmt for doc directory
Patch113: rpm-4.4.8-macro_doc_fmt.patch

Patch114: rpm-read-vendor-macros.patch

Patch115: rpm-4.4.8-dont-clean-buildroot-in-install.patch

# Fix #31287, rpm -V do not use same space count
Patch116: rpm-qv-use-same-indentation.patch

# if file exists and is not yet in db, rpm don't check and replace it
Patch117: rpm-dont-replace-config-not-in-db.patch

Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: gcc, make >= 3.79.1, sed, zlib, beecrypt >= 4.1.2, neon
BuildRequires: python, perl >= 5.8.0, bzip2 >= 0.9.0, sqlite, gettext, gawk
BuildRequires: automake-110
Requires: rpm-libs = %{version}-%{release}
Conflicts: patch < 2.5
%define python_version %(echo $(python -c "import sys; print sys.version[0:3]"))
%define _rpm_uid 37
%define _rpm_gid 37

%description
The RPM Package Manager (RPM) is a powerful command line driven
package management system capable of installing, uninstalling,
verifying, querying, and updating software packages. Each software
package consists of an archive of files along with information about
the package like its version, a description, etc.


%package build
Summary: Scripts and executable programs used to build packages.
Group: Development/Tools
Requires: rpm = %{version}-%{release}, patch >= 2.5, file, elfutils
Provides: rpmbuild(VendorConfig) = 4.1-1
Requires: getconf(GNU_LIBPTHREAD_VERSION) = NPTL

%description build
The rpm-build package contains the scripts and executable programs
that are used to build packages using the RPM Package Manager.


%package perl
Summary: Perl bindings for apps which will manipulate RPM packages.
Group: Development/Libraries
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.17
Requires: rpm = %{version}-%{release}
Requires: rpm-libs = %{version}-%{release}
Obsoletes: perl-RPM, perl-RPM2
Conflicts: perl-RPM, perl-RPM2

%description perl
The rpm-perl package contains a module that permits applications
written in the Perl programming language to use the interface
supplied by RPM Package Manager libraries.
This package should be installed if you want to develop Perl
programs that will manipulate RPM packages and databases.
(Note: rpm-perl is forked from perl-RPM2-0.66, and will obsolete existing
perl-RPM packages)


%package python
Summary: Python bindings for apps which will manipulate RPM packages.
Group: Development/Libraries
Requires: rpm = %{version}-%{release}
Requires: rpm-libs = %{version}-%{release}
Requires: python >= %{python_version}

%description python
The rpm-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by RPM Package Manager libraries.
This package should be installed if you want to develop Python
programs that will manipulate RPM packages and databases.


%package libs
Summary:  Libraries for manipulating RPM packages.
Group: Development/Libraries
Requires: getconf(GNU_LIBPTHREAD_VERSION) = NPTL, sqlite
Provides: libtool(%{_libdir}/librpmdb.la), libtool(%{_libdir}/librpmio.la)

%description libs
This package contains the RPM shared libraries.
The RPM Package Manager


%package -n popt
Version: 1.10.7
Summary: A C library for parsing command line parameters.
Group: Development/Libraries

%description -n popt
Popt is a C library for parsing command line parameters. Popt was
heavily influenced by the getopt() and getopt_long() functions, but it
improves on them by allowing more powerful argument expansion. Popt
can parse arbitrary argv[] style arrays and automatically set
variables based on command line arguments. Popt allows command line
arguments to be aliased via configuration files and includes utility
functions for parsing arbitrary strings into argv[] arrays using
shell-like rules.


%prep
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1
%patch4 -p1 -b .deps
%patch2 -p1 -b .no-static
%patch3 -p1 -b .pic
# %patch5 -p1 -b .gelf_h
%patch17 -p0 -b .improved
%patch22 -p1 -b .fail
%patch31 -p0 -b .syslog
%patch44 -p1 -b .amd64
%patch49 -p0 -b .provides
%patch56 -p0 -b .ppc32
%patch63 -p0 -b .dont-install-delta-rpms
# %patch64 -p0 -b .morepopt
%patch68 -p0 -b .region_trailer
%patch70 -p0 -b .shortcircuit
%patch71 -p0  -b .ordererase
%patch72 -p0  -b .fileconflicts
%patch77 -p0  -b .srcdefattr
%patch78 -p0  -b .fcntl
%patch82 -p0 -b .ordering
%patch83 -p1 -b .no-doc-conflicts
%patch84 -p0 -b .poptQVghost
%patch85 -p0 -b .perldirs
%patch86 -p0 -b .depsdb
%patch87 -p0 -b .no-dirname-dep
%patch88 -p0 -b .sourcepackage
%patch89 -p0 -b .cpp-compliant
%patch91 -p0 -b .check-dupl-files
%patch92 -p0 -b .newtar
%patch98 -p1 -b .free
%patch100 -p1 -b .rpmb-missing
%patch108 -p1

# rpm now check there is only one token per field
# too bad, the check is performed before macro expansion...
%patch109 -p0 -b .singletoken

# Fix diff issue when buildroot contains some "//"
%patch111 -p0 -b .trim-slash

# Fix strange issue making %pre/post/... -f not working
%patch112 -p0 -b .build-no-rpmio

# %patch113 -p0 -b .docdir-macros
%patch114 -p0 -b .read-our-macros
# %patch115 -p0 -b .noclean
%patch116 -p0 -b .rpmVspace
%patch117 -p0 -b .rpmnew

# Fix a problem where rpcgen does not work
%ifos linux
sed -i "s,RPCGEN=\"rpcgen\(.*\)\",RPCGEN=\"rpcgen -Y /usr/bin\1\"," \
    db/dist/configure
%endif

# Fix another bug regarding the python bindings

#sed -i "s,#include \"Python\.h\",#include <python%python_version/Python.h>," \
#	python/system.h


%build
unset LD_ASSUME_KERNEL || :

#	--enable-posixmutexes \
%configure \
	--without-selinux \
	--with-mutex=UNIX/fcntl \
	--without-javaglue \
	--enable-compat185 \
	--with-perl \
	--with-python=%python_version \
	--with-glob \
	--with-apidocs
%{__make} -C zlib
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'

eval $(perl '-V:installarchlib')
%{__mkdir_p} %{buildroot}/$installarchlib

%{__make_install} DESTDIR='%{buildroot}'
%{__rm} -f %{buildroot}/%{_infodir}/dir

%{__mkdir_p} %{buildroot}/etc/cron.daily
%{__install} -m 0755 scripts/rpm.daily %{buildroot}/etc/cron.daily/rpm

%{__mkdir_p} %{buildroot}/etc/logrotate.d
%{__install} -m 0644 scripts/rpm.log %{buildroot}/etc/logrotate.d/rpm

%{__mkdir_p} %{buildroot}/etc/rpm
%{__mkdir_p} %{buildroot}/var/spool/repackage
%{__mkdir_p} %{buildroot}/var/lib/rpm

for dbi in \
    Basenames Conflictname Dirnames Group Installtid Name Packages \
    Providename Provideversion Requirename Requireversion Triggername \
    Filemd5s Pubkeys Sha1header Sigmd5 \
    __db.001 __db.002 __db.003 __db.004 __db.005 __db.006 __db.007 \
    __db.008 __db.009
do
    touch %{buildroot}/var/lib/rpm/$dbi
done


%find_lang rpm
%find_lang popt


# Get rid of unpacked files
{
	pushd %{buildroot}
	%{__rm} -f ./%{_libdir}/rpm/{Specfile.pm,cpanflute,cpanflute2,rpmdiff,rpmdiff.cgi,sql.prov,sql.req,tcl.req,trpm}
	%{__rm} -rf ./%{_mandir}/man8/rpmcache.8*
	%{__rm} -rf ./%{_mandir}/man8/rpmgraph.8*
	%{__rm} -rf ./%{_mandir}/ja/man8/rpmcache.8*
	%{__rm} -rf ./%{_mandir}/ja/man8/rpmgraph.8*
	%{__rm} -rf ./%{_mandir}/pl/man8/rpmcache.8*
	%{__rm} -rf ./%{_mandir}/pl/man8/rpmgraph.8*
	%{__rm} -rf ./%{_mandir}/{fr,ko}
	%{__rm} -f ./%{_bindir}/rpm{e,i,u}
	%{__rm} -f ./%{_libdir}/python%{with_python_version}/site-packages/*.{a,la}
	%{__rm} -f ./%{_libdir}/python%{with_python_version}/site-packages/rpm/*.{a,la}
	%{__find} ./%{_libdir}/perl5 -type f \
		-a \( -name perllocal.pod -o -name .packlist \
		-o \( -name '*.bs' -a -empty \) \) -exec %{__rm} -f {} ';'
	%{__find} ./%{_libdir}/perl5 \
		-type d -depth -exec rmdir {} 2>/dev/null ';'
	popd
}


%pre
{
	userdel rpm
	groupdel rpm
	groupadd -g %{_rpm_gid} rpm
	useradd \
		-d /var/lib/rpm \
		-u %{_rpm_uid} \
		-g %{_rpm_gid} \
		-s /sbin/nologin \
		rpm
} >/dev/null 2>&1
exit 0

%post
/sbin/ldconfig
%{__chown} rpm:rpm /var/lib/rpm/*

%postun
if [[ $1 -eq 0 ]]
then
	userdel rpm 
	groupdel rpm
fi > /dev/null 2>&1
/sbin/ldconfig
exit 0

%post libs
/sbin/ldconfig

%postun libs
/sbin/ldconfig

%post -n popt
/sbin/ldconfig

%postun -n popt
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files -f rpm.lang
%defattr(-, root, root)
# %doc RPM-PGP-KEY RPM-GPG-KEY BETA-GPG-KEY
%doc CHANGES GROUPS doc/manual/[a-z]*
%dir /etc/rpm
%config /etc/cron.daily/rpm
%config /etc/logrotate.d/rpm
%attr(0755, rpm, rpm) /bin/rpm
%attr(0755, rpm, rpm) %{_bindir}/gendiff
%attr(0755, rpm, rpm) %{_bindir}/rpm2cpio
%attr(0755, rpm, rpm) %{_bindir}/rpmdb
%attr(0755, rpm, rpm) %{_bindir}/rpmquery
%attr(0755, rpm, rpm) %{_bindir}/rpmsign
%attr(0755, rpm, rpm) %{_bindir}/rpmverify
%{_includedir}/rpm/
%attr(0755, rpm, rpm) %dir %{_libdir}/rpm/
%attr(0755, rpm, rpm) %{_libdir}/rpm/debugedit
%attr(0644, rpm, rpm) %{_libdir}/rpm/rpmrc
%{_mandir}/man8/rpm.8.gz
%{_mandir}/man8/rpm2cpio.8.gz
%{_mandir}/*/man8/rpm.8.gz
%{_mandir}/*/man8/rpm2cpio.8.gz
%attr(0644, rpm, rpm) %{_libdir}/rpm/macros
%attr(0755, rpm, rpm) %{_libdir}/rpm/config.guess
%attr(0755, rpm, rpm) %{_libdir}/rpm/config.sub
%attr(0755, rpm, rpm) %{_libdir}/rpm/mkinstalldirs
%attr(0755, rpm, rpm) %{_libdir}/rpm/rpm.*
%attr(0755, rpm, rpm) %{_libdir}/rpm/rpm2cpio.sh
%attr(0755, rpm, rpm) %{_libdir}/rpm/rpm[deiukqv]
%attr(0755, rpm, rpm) %{_libdir}/rpm/tgpg
%attr(0644, rpm, rpm) %{_libdir}/rpm/rpmpopt*
%ifarch i386 i486 i586 i686 athlon pentium3 pentium4
%attr(-, rpm, rpm) %{_libdir}/rpm/i[3456]86*
%attr(-, rpm, rpm) %{_libdir}/rpm/athlon*
%attr(-, rpm, rpm) %{_libdir}/rpm/pentium*
%endif
%ifarch x86_64
%attr(-, rpm, rpm) %{_libdir}/rpm/x86_64*
%endif
%attr(-, rpm, rpm) %{_libdir}/rpm/noarch*
%attr(0755, rpm, rpm) %dir /var/lib/rpm
%attr(0755, rpm, rpm) %dir /var/spool/repackage
%define rpmdbattr %attr(0644, rpm, rpm) %verify(not md5 size mtime) %ghost %config(missingok,noreplace)
%rpmdbattr %{_localstatedir}/lib/rpm/*
%rpmdbattr %{_libdir}/rpm/rpmdb_*

%files build
%defattr(-,root,root)
%dir %{_prefix}/src/rpm
%dir %{_prefix}/src/rpm/BUILD
%dir %{_prefix}/src/rpm/SPECS
%dir %{_prefix}/src/rpm/SOURCES
%dir %{_prefix}/src/rpm/SRPMS
%dir %{_prefix}/src/rpm/RPMS
%attr(0755, rpm, rpm) %{_bindir}/rpmbuild
%attr(0755, rpm, rpm) %{_libdir}/rpm/brp-*
%attr(0755, rpm, rpm) %{_libdir}/rpm/check-files
%attr(0755, rpm, rpm) %{_libdir}/rpm/config.site
%attr(0755, rpm, rpm) %{_libdir}/rpm/cross-build
%attr(0755, rpm, rpm) %{_libdir}/rpm/find-debuginfo.sh
%attr(0755, rpm, rpm) %{_libdir}/rpm/find-lang.sh
%attr(0755, rpm, rpm) %{_libdir}/rpm/find-prov.pl
%attr(0755, rpm, rpm) %{_libdir}/rpm/find-provides
%attr(0755, rpm, rpm) %{_libdir}/rpm/find-provides.perl
%attr(0755, rpm, rpm) %{_libdir}/rpm/find-req.pl
%attr(0755, rpm, rpm) %{_libdir}/rpm/find-requires
%attr(0755, rpm, rpm) %{_libdir}/rpm/find-requires.perl
%attr(0755, rpm, rpm) %{_libdir}/rpm/getpo.sh
%attr(0755, rpm, rpm) %{_libdir}/rpm/javadeps*
%attr(0755, rpm, rpm) %{_libdir}/rpm/magic
%attr(0755, rpm, rpm) %{_libdir}/rpm/magic.mgc
%attr(0755, rpm, rpm) %{_libdir}/rpm/magic.mime
%attr(0755, rpm, rpm) %{_libdir}/rpm/magic.mime.mgc
%attr(0755, rpm, rpm) %{_libdir}/rpm/mkinstalldirs
%attr(0755, rpm, rpm) %{_libdir}/rpm/executabledeps.sh
%attr(0755, rpm, rpm) %{_libdir}/rpm/libtooldeps.sh
%attr(0755, rpm, rpm) %{_libdir}/rpm/perldeps.pl
%attr(0755, rpm, rpm) %{_libdir}/rpm/*.prov
%attr(0755, rpm, rpm) %{_libdir}/rpm/*.req
%attr(0755, rpm, rpm) %{_libdir}/rpm/pkgconfigdeps.sh
%attr(0755, rpm, rpm) %{_libdir}/rpm/pythondeps.sh
%attr(0755, rpm, rpm) %{_libdir}/rpm/rpmdeps
%attr(0755, rpm, rpm) %{_libdir}/rpm/rpm[bt]
%attr(0755, rpm, rpm) %{_libdir}/rpm/symclash.*
%attr(0755, rpm, rpm) %{_libdir}/rpm/u_pkg.sh
%attr(0755, rpm, rpm) %{_libdir}/rpm/vpkg-provides.sh
%attr(0755, rpm, rpm) %{_libdir}/rpm/vpkg-provides2.sh
%attr(0755, rpm, rpm) %{_libdir}/rpm/config.guess
%attr(0755, rpm, rpm) %{_libdir}/rpm/config.sub
%{_mandir}/man1/gendiff.1*
%{_mandir}/*/man1/gendiff.1*
%{_mandir}/man8/rpmbuild.8*
%{_mandir}/*/man8/rpmbuild.8*
%{_mandir}/man8/rpmdeps.8*
%{_mandir}/*/man8/rpmdeps.8*

%files libs
%{_libdir}/librpm-4.4.*
%{_libdir}/librpm.*
%{_libdir}/librpmbuild-4.4.*
%{_libdir}/librpmbuild.*
%{_libdir}/librpmdb-4.4.*
%{_libdir}/librpmdb.*
%{_libdir}/librpmio-4.4.*
%{_libdir}/librpmio.*


%files python
%defattr(-, root, root)
%{_libdir}/python*/site-packages/rpm/

%files perl
%defattr(-, root, root)
# %{_libdir}/perl5/*/*/perllocal.pod
%{_libdir}/perl5/vendor_perl/*/*/RPM.pm
%{_libdir}/perl5/vendor_perl/*/*/auto/RPM/
%{_mandir}/man3/RPM.3*

%files -n popt -f popt.lang
%defattr(-, root, root)
%{_includedir}/popt.h
%{_libdir}/libpopt.*
%{_mandir}/man3/popt*
