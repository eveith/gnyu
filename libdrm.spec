Name: libdrm
Version: 2.4.5
Release: 4ev
Summary: Direct Rendering Manager library
URL: http://dri.freedesktop.org/
Group: System Environment/Libraries
License: MIT
Vendor: GNyU-Linux
Source: http://dri.freedesktop.org/libdrm/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, pkg-config, udev
Requires: pkg-config, udev

%description
DRI and DRM provides mechanics to draw directly on the hardware, which greatly
improves performance and is required if you want to use the 3D functions of
your graphics card.


%prep
%setup -q


%build
%configure \
	--enable-udev
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%{_includedir}/drm/
%{_includedir}/intel_bufmgr.h
%{_includedir}/xf86*.h
%{_libdir}/libdrm*.*
%{_libdir}/pkgconfig/libdrm.pc
%{_libdir}/pkgconfig/libdrm_intel.pc
