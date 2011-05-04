Name: etcnet
Version: 0.9.10
Release: 0.9
Summary: /etc/net network configuration system
License: GPL-2
Group: System Environment/Base
URL: http://etcnet.org/
Source:	%{name}-%{version}.tar.gz
BuildRequires: make, findutils
Requires: grep, sed, iproute2
BuildArch:	noarch

%description
/etc/net represents a new approach to Linux network configuration tasks.
Inspired by the limitations of traditional network configuration subsystems,
/etc/net provides builtin support for configuration profiles, interface name
management, removable devices, full iproute2 command set, interface
dependencies resolution, QoS and firewall configuration frameworks.
/etc/net provides support for the following interface types: Ethernet, WiFi
(WEP), IPv4/IPv6 tunnels, PSK IPSec tunnels, VLAN, PLIP, Ethernet bonding and
bridging, traffic equalizer, Pent@NET, Pent@VALUE, SkyStar-2, TUN/TAP,
OpenVPN TUN/TAP, OpenSSH TUN/TAP, usbnet and PPP. Due to its modular structure,
support for new interface types can be added without overall design changes.


%prep
%setup -q
# Don't package .htaccess (https://bugzilla.altlinux.org/show_bug.cgi?id=10101)
find . -type f -a -name .htaccess -exec rm -f \{\} \;

%install
%{__make} -f contrib/Makefile prefix=%{buildroot} install
%{__mv} '%{buildroot}%{_datadir}/man' '%{buildroot}%{_mandir}' && \
    %{__rm_rf} '%{buildroot}%{_datadir}'
%{__rm_rf} '%{buildroot}%{_sysconfdir}/rc.d'


%files
%doc docs/README* docs/ChangeLog docs/TODO
%doc examples/ contrib/
%dir %{_sysconfdir}/net
%dir %{_sysconfdir}/net/scripts
%dir %{_sysconfdir}/net/ifaces
%dir %{_sysconfdir}/net/ifaces/default
%dir %{_sysconfdir}/net/ifaces/lo
%dir %{_sysconfdir}/net/ifaces/unknown
%dir %{_sysconfdir}/net/options.d
%{_sysconfdir}/net/scripts/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/net/ifaces/default/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/net/ifaces/unknown/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/net/ifaces/lo/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/net/sysctl.conf
%config %{_sysconfdir}/net/options.d/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sysconfig/network
%doc %{_mandir}/man5/etcnet-options.5*
%doc %{_mandir}/man8/etcnet.8*
%doc %{_mandir}/man8/etcnet-qos.8*
%attr(0700, root, root) /sbin/ifup
%attr(0700, root, root) /sbin/ifdown
%attr(0700, root, root) /sbin/eqos
%attr(0700, root, root) /sbin/efw
