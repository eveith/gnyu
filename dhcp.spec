Name: dhcp-server
Version: 4.1.0
Release: 5ev
Summary: The ISC DHCP server daemon
URL: http://www.isc.org/sw/bind/
Group: System Environment/Daemons 
License: BSD
Vendor: GNyU-Linux
Source0: http://ftp.isc.org/isc/dhcp/dhcp-%{version}.tar.gz
Source1: dhcp-dhclient.i
Source2: dhcp-dhcpd.i
Source3: dhcp-dhclient-script
BuildRequires: make, gcc, openssl

%description
The Internet Software Consortium DHCP distribution includes a DHCP client, a
DHCP server, and a DHCP relay agent. DHCP is a protocol for automatically
configuring nodes on an IP network. The ISC DHCP server and client are well
known for being extremely configurable, reasonably easy to use, and quite
efficient.
This package, including the DHCP server and the relay agent are used to
configure DHCP-aware clients in a network.


%package -n dhclient
Summary: ISC DHCP suite's client daemon
Group: System Environment/Daemons
License: BSD

%description -n dhclient
The Internet Software Consortium DHCP distribution includes a DHCP client, a
DHCP server, and a DHCP relay agent. DHCP is a protocol for automatically
configuring nodes on an IP network. The ISC DHCP server and client are well
known for being extremely configurable, reasonably easy to use, and quite
efficient.
This package contains the client daemon, dhclient, which is needed to
configure a linux system dynamically via DHCP.



%prep
%setup -q -n dhcp-%{version}


%build
%configure \
	--with-srv-lease-file='%{_localstatedir}/state/dhcpd.leases' \
	--with-srv6-lease-file='%{_localstatedir}/state/dhcpd6.leases' \
	--with-cli-lease-file='%{_localstatedir}/state/dhclient.leases' \
	--with-cli6-lease-file='%{_localstatedir}/state/dhclient6.leases' \
	--with-srv-pid-file='%{_localstatedir}/run/dhcpd.pid' \
	--with-srv6-pid-file='%{_localstatedir}/run/dhcpd6.pid' \
	--with-cli-pid-file='%{_localstatedir}/run/dhclient.pid' \
	--with-cli6-pid-file='%{_localstatedir}/run/dhclient6.pid' \
	--with-relay-pid-file='%{_localstatedir}/run/dhcrelay.pid' \
	--disable-dhcpv6
%{__make} %{?_smp_mflags}

# Rebuild the DHCP client. DHCP now uses -lcrypto for the whole suite, but
# dhclient lies in /sbin, whereas libcrypto* are in /usr/lib. When we request
# an IP address early during boot, /usr isn't mounted, and dhclient won't run.
# We re-build using static linking.
%{__make} -C client clean
%{__make} -C client %{?_smp_mflags} LDFLAGS='-static'
	


%install
%{__make_install} DESTDIR='%{buildroot}'

%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/initng/daemon'
%{__cat} < '%{SOURCE1}' \
	| %{__sed} \
		-e 's,@localstatedir@,%{_localstatedir},g' \
		-e 's,@dhclient@,/sbin/dhclient,g' \
	> '%{buildroot}/%{_sysconfdir}/initng/daemon/dhclient.i'
%{__cat} < '%{SOURCE2}' \
	| %{__sed} -e 's,@dhcpd@,%{_sbindir}/dhcpd,g' \
	> '%{buildroot}/%{_sysconfdir}/initng/daemon/dhcpd.i'

%{__mkdir_p} '%{buildroot}/%{_localstatedir}'/{state,run}
for i in dhcpd dhcpd6 dhclient dhclient6
do
	touch "%{buildroot}/%{_localstatedir}/run/${i}.pid"
	touch "%{buildroot}/%{_localstatedir}/state/${i}.leases"{,~}
done
touch '%{buildroot}/%{_localstatedir}/run/dhcrelay.pid'

touch '%{buildroot}/%{_sysconfdir}/dhclient.conf'
touch '%{buildroot}/%{_sysconfdir}/dhcpd.conf'

# dhclient is needed at boottime, move it to /sbin:
%{__mkdir_p} '%{buildroot}/sbin'
%{__mv} '%{buildroot}/%{_sbindir}/dhclient' '%{buildroot}/sbin'

# Install dhclient-script
%{__cp} '%{SOURCE3}' '%{buildroot}/sbin/dhclient-script'


%post
%{__ldconfig}
if [[ "${1}" -eq 1 ]]
then
	ng-update add daemon/dhcpd default
fi > /dev/null 2>&1
exit 0

%preun
if [[ "${1}" -eq 0 ]]
then
	ngc -d daemon/dhcpd
	ng-update del daemon/dhcpd default
fi > /dev/null 2>&1
exit 0

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc README LICENSE RELNOTES server/dhcpd.conf doc/api+protocol
%doc doc/References.html doc/References.txt
%attr(0640, root, root) %{_sysconfdir}/initng/daemon/dhcpd.i
%ghost %config(noreplace) %attr(0640, root, root) %{_sysconfdir}/dhcpd.conf
%attr(0700, root, root) %{_sbindir}/dhcpd
%attr(0700, root, root) %{_sbindir}/dhcrelay
%{_bindir}/omshell
%{_libdir}/libdhcpctl.a
%{_libdir}/libdst.a
%{_libdir}/libomapi.a
%{_includedir}/dhcpctl/
%{_includedir}/omapip/
%{_includedir}/isc-dhcp/
%doc %{_mandir}/man1/omshell.1*
%doc %{_mandir}/man3/dhcpctl.3*
%doc %{_mandir}/man3/omapi.3*
%doc %{_mandir}/man5/dhcp-eval.5*
%doc %{_mandir}/man5/dhcp-options.5*
%doc %{_mandir}/man5/dhcpd.conf.5*
%doc %{_mandir}/man5/dhcpd.leases.5*
%doc %{_mandir}/man8/dhcpd.8*
%doc %{_mandir}/man8/dhcrelay.8*
%ghost %attr(0640, root, root) %config(noreplace) %verify(not size md5) %{_localstatedir}/run/dhcpd.pid
%ghost %attr(0640, root, root) %config(noreplace) %verify(not size md5) %{_localstatedir}/run/dhcpd6.pid
%ghost %attr(0640, root, root) %config(noreplace) %verify(not size md5) %{_localstatedir}/run/dhcrelay.pid
%ghost %attr(0640, root, root) %config(noreplace) %{_localstatedir}/state/dhcpd.leases*
%ghost %attr(0640, root, root) %config(noreplace) %{_localstatedir}/state/dhcpd6.leases*

%files -n dhclient 
%doc README client/dhclient.conf
%attr(0640, root, root) %{_sysconfdir}/initng/daemon/dhclient.i
%ghost %config(noreplace) %attr(0640, root, root) %{_sysconfdir}/dhclient.conf
%attr(0700, root, root) /sbin/dhclient
%attr(0700, root, root) /sbin/dhclient-script
%doc %{_mandir}/*/dhclient*.*
%ghost %attr(0640, root, root) %config(noreplace) %verify(not size md5) %{_localstatedir}/run/dhclient.pid
%ghost %attr(0640, root, root) %config(noreplace) %verify(not size md5) %{_localstatedir}/run/dhclient6.pid
%ghost %attr(0640, root, root) %config(noreplace) %{_localstatedir}/state/dhclient.leases*
%ghost %attr(0640, root, root) %config(noreplace) %{_localstatedir}/state/dhclient6.leases*
