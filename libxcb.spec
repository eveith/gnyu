Name: libxcb
Version: 1.1
Release: 2ev
Summary: A programmatic interface to the X Window System Protocol
URL: http://xcb.freedesktop.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: ftp://xcb.freedesktop.org/dist/libxcb-%{version}.tar.bz2
Patch: %{name}-1.0-sloppy_lock-1.patch
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: coreutils, grep, sed, make, gcc, pkg-config, libxslt, doxygen
BuildRequires: xcb-proto >= 1.1, libXdmcp, libXau, libpthread-stubs

%description
The libxcb package provides an interface to the X Window System protocol,
which replaces the current Xlib interface. Xlib can also use XCB as a
transport layer, allowing software to make requests and receive responses with
both.


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
%doc COPYING README*
%doc %{_datadir}/doc/libxcb
%{_libdir}/libxcb*.*
%{_libdir}/pkgconfig/xcb*.pc
%{_includedir}/xcb/
