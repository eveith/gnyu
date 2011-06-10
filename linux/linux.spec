Name: linux
Version: 2.6.39.1
Release: 1.0
Summary: The Linux Kernel
URL: http://www.kernel.org
Group: System Environment/Base
License: GPL-2
Vendor: GNyU-Linux
Source: ftp://ftp.kernel.org/pub/linux/kernel/v2.6/linux-%{version}.tar.bz2
BuildRequires: grep, sed, make
Provides: kernel = %{version}-%{release}
Obsoletes: kernel < %{version}-%{release}
Conflicts: kernel < %{version}-%{release}

%description
The very basis of every OS is its kernel. This is the Linux Kernel, required
to run a Linux System.


%package headers
Summary: Linux Kernel headers
Group: Development/System
Provides: kernel-headers = %{version}-%{release}
Obsoletes: kernel-headers < %{version}-%{release}
Conflicts: kernel-headers < %{version}-%{release}

%description headers
The Kernel headers provide the interface to any program accessing kernel
routines. They're often required, so everyone who intends compiling stuff
should install this.


%prep
%setup -q


%build
%{__make} alldefconfig


%install
%{__mkdir_p} '%{buildroot}%{_prefix}/src/linux-%{version}'
%{__cp} '%{SOURCE0}' '%{buildroot}%{_prefix}/src'

%{__make} \
	ARCH=i386 \
	INSTALL_HDR_PATH='%{buildroot}%{_prefix}' \
	headers_install

%{__mkdir_p} '%{buildroot}/lib/modules/%{version}'

# These headers are provided by glibc by now, so remove them

%{__rm_rf} '%{buildroot}%{_includedir}/scsi'

# Remove leftovers...

%{__rm} '%{buildroot}%{_includedir}/.install'
%{__rm} '%{buildroot}%{_includedir}/..install.cmd'


%files
%defattr(-, root, root)
%dir /lib/modules
%dir /lib/modules/%{version}
%dir %{_prefix}/src/linux-%{version}
%{_prefix}/src/linux-%{version}.tar.bz2


%files headers
%defattr(-, root, root)
%{_prefix}/include/*
