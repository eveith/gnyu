Name: hplip
Version: 2.8.2
Release: 1ev
Summary: Imaging and printing drivers for HP products
URL: http://hplip.sourceforge.net/
Group: System Environment/Base
License: GPL-2
Vendor: GNyU-Linux
Source: http://prdownloads.sourceforge.net/hplip/hplip-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-g++ openssl, espgs, libjpeg, libusb, cups
BuildRequires: python >= 2.2, foomatic-filters >= 3.0
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
	--enable-network-build \
	--enable-pp-build \
	--disable-scan-build \
	--disable-fax-build \
	--enable-foomatic-ppd-install \
	--enable-foomatic-drv-install \
	--enable-foomatic-rip-hplip-install
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%{__rm} -rf %{buildroot}/%{_datadir}/doc

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post

%postun


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc COPYING doc/*html doc/howtos doc/images doc/install doc/styles
%doc doc/tech_docs doc/troubleshooting
%{_bindir}/hpijs
%{_libdir}/cups/filter/foomatic-rip-hplip
%dir %{_datadir}/cups/drv
%dir %{_datadir}/cups/drv/hp
%{_datadir}/cups/drv/hp/hpijs.drv
%dir %{_datadir}/ppd
%{_datadir}/ppd/HP/
