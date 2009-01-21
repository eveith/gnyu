Name: bitlbee
Version: 1.0.4
Release: 1ev
Summary: An IRC to other chat networks gateway
URL: http://www.bitlbee.org/
Group: Applications/Internet
License: GPL-2
Vendor: MSP Slackware
Source0: http://get.bitlbee.org/src/bitlbee-%{version}.tar.gz
Source1: %{name}-bitlbee.i
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, openssl, pkg-config, glib2
Requires: ucspi-tcp

%description
BitlBee allows users to talk to people on the MSN, ICQ, Jabber, Yahoo!, and 
AIM networks with any IRC client by emulating an IRC server. A virtual 
channel is created with all of the user's buddies in it, who can be talked 
to in the channel or in a query


%prep
%setup -q


%build
CFLAGS="$RPM_OPT_FLAGS"; export CFLAGS
./configure \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--etcdir=/%{_sysconfdir}/bitlbee \
	--datadir=%{_datadir}/bitlbee \
	--config=/%{_localstatedir}/lib/bitlbee \
	--msn=1 \
	--jabber=1 \
	--oscar=1 \
	--yahoo=1 \
	--debug=0 \
	--strip=1 \
	--ipv6=1 \
	--ssl=openssl
%{__make} %{?_smp_mflags}


%install
[[ -d '%{buildroot}' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%{__install} -d %{buildroot}/%{_localstatedir}/lib/bitlbee
%{__install} -d %{buildroot}/%{_sysconfdir}/bitlbee
%{__install} -m0644 motd.txt bitlbee.conf \
	%{buildroot}/%{_sysconfdir}/bitlbee

%{__mkdir_p} %{buildroot}/%{_sysconfdir}/tcpserver-cdb.d
touch %{buildroot}/%{_sysconfdir}/tcpserver-cdb.d/bitlbee.cdb

%{__mkdir_p} %{buildroot}/etc/initng/daemon
%{__cat} < %{SOURCE2} \
	| sed -e 's,@bitlbee@,%{_bindir}/bitlbee,g' \
	> %{buildroot}/etc/initng/daemon/bitlbee.i

if [[ '%{_mandir}' != '%{_datadir}/man' ]]
then
	pushd %{buildroot}
	mv ./%{_datadir}/man ./%{_mandir}
	popd
fi

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post

%postun


%clean
[[ -d '%{buildroot}' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc COPYING doc/AUTHORS doc/CHANGES doc/CREDITS doc/FAQ doc/README
/etc/initng/daemon/bitlbee.i
%dir %{_sysconfdir}/bitlbee
%config(noreplace) %{_sysconfdir}/bitlbee/bitlbee.conf
%config(noreplace) %{_sysconfdir}/bitlbee/motd.txt
%ghost %config(noreplace) %{_sysconfdir}/tcpserver-cdb.d/bitlbee.cdb
%{_bindir}/bitlbee
%{_mandir}/man8/bitlbee.8*
%{_mandir}/man5/bitlbee.conf.5*
%dir %{_datadir}/bitlbee
%{_datadir}/bitlbee/help.txt
%dir %{_localstatedir}/lib/bitlbee
