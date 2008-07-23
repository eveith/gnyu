Name: libxcb
Version: 1.1
Release: 3ev
Summary: A programmatic interface to the X Window System Protocol
URL: http://xcb.freedesktop.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: ftp://xcb.freedesktop.org/dist/libxcb-%{version}.tar.bz2
Patch0: libxcb-1.1-abstract-socket.patch
Patch1: libxcb-1.1-no-pthread-stubs.patch
Patch2: libxcb-1.1-sloppy-lock.patch
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires(prep,build,install): coreutils, pkg-config
BuildRequires(build,install): make, grep, sed
BuildRequires(build): gcc, libxslt, doxygen, xcb-proto >= 1.1
BuildRequires(build): libXdmcp, libXau

%description
The libxcb package provides an interface to the X Window System protocol,
which replaces the current Xlib interface. Xlib can also use XCB as a
transport layer, allowing software to make requests and receive responses with
both.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1


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
