Name: kde-i18n-de
Version: 3.5.9
Release: 1ev
Summary: German translations for KDE 
URL: http://www.kde.org/
Group: User Interface/Desktops
License: GPL-2
Vendor: GNyU-Linux
Source: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-i18n/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make, gettext
BuildArch: noarch

%description
Provides translations for KDE into German.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR="${RPM_BUILD_ROOT}"


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc %{_datadir}/doc/HTML/de/
%{_datadir}/locale/de/
%{_datadir}/apps/*
