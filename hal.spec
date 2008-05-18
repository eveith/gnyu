Name: hal
Version: 0.5.9.1
Release: 2ev
Summary: The Linux hardware abstraction layer
License: GPL
Group: System Environment/Daemons
Source: http://hal.freedesktop.org/releases/hal-%{version}.tar.gz
Source1: %{name}-hald.i
Patch0: %{name}-dbus_close.patch
Patch1: %{name}-kernel-headers-26.patch
Patch2: %{name}-allow-plugdev-group-on-volumes-and-power-management.patch
URL: http://www.freedesktop.org/wiki/Software/hal
Vendor: MSP Slackware
BuildRequires: coreutils, grep, sed, bash >= 2.0, make, gcc
BuildRequires: dbus >= 0.60, udev >= 089, glib2 >= 2.6.0, expat >= 1.95.8
BuildRequires: dbus-glib, util-linux >= 2.12, perl-XML-Parser, gettext
Requires: hal-info
BuildRoot: %{_tmppath}/%{name}-root
%define _hald_uid 82
%define _hal_gid 24

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
%patch1 -p1
%patch2 -p1


%build
%configure \
	--enable-manpages \
	--disable-gtk-doc \
	--disable-policy-kit \
	--enable-umount-helper \
	--with-pid-file='%{_localstatedir}/run/hald.pid' \
	--with-hwdata='%{_datadir}' \
	--with-dbus-sys='%{_sysconfdir}/dbus-1/system.d' \
	--with-hal-user=hald \
	--with-hal-group=hal \
	--with-doc-dir=%{_docdir}/%{name}-%{version}
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%find_lang hal

# Install HAL service file for InitNG 
%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/initng/daemon'
%{__cat} < %{SOURCE1} \
	| %{__sed} \
		-e 's,@rm@,%{__rm},g' \
		-e 's,@localstatedir@,%{_localstatedir},g' \
		-e 's,@hald@,%{_sbindir}/hald,g' \
	> '%{buildroot}/%{_sysconfdir}/initng/daemon/hald.i'

# Create ghost cache file; hald will create it at first run.
%{__mkdir_p} '%{buildroot}/%{_localstatedir}/cache/hald'
touch '%{buildroot}/%{_localstatedir}/cache/hald/fdi-cache'


%pre
{
	userdel hald
	groupdel hal
} > /dev/null 2>&1
groupadd -g '%{_hal_gid}' hal
useradd \
	-u '%{_hald_uid}' \
	-g '%{_hal_gid}' \
	-c 'Hardware Abstraction Layer' \
	-s /sbin/nologin \
	-d %{_sysconfdir}/hal \
	hald
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
/sbin/ldconfig
exit 0

%post
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files -f hal.lang
%defattr(-, root, root)
%doc README AUTHORS ChangeLog COPYING HACKING NEWS
%doc %{_datadir}/gtk-doc/html/libhal
%doc %{_datadir}/gtk-doc/html/libhal-storage
/etc/udev/rules.d/*
%{_sysconfdir}/initng/daemon/hald.i
%{_sysconfdir}/hal/
%config %{_sysconfdir}/dbus-1/system.d/hal.conf
/sbin/umount.hal
%{_bindir}/hal-*
%{_bindir}/lshal
%{_includedir}/hal/
%{_libdir}/hal/
%{_libdir}/libhal*
%{_libdir}/pkgconfig/hal*.pc
%{_libexecdir}/hal*
%{_mandir}/man1/*hal*1.*
%{_mandir}/man8/hald.8*
%{_sbindir}/hald
%{_datadir}/hal
%dir %{_localstatedir}/cache/hald
%ghost %{_localstatedir}/cache/hald/fdi-cache