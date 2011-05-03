Name: bridge-utils
Version: 1.5
Release: 1.0
Summary: Software Ethernet Bridge Utilities
URL: http://www.linuxfoundation.org/collaborate/workgroups/networking/bridge
Group: System Environment/Base
License: GPL-2
Source: http://downloads.sourceforge.net/project/bridge/bridge/bridge-utils-%{version}.tar.gz
BuildRequires: autoconf, grep, sed, make, gcc
BuildRequires: eglibc-devel, kernel-headers

%description
A bridge is a way to connect two Ethernet segments together in a protocol
independent way. Packets are forwarded based on Ethernet address, rather than
IP address (like a router). Since forwarding is done at Layer 2, all protocols
can go transparently through a bridge.
The Linux bridge code implements a subset of the ANSI/IEEE 802.1d standard.
The original Linux bridging was first done in Linux 2.2, then rewritten
by Lennert Buytenhek. The code for bridging has been integrated into 2.4 and
2.6 kernel series.


%prep
%setup -q
%{__autoconf}


%build
%configure \
    --sbindir=/sbin
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog THANKS README TODO
%attr(0710, root, root) /sbin/brctl
%doc %{_mandir}/man8/brctl.8*
