Name: libXtst
Version: 1.0.2
Release: 1ev
Summary: X11 Testing -- Resource extension library
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: MSP Slackware
Source: http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, pkg-config, x11-proto, libX11, libXext

%description
libXtst provides an X Window System client interface to the Record extension
to the X protocol. The Record extension allows X clients to synthesise input 
events, which is useful for automated testing.


%prep
%setup -q


%build
%configure
make %{_smp_mflags}


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc COPYING README AUTHORS
%{_libdir}/libXtst.*
%{_libdir}/pkgconfig/xtst.pc
%{_mandir}/man3/XTest*.3*
