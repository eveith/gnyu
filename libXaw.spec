Name: libXaw
Version: 1.0.3
Release: 1ev
Summary: The X Athena Widgets Library
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: MSP Slackware
Source: http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, pkg-config, x11-proto, libXt
BuildRequires: libICE, libSM, libX11, libXau, libXext, libXmu, libXp, libXpm

%description
Xaw is a widget set based on the X Toolkit Intrinsics (Xt) Library.


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
%{_includedir}/X11/Xaw/
%{_libdir}/libXaw*.*
%{_libdir}/pkgconfig/xaw*.pc
%{_mandir}/man3/Xaw.3*
%{_datadir}/aclocal/xaw.m4
