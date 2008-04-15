Name: kvpnc
Version: 0.9.0
Release: 1ev
Summary: A KDE frontend to various VPN clients
URL: http://home.gna.org/kvpnc/
Group: Applications/Security
License: GPL-2
Vendor: GNyU-Linux
Source: http://download.gna.org/kvpnc/kvpnc-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-g++, qt3, arts, kdelibs, kdebase, libgcrypt, gettext

%description
KVpnc is a KDE Desktop Environment frontend for various vpn clients. 
It supports Cisco VPN (vpnc, vpnclient (proritary client from cisco)), 
IPSec (FreeS/WAN, OpenS/WAN, stronGswan, racoon), PPTP (pptpclient), L2TP, 
OpenVPN and VTun.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%find_lang kvpnc

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files -f kvpnc.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO doc/*.txt
%doc %{_datadir}/doc/HTML/kvpnc
%doc %{_datadir}/doc/HTML/*/kvpnc
%{_bindir}/kvpnc
%{_datadir}/applnk/kvpnc.desktop
%{_datadir}/apps/kvpnc/
%{_datadir}/icons/??color/*/apps/kvpnc.png
