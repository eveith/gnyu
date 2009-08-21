Name: libxkbfile
Version: 1.0.4
Release: 1ev
Summary: A library to read and manipulate keymaps for the xkb program
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: MSP Slackware
Source: http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, pkg-config, libX11

%description
XKBD is the X implementation of kbd, which is responsible for load keymaps
that allow to use different styles of keyboards and key maps.


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
%{_libdir}/libxkbfile*.*
%{_libdir}/pkgconfig/xkbfile.pc
%{_includedir}/X11/extensions/XKB*.h
%{_includedir}/X11/extensions/XKM*.h
