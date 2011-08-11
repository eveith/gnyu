Name: rpm
Version: 5.4.1
Release: 2.0
Summary: The RPM Package Manager
URL: http://www.rpm5.org
Group: System Environment/Package Management
License: LGPL-2.1
Source0: http://rpm5.org/files/rpm/rpm-5.4/rpm-%{version}.tar.gz
Source1: cpu-os-macros.tar.gz
Source3: pcre-8.12.tar.bz2
Source4: macros-00-gnyu
Source5: macros-00-gnyu-paths
Patch0: pcre-pcreposix-glibc-conflict.patch
BuildRequires: grep, sed, make, pkg-config, gcc
BuildRequires: gettext-tools >= 0.16, bison
BuildRequires: eglibc-devel, libstdc++-devel, kernel-headers
BuildRequires: db-devel >= 5.1.19, popt-devel >= 1.15
BuildRequires: libgomp1 >= 4.5.0, beecrypt-devel >= 4.2.0
BuildRequires: neon-devel >= 0.27.0
BuildRequires: elfutils-libelf-devel, file-devel >= 4.0
BuildRequires: zlib-devel >= 1.2, bzip2-devel >= 1.0, xz-devel >= 4.999.9
BuildRequires: expat-devel, pcre-devel >= 7.0
BuildConflicts: m4 = 1.4.10
Obsoletes: rpm5 < %{version}-%{release}
Conflicts: rpm5 < %{version}-%{release}

%define rpm_uid 37
%define rpm_gid 7
%define with_perl 0
%define with_python 0
%define with_ruby 1

%if %with_perl
BuildRequires: perl >= 5.8.0
%endif

%if %with_python
BuildRequires: python >= 2.4
%endif

%if with_ruby
BuildRequires: ruby-devel >= 1.9.1
%endif


%description
The RPM Package Manager (RPM) is a powerful command line driven
package management system capable of installing, uninstalling,
verifying, querying, and updating software packages. Each software
package consists of an archive of files along with information about
the package like its version, a description, etc.


%define exeattr %attr(0755, rpm, rpm)
%define dbattr %attr(0644, rpm, rpm) %verify(not md5 size mtime) \
    %ghost %config(missingok, noreplace)


%files -f rpm.lang
%defattr(-, root, root)
%doc CHANGES ABOUT-NLS CREDITS COPYING.LIB NEWS README TODO
%doc doc/manual/[a-z]*
%attr(0755, rpm, rpm) %dir %{_sysconfdir}/rpm
%attr(0755, rpm, rpm) %dir %{_sysconfdir}/rpm/macros.d
%attr(0644, rpm, rpm) %{_sysconfdir}/rpm/macros.d/00-gnyu*

%{exeattr} %{_bindir}/rpm
%{exeattr} %{_bindir}/rpm2cpio
%{exeattr} %{_bindir}/rpmconstant

%{exeattr} %{_bindir}/multiarch-dispatch
%{exeattr} %{_bindir}/multiarch-platform

%doc %{_mandir}/man1/rpmgrep.1*
%doc %{_mandir}/man8/rpm.8*
%doc %{_mandir}/*/man8/rpm.8*
%doc %{_mandir}/man8/rpm2cpio.8*
%doc %{_mandir}/*/man8/rpm2cpio.8*
%doc %{_mandir}/man8/rpmconstant.8*
%doc %{_mandir}/man8/rpmmtree.8*

%attr(0755, rpm, rpm) %dir %{_libdir}/rpm

%attr(0644, rpm, rpm) %{_libdir}/rpm/macros
%attr(0755, rpm, rpm) %dir %{_libdir}/rpm/*-linux
%attr(0644, rpm, rpm) %{_libdir}/rpm/*-linux/macros
%attr(0755, rpm, rpm) %dir %{_libdir}/rpm/macros.d
%attr(0644, rpm, rpm) %{_libdir}/rpm/macros.d/cmake
%attr(0644, rpm, rpm) %{_libdir}/rpm/macros.d/gstreamer
%attr(0644, rpm, rpm) %{_libdir}/rpm/macros.d/java
%attr(0644, rpm, rpm) %{_libdir}/rpm/macros.d/kernel
%attr(0644, rpm, rpm) %{_libdir}/rpm/macros.d/libtool
%attr(0644, rpm, rpm) %{_libdir}/rpm/macros.d/mandriva
%attr(0644, rpm, rpm) %{_libdir}/rpm/macros.d/mono
%attr(0644, rpm, rpm) %{_libdir}/rpm/macros.d/perl
%attr(0644, rpm, rpm) %{_libdir}/rpm/macros.d/php
%attr(0644, rpm, rpm) %{_libdir}/rpm/macros.d/pkgconfig
%attr(0644, rpm, rpm) %{_libdir}/rpm/macros.d/python
%attr(0644, rpm, rpm) %{_libdir}/rpm/macros.d/ruby
%attr(0644, rpm, rpm) %{_libdir}/rpm/macros.d/selinux
%attr(0644, rpm, rpm) %{_libdir}/rpm/macros.d/tcl

%attr(0644, rpm, rpm) %{_libdir}/rpm/rpmpopt
%{_libdir}/rpm/cpuinfo.yaml

%attr(0755, rpm, rpm) %dir %{_libdir}/rpm/qf
%attr(0644, rpm, rpm) %{_libdir}/rpm/qf/*

%attr(0755, rpm, rpm) %dir %{_libdir}/rpm/helpers
%attr(0755, rpm, rpm) %{_libdir}/rpm/helpers/*

#%{exeattr} %{_libdir}/rpm/magic
#%{exeattr} %{_libdir}/rpm/magic.mgc
#%{exeattr} %{_libdir}/rpm/magic.mime
#%{exeattr} %{_libdir}/rpm/magic.mime.mgc
%{exeattr} %{_libdir}/rpm/rpm.*
%{exeattr} %{_libdir}/rpm/rpm2cpio
%{exeattr} %{_libdir}/rpm/rpmdb_loadcvt
%{exeattr} %{_libdir}/rpm/tgpg
%{exeattr} %{_libdir}/rpm/vcheck
%{exeattr} %{_libdir}/rpm/dbconvert.sh

%dir %{_libdir}/rpm/bin
%{exeattr} %{_libdir}/rpm/bin/mtree
#%{exeattr} %{_libdir}/rpm/bin/rpmkey
%{exeattr} %{_libdir}/rpm/bin/rpmrepo
%{exeattr} %{_libdir}/rpm/bin/rpmspecdump
%{exeattr} %{_libdir}/rpm/bin/wget

%dir %{_libdir}/rpm/lib

%attr(0755, rpm, rpm) %dir %{_localstatedir}/lib/rpm
%attr(0755, rpm, rpm) %dir %{_localstatedir}/spool/repackage
%{dbattr} %{_localstatedir}/lib/rpm/*


%post
%{__chown} rpm:rpm '%{_localstatedir}/lib/rpm'/*



%package libs
Summary:  Libraries for manipulating RPM packages
Group: System Environment/Package Management/Libraries
# XXX this Provides: is bogus, but getconf(...) needs to be bootstrapped.
Provides: getconf(GNU_LIBPTHREAD_VERSION) = NPTL
Requires: getconf(GNU_LIBPTHREAD_VERSION) = NPTL
Obsoletes: rpm5-libs < %{version}-%{release}
Conflicts: rpm5-libs < %{version}-%{release}


%description libs
This package contains the RPM shared libraries.


%post libs -p %{__ldconfig}
%postun libs -p %{__ldconfig}


%files libs
%defattr(-, root, root)
%{_libdir}/librpm-5.?.so
%{_libdir}/librpmconstant-5.?.so
%{_libdir}/librpmdb-5.?.so
%{_libdir}/librpmio-5.?.so
%{_libdir}/librpmmisc-5.?.so
%{_libdir}/librpmbuild-5.?.so


%package devel
Summary:  Development files for manipulating RPM packages
Group: System Environment/Package Management/Development
Requires: rpm = %{version}-%{release}
Requires: rpm-libs = %{version}-%{release}
Requires: getconf(GNU_LIBPTHREAD_VERSION) = NPTL
Requires: db-devel >= 5.1.19, popt-devel >= 1.15
Requires: libgomp1 >= 4.5.0, beecrypt-devel >= 4.2.0
Requires: neon-devel >= 0.27.0
Requires: elfutils-libelf-devel, file-devel >= 4.0
Requires: zlib-devel >= 1.2, bzip2-devel >= 1.0, xz-devel >= 4.999.9
Requires: expat-devel, pcre-devel >= 7.0
Obsoletes: rpm5-devel < %{version}-%{release}
Conflicts: rpm5-devel < %{version}-%{release}


%description devel
This package contains the RPM C library and header files. These
development files will simplify the process of writing programs that
manipulate RPM packages and databases. These files are intended to
simplify the process of creating graphical package managers or any
other tools that need an intimate knowledge of RPM packages in order
to function.
This package should be installed if you want to develop programs that
will manipulate RPM packages and databases.


%files devel
%defattr(-, root, root)
%dir %{_includedir}/rpm
%{_includedir}/rpm/*.h
%{_includedir}/multiarch-dispatch.h
%{_libdir}/librpm.a
%{_libdir}/librpm.la
%{_libdir}/librpm.so
%{_libdir}/librpmconstant.a
%{_libdir}/librpmconstant.la
%{_libdir}/librpmconstant.so
%{_libdir}/librpmdb.a
%{_libdir}/librpmdb.la
%{_libdir}/librpmdb.so
%{_libdir}/librpmio.a
%{_libdir}/librpmio.la
%{_libdir}/librpmio.so
%{_libdir}/librpmmisc.a
%{_libdir}/librpmmisc.la
%{_libdir}/librpmmisc.so
%{_libdir}/librpmbuild.a
%{_libdir}/librpmbuild.la
%{_libdir}/librpmbuild.so
%{_libdir}/pkgconfig/rpm.pc


%package build
Summary: Scripts and executable programs used to build packages
Group: System Environment/Package Management/Packaging
Requires: %{name} = %{version}-%{release}
Requires: bash, coreutils, findutils, which
Requires: tar, gzip, bip2, xz, cpio
Requires: diffutils, patch
Requires: file
Obsoletes: rpm5-build < %{version}-%{release}
Conflicts: rpm5-build < %{version}-%{release}


%description build
The rpm-build package contains the scripts and executable programs
that are used to build packages using the RPM Package Manager.


%files build
%defattr(-, root, root)
%{exeattr} %{_bindir}/gendiff
%{exeattr} %{_bindir}/rpmbuild

%{exeattr} %{_libdir}/rpm/brp-*
%{exeattr} %{_libdir}/rpm/check-files
%{exeattr} %{_libdir}/rpm/check-multiarch-files
%{exeattr} %{_libdir}/rpm/cross-build
%{exeattr} %{_libdir}/rpm/executabledeps.sh
%{exeattr} %{_libdir}/rpm/find-*
%{exeattr} %{_libdir}/rpm/gem_helper.rb
%{exeattr} %{_libdir}/rpm/getpo.sh
%{exeattr} %{_libdir}/rpm/http.req
%{exeattr} %{_libdir}/rpm/javadeps.sh
%{exeattr} %{_libdir}/rpm/libtooldeps.sh
%{exeattr} %{_libdir}/rpm/mono-find-*
%{exeattr} %{_libdir}/rpm/mkmultiarch
%{exeattr} %{_libdir}/rpm/osgideps.pl
%{exeattr} %{_libdir}/rpm/perl.prov
%{exeattr} %{_libdir}/rpm/perl.req
%{exeattr} %{_libdir}/rpm/perldeps.pl
%{exeattr} %{_libdir}/rpm/php.prov
%{exeattr} %{_libdir}/rpm/php.req
%{exeattr} %{_libdir}/rpm/pkgconfigdeps.sh
%{exeattr} %{_libdir}/rpm/pythondeps.sh
%{exeattr} %{_libdir}/rpm/pythoneggs.py
%{exeattr} %{_libdir}/rpm/rubygems.rb
%{exeattr} %{_libdir}/rpm/u_pkg.sh
%{exeattr} %{_libdir}/rpm/vpkg-provides.sh
%{exeattr} %{_libdir}/rpm/vpkg-provides2.sh

%attr(0644, rpm, rpm) %{_libdir}/rpm/macros.rpmbuild

%{exeattr} %{_libdir}/rpm/bin/debugedit
%{exeattr} %{_libdir}/rpm/bin/rpmcache
%{exeattr} %{_libdir}/rpm/bin/rpmcmp
%{exeattr} %{_libdir}/rpm/bin/rpmdeps
%{exeattr} %{_libdir}/rpm/bin/rpmdigest
%{exeattr} %{_libdir}/rpm/bin/abi-compliance-checker.pl
%{exeattr} %{_libdir}/rpm/bin/api-sanity-autotest.pl
%{exeattr} %{_libdir}/rpm/bin/chroot
%{exeattr} %{_libdir}/rpm/bin/cp
%{exeattr} %{_libdir}/rpm/bin/dbsql
%{exeattr} %{_libdir}/rpm/bin/find
%{exeattr} %{_libdir}/rpm/bin/install-sh
%{exeattr} %{_libdir}/rpm/bin/lua
%{exeattr} %{_libdir}/rpm/bin/luac
%{exeattr} %{_libdir}/rpm/bin/mkinstalldirs
%{exeattr} %{_libdir}/rpm/bin/rpmlua
%{exeattr} %{_libdir}/rpm/bin/rpmluac
%{exeattr} %{_libdir}/rpm/bin/sqlite3

%{exeattr} %{_libdir}/rpm/lib/liblua.a
%{exeattr} %{_libdir}/rpm/lib/liblua.la

%doc %{_mandir}/man1/gendiff.1*
%doc %{_mandir}/*/man1/gendiff.1*
%doc %{_mandir}/man8/rpmbuild.8*
%doc %{_mandir}/*/man8/rpmbuild.8*
%doc %{_mandir}/man8/rpmdeps.8*
%doc %{_mandir}/*/man8/rpmdeps.8*

%dir %{_prefix}/src/rpm
%dir %{_prefix}/src/rpm/BUILD
%dir %{_prefix}/src/rpm/SPECS
%dir %{_prefix}/src/rpm/SOURCES
%dir %{_prefix}/src/rpm/SRPMS
%dir %{_prefix}/src/rpm/RPMS


%if %with_perl
%package perl
Summary: Perl bindings to the RPM library
Group: System Environment/Package Management/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: rpm5-perl < %{version}-%{release}
Conflicts: rpm5-perl < %{version}-%{release}


%description perl
This package provides Perl bindings for RPM, allowing Perl scripts to query
the RPM database and use other RPM-specific functions.


%files perl
%defattr(-, root, root)
%{_libdir}/perl5/site_perl/*/*/RPM.pm
%dir %{_libdir}/perl5/site_perl/*/*/RPM
%{_libdir}/perl5/site_perl/*/*/RPM/*.pm
%dir %{_libdir}/perl5/site_perl/*/*/auto/RPM
%{_libdir}/perl5/site_perl/*/*/auto/RPM/RPM.so
%doc %{_mandir}/man3/RPM*.3pm*
%endif


%if %with_python
%package python
Summary: Python bindings for RPM
Group: System Environment/Package Management/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: rpm5-python < %{version}-%{release}
Conflicts: rpm5-python < %{version}-%{release}


%description python
This package provides Python bindings for RPM, allowing Python scripts to query
the RPM database and use other RPM-specific functions.


%files python
%defattr(-, root, root)
%dir %{_libdir}/python2.?/site-packages/rpm
%{_libdir}/python2.?/site-packages/rpm/__init__.py
%{_libdir}/python2.?/site-packages/rpm/_rpmmodule.so
%endif


%if %with_ruby
%package ruby
Summary: Ruby bindings to RPM
Group: System Environment/Package Mangement/Libraries
Requires: %{name} = %{version}-%{release}


%description ruby
This package provides Ruby bindings for RPM, allowing Ruby scripts to query
the RPM database and use other RPM-specific functions.


%files ruby
%defattr(-, root, root)

%endif


%prep
%setup -q -a 3
%{__mv} pcre-8.12 pcre
pushd pcre
%patch0 -p1
popd


%build
# Fix building beecrypt:
export LDFLAGS="$LDFLAGS -lgomp"

%configure \
    --with-bugreport='gnyu-packages@veith-m.de' \
    --with-libelf \
    %if %with_perl
        --with-perl \
    %endif
    %if with_python
        --with-python \
    %endif
    --with-popt=external \
    --with-zlib=external \
    --with-bzip2=external \
    --with-xz=external \
    --with-beecrypt=external \
    --with-expat=external \
    --with-neon=external \
    --with-file=external \
    --with-db=external \
    --with-sqlite=none \
    --without-sqlite \
    --with-dbsql=external \
    %if %with_ruby
        --with-ruby
    %endif
    --with-lua=internal \
    --with-syck=internal \
    --with-pcre=internal \
    --with-attr \
    --with-acl \
    --with-path-magic='%{_datadir}/misc/magic.mgc' \
    --with-path-macros='%{_libdir}/rpm/macros:%{_libdir}/rpm/%%{_target}/macros:%{_libdir}/rpm/%%{_target}-linux/macros:%{_sysconfdir}/rpm/%%{_target}/macros:%{_sysconfdir}/rpm/macros.d/*:~/.rpmmacros'
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%find_lang rpm

%{__mkdir_p} '%{buildroot}%{_sysconfdir}/rpm/macros.d'
%{__mkdir_p} '%{buildroot}%{_sysconfdir}/rpm/%{_target}'
%{__mkdir_p} '%{buildroot}%{_localstatedir}/spool/repackage'
%{__mkdir_p} '%{buildroot}%{_localstatedir}/lib/rpm'
%{__mkdir_p} '%{buildroot}%{_prefix}/src/rpm'/{RPMS,SRPMS,SPECS,BUILD,SOURCES}

for dbi in \
        Basenames Conflictname Dirnames Group Installtid Name Packages \
        Providename Provideversion Requirename Requireversion Triggername \
        Filemd5s Pubkeys Sha1header Sigmd5 \
        __db.001 __db.002 __db.003 __db.004 __db.005; do
    %{__touch} "%{buildroot}%{_localstatedir}/lib/rpm/${dbi}"
done
	
# Get rid of unneccessary files

%if %with_perl
    %{__find} '%{buildroot}/%{_libdir}/perl5' \
        -type f -a \( -name perllocal.pod -o -name .packlist \
        -o \( -name '*.bs' -a -empty \) \) -exec %{__rm} -vf '{}' ';'
%endif
%if %with_python
	%{__rm} -f '%{buildroot}/%{_libdir}'/python*/site-packages/*.{a,la}
	%{__rm} -f '%{buildroot}/%{_libdir}'/python*/site-packages/rpm/*.{a,la}
%endif

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'

# Remove installed RPM files that we do not package.

(
    pushd '%{buildroot}'

    for i in Specfile.pm cpanflute cpanflute2 rpmdiff \
            rpmdiff.cgi sql.prov sql.req tcl.req trpm; do
        %{__rm} -f "%{buildroot}%{_libdir}/rpm/${i}"
    done

    %{__rm_rf} '.%{_mandir}/man8'/rpmcache.8*
    %{__rm_rf} '.%{_mandir}/man8'/rpmgraph.8*
    %{__rm_rf} '.%{_mandir}/ja/man8'/rpmcache.8*
    %{__rm_rf} '.%{_mandir}/ja/man8'/rpmgraph.8*
    %{__rm_rf} '.%{_mandir}/pl/man8'/rpmcache.8*
    %{__rm_rf} '.%{_mandir}/pl/man8'/rpmgraph.8*
    %{__rm_rf} '.%{_mandir}'/{fr,ko}
    
    # If the internal popt has be used, remove installed files.

    %{__rm_rf} '.%{_includedir}'/popt.h
    %{__rm_rf} '.%{_libdir}'/libpopt.*
    %{__rm_rf} '.%{_libdir}'/pkgconfig/popt.pc
    %{__rm_rf} '.%{_datadir}'/locale/*/LC_MESSAGES/popt.mo
    %{__rm_rf} '.%{_mandir}'/man3/popt.3

    # Avoid collisions with the XAR and LZMA packages.
    
    %{__rm_rf} '.%{_mandir}'/man1/xar.1*
    %{__rm_rf} '.%{_bindir}'/xar
    %{__rm_rf} '.%{_includedir}'/xar
    %{__rm_rf} '.%{_libdir}'/libxar*
    
    %{__rm_rf} '.%{_bindir}'/lz*
    %{__rm_rf} '.%{_bindir}'/unlzma
    %{__rm_rf} '.%{_bindir}'/unxz
    %{__rm_rf} '.%{_bindir}'/xz*
    %{__rm_rf} '.%{_includedir}'/lzma*
    %{__rm_rf} '.%{_mandir}/man1'/lz*.1
    %{__rm_rf} '.%{_libdir}/pkgconfig'/liblzma*

    # PCRE leftovers

    %{__rm_rf} '.%{_datadir}/doc'
    %{__rm} '.%{_mandir}'/man?/pcre*
    %{__rm} '.%{_bindir}'/pcre*
    %{__rm} '.%{_includedir}'/pcre*
    %{__rm} '.%{_libdir}'/libpcre*
    %{__rm} '.%{_libdir}/pkgconfig'/*pcre*

    popd
)

# Install our own macro definitions

%{__install} -m0644 '%{SOURCE4}' \
    '%{buildroot}/%{_sysconfdir}/rpm/macros.d/00-gnyu'
%{__install} -m0644 '%{SOURCE5}' \
    '%{buildroot}/%{_sysconfdir}/rpm/macros.d/00-gnyu-paths'

pushd '%{buildroot}%{_libdir}/rpm'
%{__tar} -xzvf '%{SOURCE1}'
popd

# Don't require MDK::Common.

%{__sed} -i 's,use MDK::Common;,,' \
    '%{buildroot}%{_libdir}/rpm/check-multiarch-files'
