Name: libXcursor
Version: 1.1.8
Release: 1ev
Summary: The X Cursor management library
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: MSP Slackware
Source: http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, pkg-config, x11-proto
BuildRequires: libXfixes, libXrender, libX11

%description
Xcursor  is  a simple library designed to help locate and load cursors.
Cursors can be loaded from files or memory.  A library of  common  cur-
sors  exists  which  map  to  the standard X cursor names.  Cursors can
exist in several sizes and the library  automatically  picks  the  best
size.



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
%{_includedir}/X11/Xcursor/
%{_libdir}/libXcursor*.*
%{_libdir}/pkgconfig/xcursor.pc
%{_mandir}/man3/Xcursor*.3*
