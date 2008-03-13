Name: dbus-qt3
Summary: Qt Bindings to the D-BUS message bus system
Version: 0.70
Release: 1ev
Group: System Environment/Libraries
Vendor: MSP Slackware
Packager: Eric MSP Veith
License: AFL/GPL
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, libtool, gcc-core, gcc-g++
BuildRequires: qt3 >= 3.3, dbus >= 0.62
Source0: http://ranger.befunk.com/fink/dbus-qt3-%{version}.tar.bz2
Provides: libtool(%{_libdir}/libdbus-qt-1.la)
Provides: dbus-qt = %{version}

%description
This package allows to build/run Qt 3 applications that are linked against the
D-BUS system and use it.


%prep
%setup -q


%build
unset QTDIR; . /etc/profile.d/qt3.sh
%configure \
    --disable-static
%{__make} %{_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-, root, root)
%doc COPYING 
%{_libdir}/libdbus-qt-*.*
%{_includedir}/dbus-1.0/dbus/*
