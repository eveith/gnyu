Name: udev
Version: 135
Release: 3ev
Summary: A system that provides Linux systems with a dynamic /dev directory 
URL: http://www.kernel.org/pub/linux/utils/kernel/hotplug/udev.html
Group: System Environment/Base
License: GPL-2
Vendor: GNyU-Linux
Source: http://www.kernel.org/pub/linux/utils/kernel/hotplug/udev-%{version}.tar.bz2
Source1: %{name}-links.conf
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc, pkg-config, libxml2
%define _build_extras extras/ata_id extras/cdrom_id extras/collect \\\
	extras/edd_id extras/firmware extras/floppy extras/fstab_import \\\
	extras/path_id extras/rule_generator \\\
	extras/scsi_id extras/usb_id extras/volume_id

%description
udev provides Linux systems with a dynamic /dev directory and features the
ability to have persistent device names. It uses sysfs and runs entirely in
userspace.


%prep
%setup -q


%build
CFLAGS="${RPM_OPT_FLAGS}"; CXXFLAGS="${RPM_OPT_FLAGS}"
export CFLAGS CXXFLAGS
./configure \
	--prefix='%{_prefix}' \
	--exec-prefix='' \
	--sysconfdir='%{_sysconfdir}' \
	--without-selinux \
	--enable-logging \
	--with-libdir-name='%{_lib}'
%{__make} %{?_smp_mflags} 

%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} \
	DESTDIR='%{buildroot}' \
	EXTRAS='%{_build_extras}' \
	etcdir='%{_sysconfdir}' \
	sbindir='/sbin' \
	usrbindir='%{_bindir}' \
	usrsbindir='%{_sbindir}' \
	usrlibdir='%{_libdir}' \
	libudevdir='/%{_lib}/udev' \
	mandir='%{_mandir}' 

%{__mkdir_p} '%{buildroot}/lib/udev/devices'

%{__cp} -r rules/rules.d '%{buildroot}/%{_sysconfdir}/udev'
%{__cp} rules/gentoo/65-permissions.rules \
	'%{buildroot}/%{_sysconfdir}/udev/rules.d'
%{__cp} rules/packages/*.rules '%{buildroot}/%{_sysconfdir}/udev/rules.d'
%{__cp} '%{SOURCE1}' '%{buildroot}/etc/udev/links.conf'


%post
%{__ldconfig}

%postun
%{__ldconfig}


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc COPYING README NEWS TODO ChangeLog docs/writing_udev_rules
%doc docs/*
%dir %{_sysconfdir}/udev
%dir %{_sysconfdir}/udev/rules.d/
%config %attr(0644, root, root) %{_sysconfdir}/udev/rules.d/*.rules
%config %attr(0644, root, root) %{_sysconfdir}/udev/udev.conf
%config(noreplace) %attr(0644, root, root) %{_sysconfdir}/udev/links.conf
%config %{_sysconfdir}/scsi_id.config
/%{_lib}/libudev.so*
/%{_lib}/libvolume_id.so*
%dir %attr(0750, root, root) /%{_lib}/udev
%dir %attr(0750, root, root) /%{_lib}/udev/devices
/%{_lib}/udev/ata_id
/%{_lib}/udev/cdrom_id
/%{_lib}/udev/collect
/%{_lib}/udev/create_floppy_devices
/%{_lib}/udev/edd_id
/%{_lib}/udev/firmware.sh
/%{_lib}/udev/fstab_import
/%{_lib}/udev/path_id
/%{_lib}/udev/rule_generator.functions
%dir /%{_lib}/udev/rules.d
/%{_lib}/udev/rules.d/50-udev-default.rules
/%{_lib}/udev/rules.d/60-cdrom_id.rules
/%{_lib}/udev/rules.d/60-persistent-input.rules
/%{_lib}/udev/rules.d/60-persistent-storage-tape.rules
/%{_lib}/udev/rules.d/60-persistent-storage.rules
/%{_lib}/udev/rules.d/60-persistent-v4l.rules
/%{_lib}/udev/rules.d/61-persistent-storage-edd.rules
/%{_lib}/udev/rules.d/75-cd-aliases-generator.rules
/%{_lib}/udev/rules.d/75-persistent-net-generator.rules
/%{_lib}/udev/rules.d/79-fstab_import.rules
/%{_lib}/udev/rules.d/80-drivers.rules
/%{_lib}/udev/rules.d/95-udev-late.rules
/%{_lib}/udev/scsi_id
/%{_lib}/udev/usb_id
/%{_lib}/udev/vol_id
/%{_lib}/udev/write_cd_rules
/%{_lib}/udev/write_net_rules
%attr(0755, root, root) /sbin/udevd
%attr(0770, root, root) /sbin/udevadm
%{_includedir}/libudev.h
%{_includedir}/libvolume_id.h
%{_libdir}/libudev.so*
%{_libdir}/libvolume_id.*
%{_libdir}/pkgconfig/libudev.pc
%{_libdir}/pkgconfig/libvolume_id.pc
%doc %{_mandir}/man7/udev.7*
%doc %{_mandir}/man8/create_floppy_devices.8*
%doc %{_mandir}/man8/udev*.8*
%doc %{_mandir}/man8/*_id.8*
