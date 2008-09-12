Name: libdrm
Version: 2.3.1
Release: 2ev
Summary: Direct Rendering Manager library
URL: http://dri.freedesktop.org/
Group: System Environment/Libraries
License: MIT
Vendor: GNyU-Linux
Source: http://dri.freedesktop.org/libdrm/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, pkg-config

%description
DRI and DRM provides mechanics to draw directly on the hardware, which greatly
improves performance and is required if you want to use the 3D functions of
your graphics card.


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
%{_includedir}/drm/
%{_includedir}/xf86*.h
%{_libdir}/libdrm.*
%{_libdir}/pkgconfig/libdrm.pc
