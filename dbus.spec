Name: dbus
Version: 1.2.16
Release: 8ev
Summary: An IPC framework: D-BUS message bus
URL: http://www.freedesktop.org/software/dbus/
Source0: http://dbus.freedesktop.org/releases/dbus/%{name}-%{version}.tar.gz
Source1: %{name}-dbus.ii
License: AFL-2.1/GPL-2
Group: System Environment/Libraries
Vendor: GNyU-Linux
BuildRequires: make, pkg-config, gcc, expat
BuildRequires: libX11, libICE, libSM, libXdmcp, libXau
BuildRequires: gettext, doxygen, xmlto
%define dbus_uid 81

%description
D-BUS is a system for sending messages between applications. It is
used both for the systemwide message bus service, and as a
per-user-login-session messaging facility.


%prep
%setup -q


%build
#CPPFLAGS='-D_BSD_SOURCE -include %{_includedir}/syslog.h'; export CPPFLAGS
%configure \
	--enable-dnotify \
	--enable-inotify \
	--with-xml=expat \
    --with-dbus-user=dbus \
	--with-system-pid-file='%{_localstatedir}/run/dbus.pid' \
	--with-system-socket='%{_localstatedir}/run/system_bus_socket' \
	--with-session-socket-dir=/tmp \
	--enable-verbose-mode \
	--disable-asserts \
	--disable-tests \
	--disable-selinux
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/dbus-1/session.d'
%{__mkdir_p} '%{buildroot}/%{_localstatedir}/run'

%{__mkdir_p} '%{buildroot}/%{_datadir}/dbus-1/interfaces'

%{__touch} '%{buildroot}/%{_localstatedir}/run/system_bus_socket'
%{__touch} '%{buildroot}/%{_localstatedir}/run/dbus.pid'

# Remove rc.d script and install InitNG service file.
%{__rm} -rf '%{buildroot}/%{_sysconfdir}/rc.d'
%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/initng/daemon'
%{install_ifile '%{SOURCE1}' 'daemon/dbus.i'}

# Install a service directory.
%{__mkdir_p} '%{buildroot}/%{_localstatedir}/lib/dbus'
%{__touch} %{buildroot}/%{_localstatedir}/lib/dbus/machine-id


%pre
if [[ "${1}" -eq 1 ]]
then
	userdel dbus ||:
	useradd \
		-c 'System Message Bus' \
		-u %{dbus_uid} \
		-g nogroup \
		-s /sbin/nologin \
		-d '%{_localstatedir}/lib/dbus' \
		dbus  
	ng-update add daemon/dbus default
fi > /dev/null 2>&1
exit 0


%post
%{__ldconfig}
if [[ "${1}" -eq 1 ]]
then
	%{__rm} -f '%{_localstatedir}/lib/dbus/machine-id'
	dbus-uuidgen > '%{_localstatedir}/lib/dbus/machine-id'
fi
exit 0


%preun
if [[ "${1}" -eq 0 ]]
then
	ngc -d daemon/dbus
	ng-update delete daemon/dbus default
fi > /dev/null 2>&1
exit 0


%postun
%{__ldconfig}


%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING HACKING README
%attr(0700, root, root) %{_sysconfdir}/initng/daemon/dbus.i
%{_bindir}/dbus-*
%{_libdir}/libdbus-1*
%{_libdir}/dbus-1.0/
%{_libdir}/pkgconfig/dbus*.pc
%{_libexecdir}/dbus-daemon-launch-helper
%{_includedir}/dbus-1.0/
%doc %{_mandir}/man1/dbus*.1*
%attr(0755, dbus, root) %{_datadir}/dbus-1/
%dir %attr(0755, dbus, root) %{_localstatedir}/lib/dbus/
%ghost %config(noreplace) %attr(0644, dbus, root) %{_localstatedir}/lib/dbus/machine-id
%ghost %config(noreplace) %verify(not size md5) %{_localstatedir}/run/system_bus_socket
%ghost %config(noreplace) %verify(not size md5) %{_localstatedir}/run/dbus.pid
%dir %{_sysconfdir}/dbus-1
%{_sysconfdir}/dbus-1/session.conf
%{_sysconfdir}/dbus-1/system.conf
%dir %{_sysconfdir}/dbus-1/system.d
%dir %{_sysconfdir}/dbus-1/session.d
