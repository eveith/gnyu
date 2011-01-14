Name: iso-codes
Version: 3.5
Release: 1ev
Summary: A list of ISO standards (country, language, scripts, currencies)
URL: ftp://pkg-isocodes.alioth.debian.org/
Group: System Environment/Supplements
License: LGPL-2.1
Vendor: GNyU-Linux
Source: ftp://pkg-isocodes.alioth.debian.org/pub/pkg-isocodes/iso-codes-%{version}.tar.bz2
BuildRequires: make, pkg-config, gettext, python
BuildArch: noarch

%description
This package provides lists of various ISO standards (e.g. country,
language, language scripts, and currency names) in one place, rather
than repeated in many programs throughout the system.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%{__mkdir_p} '%{buildroot}/%{_libdir}'
%{__mv} '%{buildroot}/%{_datadir}/pkgconfig' '%{buildroot}/%{_libdir}'


%files
%defattr(-, root, root)
%doc README LICENSE TODO ChangeLog
%{_libdir}/pkgconfig/iso-codes.pc
%{_datadir}/iso-codes/
%{_datadir}/xml/iso-codes/
%{_datadir}/locale/*/LC_MESSAGES/iso_*.mo
