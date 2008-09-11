Name: libXpm
Version: 3.5.6
Release: 1ev
Summary: Library for the X Pixmap image format
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: MSP Slackware
Source: http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, pkg-config, x11-proto
BuildRequires: libICE, libSM, libX11, libXau, libXdmcp, libXext

%description
XPM is an image format like PNG or JPEG. It comes with X11 and is mainly used
for icons.


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
%{_bindir}/?xpm
%{_includedir}/X11/xpm.h
%{_libdir}/libXpm*.*
%{_libdir}/pkgconfig/xpm.pc
%{_mandir}/man1/?xpm.1*
