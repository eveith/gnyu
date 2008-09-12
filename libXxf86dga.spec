Name: libXxf86dga
Version: 1.0.1
Release: 1ev
Summary: X11 Direct Graphics Access extension library
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: MSP Slackware
Source: http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, pkg-config, x11-proto, libX11, libXext

%description
libXxf86dga provides the XFree86-DGA extension, which allows direct graphics
access to a framebuffer-like region, and also allows relative mouse reporting,
et al. It is mainly used by games and emulators for games.


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
%doc COPYING
%{_libdir}/libXxf86dga.*
%{_libdir}/pkgconfig/xxf86dga.pc
%{_mandir}/man3/XDGA*.3x*
%{_mandir}/man3/XF86DGA.3x*
%{_mandir}/man3/XFree86-DGA.3x*
