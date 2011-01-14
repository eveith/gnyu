Name: libXcursor
Version: 1.1.9
Release: 2ev
Summary: The X Cursor management library
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
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
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc COPYING README AUTHORS
%{_includedir}/X11/Xcursor/
%{_libdir}/libXcursor*.*
%{_libdir}/pkgconfig/xcursor.pc
%doc %{_mandir}/man3/Xcursor*.3*
