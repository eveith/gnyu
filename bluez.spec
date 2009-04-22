Name: bluez
Version: 4.36
Release: 2ev
Summary: Linux Bluetooth Stack: Userspace
URL: http://www.bluez.org/
Group: System Environment/Libraries
License: GPL-2, LGPL-2.1
Vendor: GNyU-Linux
Source: http://www.kernel.org/pub/linux/bluetooth/bluez-%{version}.tar.gz
Source1: %{name}-bluetoothd.ii
BuildRequires: make, gcc, bison, flex, pkg-config
BuildRequires: dbus, glib2, gstreamer, alsa-lib, libsndfile, libusb

%description
	BlueZ is the official Linux Bluetooth protocol stack. In order to use
	Bluetooth devices, you do not only need the appropriate kernel modules, 
	but also this userspace implementation.


%prep
	%setup -q


%build
	%configure
	%{__make} %{?_smp_mflags}


%install
	%{__make} install DESTDIR='%{buildroot}'

	%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/initng/daemon'
	%{install_ifile '%{SOURCE1}' daemon/bluetoothd.i}


%post
	%{__ldconfig}


%postun
	%{__ldconfig}


%files
	%defattr(-, root, root)
	%doc README COPYING* NEWS
	%attr(0700, root, root) %{_sysconfdir}/initng/daemon/bluetoothd.i
	%config(noreplace) %{_sysconfdir}/alsa/bluetooth.conf
	%dir %{_sysconfdir}/bluetooth
	%config(noreplace) %{_sysconfdir}/bluetooth/main.conf
	%config(noreplace) %{_sysconfdir}/bluetooth/rfcomm.conf
	%config %{_sysconfdir}/dbus-1/system.d/bluetooth.conf
	%{_bindir}/ciptool
	%{_bindir}/hcitool
	%{_bindir}/l2ping
	%{_bindir}/rfcomm
	%{_bindir}/sdptool
	%{_sbindir}/bluetoothd
	%{_sbindir}/hciattach
	%{_sbindir}/hciconfig
	%dir %{_includedir}/bluetooth
	%{_includedir}/bluetooth/*.h
	%{_libdir}/libbluetooth.*
	%{_libdir}/pkgconfig/bluez.pc
	%{_libdir}/alsa-lib/libasound_module_*_bluetooth.*
	%dir %{_libdir}/bluetooth
	%dir %{_libdir}/bluetooth/plugins
	%{_libdir}/bluetooth/plugins/audio.*
	%{_libdir}/bluetooth/plugins/hal.*
	%{_libdir}/bluetooth/plugins/input.*
	%{_libdir}/bluetooth/plugins/network.*
	%{_libdir}/bluetooth/plugins/serial.*
	%{_libdir}/bluetooth/plugins/service.*
	%{_libdir}/gstreamer-0.10/libgstbluetooth.*
	%doc %{_mandir}/man1/ciptool.1*
	%doc %{_mandir}/man1/hcitool.1*
	%doc %{_mandir}/man1/l2ping.1*
	%doc %{_mandir}/man1/rfcomm.1*
	%doc %{_mandir}/man1/sdptool.1*
	%doc %{_mandir}/man8/bluetoothd.8*
	%doc %{_mandir}/man8/hciattach.8*
	%doc %{_mandir}/man8/hciconfig.8*
