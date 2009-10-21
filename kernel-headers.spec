Name: kernel-headers
Version: 2.6.31.4
Release: 1.0ev
Summary: Linux Kernel C headers
URL: http://www.kernel.org/
Group: Development/Headers
License: GPL-2
Vendor: GNyU-Linux
Source: http://www.kernel.org/pub/linux/kernel/v2.6/linux-%{version}.tar.bz2
BuildRequires: make, gcc

%description
The Linux Kernel is the foundation of the whole GNU/Linux system. Its kernel
headers are commonly required to develop and compile software that needs to be
aware of the semantics of the system.


%prep
	%setup -q -n 'linux-%{version}'


%build
	%{__make} defconfig


%install
	%{__mkdir_p} '%{buildroot}/%{_includedir}'
	%{__make} headers_install INSTALL_HDR_PATH='%{buildroot}/%{_prefix}'
	%{__find} '%{buildroot}' \
		\( -name '.install' -or -name '..install.cmd' \) \
		-exec %{__rm} '{}' \;


%files
	%defattr(-, root, root)
	%doc MAINTAINERS COPYING CREDITS README REPORTING-BUGS
	%dir %{_includedir}/asm
	%{_includedir}/asm/*
	%dir %{_includedir}/asm-generic
	%{_includedir}/asm-generic/*
	%dir %{_includedir}/drm
	%{_includedir}/drm/*
	%dir %{_includedir}/linux
	%{_includedir}/linux/*
	%dir %{_includedir}/mtd
	%{_includedir}/mtd/*
	%dir %{_includedir}/rdma
	%{_includedir}/rdma/*
	%dir %{_includedir}/scsi
	%{_includedir}/scsi/*
	%dir %{_includedir}/sound
	%{_includedir}/sound/*
	%dir %{_includedir}/video
	%{_includedir}/video/*
	%dir %{_includedir}/xen
	%{_includedir}/xen/*
