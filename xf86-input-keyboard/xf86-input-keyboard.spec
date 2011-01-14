Name: xf86-input-keyboard
Version: 1.2.2
Release: 1ev
Summary: Xorg X11 keyboard input driver
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/archive/individual/driver/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, pkg-config, xorg-proto >= 7.3
Requires: xorg-fslayout >= 7.3

%description
This driver adds keyboard input support to the X.org X11 server. 


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
%{_libdir}/xorg/modules/input/kbd_drv.*
%doc %{_mandir}/man4/kbd.4*
