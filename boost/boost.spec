Name: boost
Version: 1.47.0
%define name_version %(echo %{name}-%{version} | sed -e 's,[-.],_,g')
Release: 1.0
Summary: A set of free, peer-reviewed, portable C++ source libraries
URL: http://www.boost.org/
Group: System Environment/Libraries
License: Boost Software License 1.0
Source: http://sourceforge.net/projects/boost/boost/%{version}/%{name_version}.tar.bz2
BuildRequires: grep, sed, make
BuildRequires: gcc
BuildRequires: libstdc++-devel, expat-devel
BuildRequires: zlib-devel, bzip2-devel, xz-devel
BuildRequires: python-devel
Requires: libboost%{version}


%description
Boost provides free peer-reviewed portable C++ source libraries.  These
libraries work well with the C++ Standard Library. Boost libraries are
intended to be widely useful, and usable across a broad spectrum of
applications.


%files
%defattr(-, root, root)
%doc LICENSE*



%package devel
Summary: Development headers for Boost
Group: Development/Libraries


%description devel
Header files used to build programs that make use of Boost.


%files devel
%defattr(-, root, root)
%doc doc/html doc/images LICENSE* *.htm* *.css *.png

%{_libdir}/libboost_*.a
%{_libdir}/libboost_*.so

%dir %{_includedir}/boost
%{_includedir}/boost/*


%package -n libboost%{version}
Summary: A set of free, peer-reviewed, portable C++ utility libraries
Group: System Environment/Libraries


%description -n libboost%{version}
Boost provides free peer-reviewed portable C++ source libraries.  These
libraries work well with the C++ Standard Library. Boost libraries are
intended to be widely useful, and usable across a broad spectrum of
applications.


%files -n libboost%{version}
%defattr(-, root, root)
%doc LICENSE*
%{_libdir}/libboost_*.so.%{version}


%post -n libboost%{version} -p %{__ldconfig}
%postun -n libboost%{version} -p %{__ldconfig}


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
	--layout=system \
	threading=multi \
	variant=release \
    link=shared \
	cflags="$cflags" \
	cxxflags="$cxxflags"


%install
cc="${CC:-%{_target_platform}-gcc}"
cflags="${CFLAGS:-%{optflags}}"
cxxflags="${CXXFLAGS:-%{optflags}}"
export CC CFLAGS CXXFLAGS

./bjam install \
	--prefix='%{buildroot}%{_prefix}' \
	--layout=system \
	threading=multi \
	variant=release \
    link=shared \
	cflags="$cflags" \
	cxxflags="$cxxflags"
