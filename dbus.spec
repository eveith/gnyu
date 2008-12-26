%define dbus_user_uid 81

Summary: D-BUS message bus
Name: dbus
Version: 1.0.2
Release: 1ev
URL: http://www.freedesktop.org/software/dbus/
Source0: http://dbus.freedesktop.org/releases/dbus/%{name}-%{version}.tar.gz
Source1: %{name}-dbus.i
Patch0: dbus-0.22-fix-match-rule-equal.patch
Patch1: dbus-1.0.0-no_fatal_checks.patch
Patch2: dbus-1.0.1-fix-upgrade-mess.patch
Patch3: dbus-1.0.1-pthread-holder-fix.patch
License: AFL/GPL
Group: System Environment/Libraries
Vendor: MSP Slackware
BuildRoot: %{_tmppath}/%{name}-root
PreReq: /usr/sbin/useradd
BuildRequires: make, gcc-core, expat, libxml2, libX11, libSM, libXau, libICE
BuildRequires: libXdmcp
%define _dbus_uid 81

%description
D-BUS is a system for sending messages between applications. It is
used both for the systemwide message bus service, and as a
per-user-login-session messaging facility.


%prep
%setup -q
# %patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
# %patch -P 3 -p1


%build
%configure \
	--enable-dnotify \
    --with-dbus-user=dbus \
	--with-system-pid-file=%{_localstatedir}/run/dbus.pid \
	--with-system-socket=%{_localstatedir}/run/system_bus.socket \
	--with-session-socket-dir=/tmp \
	--disable-debug \
	--enable-verbose-mode \
	--disable-asserts \
	--disable-tests \
    --disable-warnings \
	--disable-selinux
%{__make} %{_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && rm -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'

# Remove rc.d script and install InitNG service file.
%{__rm} -rf %{buildroot}/etc/rc.d
%{__mkdir_p} %{buildroot}/etc/initng/daemon
%{__cat} < %{SOURCE1} \
	| %{__sed} \
		-e 's,@dbus-daemon@,%{_bindir}/dbus-daemon,g' \
		-e 's,@localstatedir@,%{_localstatedir},g' \
	> %{buildroot}/etc/initng/daemon/dbus.i

# Install a service directory.
%{__mkdir_p} %{buildroot}/%{_localstatedir}/lib/dbus
touch %{buildroot}/%{_localstatedir}/lib/dbus/machine-id


%clean
[[ '%{buildroot}' != '/' ]] && rm -rf '%{buildroot}'


%pre
userdel dbus > /dev/null 2>&1 || :
useradd \
	-c 'System Message Bus' \
	-u %{_dbus_uid} \
	-g nogroup \
	-s /sbin/nologin \
	-d /%{_localstatedir}/lib/dbus \
	dbus  
exit 0

%post
/sbin/ldconfig
%{__rm} -f %{_localstatedir}/lib/dbus/machine-id
dbus-uuidgen > %{_localstatedir}/lib/dbus/machine-id || :
exit 0

%preun
if [ "$1" -eq 0 ] && ngc -s | grep -q dbus
then
	ngc -d daemon/dbus || :
fi

%postun
/sbin/ldconfig
if [ "$1" = '0' ]
then
	ngc -d daemon/dbus
	ng-update delete daemon/dbus
	userdel dbus 
fi > /dev/null 2>&1


%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING HACKING README
/etc/initng/daemon/dbus.i
%{_bindir}/dbus-*
%{_libdir}/libdbus-1*
%{_libdir}/dbus-1.0/
%{_libdir}/pkgconfig/dbus*.pc
%{_includedir}/dbus-1.0/
%{_mandir}/man1/dbus*.1*
%attr(755, dbus, root) %{_datadir}/dbus-1/
%dir %attr(755, dbus, root) %{_localstatedir}/lib/dbus/
%ghost %config(noreplace) %attr(644, dbus, root) %{_localstatedir}/lib/dbus/machine-id
%attr(755, dbus, root) %{_localstatedir}/run/dbus
%dir %{_sysconfdir}/dbus-1
%{_sysconfdir}/dbus-1/session.conf
%{_sysconfdir}/dbus-1/system.conf
%{_sysconfdir}/dbus-1/system.d/
