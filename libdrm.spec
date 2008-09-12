Name: libdrm
Version: 2.3.0
Release: 1ev
Summary: Direct Rendering Manager library
URL: http://dri.freedesktop.org/
Group: System Environment/Libraries
License: MIT
Vendor: MSP Slackware
Source: http://dri.freedesktop.org/libdrm/%{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, pkg-config

%description
DRI and DRM provides mechanics to draw directly on the hardware, which greatly
improves performance and is required if you want to use the 3D functions of
your graphics card.


%prep
%setup -q


%build
%configure
make %{_smp_mflags}


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"

[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%{_includedir}/drm/
%{_includedir}/xf86*.h
%{_libdir}/libdrm.*
%{_libdir}/pkgconfig/libdrm.pc
