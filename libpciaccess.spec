Name: libpciaccess
Version: 0.10.5
Release: 2ev
Summary: Generic PCI access library for X
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://ftp.x.org/pub/individual/lib/libpciaccess-%{version}.tar.bz2
BuildRequires: make, gcc, pkg-config, zlib

%description
Provides functionality for X to access the PCI bus and devices in a 
platform-independant way.


%prep
%setup -q


%build
%configure \
	--with-zlib \
	--with-pciids-path='%{_datadir}/pci.ids'
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc README NEWS AUTHORS ChangeLog COPYING
%{_includedir}/pciaccess.h
%{_libdir}/libpciaccess.*
%{_libdir}/pkgconfig/pciaccess.pc
