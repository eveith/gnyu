Name: libICE
Version: 1.0.3
Release: 1ev
Summary: X Inter Client Exchange Library
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: MSP Slackware
Source: http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, pkg-config, x11-proto, xtrans

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
%{_includedir}/X11/ICE/
%{_libdir}/libICE*.*
%{_libdir}/pkgconfig/ice.pc
