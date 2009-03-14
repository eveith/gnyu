Name: libxcb
Version: 1.2
Release: 4ev
Summary: A programmatic interface to the X Window System Protocol
URL: http://xcb.freedesktop.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: ftp://xcb.freedesktop.org/dist/libxcb-%{version}.tar.bz2
Patch0: libxcb-1.1-abstract-socket.patch
Patch1: libxcb-1.1-no-pthread-stubs.patch
Patch2: libxcb-1.1-sloppy-lock.patch
BuildRequires(build,install): make
BuildRequires: pkg-config >= 0.9.0, gcc, python >= 2.5
BuildRequires: libxslt, doxygen, xcb-proto >= 1.1
BuildRequires: %{_libdir}/python%{_python_base_version}/site-packages/xcbgen
BuildRequires: libXdmcp, libXau >= 0.99.2

%description
The libxcb package provides an interface to the X Window System protocol,
which replaces the current Xlib interface. Xlib can also use XCB as a
transport layer, allowing software to make requests and receive responses with
both.


%prep
%setup -q
#%patch0 -p1
#%patch1 -p1
#%patch2 -p1


%build
%configure \
	--enable-xinput
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc COPYING README*
%doc %{_datadir}/doc/libxcb
%{_libdir}/libxcb*.*
%{_libdir}/pkgconfig/xcb*.pc
%{_includedir}/xcb/
