Name: wireless-tools
Version: 29
Release: 1.0
Summary: Configuration tools for wireless network interfaces
URL: http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/Tools.html
Group: System Environment/Base
License: GPL-2
Source: http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/wireless_tools.%{version}.tar.gz
BuildRequires: grep, sed, make, gcc
BuildRequires: eglibc-devel, kernel-headers

%description
The wireless tools allow to configure wireless network adapters through the
Kernel's native interface.


%package -n ifrename
Summary: Network interface renaming tool
Group: System Environment/Base

%description -n ifrename
ifrename allows to rename network interfaces based on various criteria.


%package -n libiw29
Summary: Wireless Tools Library
Group: System Environment/Libraries

%description -n libiw29
Wireless tools are used to manipulate the Linux Wireless Extensions. The
Wireless Extension is an interface allowing you to set Wireless LAN specific
parameters and get the specific stats.
This package contains the dynamic library libiw. 


%package devel
Summary: Development headers for libiw
Group: Development/Libraries

%description devel
Wireless tools are used to manipulate the Linux Wireless Extensions. The
Wireless Extension is an interface allowing you to set Wireless LAN specific
parameters and get the specific stats.
This package contains the header files and static version of libiw. 


%prep
%setup -q -n 'wireless_tools.%{version}'


%build
%{__make} %{?_smp_mflags} \
    PREFIX='%{_prefix}'


%install
%{__make} install \
    PREFIX='%{buildroot}%{_prefix}'

%{__mkdir} '%{buildroot}/sbin'
%{__mv} '%{buildroot}%{_sbindir}/ifrename' '%{buildroot}/sbin'

%{__mkdir_p} '%{buildroot}%{_sysconfdir}'
%{__touch} '%{buildroot}%{_sysconfdir}/iftab'

%{__mkdir_p} '%{buildroot}%{_sysconfdir}/udev/rules.d'
%{__install} -m0610 -oroot -groot 19-udev-ifrename.rules \
    '%{buildroot}%{_sysconfdir}/udev/rules.d'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%files
%defattr(-, root, root)
%doc README CHANGELOG* COPYING PCMCIA.txt HOTPLUG.txt DISTRIBUTIONS.txt
%{_sbindir}/iwconfig
%{_sbindir}/iwevent
%{_sbindir}/iwgetid
%{_sbindir}/iwlist
%{_sbindir}/iwpriv
%{_sbindir}/iwspy
%doc %{_mandir}/man8/iwconfig.8*
%doc %{_mandir}/man8/iwevent.8*
%doc %{_mandir}/man8/iwgetid.8*
%doc %{_mandir}/man8/iwlist.8*
%doc %{_mandir}/man8/iwspy.8*
%doc %{_mandir}/man8/iwpriv.8*


%files -n ifrename
%defattr(-, root, root)
%doc README IFRENAME-VS-XXX.txt COPYING
%{_sysconfdir}/udev/rules.d/19-udev-ifrename.rules
%ghost %config %attr(0610, root, root) %{_sysconfdir}/iftab
%attr(0710, root, root) /sbin/ifrename
%doc %{_mandir}/man8/ifrename.8*
%doc %{_mandir}/man5/iftab.5*


%files -n libiw29
%defattr(-, root, root)
%doc README CHANGELOG* COPYING PCMCIA.txt HOTPLUG.txt DISTRIBUTIONS.txt
%{_libdir}/libiw.so.29


%files devel
%defattr(-, root, root)
%doc README CHANGELOG* COPYING PCMCIA.txt HOTPLUG.txt DISTRIBUTIONS.txt
%{_libdir}/libiw.so
%{_includedir}/wireless.h
%{_includedir}/iwlib.h
%doc %{_mandir}/man7/wireless.7*
