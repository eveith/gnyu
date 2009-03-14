Name: libICE
Version: 1.0.5
Release: 3ev
Summary: X Inter Client Exchange Library
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, pkg-config >= 0.9.0
BuildRequires: xorg-xproto, xtrans

%description
Based on X authentication, the ICE protocol allows X clients to exchange
messages of every kind, either locally via sockets or over network by TCP/IP.


%prep
%setup -q


%build
%configure \
	--enable-unix-transport \
	--enable-tcp-transport \
	--enable-IPv6
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
%{_includedir}/X11/ICE/
%{_libdir}/libICE*.*
%{_libdir}/pkgconfig/ice.pc
