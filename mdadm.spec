Name: mdadm
Version: 2.6.8
Release: 2ev
Summary: A tool to create, maintain, and monitor Linux Software RAID
URL: http://www.cse.unsw.edu.au/~neilb/source/mdadm/
Group: System Environment/Base
License: GPL-2
Vendor: GNyU-Linux
Source: http://www.kernel.org/pub/linux/utils/raid/mdadm/mdadm-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root

%description
mdadm is a tool for creating, maintaining, and monitoring Linux "md" device
arrays, also known as Software RAID. 


%prep
%setup -q


%build
%{__make} %{?_smp_mflags} CWFLAGS="${RPM_OPT_FLAGS}"


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} \
	SYSCONFDIR='%{_sysconfdir}' \
	MANDIR='%{_mandir}' \
	DESTDIR="${RPM_BUILD_ROOT}" \
	INSTALL='%{__install}'
%{__mkdir_p} '%{buildroot}/etc'
touch '%{buildroot}/etc/mdadm.conf'

%{__rm} -f '%{buildroot}/%{_infodir}/dir'


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc ANNOUNCE* COPYING ChangeLog README*
%config(noreplace) %ghost %attr(0600, root, root) %{_sysconfdir}/mdadm.conf
%attr(0750, root, root) /sbin/mdadm
%doc %{_mandir}/man4/md.4*
%doc %{_mandir}/man5/mdadm.conf.5*
%doc %{_mandir}/man8/mdadm.8*
