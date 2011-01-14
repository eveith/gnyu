Name: mdadm
Version: 3.1.2
Release: 4.0ev
Summary: A tool to create, maintain, and monitor Linux Software RAID
URL: http://www.cse.unsw.edu.au/~neilb/source/mdadm
Group: System Environment/Base
License: GPL-2
Vendor: GNyU-Linux
Source: http://www.kernel.org/pub/linux/utils/raid/mdadm/mdadm-%{version}.tar.bz2
Source1: %{name}-mdadm.ii
BuildRequires: make, gcc, kernel-headers

%description
mdadm is a tool for creating, maintaining, and monitoring Linux "md" device
arrays, also known as Software RAID. 


%prep
%setup -q


%build
CFLAGS="${CFLAGS:-%{optflags}} -D\"u8=__u8\""
%{__make} %{?_smp_mflags} CXFLAGS="${CFLAGS}"


%install
%{__make_install} \
	SYSCONFDIR='%{_sysconfdir}' \
	MANDIR='%{_mandir}' \
	DESTDIR="${RPM_BUILD_ROOT}" \
	INSTALL='%{__install}'

%{__mkdir_p} '%{buildroot}/%{_sysconfdir}'
%{__cp} mdadm.conf-example '%{buildroot}/%{_sysconfdir}/mdadm.conf'

%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/initng/daemon'
%{install_ifile %{SOURCE1} daemon/mdadm.i}


%files
%defattr(-, root, root)
%doc ANNOUNCE* COPYING ChangeLog README*
%attr(0750, root, root) %{_sysconfdir}/initng/daemon/mdadm.i
%config(noreplace) %attr(0600, root, root) %{_sysconfdir}/mdadm.conf
%attr(0710, root, root) /sbin/mdadm
%attr(0710, root, root) /sbin/mdmon
%attr(0640, root, root) /%{_lib}/udev/rules.d/64-md-raid.rules
%doc %{_mandir}/man4/md.4*
%doc %{_mandir}/man5/mdadm.conf.5*
%doc %{_mandir}/man8/mdadm.8*
%doc %{_mandir}/man8/mdmon.8*
