Name: udev
Version: 171
Release: 1.0
Summary: A system that provides Linux systems with a dynamic /dev directory 
URL: http://www.kernel.org/pub/linux/utils/kernel/hotplug/udev.html
Group: System Environment/Base
License: GPL-2
Source: http://www.kernel.org/pub/linux/utils/kernel/hotplug/udev-%{version}.tar.bz2
BuildRequires: grep, sed, gawk, make >= 3.79.1, gcc
BuildRequires: pkg-config
BuildRequires: glib-devel >= 2.22.0, gobject-introspection-devel >= 0.10.0
BuildRequires: acl-devel, libusb-1_0-devel, usbutils, pciutils
%define build_extras extras/ata_id extras/cdrom_id extras/collect \\\
	extras/edd_id extras/firmware extras/floppy extras/fstab_import \\\
	extras/path_id extras/rule_generator \\\
	extras/scsi_id extras/usb_id extras/volume_id


%description
udev provides Linux systems with a dynamic /dev directory and features the
ability to have persistent device names. It uses sysfs and runs entirely in
userspace.


%files
%defattr(-, root, root)
%doc COPYING README NEWS TODO ChangeLog 
%doc extras/keymap/README.keymap.txt

/lib/systemd/system/basic.target.wants/udev-trigger.service
/lib/systemd/system/basic.target.wants/udev.service
/lib/systemd/system/sockets.target.wants/udev-control.socket
/lib/systemd/system/sockets.target.wants/udev-kernel.socket
/lib/systemd/system/udev-control.socket
/lib/systemd/system/udev-kernel.socket
/lib/systemd/system/udev-settle.service
/lib/systemd/system/udev-trigger.service
/lib/systemd/system/udev.service

%dir %{_sysconfdir}/udev
%dir %{_sysconfdir}/udev/rules.d/
%config %attr(0644, root, root) %{_sysconfdir}/udev/udev.conf
#%config(noreplace) %attr(0644, root, root) %{_sysconfdir}/udev/links.conf
#%config %{_sysconfdir}/scsi_id.config

%dir %attr(0750, root, root) /%{_lib}/udev
/%{_lib}/udev/ata_id
/%{_lib}/udev/cdrom_id
/%{_lib}/udev/collect
/%{_lib}/udev/create_floppy_devices
/%{_lib}/udev/findkeyboards
/%{_lib}/udev/firmware
/%{_lib}/udev/input_id
/%{_lib}/udev/keyboard-force-release.sh
/%{_lib}/udev/keymap
/%{_lib}/udev/mtd_probe
/%{_lib}/udev/path_id
/%{_lib}/udev/pci-db
/%{_lib}/udev/rule_generator.functions
/%{_lib}/udev/scsi_id
/%{_lib}/udev/udev-acl
/%{_lib}/udev/usb-db
/%{_lib}/udev/usb_id
/%{_lib}/udev/v4l_id
/%{_lib}/udev/write_cd_rules
/%{_lib}/udev/write_net_rules
%dir %attr(0750, root, root) /%{_lib}/udev/devices

%dir /%{_lib}/udev/keymaps
/%{_lib}/udev/keymaps/*

%dir /%{_lib}/udev/rules.d
/%{_lib}/udev/rules.d/*.rules

%attr(0700, root, root) /sbin/udevd
%attr(0750, root, root) /sbin/udevadm

%doc %{_mandir}/man7/udev.7*
%doc %{_mandir}/man8/udev*.8*
%doc %{_mandir}/man8/scsi_id.8*

%dir %{_prefix}/lib/ConsoleKit
%dir %{_prefix}/lib/ConsoleKit/run-seat.d
%{_prefix}/lib/ConsoleKit/run-seat.d/udev-acl.ck


%package -n libudev0
Summary: Dynamic library to access udev device information
Group: System Environment/Libraries
License: LGPL-2.1


%description -n libudev0
This package contains the dynamic library libudev, which provides
access to udev device information


%files -n libudev0
%defattr(-, root, root)
/%{_lib}/libudev.so.0*


%post -n libudev0 -p %{__ldconfig}
%postun -n libudev0 -p %{__ldconfig}

 
%package -n libudev-devel
Summary: Development files for libudev
Group: Development/Libraries
License: LGPL-2.1
Requires: libudev0 = %{version}-%{release}
 

%description -n libudev-devel
This package contains the development files for the library libudev, a
dynamic library, which provides access to udev device information.


%files -n libudev-devel
%defattr(-, root, root)
%{_includedir}/libudev.h
 
%{_libdir}/libudev.la
%{_libdir}/libudev.so

%{_libdir}/pkgconfig/libudev.pc
%{_datadir}/pkgconfig/udev.pc

%doc %{_datadir}/gtk-doc/html/libudev


%package -n libgudev-1_0-0
Summary: GObject library, to access udev device information
Group: System Environment/Libraries
License: LGPL-2.1
Requires: libudev0 = %{version}-%{release}

 
%description -n libgudev-1_0-0
This package contains the GObject library libgudev, which provides
access to udev device information.


%files -n libgudev-1_0-0
%defattr(-, root, root)
/%{_lib}/libgudev-1.0.so.0*
%{_libdir}/girepository-1.0/GUdev-1.0.typelib


%post -n libgudev-1_0-0 -p %{__ldconfig}
%postun -n libgudev-1_0-0 -p %{__ldconfig}
 

%package -n libgudev-1_0-devel
Summary: Devel package for libgudev
Group: Development/Libraries
License: LGPL-2.1
Requires: libgudev-1_0-0 = %{version}-%{release}
Requires: libudev-devel = %{version}-%{release}
Requires: glib-devel
 
%description -n libgudev-1_0-devel
This is the devel package for the GObject library libgudev, which
provides GObject access to udev device information.


%files -n libgudev-1_0-devel
%defattr(-, root, root)
%dir %{_includedir}/gudev-1.0
%dir %{_includedir}/gudev-1.0/gudev
%{_includedir}/gudev-1.0/gudev/gudev*.h 

%{_libdir}/libgudev-1.0.so
%{_libdir}/libgudev-1.0.la
%{_libdir}/pkgconfig/gudev-1.0.pc

%{_datadir}/gir-1.0/GUdev-1.0.gir

%doc %{_datadir}/gtk-doc/html/gudev


%prep
%setup -q

# prevent man pages from re-building (xmlto)
%{__find} . -name "*.[1-8]" -exec %{__touch} '{}' \;


%build
%configure \
	--prefix='%{_prefix}' \
    --sbindir=/sbin \
    --libexecdir=/lib/udev \
	--sysconfdir='%{_sysconfdir}' \
	--without-selinux \
    --with-rootlibdir='/%{_lib}' \
    --enable-floppy \
    --with-systemdsystemunitdir=/lib/systemd/system
%{__make} %{?_smp_mflags} V=1

%install
%{__make} install DESTDIR='%{buildroot}'
%{__rm_rf} '%{buildroot}%{_datadir}/doc'
