Name: hal
Version: 0.5.13
Release: 7ev
Summary: The Linux Hardware Abstraction Layer
License: GPL-2
Group: System Environment/Daemons
Source: http://hal.freedesktop.org/releases/hal-%{version}.tar.gz
Source1: %{name}-hald.ii
Patch2: %{name}-allow-plugdev-group-on-volumes-and-power-management.patch
URL: http://www.freedesktop.org/wiki/Software/hal
Vendor: GNyU-Linux
BuildRequires: make, pkg-config, gcc, gettext, xmlto
BuildRequires: dbus >= 0.61, policykit, glib2 >= 2.10.0, dbus-glib
BuildRequires: libusb, pciutils, udev >= 125
BuildRequires: expat >= 1.95.8, libxml2, util-linux-ng >= 2.15
BuildRequires: hal-info >= 20080310
Requires: hal-info >= 20080310, %{_bindir}/udevinfo
%define hald_uid 82
%define hal_gid 28
%define hal_hardware_groups console,tty,uucp,floppy,disk,cdrom,plugdev,tape,usb,lp,audio,video,scanner

%description
The point of HAL is to merge information from various sources such that desktop
applications can locate and use hardware devices. The point is that the exact
set of information to merge varies by device and bus type. In order to do this,
we need to define a format for the information, hence the HAL specification. 
We may read some stuff from the hardware itself, then add some info provided by
the kernel, then add some metadata from some systemwide files, then add some
data that has been obtained by the desktop and stored per-user, then look at
some blacklist, and finally we have a complete picture of everything known about
that particular device. 
An extra value is that we can do this in an operating system independent way.
Stuff like this is important to the major desktop environments.


%prep
%setup -q
%patch2 -p1


%build
%configure \
	--enable-man-pages \
	--enable-docbook-docs \
	--disable-gtk-doc \
	--enable-policy-kit \
	--disable-console-kit \
	--enable-umount-helper \
	--with-pid-file='%{_localstatedir}/run/hald.pid' \
	--with-hwdata='%{_datadir}' \
	--with-dbus-sys='%{_sysconfdir}/dbus-1/system.d' \
	--with-hal-user=hald \
	--with-hal-group=hal
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

# Install HAL service file for InitNG 
%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/initng/daemon'
%{install_ifile '%{SOURCE1}' 'daemon/hald.i'}

# Create ghost cache file; hald will create it at first run.
%{__mkdir_p} '%{buildroot}/%{_localstatedir}/cache/hald'
%{__touch} '%{buildroot}/%{_localstatedir}/cache/hald/fdi-cache'

# Move udev rules
%{__mkdir_p} '%{buildroot}/%{_lib}'
%{__mv} '%{buildroot}/%{_libdir}/udev' '%{buildroot}/%{_lib}'

# Pid file ghost
%{__mkdir_p} '%{buildroot}/%{_localstatedir}/run'
%{__touch} '%{buildroot}/%{_localstatedir}/run/hald.pid'


%pre
if [[ "${1}" -eq 1 ]]
then
	groupadd -g '%{hal_gid}' hal
	useradd \
		-u '%{hald_uid}' \
		-g '%{hal_gid}' \
		-G '%{hal_hardware_groups}' \
		-c 'Hardware Abstraction Layer' \
		-s /sbin/nologin \
		-d '%{_sysconfdir}/hal' \
		hald
fi > /dev/null 2>&1
kill -HUP $(< %{_localstatedir}/run/dbus.pid)
exit 0


%postun
if [[ "${1}" -eq 0 ]]
then
	ngc -d daemon/hald
	ng-update delete hald default
	userdel hald
	groupdel hal
fi > /dev/null 2>&1
%{__ldconfig}
exit 0


%post
%{__ldconfig}


%files
%defattr(-, root, root)
%doc README AUTHORS ChangeLog COPYING HACKING NEWS
%dir %{_datadir}/doc/hal
%dir %{_datadir}/doc/hal/spec
%doc %{_datadir}/doc/hal/spec/*.*
%dir %{_datadir}/gtk-doc/html/libhal
%dir %{_datadir}/gtk-doc/html/libhal-storage
%doc %{_datadir}/gtk-doc/html/libhal/*.*
%doc %{_datadir}/gtk-doc/html/libhal-storage/*.*
%{_sysconfdir}/initng/daemon/hald.i
%dir %{_sysconfdir}/hal
%config %{_sysconfdir}/dbus-1/system.d/hal.conf
/sbin/umount.hal
/%{_lib}/udev/rules.d/90-hal.rules
%{_bindir}/hal-*
%{_bindir}/lshal
%{_includedir}/hal/
%{_libdir}/libhal*
%{_libdir}/pkgconfig/hal*.pc
%{_libexecdir}/hal*
%doc %{_mandir}/man1/hal-disable-polling.1*
%doc %{_mandir}/man1/hal-is-caller-privileged.1*
%doc %{_mandir}/man1/hal-find-by-capability.1*
%doc %{_mandir}/man1/hal-find-by-property.1*
%doc %{_mandir}/man1/hal-get-property.1*
%doc %{_mandir}/man1/hal-is-caller-locked-out.1*
%doc %{_mandir}/man1/hal-lock.1*
%doc %{_mandir}/man1/hal-set-property.1*
%doc %{_mandir}/man1/lshal.1*
%doc %{_mandir}/man8/hald.8*
%{_sbindir}/hald
%{_datadir}/hal
%{_datadir}/PolicyKit/policy/org.freedesktop.hal.*policy
%dir %{_localstatedir}/cache/hald
%ghost %{_localstatedir}/cache/hald/fdi-cache
%dir %{_libexecdir}/scripts
%{_libexecdir}/scripts/hal-*
%dir %{_libexecdir}/scripts/linux
%{_libexecdir}/scripts/linux/hal-*
%ghost %config %{_localstatedir}/run/hald.pid
