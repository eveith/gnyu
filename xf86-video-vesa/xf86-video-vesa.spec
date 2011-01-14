Name: xf86-video-vesa
Version: 1.3.0
Release: 1ev
Summary: Xorg X11 VESA video driver
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/archive/individual/driver/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, pkg-config, xorg-proto >= 7.3
Requires: xorg-fslayout >= 7.3

%description
One of the most basic video drivers is the VESA driver. It does not feature
graphics accelleration of any type, but it will work in almost every case.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc COPYING ChangeLog 
%{_libdir}/xorg/modules/drivers/vesa_drv.*
%doc %{_mandir}/man4/vesa.4*
