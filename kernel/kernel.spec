Name: kernel
Version: 2.6.23.17
Release: 1ev
Summary: The Linux Kernel
URL: http://www.kernel.org/
Group: System Environment/Base
License: GPL-2
Vendor: GNyU-Linux
Source: ftp://ftp.kernel.org/pub/linux/kernel/v2.6/linux-%{version}.tar.bz2
Source1: %{name}-create_biarch_asm.sh
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: coreutils, make, gcc
Requires: fhs
Prefix: /usr

%description
The very basis of every OS is its kernel. This is the Linux Kernel, required
to run a Linux System.


%package headers
Summary: Linux Kernel headers
Group: Development/System

%description headers
The Kernel headers provide the interface to any program accessing kernel
routines. They're often required, so everyone who intends compiling stuff
should install this.


%prep
%setup -q -n 'linux-%{version}'


%build
%{__make} menuconfig
%{__make} V=1


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__mkdir_p} '%{buildroot}/boot'

%ifarch %ix86
%{__fakeroot} %{__make} \
	ARCH=i386 \
	INSTALL_HDR_PATH='%{buildroot}/%{_prefix}' \
	headers_install

%{__install} -m 0644 arch/i386/boot/bzImage \
	'%{buildroot}/boot/vmlinuz-%{version}'
%else
%{__fakeroot} %{__make} \
	ARCH='%{_arch}' \
	INSTALL_HDR_PATH='%{buildroot}/%{_prefix}' \
	headers_install
%{__install} -m 0644 'arch/%{_arch}/boot/bzImage' \
	'%{buildroot}/boot/vmlinuz-%{version}'
%endif

# These headers are provided by glibc by now, so remove them
%{__rm} -rf '%{buildroot}/%{_includedir}/scsi'
%{__rm} -f '%{buildroot}/%{_includedir}/asm*/atomic.h'
%{__rm} -f '%{buildroot}/%{_includedir}/asm*/io.h'
%{__rm} -f '%{buildroot}/%{_includedir}/asm*/irq.h'


%{__install} -m 0644 System.map '%{buildroot}/boot/System.map-%{version}'
%{__install} -m 0600 .config '%{buildroot}/boot/config-%{version}'

%{__fakeroot} %{__make} modules_install INSTALL_MOD_PATH='%{buildroot}'


%post
echo 
echo "***"
echo "Be sure to update your bootloader's configuration."
echo "***"
echo

%postun
echo 
echo "***"
echo "Be sure to update your bootloader's configuration."
echo "***"
echo


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%dir /lib/modules
/lib/modules/%{version}
/boot/vmlinuz-%{version}
/boot/System.map-%{version}
/boot/config-%{version}

%files headers
%defattr(-, root, root)
/usr/include/*
