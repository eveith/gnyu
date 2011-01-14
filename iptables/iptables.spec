Name: iptables
Version: 1.4.8
Release: 1.0ev
Summary: Userspace utilities for the kernel package filter
URL: http://www.netfilter.org/
Group: System Environment/Base
License: GPL-2
Vendor: GNyU Linux
Source: ftp://ftp.netfilter.org/pub/iptables/%{name}-%{version}.tar.bz2
BuildRequires: make, gcc, libtool, kernel-headers

%description
iptables is the userspace command line program used to configure the Linux
2.4.x and 2.6.x IPv4 packet filtering ruleset. It is targeted towards system
administrators. 
Since Network Address Translation is also configured from the packet filter
ruleset, iptables is used for this, too. 
The iptables package also includes ip6tables. ip6tables is used for
configuring the IPv6 packet filter.


%package devel
Summary: Development package for iptables
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
iptables development headers and libraries.


%prep
%setup -q


%build
%configure \
	--sbindir=/sbin \
	--bindir=/bin \
	--libdir='/%{_lib}' \
	--libexecdir='/%{_lib}'
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

%{__mkdir_p} '%{buildroot}/%{_libdir}'
%{__mv} '%{buildroot}/%{_lib}/pkgconfig' '%{buildroot}/%{_libdir}'


%preun
if [ "$1" -gt 0 ]; then
	iptables-save
fi


%post
%{__ldconfig}
iptables-restore


%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc COPYING INCOMPATIBILITIES COMMIT_NOTES
%attr(0710, root, root) /sbin/ip6tables
%attr(0710, root, root) /sbin/ip6tables-multi
%attr(0710, root, root) /sbin/ip6tables-restore
%attr(0710, root, root) /sbin/ip6tables-save
%attr(0710, root, root) /sbin/iptables
%attr(0710, root, root) /sbin/iptables-multi
%attr(0710, root, root) /sbin/iptables-restore
%attr(0710, root, root) /sbin/iptables-save
%attr(0710, root, root) /bin/iptables-xml
/%{_lib}/libip4tc.so*
/%{_lib}/libip6tc.so*
/%{_lib}/libiptc.so*
/%{_lib}/libxtables.so*
%dir /%{_lib}/xtables
/%{_lib}/xtables/lib*.so
%doc %{_mandir}/man8/ip6tables.8*
%doc %{_mandir}/man8/ip6tables-restore.8*
%doc %{_mandir}/man8/ip6tables-save.8*
%doc %{_mandir}/man8/iptables-restore.8*
%doc %{_mandir}/man8/iptables-save.8*
%doc %{_mandir}/man8/iptables-xml.8*
%doc %{_mandir}/man8/iptables.8*


%files devel
%defattr(-, root, root)
%doc COPYING INCOMPATIBILITIES COMMIT_NOTES
/%{_lib}/libip4tc.la
/%{_lib}/libip6tc.la
/%{_lib}/libiptc.la
/%{_lib}/libxtables.la
%{_includedir}/*.h
%dir %{_includedir}/libiptc
%{_includedir}/libiptc/*.h
%{_libdir}/pkgconfig/libiptc.pc
%{_libdir}/pkgconfig/xtables.pc
