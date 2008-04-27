Name: libxcb
Version: 1.0
Release: 1ev
Summary: A programmatic interface to the X Window System Protocol
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: MSP Slackware
Source: ftp://ftp.x.org/pub/current/src/extras/libxcb-%{version}.tar.bz2
Patch: %{name}-1.0-sloppy_lock-1.patch
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, xcb-proto, libXdmcp, libXau, pkg-config, libxslt
BuildRequires: doxygen, libpthread-stubs

%description
The libxcb package provides an interface to the X Window System protocol,
which replaces the current Xlib interface. Xlib can also use XCB as a
transport layer, allowing software to make requests and receive responses with
both.


%prep
%setup -q
%patch0 -p1


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
%doc COPYING README*
%doc %{_datadir}/doc/libxcb
%{_libdir}/libxcb*.*
%{_libdir}/pkgconfig/xcb*.pc
%{_includedir}/xcb/
