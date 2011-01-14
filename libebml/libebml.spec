Name: libebml
Version: 0.7.8
Release: 2ev
Summary: A C++ library to parse EBML files (like the Matroska codec)
URL: http://www.matroska.org/
Group: System Environment/Libraries
License: LGPL-2.1
Vendor: GNyU-Linux
Source: http://dl.matroska.org/downloads/%{name}/%{name}-%{version}.tar.bz2
BuildRequires: make, gcc-g++

%description
EBML was designed to be a simplified binary extension of XML for
the purpose of storing and manipulating data in a hierarchical
form with variable field lengths.
It uses the same paradigms as XML files, ie syntax and semantic
are separated. So a generic EBML library could read any format
based on it. The interpretation of data is up to a specific
application that knows how each elements (equivalent of XML tag)
has to be handled.

%prep
%setup -q


%build
pushd 'make/linux'
%{__make} %{?_smp_mflags} \
    CXX="${CXX:-%{_target_platform}-g++}" \
    CXXFLAGS="${CXXFLAGS:-%{optflags}}" \
    prefix="%{_prefix}" \
    staticlib sharedlib
popd


%install
pushd 'make/linux'
%{__make} %{?_smp_mflags} \
    CXX="${CXX:-%{_target_platform}-g++}" \
    CXXFLAGS="${CXXFLAGS:-%{optflags}}" \
    prefix="%{buildroot}/%{_prefix}" \
    install
popd


%post
%{__ldconfig}


%postun
%{__ldconfig}



%files
%defattr(-, root, root)
%doc LICENSE.LGPL
%dir %{_includedir}/ebml
%{_includedir}/ebml/*.h
%dir %{_includedir}/ebml/c
%{_includedir}/ebml/c/*.h
%{_libdir}/libebml.*
