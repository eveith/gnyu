Name: libxkbfile
Version: 1.0.5
Release: 2ev
Summary: A library to read and manipulate keymaps for the xkb program
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
BuildRequires: make, gcc, pkg-config, libX11

%description
XKBD is the X implementation of kbd, which is responsible for load keymaps
that allow to use different styles of keyboards and key maps.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR="${RPM_BUILD_ROOT}"


%post
%{__ldconfig}


%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc COPYING README AUTHORS
%{_libdir}/libxkbfile*.*
%{_libdir}/pkgconfig/xkbfile.pc
%{_includedir}/X11/extensions/XKB*.h
%{_includedir}/X11/extensions/XKM*.h
