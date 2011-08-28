Name: satsolver
Version: 0.17.1
Release: 1.2
Summary: A package dependency solver using the Boolean Satisfiability approach
URL: git://gitorious.org/opensuse/sat-solver.git
Group: System Environment/Package Management/Libraries
License: BSD
Source: sat-solver-%{version}.tar.xz
Patch: rpm5.patch
BuildRequires: cmake >= 2.4.0, gcc
BuildRequires: doxygen
BuildRequires: eglibc-devel
BuildRequires: expat-devel, zlib-devel, check-devel
BuildRequires: ruby1.9-devel, rpm-devel >= 5.3.10
Requires: rpm = %(rpm --queryformat='%{VERSION}-%{RELEASE}' -q rpm)


%description
This is a package dependency solver that uses the Boolean Satisfiability
Problem approach to solve dependencies between packages.
See http://idea.opensuse.org/content/ideas/fast-installation-tool
for the motivation.


%files
%defattr(-, root, root)
%doc README LICENSE.BSD
%{_bindir}/deltainfoxml2solv
%{_bindir}/deptestomatic
%{_bindir}/dumpsolv
%{_bindir}/helix2solv
%{_bindir}/installcheck
%{_bindir}/mergesolv
%{_bindir}/repo2solv.sh
%{_bindir}/repomdxml2solv
%{_bindir}/rpmdb2solv
%{_bindir}/rpmmd2solv
%{_bindir}/rpms2solv
%{_bindir}/solv
%{_bindir}/susetags2solv
%{_bindir}/updateinfoxml2solv


%package devel
Summary: Development files for satsolver
Group: Development/Libraries


%description devel
This is a package dependency solver that uses the Boolean Satisfiability
Problem approach to solve dependencies between packages.
See http://idea.opensuse.org/content/ideas/fast-installation-tool
for the motivation.
The development package contains header files and static libraries needed to
compile programs that make use of the satsolver.


%files devel
%defattr(-, root, root)
%doc README LICENSE.BSD

%{_libdir}/libsatsolver.a
%{_libdir}/libsatsolverext.a

%dir %{_includedir}/satsolver
%dir %{_includedir}/satsolver/*.h


%prep
%setup -q -n 'sat-solver-%{version}'
#%patch0 -p1
%{__mkdir_p} build


%build
pushd build
%cmake -DRPM5=TRUE -DFEDORA=TRUE ..
%{__make} %{?_smp_mflags} VERBOSE=1
popd


%install
pushd build
%{__make} install DESTDIR='%{buildroot}'
popd


%check
%{__make} check ||:
