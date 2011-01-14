Name: libXau
Version: 1.0.4
Release: 2ev
Summary: A library implementing the X11 authentication protocol
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: ftp://ftp.x.org/pub/individual/lib/libXau-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, pkg-config >= 0.9.0, xorg-xproto

%description
The libXau package contains a library implementing the X11 Authorization
Protocol. This is useful for restricting client access to the display.


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
%doc COPYING README
%{_libdir}/libXau.*
%{_includedir}/X11/Xauth.h
%{_libdir}/pkgconfig/xau.pc
%doc %{_mandir}/man3/Xau*.3*
