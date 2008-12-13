Name: libmcs 
Version: 0.4.1
Release: 1ev
Summary: A configuration storage abstracting library
URL: http://sacredspiral.co.uk/~nenolod/mcs/
Group: System Environment/Libraries
License: BSD
Vendor: GNyU-Linux
Source: http://sacredspiral.co.uk/~nenolod/mcs/mcs-%{version}.tgz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, pkg-config

%description
mcs is a library and set of userland tools which abstract the storage of
configuration settings away from userland applications.
It is hoped that by using mcs, that the applications which use it will
generally have a more congruent feeling in regards to settings.
There have been other projects like this before (such as GConf), but unlike
those projects, mcs strictly handles abstraction. It does not impose any
specific data storage requirement, nor is it tied to any desktop environment
or software suite.


%prep
%setup -q -n mcs-%{version}


%build
%configure 
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR="${RPM_BUILD_ROOT}"


%post
%{__ldconfig}

%postun
%{__ldconfig}


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc AUTHORS COPYING GIT-Access README TODO
%{_bindir}/mcs*
%{_includedir}/libmcs/
%{_libdir}/libmcs.*
%{_libdir}/mcs/
%{_libdir}/pkgconfig/libmcs.pc
