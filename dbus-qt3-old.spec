Name: dbus-qt3-old
Version: 0.70
Release: 1ev
Summary: D-BUS Qt3 bindings compatible with old application API and new D-BUS
URL: http://www.freedesktop.org/wiki/Software/dbus
Group: System Environment/Libraries
License: GPL-2
Vendor: GNyU-Linux
Source: http://www.kolumbus.fi/juuso.alasuutari/dbus-qt3-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: coreutils, grep, sed, make, gcc, gcc-g++, qt3, dbus >= 0.91
BuildRequires: libstdc++

%description
When the D-BUS team prepared the 1.0 release, they decided to externalize the
bindings. Moreover, the application API changed. Although D-BUS Qt3 bindings
exist, they're often not quite compatible with the old applications API. This
package contains a library that provides the old API.


%prep
%setup -q -n 'dbus-qt3-%{version}'


%build
%configure
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc AUTHORS NEWS README COPYING
%{_includedir}/dbus-1.0/dbus/connection.h
%{_includedir}/dbus-1.0/dbus/dbus-qt.h
%{_includedir}/dbus-1.0/dbus/message.h
%{_includedir}/dbus-1.0/dbus/server.h
%{_libdir}/libdbus-qt-1.*
