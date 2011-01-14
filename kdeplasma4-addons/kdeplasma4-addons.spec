Name: kdeplasma4-addons
Version: 4.3.2
Release: 1.0ev
Summary: Addons to KDE's plasma desktop shell
URL: http://www.kde.org/
Group: User Interface/Desktops
License: GPL-2, LGPL-2.1
Vendor: GNyU-Linux
Source: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdeplasma-addons-%{version}.tar.bz2
BuildRequires: cmake >= 2.6.2, make, flex, bison, gcc-g++, perl, gettext
BuildRequires: libX11, libSM, libICE, libXrender, libXt, libxkbfile
BuildRequires: qt4 >= 4.5.0, automoc4 >= 0.9.88
BuildRequires: kdelibs4 = %{version}, kdebase4 = %{version}
BuildRequires: kdepimlibs4 = %{version}, kdegraphics4 = %{version}
BuildRequires: mesalib, soprano

%description


%prep
	%setup -q -n 'kdeplasma-addons-%{version}'


%build
	%{cmake} .
	%{__make} %{?_smp_mflags}


%install
	%{__make} install DESTDIR='%{buildroot}'

	[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
		&& %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post


%postun


%files
	%defattr(-, root, root)
	%doc 
	%config %{_sysconfdir}/kde4/comic.knsrc
	%config %{_sysconfdir}/kde4/virus_wallpaper.knsrc
	%{_bindir}/lancelot
	%dir %{_includedir}/conversion
	%{_includedir}/conversion/*.h
	%dir %{_includedir}/lancelot
	%dir %{_includedir}/lancelot/layouts
	%dir %{_includedir}/lancelot/models
	%dir %{_includedir}/lancelot/widgets
	%{_includedir}/lancelot/*.h
	%{_includedir}/lancelot/*/*.h
	%{_libdir}/kde4/kcm_krunner_spellcheck.so
	%{_libdir}/kde4/krunner_browserhistory.so
	%{_libdir}/kde4/krunner_contacts.so
	%{_libdir}/kde4/krunner_converter.so
	%{_libdir}/kde4/krunner_katesessions.so
	%{_libdir}/kde4/krunner_konquerorsessions.so
	%{_libdir}/kde4/krunner_konsolesessions.so
	%{_libdir}/kde4/krunner_spellcheckrunner.so
	%{_libdir}/kde4/plasma-applet_systemloadviewer.so
	%{_libdir}/kde4/plasma_applet_bball.so
	%{_libdir}/kde4/plasma_applet_binaryclock.so
	%{_libdir}/kde4/plasma_applet_bubblemon.so
	%{_libdir}/kde4/plasma_applet_calculator.so
	%{_libdir}/kde4/plasma_applet_charselect.so
	%{_libdir}/kde4/plasma_applet_comic.so
	%{_libdir}/kde4/plasma_applet_dict.so
	%{_libdir}/kde4/plasma_applet_eyes.so
	%{_libdir}/kde4/plasma_applet_fifteenPuzzle.so
	%{_libdir}/kde4/plasma_applet_fileWatcher.so
	%{_libdir}/kde4/plasma_applet_frame.so
	%{_libdir}/kde4/plasma_applet_fuzzy_clock.so
	%{_libdir}/kde4/plasma_applet_incomingmsg.so
	%{_libdir}/kde4/plasma_applet_kolourpicker.so
	%{_libdir}/kde4/plasma_applet_konqprofiles.so
	%{_libdir}/kde4/plasma_applet_konsoleprofiles.so
	%{_libdir}/kde4/plasma_applet_lancelot_launcher.so
	%{_libdir}/kde4/plasma_applet_lancelot_part.so
	%{_libdir}/kde4/plasma_applet_leavenote.so
	%{_libdir}/kde4/plasma_applet_life.so
	%{_libdir}/kde4/plasma_applet_luna.so
	%{_libdir}/kde4/plasma_applet_magnifique.so
	%{_libdir}/kde4/plasma_applet_mediaplayer.so
	%{_libdir}/kde4/plasma_applet_microblog.so
	%{_libdir}/kde4/plasma_applet_news.so
	%{_libdir}/kde4/plasma_applet_notes.so
	%{_libdir}/kde4/plasma_applet_nowplaying.so
	%{_libdir}/kde4/plasma_applet_opendesktop.so
	%{_libdir}/kde4/plasma_applet_paste.so
	%{_libdir}/kde4/plasma_applet_pastebin.so
	%{_libdir}/kde4/plasma_applet_previewer.so
	%{_libdir}/kde4/plasma_applet_rssnow.so
	%{_libdir}/kde4/plasma_applet_rtm.so
	%{_libdir}/kde4/plasma_applet_showdashboard.so
	%{_libdir}/kde4/plasma_applet_showdesktop.so
	%{_libdir}/kde4/plasma_applet_timer.so
	%{_libdir}/kde4/plasma_applet_unitconverter.so
	%{_libdir}/kde4/plasma_applet_weather.so
	%{_libdir}/kde4/plasma_applet_weatherstation.so
	%{_libdir}/kde4/plasma_comic_krossprovider.so
	%{_libdir}/kde4/plasma_engine_comic.so
	%{_libdir}/kde4/plasma_engine_microblog.so
	%{_libdir}/kde4/plasma_engine_ocs.so
	%{_libdir}/kde4/plasma_engine_potd.so
	%{_libdir}/kde4/plasma_engine_rtm.so
	%{_libdir}/kde4/plasma_packagestructure_comic.so
	%{_libdir}/kde4/plasma_potd_apodprovider.so
	%{_libdir}/kde4/plasma_potd_epodprovider.so
	%{_libdir}/kde4/plasma_potd_flickrprovider.so
	%{_libdir}/kde4/plasma_potd_oseiprovider.so
	%{_libdir}/kde4/plasma_potd_wcpotdprovider.so
	%{_libdir}/kde4/plasma_wallpaper_pattern.so
	%{_libdir}/kde4/plasma_wallpaper_virus.so
	%{_libdir}/kde4/plasma_wallpaper_weather.so
	%{_libdir}/libconversion.so*
	%{_libdir}/liblancelot.so*
	%{_libdir}/libocsclient.so*
	%{_libdir}/libplasmacomicprovidercore.so*
	%{_libdir}/libplasmapotdprovidercore.so*
	%{_libdir}/libplasmaweather.so*
	%{_libdir}/librtm.so*
	%dir %{_datadir}/apps/bball
	%{_datadir}/apps/bball/*.svgz
	%{_datadir}/apps/bball/bounce.ogg
	%{_datadir}/apps/cmake/modules/FindConversion.cmake
	%dir %{_datadir}/apps/desktoptheme/*/lancelot
	%dir %{_datadir}/apps/desktoptheme/default/bubblemon
	%dir %{_datadir}/apps/desktoptheme/default/fifteenPuzzle
	%dir %{_datadir}/apps/desktoptheme/default/rssnow
	%dir %{_datadir}/apps/desktoptheme/default/stylesheets
	%dir %{_datadir}/apps/desktoptheme/default/weather
	%dir %{_datadir}/apps/desktoptheme/default/weatherstation
	%dir %{_datadir}/apps/desktoptheme/default/widgets
	%{_datadir}/apps/desktoptheme/*/*/*.*
	%dir %{_datadir}/apps/lancelot
	%{_datadir}/apps/lancelot/lancelot.notifyrc
	%dir %{_datadir}/apps/plasma-applet-frame
	%{_datadir}/apps/plasma-applet-frame/picture-frame-default.jpg
	%dir %{_datadir}/apps/plasma-applet-opendesktop
	%{_datadir}/apps/plasma-applet-opendesktop/user.css
	%{_datadir}/apps/plasma/services/rtm*.operations
	%{_datadir}/apps/plasma/services/tweet.operations
	%dir %{_datadir}/apps/plasma_pastebin
	%{_datadir}/apps/plasma_pastebin/plasma_pastebin.notifyrc
	%dir %{_datadir}/apps/plasma_wallpaper_pattern
	%dir %{_datadir}/apps/plasma_wallpaper_pattern/patterns
	%{_datadir}/apps/plasma_wallpaper_pattern/patterns/*.*
	%dir %{_datadir}/apps/rssnow
	%dir %{_datadir}/apps/rssnow/feeds
	%{_datadir}/dbus-1/services/org.kde.lancelot.service
	%{_datadir}/icons/hicolor/*/*apps/bball.*
	%{_datadir}/icons/hicolor/*/*apps/lancelot-part.png
	%{_datadir}/icons/hicolor/*/*apps/lancelot.png
	%{_datadir}/icons/hicolor/*/*apps/previewer.png
	%{_datadir}/icons/hicolor/*/*apps/accessories-dictionary.svgz
	%{_datadir}/icons/hicolor/*/*apps/fifteenpuzzle.svgz
	%{_datadir}/kde4/services/ServiceMenus/preview.desktop
	%{_datadir}/kde4/services/*.desktop
	%{_datadir}/kde4/servicetypes/plasma_*.desktop
	%{_datadir}/mime/packages/lancelotpart-mime.xml
