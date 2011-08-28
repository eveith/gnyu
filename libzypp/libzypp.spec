Name: libzypp
Version: 9.9.2
Release: 1.1
Summary: Package, Patch, Pattern, and Product Management
URL: http://doc.opensuse.org/projects/libzypp
Group: System Environment/Package Management
License: GPL-2.0
Source0: %{name}-%{version}.tar.xz
Patch0: rpm5.patch
Patch1: fix-for-rpm-4.9.patch
Patch2: rpm5-no-rpmdbinit.patch
Patch3: fix_for_compile_wth_gcc-4.6.0.patch
Patch4: libzypp-compatargs.patch
BuildRequires: cmake >= 2.6, pkg-config, make
BuildRequires: gcc, gcc-g++
BuildRequires: eglibc-devel, libstdc++-devel, boost-devel
BuildRequires: rpm-devel >= 5.0.0, db-devel, satsolver-devel >= 0.14.17
BuildRequires: zlib-devel
BuildRequires: libudev-devel
BuildRequires: openssl-devel, curl-devel
BuildRequires: expat-devel, libxml2-devel
BuildRequires: doxygen


%description
libzypp provides all the functionality for a package manager:
  - An API for package repository management, supporting most common
    repository metadata formats and signed repositories.
  - An API for solving packages, products, patterns and patches (installation,
    removal, update and distribution upgrade operations) dependencies, with
    additional features like locking.
  - An API for commiting the transaction to the system over a rpm target.
    Supporting deltarpm calculation, media changing and installation order
    calculation.
  - An API for browsing available and installed software, with some facilities
    for programs with an user interface.
  - A suite of maintained solving testcases representing common and uncommon
    operations on Linux software management


%files -f zypp.lang
%defattr(-, root, root)
%dir %{_sysconfdir}/zypp
%dir %{_sysconfdir}/zypp/repos.d
%dir %{_sysconfdir}/zypp/services.d
%config(noreplace) %{_sysconfdir}/zypp/zypp.conf
%config(noreplace) %{_sysconfdir}/zypp/systemCheck
%config(noreplace) %{_sysconfdir}/logrotate.d/zypp-history.lr

%{_bindir}/package-manager
%{_bindir}/package-manager-su
%{_bindir}/zypp-CheckAccessDeleted

%dir %{_localstatedir}/lib/zypp
%dir %{_localstatedir}/log/zypp
%dir %{_localstatedir}/cache/zypp

%dir %{_prefix}/lib/zypp
%{_prefix}/lib/zypp/notify-message

%dir %{_datadir}/zypp
%dir %{_datadir}/zypp/schema
%dir %{_datadir}/zypp/schema/yum
%{_datadir}/zypp/schema/yum/*.rng

%{_libdir}/libzypp*so.*

%doc %{_mandir}/man5/locks.5.*


%post
%{__ldconfig}
[ -f '%{_localstatedir}/cache/zypp/zypp.db' ] \
    && %{__rm} '%{_localstatedir}/cache/zypp/zypp.db'
exit 0


%postun -p %{__ldconfig}


%package devel
Summary: Development files for libzypp
Group: System Environment/Package Management/Development
Requires: pkg-config


%description devel
libzypp provides functionality for a package manager, such as repository
management, installing packages, etc.
This package contains the development files needed for compiling applications
that make use of libzypp.


%files devel
%defattr(-,root,root)
%{_libdir}/libzypp.so
%{_includedir}/zypp
%{_datadir}/cmake/Modules/*
%{_libdir}/pkgconfig/libzypp.pc


%prep
%setup -q
%patch0 -p1
%patch2 -p1
%patch4 -p1


%build
%{__mkdir} 'build'
pushd 'build'
%{cmake} ..
%{__make} %{?_smp_mflags} V=1
%{__make} -C po %{?_smp_mflags} translations
popd


%install
pushd 'build'
%{__make} install DESTDIR='%{buildroot}'
%{__make} -C po install DESTDIR='%{buildroot}'
popd

%find_lang zypp

%{__mkdir_p} '%{buildroot}%{_sysconfdir}/zypp/repos.d'
%{__mkdir_p} '%{buildroot}%{_sysconfdir}/zypp/services.d'
%{__mkdir_p} '%{buildroot}%{_prefix}/lib/zypp'
%{__mkdir_p} '%{buildroot}%{_prefix}/lib/zypp/plugins'
%{__mkdir_p} '%{buildroot}%{_prefix}/lib/zypp/plugins/commit'
%{__mkdir_p} '%{buildroot}%{_prefix}/lib/zypp/plugins/services'
%{__mkdir_p} '%{buildroot}%{_prefix}/lib/zypp/plugins/system'
%{__mkdir_p} '%{buildroot}%{_prefix}/lib/zypp/plugins/urlresolver'
%{__mkdir_p} '%{buildroot}%{_localstatedir}/lib/zypp'
%{__mkdir_p} '%{buildroot}%{_localstatedir}/log/zypp'
%{__mkdir_p} '%{buildroot}%{_localstatedir}/cache/zypp'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%check
pushd 'build'
%{__make} -C tests ||:
pushd 'tests'
LD_LIBRARY_PATH="${PWD}/../zypp:${LD_LIBRARY_PATH}" ctest . ||:
popd
popd
