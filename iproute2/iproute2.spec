Name: iproute2
Version: 2.6.38
Release: 1.0
Summary: Tools for controlling TCP/IP networking and traffic
URL: http://www.linuxfoundation.org/collaborate/workgroups/networking/iproute2
Group: System Environment/Base
License: GPL-2
Source: http://devresources.linuxfoundation.org/dev/iproute2/download/iproute2-%{version}.tar.bz2
BuildRequires: grep, sed, make, gcc, bison, flex
BuildRequires: eglibc-devel, kernel-headers
BuildRequires: iptables-devel >= 1.4.5

%description
The iproute suite, also known as iproute2, is a collection of utilities for
networking and traffic control.
These tools communicate with the Linux kernel via the (rt)netlink interface,
providing advanced features not available through the legacy net-tools
commands 'ifconfig' and 'route'.


%package devel
Summary: Development headers for iproute2 extension building
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
The iproute suite, also known as iproute2, is a collection of utilities for
networking and traffic control.
This package contains the header files and static libraries for compiling
iproute extensions, and is needed only for development. 


%prep
%setup -q

# Disable arpd for now:
%{__sed} -i 's,^TARGETS=\(.*\)arpd\(.*\),TARGETS=\1\2,' misc/Makefile


%build
%{__make} %{?_smp_mflags}


%install
%{__make} install \
    MANDIR='%{_mandir}' \
    DESTDIR='%{buildroot}'
    
%{__rm_rf} '%{buildroot}/share/doc'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%files
%defattr(-, root, root)
%doc COPYING ChangeLog README* RELNOTES doc examples
%dir %{_sysconfdir}/iproute2
%{_sysconfdir}/iproute2/ematch_map
%{_sysconfdir}/iproute2/rt_dsfield
%{_sysconfdir}/iproute2/rt_protos
%{_sysconfdir}/iproute2/rt_realms
%{_sysconfdir}/iproute2/rt_scopes
%{_sysconfdir}/iproute2/rt_tables
%attr(0710, root, root) /sbin/ip
/sbin/rtmon
/sbin/ifcfg
/sbin/rtpr
/sbin/routel
/sbin/routef
%attr(0710, root, root) /sbin/tc
%attr(0710, root, root) /sbin/ss
/sbin/nstat
/sbin/ifstat
/sbin/rtacct
/sbin/lnstat
/sbin/rtstat
/sbin/ctstat
/sbin/genl
%dir /%{_lib}/tc
/%{_lib}/tc/m_xt.so
/%{_lib}/tc/m_ipt.so
%dir %{_libdir}/tc
%{_libdir}/tc/*.dist
%doc %{_mandir}/man8/arpd.8*
%doc %{_mandir}/man8/ip.8*
%doc %{_mandir}/man8/lnstat.8*
%doc %{_mandir}/man8/routel.8*
%doc %{_mandir}/man8/rtacct.8*
%doc %{_mandir}/man8/rtmon.8*
%doc %{_mandir}/man8/ss.8*
%doc %{_mandir}/man8/tc-bfifo.8*
%doc %{_mandir}/man8/tc-cbq-details.8*
%doc %{_mandir}/man8/tc-cbq.8*
%doc %{_mandir}/man8/tc-drr.8*
%doc %{_mandir}/man8/tc-htb.8*
%doc %{_mandir}/man8/tc-pfifo_fast.8*
%doc %{_mandir}/man8/tc-prio.8*
%doc %{_mandir}/man8/tc-red.8*
%doc %{_mandir}/man8/tc-sfq.8*
%doc %{_mandir}/man8/tc-tbf.8*
%doc %{_mandir}/man8/tc.8*
%doc %{_mandir}/man8/tc-pfifo.8*
%doc %{_mandir}/man8/rtstat.8*
%doc %{_mandir}/man8/ctstat.8*
%doc %{_mandir}/man8/nstat.8*
%doc %{_mandir}/man8/routef.8*
%doc %{_mandir}/man3/libnetlink.3*
