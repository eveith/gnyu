Name: xcb-proto
Version: 1.0
Release: 1ev
Summary: XML-XCB protocol descriptions for libxcb
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: MSP Slackware
Source: ftp://ftp.x.org/pub/current/src/extras/xcb-proto-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, libxml2
Requires: pkg-config

%description
The xcb-proto package provides the XML-XCB protocol descriptions that libxcb
uses to generate the majority of its code and API. 


%prep
%setup -q


%build
%configure
make %{_smp_mflags}


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"

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
%doc README COPYING*
%{_datadir}/xcb/
%{_libdir}/pkgconfig/xcb-proto.pc
