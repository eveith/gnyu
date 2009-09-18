Name: hdparm
Version: 8.6
Release: 1ev
Summary: A shell utility for manipulating Linux IDE drive/driver parameters
URL: http://sourceforge.net/projects/hdparm/
Group: System Environment/Base
License: BSD
Vendor: MSP Slackware
Source: http://downloads.sourceforge.net/hdparm/hdparm-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc

%description
hdparm is a Linux shell utility for viewing and manipulating various IDE 
drive and driver parameters. Most drives can benefit from improved performance 
using a command similar to "hdparm -qm8 -qu1 -qc1 -qd1 /dev/hda".


%prep
%setup -q


%build
%{__make} %{?_smp_mflags} \
	CC=%{_target_platform}-gcc \
	CFLAGS="$RPM_OPT_FLAGS"


%install
[[ -d '%{buildroot}' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} \
	DESTDIR=%{buildroot} \
	binprefix=/ \
	manprefix=%{_prefix} \
	sbindir=/sbin \
	mandir=%{_mandir} \
	oldmandir=%{_mandir}

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%clean
[[ -d '%{buildroot}' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc README* hdparm.lsm LICENSE.TXT TODO
/sbin/hdparm
%{_mandir}/man8/hdparm.8*
