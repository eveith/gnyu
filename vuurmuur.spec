Name: vuurmuur
Version: 0.7
Release: 3.0ev
Summary: IPTables firewall monitoring and auditing daemons
URL: http://vuurmuur.sf.net/
Group: System Environment/Daemons
License: GPL-2
Vendor: GNyU-Linux
Source0: ftp://ftp.vuurmuur.org/releases/0.7/Vuurmuur-%{version}.tar.gz
Source1: %{name}-config.conf
Source3: %{name}-vuurmuur.ii
BuildRequires: make, gcc, libtool
BuildRequires: libvuurmuur-devel = %{version}
Requires: iptables >= 1.3.8

%description
The backend of Vuurmuur monitors the firewall itself: In- and outgoing
traffic, connection attempts, and so on. It can take actions against attackers
(i.e., by watching for multiple connections attempts from one host to a
particular service) or enforce block lists.


%prep
%setup -q -n 'Vuurmuur-%{version}'
%{__gzip} -dc 'vuurmuur-%{version}.tar.gz' | %{__tar} -x
%setup -D -T -n 'Vuurmuur-%{version}/vuurmuur-%{version}'


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

for d in interfaces services zones rules; do
	%{__mkdir_p} "%{buildroot}%{_sysconfdir}/vuurmuur/textdir/${d}"
done

%{__touch} '%{buildroot}%{_sysconfdir}/vuurmuur/textdir/rules/rules.conf'
%{__touch} \
	'%{buildroot}%{_sysconfdir}/vuurmuur/textdir/rules/blocklist.conf'
%{__cp} '%{SOURCE1}' '%{buildroot}%{_sysconfdir}/vuurmuur/config.conf'

%{__mkdir_p} '%{buildroot}%{_sysconfdir}/initng/daemon'
%{install_ifile '%{SOURCE3}' daemon/vuurmuur.i}

%{__mkdir_p} '%{buildroot}%{_localstatedir}/log/vuurmuur'
for f in audit debug error traffic vuurmuur; do
	%{__touch} "%{buildroot}%{_localstatedir}/log/vuurmuur/${f}.log"
done


%post
for service in '%{_datadir}/vuurmuur/services'/*; do
	basename=$(basename "${service}")
	if [[ ! -e "%{_sysconfdir}/vuurmuur/textdir/services/${basename}" ]]; then
		%{__install} -m0600 "%{_datadir}/vuurmuur/services/${basename}" \
			"%{_sysconfdir}vuurmuur/textdir/services/${basename}"
	fi
done


%preun
if [[ "$1" -eq 0 ]]; then
	ngc -d 'daemon/vuurmuur'
	ng-update remove daemon/vuurmuur
fi > /dev/null 2>&1
exit 0


%files
%defattr(-, root, root)
%doc README INSTALL*
%dir %attr(0750, root, root) %{_sysconfdir}/vuurmuur
%dir %attr(0750, root, root) %{_sysconfdir}/vuurmuur/textdir
%dir %attr(0750, root, root) %{_sysconfdir}/vuurmuur/textdir/rules
%dir %attr(0750, root, root) %{_sysconfdir}/vuurmuur/textdir/interfaces
%dir %attr(0750, root, root) %{_sysconfdir}/vuurmuur/textdir/services
%dir %attr(0750, root, root) %{_sysconfdir}/vuurmuur/textdir/zones
%config(noreplace) %attr(0640, root, root) %{_sysconfdir}/vuurmuur/config.conf
%ghost %config(noreplace) %attr(0640, root, root) %{_sysconfdir}/vuurmuur/textdir/rules/rules.conf
%ghost %config(noreplace) %attr(0640, root, root) %{_sysconfdir}/vuurmuur/textdir/rules/blocklist.conf
%attr(0700, root, root) %{_sysconfdir}/initng/daemon/vuurmuur.i
%attr(0700, root, root) %{_bindir}/vuurmuur
%attr(0700, root, root) %{_bindir}/vuurmuur_log
%attr(0750, root, root) %{_bindir}/vuurmuur_script
%doc %{_mandir}/man8/vuurmuur.8*
%doc %{_mandir}/man8/vuurmuur_log.8*
%doc %{_mandir}/man8/vuurmuur_script.8*
%doc %{_mandir}/*/man8/vuurmuur.8*
%doc %{_mandir}/*/man8/vuurmuur_log.8*
%doc %{_mandir}/*/man8/vuurmuur_script.8*
%dir %{_datadir}/vuurmuur/config
%dir %{_datadir}/vuurmuur/scripts
%dir %{_datadir}/vuurmuur/services
%{_datadir}/vuurmuur/scripts/*
%{_datadir}/vuurmuur/services/*
%config %{_datadir}/vuurmuur/config/*
%dir %{_localstatedir}/log/vuurmuur
%ghost %config(noreplace) %verify(not size md5 mtime) %{_localstatedir}/log/vuurmuur/*.log
