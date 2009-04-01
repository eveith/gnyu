Name: libX11
Version: 1.1.4
Release: 6ev
Summary: X11 client-side library
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/releases/individual/lib/libX11-%{version}.tar.bz2
Patch: %{name}-1.1.2-badargs-1.patch
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, pkg-config >= 0.9.0
BuildRequires: xorg-xproto >= 7.0.13, xorg-xcmiscproto, xorg-bigreqsproto
BuildRequires: xorg-xextproto, xtrans
BuildRequires: libXdmcp, libXau, libxcb >= 0.9.92
BuildConflicts: xorg-xproto > 7.0.13
Requires: xorg-fslayout >= 7.3

%description
This package provides the main client interface to the X Window System, 
and is otherwise known as 'Xlib'. It provides a complete API for the basic 
functions of the window system. 


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make_install} DESTDIR='%{buildroot}'


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc COPYING README AUTHORS
%{_includedir}/X11/ImUtil.h
%{_includedir}/X11/XKBlib.h
%{_includedir}/X11/Xcms.h
%{_includedir}/X11/Xlib-xcb.h
%{_includedir}/X11/Xlib.h
%{_includedir}/X11/XlibConf.h
%{_includedir}/X11/Xlibint.h
%{_includedir}/X11/Xlocale.h
%{_includedir}/X11/Xregion.h
%{_includedir}/X11/Xresource.h
%{_includedir}/X11/Xutil.h
%{_includedir}/X11/cursorfont.h
%dir %{_libdir}/X11
%doc %{_libdir}/X11/Xcms.txt
%{_libdir}/libX11-xcb.*
%{_libdir}/libX11.*
%{_libdir}/pkgconfig/x11-xcb.pc
%{_libdir}/pkgconfig/x11.pc
%{_datadir}/X11/XErrorDB
%{_datadir}/X11/XKeysymDB
%{_datadir}/X11/locale/
%doc %{_mandir}/man3/*.3*
