Name: dhcp-server
Version: 3.0.5
Release: 1ev
Summary: The ISC DHCP server daemon
URL: http://www.isc.org/sw/bind/
Group: System Environment/Daemons 
License: BSD
Vendor: MSP Slackware
Source0: http://ftp.isc.org/isc/dhcp/dhcp-%{version}.tar.gz
Source1: dhcp-dhclient.i
Source2: dhcp-dhcpd.i
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core

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
cat << __END__ > site.conf
CC_OPTIONS="$RPM_OPT_FLAGS"
DEBUG=
CC=%{_target_platform}-gcc
USRBINDIR=%{_bindir}
BINDIR=%{_bindir}
CLIENTBINDIR=/sbin
ADMMANDIR=%{_mandir}/man8
ADMMANEXT=".8"
FFMANDIR=%{_mandir}/man5
FFMANEXT=".5"
LIBDIR=%{_libdir}
INCDIR=%{_includedir}
VARRUN=/%{_var}/run/dhcp
VARLIB=/%{_var}/lib/dhcp
__END__

./configure
make %{_smp_mflags}
	


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"

pushd "$RPM_BUILD_ROOT"

mkdir -p ./etc/initng/daemon
cp %{SOURCE1} ./etc/initng/daemon/dhclient.i
cat %{SOURCE2} \
	| sed 's,@dhcpd@,%{_bindir}/dhcpd,g' \
	> ./etc/initng/daemon/dhcpd.i

mkdir -p ./%{_var}/{lib,run}/dhcp
touch ./%{_var}/lib/dhcp/{dhcpd,dhclient}.leases{,~} \
	./%{_var}/run/dhcp/{dhcpd,dhclient}.pid

touch ./etc/dhclient.conf ./etc/dhcpd.conf

popd

[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
/sbin/ldconfig
if [ "$1" -gt 1 ] && ngc -s | grep 'daemon/dhcpd' > /dev/null 2>&1
then
	ngc -r daemon/dhclient > /dev/null 2>&1 || :
fi

%preun
if [ "$1" -eq 0 ] && ngc -s | grep 'daemon/dhcpd' > /dev/null 2>&1
then
	ngc -d daemon/dhclient > /dev/null 2>&1 || :
fi


%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc README server/dhcpd.conf
/etc/initng/daemon/dhcpd.i
%ghost %config(noreplace) /etc/dhcpd.conf
%{_bindir}/dhcpd
%{_bindir}/dhcrelay
%{_bindir}/omshell
%{_libdir}/*.a
%{_includedir}/dhcpctl.h
%{_includedir}/omapip/
%{_includedir}/isc-dhcp/
%{_mandir}/man1/omshell.1*
%{_mandir}/man3/*.3*
%{_mandir}/man5/dhcp*.5*
%{_mandir}/man8/dhc*.8*
%dir /%{_var}/lib/dhcp
%dir /%{_var}/run/dhcp
%ghost /%{_var}/run/dhcp/dhcpd.pid
%ghost /%{_var}/lib/dhcp/dhcpd.leases*

%files -n dhclient 
%doc README client/dhclient.conf
/etc/initng/daemon/dhclient.i
%ghost %config(noreplace) /etc/dhclient.conf
/sbin/dhclient*
%{_mandir}/*/dhclient*.*
%dir /%{_var}/lib/dhcp
%dir /%{_var}/run/dhcp
%ghost /%{_var}/run/dhcp/dhclient.pid
%ghost /%{_var}/lib/dhcp/dhclient.leases*
