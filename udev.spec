Name: udev
Version: 105
Release: 2ev
Summary: A system that provides Linux systems with a dynamic /dev directory. 
URL: http://www.kernel.org/pub/linux/utils/kernel/hotplug/udev.html
Group: System Environment/Base
License: GPL-2
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: http://www.kernel.org/pub/linux/utils/kernel/hotplug/udev-%{version}.tar.bz2
Source1: udev-05-udev-early.rules
Source2: udev-60-persistent-input.rules
Source3: udev-60-persistent-storage.rules
Source4: udev-95-udev-late.rules
Source5: udev-50-udev.rules
Patch0: udev-extras.patch
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc-core, sed
%define _build_extras extras/ata_id extras/cdrom_id extras/dasd_id \\\
	extras/edd_id extras/firmware extras/floppy extras/path_id \\\
	extras/path_id extras/rule_generator extras/run_directory \\\
	extras/scsi_id extras/usb_id extras/volume_id

%description
udev provides Linux systems with a dynamic /dev directory and features the
ability to have persistent device names. It uses sysfs and runs entirely in
userspace.


%prep
%setup -q
%patch -P 0 -p1


%build
%{__make} \
	prefix=/ \
	mandir=%{_mandir} \
	USE_LOG=true \
	USE_SELINUX=false \
	DEBUG=false \
	OPTFLAGS="$RPM_OPT_FLAGS -Os" \
	EXTRAS='%{_build_extras}' \
	V=1
	


%install
[[ -d '%{buildroot}' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} \
	DESTDIR='%{buildroot}' \
	etcdir=/etc \
	sbindir=/sbin \
	usrbindir=%{_bindir} \
	usrsbindir=%{_sbindir} \
	usrlibdir=%{_libdir} \
	includedir=%{_includedir} \
	libudevdir=/%{_lib}/udev \
	mandir=%{_mandir} \
	EXTRAS='%{_build_extras}' 
%{__mkdir_p} %{buildroot}/lib/udev/devices

# Install udev helpers.
for file in load_floppy_module.sh check-cdrom.sh 
do
	%{__install} -m0755 extras/"$file" %{buildroot}/lib/udev/
done

# Install udev rules
%{__install} -d %{buildroot}/etc/udev/rules.d
for file in %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5}
do
	newfile=$(echo $file | %{__sed} "s,^${RPM_SOURCE_DIR}/\?udev-,,")
	%{__install} -m0644 "$file" "${RPM_BUILD_ROOT}/etc/udev/rules.d/$newfile"
done


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ -d '%{buildroot}' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc COPYING FAQ README RELEASE* TODO ChangeLog
%doc docs/*
%dir /etc/udev
/etc/udev/rules.d/
%config /etc/udev/udev.conf
%config /etc/scsi_id.config
/%{_lib}/libvolume_id.so*
/%{_lib}/udev/
/sbin/udevd
/sbin/udevtrigger
/sbin/udevsettle
/sbin/udevcontrol
/sbin/scsi_id
%{_includedir}/libvolume_id.h
%{_bindir}/udevinfo
%{_bindir}/udevtest
%{_libdir}/libvolume_id.*
%{_libdir}/pkgconfig/libvolume_id.pc
%{_sbindir}/udevmonitor
%{_mandir}/man7/udev.7*
%{_mandir}/man8/udev*.8*
%{_mandir}/man8/*_id.8*
