Name: lxc
Version: 0.7.3
Release: 1.0
Summary: An extended chroot and virtualization solution (Linux Containers)
URL: http://lxc.sourceforge.net
Group: System Environment/Base
License: LGPL-2.1
Source: http://lxc.sourceforge.net/download/lxc/%{name}-%{version}.tar.gz
BuildRequires: make, gcc
BuildRequires: libcap2, libcap2-devel, kernel-headers >= 2.6.29

%description
The container technology is actively being pushed into the mainstream linux
kernel. It provides the resource management through the control groups  aka
process containers and resource isolation through the namespaces.
The  linux  containers, lxc, aims to use these new functionnalities to pro-
vide an userspace container object which provides full  resource  isolation
and resource control for an applications or a system.


%package -n liblxc.0
Summary: LXC userspace implementation
Group: System Environment/Libraries

%description -n liblxc.0
Linux Resource Containers provide process and resource isolation without the
overhead of full virtualization.
This package contains libraries for running lxc applications.


%package devel
Summary: Development headers needed when developing applications using LXC
Group: Development/Libraries
Requires: liblxc.0 = %{version}-%{release}, pkg-config

%description devel
The container technology is actively being pushed into the mainstream linux
kernel. It provides the resource management through the control groups  aka
process containers and resource isolation through the namespaces. If you want
to develop applications that use LXC through linking to liblxc, you will need
to install this package.



%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install install-man DESTDIR='%{buildroot}'

%{__mv} '%{buildroot}%{_datadir}/pkgconfig' '%{buildroot}%{_libdir}'
%{__rm_rf} '%{buildroot}%{_datadir}/doc'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post -n liblxc.0 -p %{__ldconfig}
%postun -n liblxc.0 -p %{__ldconfig}


%files
%defattr(-, root, root)
%doc AUTHORS CONTRIBUTING COPYING ChangeLog MAINTAINERS NEWS README TODO
%doc doc/examples
%{_bindir}/lxc-attach
%{_bindir}/lxc-cgroup
%{_bindir}/lxc-checkconfig
%{_bindir}/lxc-checkpoint
%{_bindir}/lxc-console
%{_bindir}/lxc-create
%{_bindir}/lxc-destroy
%{_bindir}/lxc-execute
%{_bindir}/lxc-freeze
%{_bindir}/lxc-info
%{_bindir}/lxc-kill
%{_bindir}/lxc-ls
%{_bindir}/lxc-monitor
%{_bindir}/lxc-netstat
%{_bindir}/lxc-ps
%{_bindir}/lxc-restart
%{_bindir}/lxc-setcap
%{_bindir}/lxc-setuid
%{_bindir}/lxc-start
%{_bindir}/lxc-stop
%{_bindir}/lxc-unfreeze
%{_bindir}/lxc-unshare
%{_bindir}/lxc-version
%{_bindir}/lxc-wait
%dir %{_libdir}/lxc
%{_libdir}/lxc/*


%files -n liblxc.0
%defattr(-, root, root)
%doc AUTHORS CONTRIBUTING COPYING ChangeLog MAINTAINERS NEWS README TODO
%{_libdir}/liblxc.so
%{_libdir}/liblxc.so.0*


%files devel
%defattr(-, root, root)
%doc AUTHORS CONTRIBUTING COPYING ChangeLog MAINTAINERS NEWS README TODO
%dir %{_includedir}/lxc
%{_includedir}/lxc/*.h
%{_libdir}/pkgconfig/lxc.pc
