Name: kde-i18n-de
Version: 3.5.6
Release: 1ev
Summary: German translations for KDE 
URL: http://www.kde.org/
Group: User Interface/Desktops
License: GPL
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
BuildArch: noarch

%description
Provides translations for KDE into German.


%prep
%setup -q


%build
%configure
make


%install
make install DESTDIR="$RPM_BUILD_ROOT"
rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir


%clean
rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-, root, root)
%doc %{_datadir}/doc/HTML/de/
%{_datadir}/locale/de/
%{_datadir}/apps/*
