Name: libXinerama
Version: 1.0.3
Release: 2ev
Summary: A library to combine several physical devices into one big screen
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
BuildRequires: make, gcc, pkg-config >= 0.9.0
BuildRequires: xorg-xineramaproto, xorg-xextproto
BuildRequires: libX11, libXext

%description
Xinerama is a simple library designed to interface  the  Xinerama
Extension   for  retrieving  information  about  physical  output
devices which may be combined into a single logical X screen.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc COPYING README AUTHORS
%{_libdir}/libXinerama*.*
%{_libdir}/pkgconfig/xinerama.pc
%{_mandir}/man3/Xinerama*.3*
