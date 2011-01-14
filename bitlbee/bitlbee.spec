Name: bitlbee
Version: 1.2.3
Release: 2ev
Summary: An IRC to other chat networks gateway
URL: http://www.bitlbee.org/
Group: Applications/Internet
License: GPL-2
Vendor: GNyU-Linux
Source0: http://get.bitlbee.org/src/bitlbee-%{version}.tar.gz
Source1: %{name}-bitlbee.i
Source2: %{name}-bitlbee.tcpserver-rules.txt
BuildRequires: make, gcc, gnutls, pkg-config, glib2
Requires: ucspi-tcp
%define bitlbee_uid 508
%define bitlbee_gid 99

%description
BitlBee allows users to talk to people on the MSN, ICQ, Jabber, Yahoo!, and 
AIM networks with any IRC client by emulating an IRC server. A virtual 
channel is created with all of the user's buddies in it, who can be talked 
to in the channel or in a query


%prep
%setup -q


%build
CFLAGS="${RPM_OPT_FLAGS}"; export CFLAGS
./configure \
	--prefix='%{_prefix}' \
	--bindir='%{_bindir}' \
	--etcdir='%{_sysconfdir}/bitlbee' \
	--datadir='%{_datadir}/bitlbee' \
	--config='%{_localstatedir}/lib/bitlbee' \
	--ipcsocket='/tmp/bitlbee.sock' \
	--msn=1 \
	--jabber=1 \
	--oscar=1 \
	--yahoo=1 \
	--debug=0 \
	--strip=1 \
	--ipv6=1 \
	--ssl=gnutls
%{__make} %{?_smp_mflags}


%install
%{__make_install} DESTDIR='%{buildroot}'
%{__install} -d %{buildroot}/%{_localstatedir}/lib/bitlbee
%{__install} -d %{buildroot}/%{_sysconfdir}/bitlbee
%{__install} -m0644 motd.txt bitlbee.conf \
	%{buildroot}/%{_sysconfdir}/bitlbee
touch '%{buildroot}/%{_sysconfdir}/bitlbee/bitlbee.tcpserver-rules.cdb'
touch '%{buildroot}/%{_sysconfdir}/bitlbee/bitlbee.tcpserver-rules.cdb.tmp'
%{__mkdir_p} '%{buildroot}/tmp'
touch '%{buildroot}/tmp/bitlbee.sock'

%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/initng/daemon'
%{__cat} < '%{SOURCE1}' \
	| %{__sed} -e 's,@bitlbee@,%{_bindir}/bitlbee,g' \
		-e 's,@sysconfdir@,%{_sysconfdir},g' \
		-e 's,@bitlbee_uid@,%{bitlbee_uid},g' \
		-e 's,@bitlbee_gid@,%{bitlbee_gid},g' \
	> '%{buildroot}/%{_sysconfdir}/initng/daemon/bitlbee.i'
%{__cat} < '%{SOURCE2}' > '%{buildroot}/%{_sysconfdir}/bitlbee/bitlbee.tcpserver-rules.txt'

# Move manpages if installed in the wrong place
if [[ '%{_mandir}' != '%{_datadir}/man' ]]
then
	pushd '%{buildroot}'
	%{__mv} ./%{_datadir}/man ./%{_mandir}
	popd
fi


%pre
if [[ "${1}" -eq 1 ]]
then
	useradd \
		-u '%{bitlbee_uid}' \
		-g '%{bitlbee_gid}' \
		-c 'Bitlbee IRC-to-IM gateway daemon user' \
		-s /sbin/nologin \
		-d '%{_localstatedir}/lib/bitlbee' \
		bitlbee
fi

%postun
if [[ "${1}" -eq 0 ]]
then
	ngc -d daemon/bitlbee
	ng-update delete daemon/bitlbee default
	userdel bitlbee
fi > /dev/null 2>&1
exit 0


%files
%defattr(-, root, root)
%doc COPYING doc/AUTHORS doc/CHANGES doc/CREDITS doc/FAQ doc/README
%attr(0700, root, root) %{_sysconfdir}/initng/daemon/bitlbee.i
%dir %{_sysconfdir}/bitlbee
%attr(0600, root, root) %config(noreplace) %{_sysconfdir}/bitlbee/bitlbee.tcpserver-rules.txt
%attr(0600, root, root) %ghost %{_sysconfdir}/bitlbee/bitlbee.tcpserver-rules.cdb.tmp
%attr(0440, bitlbee, root) %ghost %{_sysconfdir}/bitlbee/bitlbee.tcpserver-rules.cdb
%config(noreplace) %{_sysconfdir}/bitlbee/bitlbee.conf
%config(noreplace) %{_sysconfdir}/bitlbee/motd.txt
%{_bindir}/bitlbee
%doc %{_mandir}/man8/bitlbee.8*
%doc %{_mandir}/man5/bitlbee.conf.5*
%dir %{_datadir}/bitlbee
%{_datadir}/bitlbee/help.txt
%attr(0770, bitlbee, root) %dir %{_localstatedir}/lib/bitlbee
%ghost /tmp/bitlbee.sock
