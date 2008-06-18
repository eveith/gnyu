Name: dbus-qt3
Summary: Qt Bindings to the D-BUS message bus system
Version: 0.8
Release: 1ev
Group: System Environment/Libraries
Vendor: GNyU-Linux
License: AFL/GPL-2
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: coreutils, grep, sed, make >= 3.79.1, libtool, gcc, gcc-g++
BuildRequires: qt3 >= 3.3, dbus >= 0.62, libstdc++
Source0: http://people.freedesktop.org/~krake/dbus-1-qt3/libdbus-1-qt3-%{version}.tar.gz
Provides: dbus-qt = %{version}

%description
This package allows to build/run Qt 3 applications that are linked against the
D-BUS system and use it.


%prep
%setup -q -n libdbus-1-qt3-%{version}


%build
unset QTDIR; . /etc/profile.d/qt3.sh
%configure \
    --disable-static \
	--disable-debug \
	--disable-warnings
%{__make} %{?_smp_mflags}

pushd tools/dbusxml2qt3
qmake
%{__make} %{?_smp_mflags}
popd


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%{__install} -D -m 0755 \
	./tools/dbusxml2qt3/dbusxml2qt3 \
	%{buildroot}/%{_bindir}/dbusxml2qt3


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-, root, root)
%doc COPYING 
%{_bindir}/dbusxml2qt3
%{_libdir}/libdbus-1-qt3.*
%{_libdir}/pkgconfig/dbus-1-qt3.pc
%{_includedir}/dbus-1.0/qt3/
