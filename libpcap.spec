Name: libpcap
Version: 0.9.8
Release: 1ev
Summary: A packet capturing library
URL: http://www.tcpdump.org/
Group: System Environment/Libraries
License: BSD
Vendor: GNyU-Linux
Source: http://www.tcpdump.org/release/libpcap-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: coreutils, grep, sed, gawk, make, gcc, flex >= 2.5.4, bison

%description
libpcap is a system-independent interface for user-level packet capture.
It provides a portable framework for low-level network monitoring.
Applications using this library include network statistics collection,
security monitoring, network debugging, etc. Since almost every system vendor
provides a different interface for packet capture, and since several tools that
require this functionality are developed, this system-independent API eases in
porting and alleviates the need for several system-dependent packet capture
modules in each application.


%prep
%setup -q


%build
%configure \
	--enable-ipv6
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc README* SUNOS4 TODO VERSION LICENSE CVS CREDITS CHANGES
%{_includedir}/pcap*.h
%{_libdir}/libpcap.a
%{_mandir}/man3/pcap.3*
