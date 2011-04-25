Name: lxc
Version: 0.7.4.1
Release: 1.0
Summary: An extended chroot and virtualization solution (Linux Containers)
URL: http://lxc.sourceforge.net
Group: System Environment/Base
License: LGPL-2.1
Source: http://lxc.sourceforge.net/download/lxc/%{name}-%{version}.tar.gz
BuildRequires: grep, sed, make, gcc
#BuildRequires: libcap2-devel
BuildRequires: eglibc-devel, kernel-headers >= 2.6.29
BuildRequires: docbook-utils, docbook-dtds

%description
The container technology is actively being pushed into the mainstream linux
kernel. It provides the resource management through the control groups  aka
process containers and resource isolation through the namespaces.
The  linux  containers, lxc, aims to use these new functionnalities to pro-
vide an userspace container object which provides full  resource  isolation
and resource control for an applications or a system.


%package -n liblxc0
Summary: LXC userspace implementation
Group: System Environment/Libraries

%description -n liblxc0
Linux Resource Containers provide process and resource isolation without the
overhead of full virtualization.
This package contains libraries for running lxc applications.


%package devel
Summary: Development headers needed when developing applications using LXC
Group: Development/Libraries
Requires: liblxc0 = %{version}-%{release}, pkg-config

%description devel
The container technology is actively being pushed into the mainstream linux
kernel. It provides the resource management through the control groups  aka
process containers and resource isolation through the namespaces. If you want
to develop applications that use LXC through linking to liblxc, you will need
to install this package.



%prep
%setup -q


%build
%configure \
    --with-config-path='%{_localstatedir}/lib/lxc' \
    --with-rootfs-path='%{_libdir}/lxc/rootfs'
%{__make} %{?_smp_mflags}


%install
%{__make} install install-man DESTDIR='%{buildroot}'

%{__mkdir_p} '%{buildroot}%{_libdir}/lxc/rootfs'
%{__mkdir_p} '%{buildroot}%{_localstatedir}/lib/lxc'

%{__mv} '%{buildroot}%{_datadir}/pkgconfig' '%{buildroot}%{_libdir}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%check
%{__make} check


%post -n liblxc0 -p %{__ldconfig}
%postun -n liblxc0 -p %{__ldconfig}


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
%dir %{_libdir}/lxc/rootfs
%doc %{_libdir}/lxc/rootfs/README
%{_libdir}/lxc/lxc-init
%dir %{_libdir}/lxc/templates
%{_libdir}/lxc/templates/lxc-*
%dir %{_localstatedir}/lib/lxc
%dir %{_datadir}/doc/lxc
%dir %{_datadir}/doc/lxc/examples
%doc %{_datadir}/doc/lxc/examples/*.conf
%doc %{_mandir}/man1/lxc-cgroup.1*
%doc %{_mandir}/man1/lxc-checkpoint.1*
%doc %{_mandir}/man1/lxc-console.1*
%doc %{_mandir}/man1/lxc-create.1*
%doc %{_mandir}/man1/lxc-destroy.1*
%doc %{_mandir}/man1/lxc-execute.1*
%doc %{_mandir}/man1/lxc-freeze.1*
%doc %{_mandir}/man1/lxc-kill.1*
%doc %{_mandir}/man1/lxc-ls.1*
%doc %{_mandir}/man1/lxc-monitor.1*
%doc %{_mandir}/man1/lxc-ps.1*
%doc %{_mandir}/man1/lxc-restart.1*
%doc %{_mandir}/man1/lxc-start.1*
%doc %{_mandir}/man1/lxc-stop.1*
%doc %{_mandir}/man1/lxc-unfreeze.1*
%doc %{_mandir}/man1/lxc-wait.1*
%doc %{_mandir}/man5/lxc.conf.5*
%doc %{_mandir}/man7/lxc.7*



%files -n liblxc0
%defattr(-, root, root)
%doc AUTHORS CONTRIBUTING COPYING ChangeLog MAINTAINERS NEWS README TODO
%{_libdir}/liblxc.so.0*


%files devel
%defattr(-, root, root)
%doc AUTHORS CONTRIBUTING COPYING ChangeLog MAINTAINERS NEWS README TODO
%dir %{_includedir}/lxc
%{_libdir}/liblxc.so
%{_includedir}/lxc/*.h
%{_libdir}/pkgconfig/lxc.pc
