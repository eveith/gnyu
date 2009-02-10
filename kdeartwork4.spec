Name: kdeartwork4
Version: 4.2.0
Release: 1ev
Summary: Miscellaneous artworks for KDE 4
URL: http://www.kde.org/
Group: User Interface/Desktops
License: GPL-2, LGPL-2.1, FDL-1.2
Vendor: GNyU-Linux
Source: ftp://ftp.kde.org/pub/kde/stable/4.2.0/src/kdeartwork-%{version}.tar.bz2
BuildRequires: cmake >= 2.4.5, make, gcc-g++, qt4, automoc4 >= 0.8.86
BuildRequires: libX11, libICE, libXpm
BuildRequires: kdelibs4, kdebase4, kdebase4-workspace, phonon >= 4.3.0, strigi
BuildRequires: xscreensaver, mesalib
Requires: xscreensaver, kdebase4, kdebase4-workspace
Obsoletes: kdeartwork < %{version}

%description
This package contains additional
* themes,
* screensaver,
* sounds,
* wallpapers,
* widget styles and
* window styles
for KDE. We placed them into this module so that kdebase won't be too bloated.


%prep
%setup -q -T -c -a0 -n 'kdebase-%{version}'
%{__mkdir_p} 'kdeartwork-%{version}-obj'


%build
pushd 'kdeartwork-%{version}-obj'
%{cmake} \
	-DKDE_DISTRIBUTION_TEXT='%{vendor}' \
	-DCONFIG_INSTALL_DIR='%{_sysconfdir}/kde4' \
	-DSYSCONF_INSTALL_DIR='%{_sysconfdir}/kde4' \
	-DMAN_INSTALL_DIR='%{_mandir}' \
	-DQT_QMAKE_EXECUTABLE:FILEPATH='%{_libdir}/qt4/bin/qmake' \
	'../kdeartwork-%{version}'
%{__make} %{?_smp_mflags}
popd


%install
pushd 'kdeartwork-%{version}-obj'
%{__make} install DESTDIR='%{buildroot}'
popd


%post

%postun


%files
%defattr(-, root, root)
%doc 'kdeartwork-%{version}/README'
%doc 'kdeartwork-%{version}'/COPYING*
%{_datadir}/apps/color-schemes/*.colors
%{_datadir}/icons/kdeclassic/
%dir %{_datadir}/emoticons/ccmathteam.com
%dir %{_datadir}/emoticons/greggman.com
%dir %{_datadir}/emoticons/phpBB
%dir %{_datadir}/emoticons/Plain
%dir %{_datadir}/emoticons/RedOnes
%dir %{_datadir}/emoticons/tweakers.net
%dir %{_datadir}/emoticons/Boxed
%dir %{_datadir}/emoticons/KMess
%dir %{_datadir}/emoticons/KMess-Blue
%dir %{_datadir}/emoticons/KMess-Violet
%{_datadir}/emoticons/*/*.*
%{_bindir}/*.kss
%{_bindir}/kxs*
%{_libdir}/kde4/kstyle_phase_config.so
%{_libdir}/kde4/plugins/styles/phasestyle.so
%{_datadir}/kde4/services/ScreenSavers/*.desktop
%{_datadir}/apps/desktoptheme/Aya/
%{_datadir}/apps/desktoptheme/Clean-Blend/
%{_datadir}/apps/desktoptheme/Elegance/
%{_datadir}/apps/desktoptheme/Silicon/
%{_datadir}/apps/desktoptheme/heron/
%{_datadir}/apps/desktoptheme/slim-glow/
%dir %{_datadir}/apps/kscreensaver
%{_datadir}/apps/kscreensaver/*.png
%dir %{_datadir}/apps/kfiresaver
%dir %{_datadir}/apps/kstyle
%dir %{_datadir}/apps/kstyle/themes
%{_datadir}/apps/kstyle/themes/phase.themerc
%{_datadir}/apps/kfiresaver/*.*
%{_datadir}/sounds/*.*
%{_datadir}/wallpapers/Colorado_Farm/
%{_datadir}/wallpapers/Emotion/
%{_datadir}/wallpapers/Golden_Ripples/
%{_datadir}/wallpapers/Green_Concentration/
%{_datadir}/wallpapers/Leafs_Labyrinth/
%{_datadir}/wallpapers/Skeeter_Hawk/
