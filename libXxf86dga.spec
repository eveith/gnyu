Name: libXxf86dga
Version: 1.0.2
Release: 2ev
Summary: X11 Direct Graphics Access extension library
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, pkg-config, xorg-proto, libX11, libXext

%description
libXxf86dga provides the XFree86-DGA extension, which allows direct graphics
access to a framebuffer-like region, and also allows relative mouse reporting,
et al. It is mainly used by games and emulators for games.


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
%doc COPYING
%{_libdir}/libXxf86dga.*
%{_libdir}/pkgconfig/xxf86dga.pc
%doc %{_mandir}/man3/XDGA*.3*
%doc %{_mandir}/man3/XF86DGA.3*
%doc %{_mandir}/man3/XFree86-DGA.3*
