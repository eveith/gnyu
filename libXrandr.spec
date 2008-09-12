Name: libXrandr
Version: 1.2.2
Release: 2ev
Summary: X Resize, Rotate and Reflection extension library
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, pkg-config, xorg-proto
BuildRequires: libX11, libXext, libXrender

%description
libXrandr provides an X Window System client interface to the RandR extension
to the X protocol. The RandR extension allows for run-time configuration of 
display attributes such as resolution, rotation, and reflection.


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
%doc COPYING README AUTHORS
%{_libdir}/libXrandr*.*
%{_libdir}/pkgconfig/xrandr.pc
%{_includedir}/X11/extensions/Xrandr.h
%doc %{_mandir}/man3/XRR*.3*
%doc %{_mandir}/man3/Xrandr.3*
