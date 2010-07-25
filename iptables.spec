Name: iptables
Version: 1.4.0
Release: 1ev
Summary: Userspace utilities for the kernel package filter
URL: http://www.netfilter.org/
Group: System Environment/Base
License: GPL-2
Vendor: MSP Slackware
Source: ftp://ftp.netfilter.org/pub/iptables/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: gcc-core, make >= 3.79.1

%description
iptables is the userspace command line program used to configure the Linux
2.4.x and 2.6.x IPv4 packet filtering ruleset. It is targeted towards system
administrators. 
Since Network Address Translation is also configured from the packet filter
ruleset, iptables is used for this, too. 
The iptables package also includes ip6tables. ip6tables is used for
configuring the IPv6 packet filter.


%prep
%setup -q


%build
%{__make} \
	CC='%{_target_platform}-gcc' \
	COPT_FLAGS="$RPM_OPT_FLAGS" \
	BINDIR='%{_sbindir}' \
	LIBDIR='%{_libdir}' \
	MANDIR='%{_mandir}' \
	INCDIR='%{_includedir}'


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} \
	BINDIR='%{_sbindir}' \
	LIBDIR='%{_libdir}' \
	MANDIR='%{_mandir}' \
	INCDIR='%{_includedir}' \
	DESTDIR='%{buildroot}' \
	PREFIX='%{_prefix}'


%preun
if [ "$1" != "0" ]
then
	iptables-save
fi

%post
/sbin/ldconfig
iptables-restore

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc COPYING INCOMPATIBILITIES COMMIT_NOTES
%{_libdir}/iptables/
%{_mandir}/man8/ip6tables.8*
%{_mandir}/man8/ip6tables-restore.8*
%{_mandir}/man8/ip6tables-save.8*
%{_mandir}/man8/iptables-restore.8*
%{_mandir}/man8/iptables-save.8*
%{_mandir}/man8/iptables.8*
%{_sbindir}/ip6tables
%{_sbindir}/ip6tables-restore
%{_sbindir}/ip6tables-save
%{_sbindir}/iptables
%{_sbindir}/iptables-restore
%{_sbindir}/iptables-save
%{_sbindir}/iptables-xml
