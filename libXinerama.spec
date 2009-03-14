Name: libXinerama
Version: 1.0.2
Release: 1ev
Summary: A library to combine several physical devices into one big screen
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: MSP Slackware
Source: http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, pkg-config, libX11, libXext

%description
Xinerama is a simple library designed to interface  the  Xinerama
Extension   for  retrieving  information  about  physical  output
devices which may be combined into a single logical X screen.


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
%{_libdir}/libXinerama*.*
%{_libdir}/pkgconfig/xinerama.pc
%{_mandir}/man3/Xinerama*.3*
