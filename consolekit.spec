Name: consolekit
Version: 0.3.0
Release: 1.1ev
Summary: A framework for tracking users, login sessions and seats
URL: http://www.freedesktop.org/wiki/Software/ConsoleKit
Group: System Environment/Daemons
License: GPL-2
Vendor: GNyU-Linux
Source: http://www.freedesktop.org/software/ConsoleKit/dist/ConsoleKit-%{version}.tar.bz2
Source1: %{name}-console-kit-daemon.ii
BuildRequires: pkg-config >= 0.9.0, make, gcc, gettext >= 0.17
BuildRequires: dbus >= 0.30, glib2 >= 2.7.0, libX11 >= 1.0.0, policykit >= 0.7
BuildRequires: zlib, libpam, xmlto, libxml2

%description
onsoleKit is a framework for defining and tracking users, login sessions, and
seats. It aims to provide a true multi-user environment with multiple
sessions, session switching, hardware-awareness (a seat) and other features.


%prep
	%setup -q -n 'ConsoleKit-%{version}'


%build
	%configure \
		--enable-pam-module \
		--with-pid-file='%{_localstatedir}/run/console-kit-daemon.pid' \
		--with-pam-module-dir='/%{_lib}/security'
	%{__make} %{?_smp_mflags}


%install
	%{__make} install DESTDIR='%{buildroot}'
	%{install_ifile '%{SOURCE1}' daemon/console-kit-daemon.i}
	%{__mkdir_p} '%{buildroot}/%{_localstatedir}/run'
	%{__touch} '%{buildroot}/%{_localstatedir}/run/console-kit-daemon.pid'


%post
	%{__ldconfig}


%postun
	%{__ldconfig}


%files
	%defattr(-, root, root)
	%doc AUTHORS COPYING HACKING NEWS README TODO
	%attr(0710, root, root) %{_sysconfdir}/initng/daemon/console-kit-daemon.i
	%dir %{_sysconfdir}/ConsoleKit
	%dir %{_sysconfdir}/ConsoleKit/seats.d
	%config %{_sysconfdir}/ConsoleKit/seats.d/00-primary.seat
	%config %{_sysconfdir}/dbus-1/system.d/ConsoleKit.conf
	/%{_lib}/security/pam_ck_connector.*
	%{_bindir}/ck-history
	%{_bindir}/ck-launch-session
	%{_bindir}/ck-list-sessions
	%dir %{_includedir}/ConsoleKit
	%dir %{_includedir}/ConsoleKit/ck-connector
	%{_includedir}/ConsoleKit/ck-connector/ck-connector.h
	%dir %{_libdir}/ConsoleKit
	%dir %{_libdir}/ConsoleKit/scripts
	%{_libdir}/ConsoleKit/scripts/ck-system-restart
	%{_libdir}/ConsoleKit/scripts/ck-system-stop
	%{_libdir}/libck-connector.*
	%{_libdir}/pkgconfig/ck-connector.pc
	%{_libexecdir}/ck-collect-session-info
	%{_libexecdir}/ck-get-x11-display-device
	%{_libexecdir}/ck-get-x11-server-pid
	%doc %{_mandir}/man8/pam_ck_connector.8*
	%attr(0710, root, root) %{_sbindir}/ck-log-system-restart
	%attr(0710, root, root) %{_sbindir}/ck-log-system-start
	%attr(0710, root, root) %{_sbindir}/ck-log-system-stop
	%attr(0710, root, root) %{_sbindir}/console-kit-daemon
	%dir %{_datadir}/PolicyKit
	%dir %{_datadir}/PolicyKit/policy
	%{_datadir}/PolicyKit/policy/org.freedesktop.consolekit.policy
	%{_datadir}/dbus-1/interfaces/org.freedesktop.ConsoleKit.*.xml
	%{_datadir}/dbus-1/system-services/org.freedesktop.ConsoleKit.service
	%ghost %config(noreplace) %{_localstatedir}/run/console-kit-daemon.pid
