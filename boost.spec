Name: boost
Version: 1.42.0
%define name_version %(echo %{name}-%{version} | sed -e 's,[-.],_,g')
Release: 2.0ev
Summary: A set of free, peer-reviewed, portable C++ source libraries
URL: http://www.boost.org/
Group: System Environment/Libraries
License: Boost Software License 1.0
Vendor: GNyU-Linux
Source: http://sourceforge.net/projects/boost/boost/%{version}/%{name_version}.tar.bz2
Patch: %{name}-jam_src_build-gcc42.patch
Patch1: %{name}-use-rpm-optflags.patch
Patch2: %{name}-configure.patch
BuildRequires: make, gcc, python
BuildRequires: libgcc_s, libstdc++, zlib

%description


%package devel
Summary: Development headers for Boost
Group: Development/Libraries

%description devel
Header files used to build programs that make use of Boost.


%prep
%setup -q -n %{name_version}


%build
cc="${CC:-%{_target_platform}-gcc}"
cflags="${CFLAGS:-%{optflags}}"
cxxflags="${CXXFLAGS:-%{optflags}}"
export CC CFLAGS CXXFLAGS

./bootstrap.sh \
	--prefix='%{_prefix}' \
	--with-icu
./bjam %{?_smp_mflags} \
	--layout=tagged \
	threading=multi \
	variant=release \
	cflags="$cflags" \
	cxxflags="$cxxflags"


%install
./bjam install \
	--layout=tagged \
	--prefix='%{buildroot}%{_prefix}'


%post
%{__ldconfig}


%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc README.txt LICENSE*
%{_libdir}/libboost_*.a
%{_libdir}/libboost_*.so
%{_libdir}/libboost_*.so.%{version}


%files devel
%defattr(-, root, root)
%doc doc/html doc/images README.txt LICENSE* *.htm* *.css *.png
%dir %{_includedir}/boost
%{_includedir}/boost/*
