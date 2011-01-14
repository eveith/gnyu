Name: libXrandr
Version: 1.2.2
Release: 1ev
Summary: X Resize, Rotate and Reflection extension library
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: MSP Slackware
Source: http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, pkg-config, x11-proto
BuildRequires: libX11, libXext, libXrender

%description
libXrandr provides an X Window System client interface to the RandR extension
to the X protocol. The RandR extension allows for run-time configuration of 
display attributes such as resolution, rotation, and reflection.


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
%{_libdir}/libXrandr*.*
%{_libdir}/pkgconfig/xrandr.pc
%{_includedir}/X11/extensions/Xrandr.h
%{_mandir}/man3/XRR*.3*
%{_mandir}/man3/Xrandr.3*
