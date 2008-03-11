Name: mdadm
Version: 2.6
Release: 1ev
Summary: A tool to create, maintain, and monitor Linux Software RAID
URL: http://www.cse.unsw.edu.au/~neilb/source/mdadm/
Group: System Environment/Base
License: GPL
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: http://www.cse.unsw.edu.au/~neilb/source/mdadm/mdadm-%{version}.tgz
Buildroot: %{_tmppath}/%{name}-root

%description
mdadm is a tool for creating, maintaining, and monitoring Linux "md" device
arrays, also known as Software RAID. 


%prep
%setup -q


%build
make CWFLAGS="$RPM_OPT_FLAGS"


%install
make install MANDIR=%{_mandir} DESTDIR="$RPM_BUILD_ROOT" \
	INSTALL="$(which install)"

mkdir -p ${RPM_BUILD_ROOT}/etc
touch ${RPM_BUILD_ROOT}/etc/mdadm.conf

rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir


%clean
rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-, root, root)
%doc ANNOUNCE* COPYING ChangeLog README*
%config(noreplace) %ghost /etc/mdadm.conf
/sbin/mdadm
%{_mandir}/man4/md.4.gz
%{_mandir}/man5/mdadm.conf.5.gz
%{_mandir}/man8/mdadm.8.gz
