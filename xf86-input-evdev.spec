Name: xf86-input-evdev
Version: 2.0.4
Release: 1ev
Summary: X.org X11 generic (kernel event-based) input device driver
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/archive/individual/driver/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, xorg-xserver, xorg-proto
Requires: xorg-fslayout

%description
evdev  is  an X.org X11 input  driver for Linux' generic event
devices.  It therefore supports all input devices that the kernel knows
about, including most mice and keyboards.

The  evdev  driver  can  serve  as  both a pointer and a keyboard input
device, and may be used as both the core keyboard and the core pointer.
Multiple  input  devices  are  supported  by multiple instances of this
driver, with one Load directive for evdev in the Module section of your
X.org X11 config file for each input device that will use this driver.


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
%{_libdir}/xorg/modules/input/evdev_drv.??
%doc %{_mandir}/man4/evdev.4*
