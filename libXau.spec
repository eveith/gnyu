Name: libXau
Version: 1.0.3
Release: 1ev
Summary: A library implementing the X11 authentication protocol
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: MSP Slackware
Source: ftp://ftp.x.org/pub/individual/lib/libXau-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, x11-proto
Requires: pkg-config, x11-proto

%description
The libXau package contains a library implementing the X11 Authorization
Protocol. This is useful for restricting client access to the display.


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
%doc COPYING README
%{_libdir}/libXau.*
%{_includedir}/X11/Xauth.h
%{_libdir}/pkgconfig/xau.pc
%{_mandir}/man3/Xau*.3*
