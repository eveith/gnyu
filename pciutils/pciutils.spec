Name: pciutils
Version: 3.1.7
Release: 1.0
Summary: Programs for inspecting and manipulating configuration of PCI devices
URL: http://mj.ucw.cz/pciutils.html
Group: Applications/Hardware
License: GPL-2
Source: http://www.kernel.org/pub/software/utils/pciutils/pciutils-%{version}.tar.bz2
BuildRequires: make, gcc
BuildRequires: eglibc-devel, kernel-headers
BuildRequires: zlib-devel
BuildRequires: gzip, wget

%description
The PCI Utilities package contains a library for portable access to PCI bus
configuration registers and several utilities based on this library.


%package devel
Summary: Development files for libpci
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
The PCI Utilities package contains a library for portable access to PCI bus
configuration registers and several utilities based on this library.
This package includes header files and API documentation for developing and
compiling programs that make use of libpci.


%package -n libpci3
Summary: A library for inspecting and manipulation PCI device configuration
Group: System Environment/Libraries

%description -n libpci3
The PCI Utilities package contains a library for portable access to PCI bus
configuration registers and several utilities based on this library.


%prep
%setup -q


%build
%{__make} %{?_smp_mflags} \
    CC="${CC:-%{__cc}}" \
    OPT="${CFLAGS:-%{optflags}}" \
    ZLIB=yes \
    SHARED=yes \
    PREFIX='%{_prefix}'


%install
%{__make} install install-lib \
    PREFIX='%{_prefix}' \
    DESTDIR='%{buildroot}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post -n libpci3 -p %{__ldconfig}
%postun -n libpci3 -p %{__ldconfig}


%files
%defattr(-, root, root)
%doc COPYING README TODO

%{_sbindir}/lspci
%attr(0700, root, root) %{_sbindir}/setpci
%{_sbindir}/update-pciids

%{_datadir}/pci.ids*

%doc %{_mandir}/man8/lspci.8*
%doc %{_mandir}/man8/setpci.8*
%doc %{_mandir}/man8/update-pciids.8*


%files devel
%defattr(-, root, root)
%doc COPYING README TODO

%{_libdir}/pkgconfig/libpci.pc

%dir %{_includedir}/pci
%{_includedir}/pci/*.h

%doc %{_mandir}/man7/pcilib.7*


%files -n libpci3
%defattr(-, root, root)
%doc COPYING README TODO
%{_libdir}/libpci.so.3*
