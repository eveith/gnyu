Name: kernel
Version: 2.6.22.2
Release: 1ev
Summary: The Linux Kernel
URL: http://www.kernel.org/
Group: System Environment/Base
License: GPL
Vendor: MSP Slackware
Source: ftp://ftp.kernel.org/pub/linux/kernel/v2.6/linux-%{version}.tar.bz2
Source1: %{name}-create_biarch_asm.sh
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: gcc-core, make
Requires: fhs

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
%setup -q -n linux-%{version}


%build
make menuconfig
make V=1


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"

mkdir -p "$RPM_BUILD_ROOT"/boot

%ifarch %ix86
make \
	ARCH=i386 \
	INSTALL_HDR_PATH="${RPM_BUILD_ROOT}/usr" \
	headers_install

	cp -v arch/i386/boot/bzImage "$RPM_BUILD_ROOT"/boot/vmlinuz-%{version}
%else
make \
	ARCH=%{_arch} \
	INSTALL_HDR_PATH="${RPM_BUILD_ROOT}/usr" \
	headers_install

	cp -v arch/%{_arch}/boot/bzImage "$RPM_BUILD_ROOT"/boot/vmlinuz-%{version}
%endif
cp -v System.map "$RPM_BUILD_ROOT"/boot/System.map-%{version}
cp -v .config "$RPM_BUILD_ROOT"/boot/config-%{version}

make modules_install INSTALL_MOD_PATH="$RPM_BUILD_ROOT"


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
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


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
