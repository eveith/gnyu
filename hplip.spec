Name: hplip
Version: 3.9.8
Release: 3ev
Summary: Imaging and printing drivers for HP products
URL: http://hplip.sourceforge.net/
Group: System Environment/Base
License: GPL-2
Vendor: GNyU-Linux
Source: http://prdownloads.sourceforge.net/hplip/hplip-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: pkg-config, make, gcc, gcc-g++,
BuildRequires: libstdc++, libjpeg, cups
Requires: foomatic-filters >= 3.0

%description
HPLIP is an HP developed solution for printing, scanning, and faxing with 
HP inkjet and laser based printers in Linux.
The HPLIP project provides printing support for 1,264 printer models, 
including Deskjet, Officejet, Photosmart, PSC (Print Scan Copy), 
Business Inkjet, LaserJet, Edgeline MFP, and LaserJet MFP.


%prep
%setup -q


%build
%configure \
	--enable-hpijs-only-build \
	--enable-pp-build \
	--enable-foomatic-drv-install \
	--with-drvdir='%{_libdir}/cups/driver' \
	--with-hpppddir='%{_datadir}/cups/model' \
	--disable-scan-build \
	--disable-gui-build \
	--disable-fax-build \
	--disable-network-build
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%files
%defattr(-, root, root)
%doc COPYING doc/*html doc/images doc/styles
%{_libdir}/cups/driver/hpcups.drv
%{_libdir}/cups/driver/hpijs.drv
%{_libdir}/cups/filter/hpcups
%{_datadir}/cups/model/*.ppd*
%dir %{_datadir}/doc/hplip-%{version}
%doc %{_datadir}/doc/hplip-%{version}/*
