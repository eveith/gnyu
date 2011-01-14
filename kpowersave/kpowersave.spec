Name: kpowersave
Version: 0.7.3
Release: 2ev
Summary: Provides powersave monitoring functions for workstations and notebooks
URL: http://sourceforge.net/projects/powersave/
Group: Unser Interface/Desktops
License: GPL-2
Vendor: GNyU-Linux
Source: http://downloads.sourceforge.net/powersave/kpowersave-0.7.3.tar.bz2
BuildRequires: make, gcc-g++, qt3, kdelibs >= 3.5, dbus >= 0.9, dbus-qt3-old
BuildRequires: hal >= 0.5.9.1, pkg-config, gettext, libstdc++, libXdmcp

%description
KPowersave provides battery monitoring, CPU frequency control and 
suspend/standby triggers, and more power management features for KDE. 
It uses HAL (formerly the powersave daemon) and supports APM and ACPI 
for several architectures.


%prep
%setup -q
%{__make} -f admin/Makefile.common cvs ||:


%build
%configure \
	--disable-debug \
	--disable-warnings
%{__make} %{?_smp_mflags}


%install
%{__make_install} DESTDIR='%{buildroot}'
%find_lang kpowersave


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files -f kpowersave.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog* COPYING README NEWS TODO
%doc %{_datadir}/doc/HTML/*/kpowersave
%{_bindir}/kpowersave
%{_libdir}/kde3/kpowersave.*
%{_libdir}/libkdeinit_kpowersave.*
%{_datadir}/autostart/kpowersave-autostart.desktop
%{_datadir}/config/kpowersaverc
%{_datadir}/applications/kde/kpowersave.desktop
%{_datadir}/apps/kpowersave/
%{_datadir}/icons/hicolor/*/apps/kpowersave.png
