Name: vpnc
Version: 0.5.1
Release: 2ev
Summary: A client for the Cisco VPN concentrator
URL: http://www.unix-ag.uni-kl.de/~massar/vpnc/
Group: Applications/Security
License: GPL-2
Vendor: GNyU-Linux
Source: http://www.unix-ag.uni-kl.de/~massar/vpnc/vpnc-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make >= 3.79.1, gcc, libgcrypt >= 1.1.90, libgpg-error, perl
BuildRequires: openssl
Requires: iproute2

%description
A VPN client compatible with Cisco's EasyVPN equipment.
Supports IPSec (ESP) with Mode Configuration and Xauth.  Supports only
shared-secret IPSec authentication with Xauth,
AES (256, 192, 128), 3DES, 1DES, MD5, SHA1,
DH1/2/5 and IP tunneling.
It runs entirely in userspace. Only "Universal TUN/TAP device
driver support" is needed in kernel.


%prep
%setup -q


%build
%{__make} %{?_smp_mflags} \
	CC='%{_target_platform}-gcc' \
	CFLAGS="$RPM_OPT_FLAGS" 


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} \
	PREFIX='%{_prefix}' \
	BINDIR='%{_bindir}' \
	MANDIR='%{_mandir}' \
	SBINDIR='%{_sbindir}' \
	DESTDIR='%{buildroot}'

[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc README COPYING TODO VERSION 
%dir /etc/vpnc
%config /etc/vpnc/*
%{_bindir}/cisco-decrypt
%{_bindir}/pcf2vpnc
%{_sbindir}/vpnc*
%{_mandir}/man1/cisco-decrypt.1*
%{_mandir}/man1/pcf2vpnc.1*
%{_mandir}/man8/vpnc.8*
