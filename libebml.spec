Name: libebml
Version: 0.7.7
Release: 1ev
Summary: A C++ library to parse EBML files (like the Matroska codec)
URL: http://www.matroska.org/
Group: System Environment/Libraries
License: LGPL
Vendor: MSP Slackware
Source: http://dl.matroska.org/downloads/%{name}/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
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
make \
	CXX="%{_target_platform}-g++" \
	CXXFLAGS="$RPM_OPT_FLAGS" \
	prefix="%{_prefix}" \
	staticlib sharedlib
popd


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
pushd 'make/linux'
make \
	CXX="%{_target_platform}-gcc" \
	CXXFLAGS="$RPM_OPT_FLAGS" \
	prefix="${RPM_BUILD_ROOT}/%{_prefix}" \
	install
popd


[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc LICENSE.LGPL
%{_includedir}/ebml/
%{_libdir}/libebml.*
