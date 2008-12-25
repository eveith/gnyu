Name: rpm5
Version: 5.1.6
Release: 2ev
Summary: The RPM Package Manager
URL: http://www.rpm5.org/
Group: System Environment/Base
License: LGPL-2.1
Vendor: GNyU-Linux
Source0: http://rpm5.org/files/rpm/rpm-5.1/rpm-%{version}.tar.gz
Source1: %{name}-gnyu-macros
BuildRequires: make, gcc, python >= 2.4, perl >= 5.6, popt >= 1.9
BuildRequires: beecrypt >= 4.0, uuid1, openssl >= 0.9.8, neon >= 0.26.0
BuildRequires: gettext >= 0.16, pcre >= 7.0, elfutils-libelf, bzip2, zlib
BuildRequires: sqlite, pkg-config, expat, libxml2
BuildConflicts: m4 = 1.4.10
Provides: rpm = %{version}-%{release}
Obsoletes: rpm < %{version}-%{release}, rpm-libs < %{version}-%{release}
%define rpm_uid 37
%define rpm_gid 7

%description
The RPM Package Manager (RPM) is a powerful command line driven
package management system capable of installing, uninstalling,
verifying, querying, and updating software packages. Each software
package consists of an archive of files along with information about
the package like its version, a description, etc.


%package build
Summary: Scripts and executable programs used to build packages
Group: Development/Tools
Requires: %{name} = %{version}-%{release}
Requires: bash, coreutils, tar, gzip, bzip2, lzma, patch, diffutils
Requires: findutils, grep, sed, gawk
Provides: rpm-build = %{version}-%{release}
Obsoletes: rpm-build < %{version}-%{release}, rpm-libs < %{version}

%description build
The rpm-build package contains the scripts and executable programs
that are used to build packages using the RPM Package Manager.


%package perl
Summary: Perl bindings to the RPM library
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
Provides: rpm-perl = %{version}-%{release}
Obsoletes: rpm-perl < %{version}-%{release}

%description perl
This package provides Perl bindings for RPM, allowing Perl scripts to query
the RPM database and use other RPM-specific functions.


%package python
Summary: Python bindings for RPM
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
Provides: rpm-python = %{version}-%{release}
Obsoletes: rpm-python < %{version}-%{release}

%description python
This package provides Python bindings for RPM, allowing Python scripts to query
the RPM database and use other RPM-specific functions.


%prep
%setup -q -n 'rpm-%{version}'


%build
%configure \
	--with-libelf \
	--with-perl \
	--with-python \
	--with-zlib \
	--with-bzip2 \
	--with-lzma \
	--with-beecrypt \
	--with-file=internal \
	--with-db=internal \
	--with-sqlite=external \
	--with-db-largefile \
	--with-dbapi=db \
	--with-lua=internal \
	--with-pcre \
	--with-xar=internal \
	--with-path-macros='%{_libdir}/rpm/macros:%{_sysconfdir}/rpm/macros.d/*:~/.rpmmacros' \
	--with-db-tools-integrated \
	--enable-build-pic \
	--enable-build-pie 
%{__make} %{?_smp_mflags}


%install
%{__make_install} DESTDIR='%{buildroot}'
%find_lang rpm

%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/rpm/macros.d'
%{__mkdir_p} '%{buildroot}/%{_localstatedir}/spool/repackage'
%{__mkdir_p} '%{buildroot}/%{_localstatedir}/lib/rpm'
%{__mkdir_p} '%{buildroot}/%{_prefix}/src/rpm'/{RPMS,SRPMS,SPECS,BUILD,SOURCES}
for dbi in \
	Basenames Conflictname Dirnames Group Installtid Name Packages \
	Providename Provideversion Requirename Requireversion Triggername \
	Filemd5s Pubkeys Sha1header Sigmd5 \
	__db.001 __db.002 __db.003 __db.004 __db.005
do
    touch "%{buildroot}/%{_localstatedir}/lib/rpm/${dbi}"
done

# Get rid of unneccessary files
find '%{buildroot}/%{_libdir}/perl5' \
	-type f -a \( -name perllocal.pod -o -name .packlist \
    -o \( -name '*.bs' -a -empty \) \) -exec %{__rm} -vf '{}' ';'
%{__rm} -f '%{buildroot}/%{_libdir}'/python*/site-packages/*.{a,la}
%{__rm} -f '%{buildroot}/%{_libdir}'/python*/site-packages/rpm/*.{a,la}
[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'
find '%{buildroot}/%{_mandir}' -name rpmgraph\* -exec %{__rm} '{}' \;
%{__rm} -f '%{buildroot}/%{_libdir}/rpm'/{Specfile.pm,cpanflute,cpanflute2,rpmdiff,rpmdiff.cgi,sql.prov,sql.req,tcl.req,trpm}

# Avoid collisions with xar package, XAR is compiled in and not needed
%{__rm} -f '%{buildroot}/%{_bindir}/xar'
%{__rm} -f '%{buildroot}/%{_mandir}'/man1/xar.1*
%{__rm} -f '%{buildroot}/%{_libdir}'/libxar*
%{__rm} -rf '%{buildroot}/%{_includedir}/xar'

# Install our own macro definitions
%{__install} -m0644 '%{SOURCE1}' \
	'%{buildroot}/%{_sysconfdir}/rpm/macros.d/00-gnyu'


%pre
if [[ "${1}" -eq 1 ]]
then
	userdel rpm > /dev/null 2>&1 ||:
	groupdel rpm > /dev/null 2>&1 ||:
	groupadd -g '%{rpm_gid}' rpm
	useradd \
		-u '%{rpm_uid}' \
		-g '%{rpm_gid}' \
		-c 'RPM database owner' \
		-s /sbin/nologin \
		-d '%{_localstatedir}/lib/rpm' \
		rpm
fi


%post
%{__ldconfig}
%{__chown} rpm:rpm '%{_localstatedir}'/lib/rpm/*

%postun
%{__ldconfig}
if [[ "${1}" -eq 0 ]]
then
	userdel rpm
	groupdel rpm
fi
exit 0


%files -f rpm.lang
%defattr(-, root, root)
%doc CHANGES ABOUT-NLS CREDITS COPYING.LIB NEWS README TODO
%doc doc/manual/[a-z]*
%attr(0755, rpm, rpm) %dir %{_sysconfdir}/rpm
%attr(0755, rpm, rpm) %dir %{_sysconfdir}/rpm/macros.d
%attr(0644, rpm, rpm) %{_sysconfdir}/rpm/macros.d/00-gnyu
%define exeattr %attr(0755, rpm, rpm)
%define dbattr %attr(0644, rpm, rpm) %verify(not md5 size mtime) \
	%ghost %config(missingok, noreplace)
%{exeattr} %{_bindir}/rpm
%{exeattr} %{_bindir}/rpm2cpio
%{exeattr} %{_bindir}/rpmcache
%{exeattr} %{_bindir}/rpmconstant
%{exeattr} %{_bindir}/rpmgrep
%{exeattr} %{_bindir}/rpmmtree
%{_libdir}/librpm*.*
%{_libdir}/pkgconfig/rpm.pc
%dir %{_includedir}/rpm
%{_includedir}/rpm/*.h
%doc %{_mandir}/man1/rpmgrep.1*
%doc %{_mandir}/man8/rpm.8*
%doc %{_mandir}/*/man8/rpm.8*
%doc %{_mandir}/man8/rpm2cpio.8*
%doc %{_mandir}/*/man8/rpm2cpio.8*
%doc %{_mandir}/man8/rpmcache.8*
%doc %{_mandir}/*/man8/rpmcache.8*
%doc %{_mandir}/man8/rpmconstant.8*
%doc %{_mandir}/man8/rpmmtree.8*
%attr(0755, rpm, rpm) %dir %{_libdir}/rpm
%attr(0644, rpm, rpm) %{_libdir}/rpm/macros
%attr(0644, rpm, rpm) %{_libdir}/rpm/rpmpopt
%{exeattr} %{_libdir}/rpm/db_*
%{exeattr} %{_libdir}/rpm/magic
%{exeattr} %{_libdir}/rpm/magic.mgc
%{exeattr} %{_libdir}/rpm/magic.mime
%{exeattr} %{_libdir}/rpm/magic.mime.mgc
%{exeattr} %{_libdir}/rpm/rpm.*
%{exeattr} %{_libdir}/rpm/rpm2cpio
%{exeattr} %{_libdir}/rpm/rpmdb_loadcvt
%{exeattr} %{_libdir}/rpm/tgpg
%{exeattr} %{_libdir}/rpm/vcheck
%attr(0755, rpm, rpm) %dir %{_localstatedir}/lib/rpm
%attr(0755, rpm, rpm) %dir %{_localstatedir}/spool/repackage
%{dbattr} %{_localstatedir}/lib/rpm/*

%files build
%defattr(-, root, root)
%{exeattr} %{_bindir}/gendiff
%{exeattr} %{_bindir}/rpmbuild
%{exeattr} %{_bindir}/rpmdigest
%{exeattr} %{_bindir}/rpmrepo
%{exeattr} %{_libdir}/rpm/brp-*
%{exeattr} %{_libdir}/rpm/check-files
%{exeattr} %{_libdir}/rpm/cross-build
%{exeattr} %{_libdir}/rpm/debugedit
%{exeattr} %{_libdir}/rpm/executabledeps.sh
%{exeattr} %{_libdir}/rpm/find-*
%{exeattr} %{_libdir}/rpm/getpo.sh
%{exeattr} %{_libdir}/rpm/http.req
%{exeattr} %{_libdir}/rpm/install-sh
%{exeattr} %{_libdir}/rpm/javadeps.sh
%{exeattr} %{_libdir}/rpm/libtooldeps.sh
%{exeattr} %{_libdir}/rpm/mkinstalldirs
%{exeattr} %{_libdir}/rpm/mono-find-*
%{exeattr} %{_libdir}/rpm/osgideps.pl
%{exeattr} %{_libdir}/rpm/perl.prov
%{exeattr} %{_libdir}/rpm/perl.req
%{exeattr} %{_libdir}/rpm/perldeps.pl
%{exeattr} %{_libdir}/rpm/php.prov
%{exeattr} %{_libdir}/rpm/php.req
%{exeattr} %{_libdir}/rpm/pkgconfigdeps.sh
%{exeattr} %{_libdir}/rpm/pythondeps.sh
%{exeattr} %{_libdir}/rpm/rpmcmp
%{exeattr} %{_libdir}/rpm/u_pkg.sh
%{exeattr} %{_libdir}/rpm/vpkg-provides.sh
%{exeattr} %{_libdir}/rpm/vpkg-provides2.sh
%{exeattr} %{_libdir}/rpm/rpmdeps
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

%files perl
%defattr(-, root, root)
%{_libdir}/perl5/site_perl/*/*/RPM.pm
%dir %{_libdir}/perl5/site_perl/*/*/RPM
%{_libdir}/perl5/site_perl/*/*/RPM/*.pm
%dir %{_libdir}/perl5/site_perl/*/*/auto/RPM
%{_libdir}/perl5/site_perl/*/*/auto/RPM/RPM.so
%doc %{_mandir}/man3/RPM*.3pm*

%files python
%defattr(-, root, root)
%dir %{_libdir}/python2.?/site-packages/rpm
%{_libdir}/python2.?/site-packages/rpm/__init__.py
%{_libdir}/python2.?/site-packages/rpm/_rpmmodule.so
