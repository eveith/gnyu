Name: usbutils
Version: 003
Release: 1.0
Summary: Tools for exmining a system's USB configuration
URL: http://www.kernel.org/pub/linux/utils/usb/usbutils
Group: System Environment/Utilities
License: GPL-2
Source: http://www.kernel.org/pub/linux/utils/usb/usbutils/usbutils-%{version}.tar.bz2
BuildRequires: grep, sed, make, gcc
BuildRequires: eglibc-devel, linux-headers
BuildRequires: libusb-1_0-devel >= 1.0.0, zlib-devel

%description
This package contains the lsusb utility for inspecting the devices connected
to the USB bus. It shows a graphical representation of the devices that are
currently plugged in, showing the topology of the USB bus. It also displays
information on each individual device on the bus.  More information can be
found at the Linux USB web site http://www.linux-usb.org.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%check
%{__make} check



%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog README NEWS

%{_bindir}/lsusb
%{_bindir}/lsusb.py
%{_bindir}/usb-devices
%{_bindir}/usbhid-dump
%attr(0700, root, root) %{_sbindir}/update-usbids.sh

%attr(0644, root, root) %{_datadir}/usb.ids*

%{_datadir}/pkgconfig/usbutils.pc

%doc %{_mandir}/man1/usb-devices.1*
%doc %{_mandir}/man8/lsusb.8*
