Name: policykit
Version: 0.9
Release: 1ev
Summary: An authorization framework for hardware access from desktops
URL: http://www.freedesktop.org/wiki/Software/PolicyKit
Group: System Environment/Daemons
License: MIT
Vendor: GNyU-Linux
Source: http://hal.freedesktop.org/releases/PolicyKit-%{version}.tar.gz
BuildRequires: make, pkg-config >= 0.9.0, gcc, perl, intltool, gettext
BuildRequires: glib2, dbus, dbus-glib, libpam
BuildRequires: expat, perl-XML-Parser
%define polkit_gid 30
%define polkit_uid 30

%description
PolicyKit is an application-level toolkit for defining and handling the policy
that allows unprivileged processes to speak to privileged processes: It is a
framework for centralizing the decision making process with respect to
granting access to privileged operations for unprivileged applications.
PolicyKit is specifically targeting applications in rich desktop environments
on multi-user UNIX-like operating systems. It does not imply or rely on any
exotic kernel features.


%prep
	%setup -q -n 'PolicyKit-%{version}'


%build
	%configure \
		--enable-man-pages \
		--with-authfw=pam \
		--with-pam-module-dir='/%{_lib}/security' \
		--with-pam-include=system-auth \
		--with-polkit-user=polkit \
		--with-polkit-group=polkit
	%{__make} %{?_smp_mflags}


%install
	%{__make} install DESTDIR='%{buildroot}'

	%{__mkdir_p} '%{buildroot}/%{_localstatedir}'/{run,lib}/PolicyKit
	%{__mkdir_p} '%{buildroot}/%{_localstatedir}'/lib/PolicyKit-public

	[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
		&& %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%pre
	if [[ "${1}" -eq 1 ]]
	then
		groupadd \
			-g '%{polkit_gid}' \
			polkit
		useradd \
			-u '%{polkit_uid}' \
			-g '%{polkit_gid}' \
			-s /sbin/nologin \
			-d '%{_localstatedir}/lib/PolicyKit' \
			polkit
	fi > /dev/null 2>&1
	exit 0


%postun
	if [[ "${1}" -eq 0 ]]
	then
		userdel polkit
		groupdel polkit
	fi > /dev/null 2>&1
	exit 0


%files
	%defattr(-, root, root)
	%doc README NEWS HACKING AUTHORS COPYING
	%dir %{_sysconfdir}/PolicyKit
	%config(noreplace) %{_sysconfdir}/PolicyKit/PolicyKit.conf
	%config %{_sysconfdir}/dbus-1/system.d/org.freedesktop.PolicyKit.conf
	%config(noreplace) %{_sysconfdir}/pam.d/polkit
	%attr(0755, root, root) %{_sysconfdir}/profile.d/polkit-bash-completion.sh
	%{_bindir}/polkit-action
	%{_bindir}/polkit-auth
	%{_bindir}/polkit-config-file-validate
	%{_bindir}/polkit-policy-file-validate
	%{_includedir}/PolicyKit/
	%{_libdir}/libpolkit-dbus.*
	%{_libdir}/libpolkit-grant.*
	%{_libdir}/libpolkit.*
	%{_libdir}/pkgconfig/polkit-dbus.pc
	%{_libdir}/pkgconfig/polkit-grant.pc
	%{_libdir}/pkgconfig/polkit.pc
	%attr(2751, root, polkit) %{_libexecdir}/polkit-explicit-grant-helper
	%attr(2751, root, polkit) %{_libexecdir}/polkit-grant-helper
	%attr(4751, root, polkit) %{_libexecdir}/polkit-grant-helper-pam
	%attr(2751, root, polkit) %{_libexecdir}/polkit-read-auth-helper
	%attr(4751, root, polkit) %{_libexecdir}/polkit-resolve-exe-helper
	%attr(2751, root, polkit) %{_libexecdir}/polkit-revoke-helper
	%attr(4751, root, polkit) %{_libexecdir}/polkit-set-default-helper
	%attr(0751, root, polkit) %{_libexecdir}/polkitd
	%doc %{_mandir}/man1/polkit-action.1*
	%doc %{_mandir}/man1/polkit-auth.1*
	%doc %{_mandir}/man1/polkit-config-file-validate.1*
	%doc %{_mandir}/man1/polkit-policy-file-validate.1*
	%doc %{_mandir}/man5/PolicyKit.conf.5*
	%doc %{_mandir}/man8/PolicyKit.8*
	%dir %{_datadir}/PolicyKit
	%{_datadir}/PolicyKit/config.dtd
	%dir %{_datadir}/PolicyKit/policy
	%{_datadir}/PolicyKit/policy/org.freedesktop.policykit.policy
	%{_datadir}/dbus-1/interfaces/org.freedesktop.PolicyKit.AuthenticationAgent.xml
	%{_datadir}/dbus-1/system-services/org.freedesktop.PolicyKit.service
	%dir %{_localstatedir}/lib/misc
	%attr(0644, polkit, polkit) %{_localstatedir}/lib/misc/PolicyKit.reload
	%dir %attr(0770, root, polkit) %{_localstatedir}/run/PolicyKit
	%dir %attr(0770, root, polkit) %{_localstatedir}/lib/PolicyKit
	%dir %attr(0755, root, polkit) %{_localstatedir}/lib/PolicyKit-public
