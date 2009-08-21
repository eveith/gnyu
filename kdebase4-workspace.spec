Name: kdebase4-workspace
Version: 4.2.4
Release: 6ev
Summary: KDE Desktop Applications such as the panel or the login manager
URL: http://www.kde.org/
Group: User Interface/Desktops
License: GPL-2, LGPL-2.1, FDL-1.2
Vendor: GNyU-Linux
Source: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdebase-workspace-%{version}.tar.bz2
Source1: %{name}-kde.pamd
Source2: %{name}-kdm.ii
BuildRequires: cmake >= 2.4.5, make, gcc-g++, qt4 >= 4.2.0, automoc4 >= 0.8.87
BuildRequires: kdelibs4 = %{version}, kdepimlibs4 = %{version}
BuildRequires: kdebase4-runtime = %{version}, kdebindings4 = %{version}
BuildRequires: glib2, soprano, perl, qimageblitz >= 0.0.4
BuildRequires: libX11, libICE, libSM, libXext, libXcomposite, libxkbfile,
BuildRequires: libXScrnSaver, libXft, libxklavier >= 3.0
BuildRequires: freetype, fontconfig, libusb, libpam, phonon >= 4.3.0, bluez
Requires: dbus, kdebase4-runtime >= %{version}

%description
KDE Workspace consisting of what is the desktop. This means it includes
Plasma, i. e. desktop and panels, the KDM login manager, and so on.


%prep
	%setup -q -T -c -a0 -n 'kdebase-%{version}'
	%{__mkdir_p} 'kdebase-workspace-%{version}-obj'


%build
	pushd 'kdebase-workspace-%{version}-obj'
	%{cmake} \
		-DKDE_DISTRIBUTION_TEXT='%{vendor}' \
		-DCONFIG_INSTALL_DIR='%{_sysconfdir}/kde4' \
		-DSYSCONF_INSTALL_DIR='%{_sysconfdir}/kde4' \
		-DMAN_INSTALL_DIR='%{_mandir}' \
		-DQT_QMAKE_EXECUTABLE:FILEPATH='%{_libdir}/qt4/bin/qmake' \
		'../kdebase-workspace-%{version}'
	%{__make} %{?_smp_mflags}
	popd


%install
	pushd 'kdebase-workspace-%{version}-obj'
	%{__make} install DESTDIR='%{buildroot}'
	popd
	
	%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/pam.d'
	%{__install} '%{SOURCE1}' '%{buildroot}/%{_sysconfdir}/pam.d/kde'
	
	%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/initng/daemon'
	%{install_ifile '%{SOURCE2}' daemon/kdm.i}


%post
	%{__ldconfig}
	

%postun
	%{__ldconfig}
	

%files
	%defattr(-, root, root)
	%doc 'kdebase-workspace-%{version}'/README*
	%doc 'kdebase-workspace-%{version}'/COPYING*
	%doc %{_datadir}/doc/HTML/en/*
	%attr(0700, root, root) %{_sysconfdir}/initng/daemon/kdm.i
	%config %{_sysconfdir}/kde4/background.knsrc
	%config %{_sysconfdir}/kde4/colorschemes.knsrc
	%config %{_sysconfdir}/kde4/kdm.knsrc
	%dir %{_sysconfdir}/kde4/kdm
	%{_sysconfdir}/kde4/kdm/README
	%config %{_sysconfdir}/kde4/kdm/Xaccess
	%config %{_sysconfdir}/kde4/kdm/Xreset
	%config %{_sysconfdir}/kde4/kdm/Xresources
	%config %{_sysconfdir}/kde4/kdm/Xsession
	%config %{_sysconfdir}/kde4/kdm/Xsetup
	%config %{_sysconfdir}/kde4/kdm/Xstartup
	%config %{_sysconfdir}/kde4/kdm/Xwilling
	%config %{_sysconfdir}/kde4/kdm/backgroundrc
	%config %{_sysconfdir}/kde4/kdm/kdmrc
	%config %{_sysconfdir}/kde4/klipperrc
	%config %{_sysconfdir}/kde4/ksplash.knsrc
	%config %{_sysconfdir}/kde4/ksysguard.knsrc
	%config %{_sysconfdir}/kde4/plasma-overlayrc
	%config %{_sysconfdir}/kde4/plasma-themes.knsrc
	%config %{_sysconfdir}/kde4/wallpaper.knsrc
	%config %{_sysconfdir}/kde4/ksysguarddrc
	%config %{_sysconfdir}/kde4/systemsettingsrc
	%config(noreplace) %{_sysconfdir}/pam.d/kde
	%{_bindir}/genkdmconf
	%{_bindir}/kaccess
	%{_bindir}/kapplymousetheme
	%{_bindir}/kblankscrn.kss
	%{_bindir}/kcheckrunning
	%{_bindir}/kcminit
	%{_bindir}/kcminit_startup
	%{_bindir}/kdm
	%{_bindir}/kdmctl
	%{_bindir}/kdostartupconfig4
	%{_bindir}/kfontinst
	%{_bindir}/kfontview
	%{_bindir}/klipper
	%{_bindir}/kmenuedit
	%{_bindir}/krandom.kss
	%{_bindir}/krandrtray
	%{_bindir}/krdb
	%{_bindir}/krunner
	%{_bindir}/ksmserver
	%{_bindir}/ksplashsimple
	%{_bindir}/ksplashx
	%{_bindir}/ksplashx_scale
	%{_bindir}/kstartupconfig4
	%{_bindir}/ksysguard
	%{_bindir}/ksysguardd
	%{_bindir}/ksystraycmd
	%{_bindir}/kwin
	%{_bindir}/kwin_killer_helper
	%{_bindir}/kwin_rules_dialog
	%{_bindir}/kxkb
	%{_bindir}/plasma
	%{_bindir}/plasma-overlay
	%{_bindir}/plasmaengineexplorer
	%{_bindir}/plasmapkg
	%{_bindir}/plasmoidviewer
	%{_bindir}/safestartkde
	%{_bindir}/setscheduler
	%{_bindir}/solid-bluetooth
	%{_bindir}/solid-network
	%{_bindir}/solid-powermanagement
	%{_bindir}/startkde
	%{_bindir}/systemsettings
	%dir %{_includedir}/KDE/Plasma/Weather
	%{_includedir}/KDE/Plasma/Weather/*
	%dir %{_includedir}/kephal
	%dir %{_includedir}/plasmaclock
	%dir %{_includedir}/solid/control
	%dir %{_includedir}/solid/control/ifaces
	%dir %{_includedir}/taskmanager
	%dir %{_includedir}/ksysguard
	%dir %{_includedir}/kworkspace
	%dir %{_includedir}/ksgrd
	%dir %{_includedir}/plasma/weather
	%{_includedir}/plasma/weather/*.h
	%{_includedir}/solid/control/*.h
	%{_includedir}/solid/control/ifaces/*.h
	%{_includedir}/*.h
	%{_includedir}/*/*.h
	%dir %{_libdir}/KDE4Workspace-*
	%dir %{_libdir}/KDE4Workspace-*/cmake
	%{_libdir}/KDE4Workspace-*/cmake/*.cmake
	%{_libdir}/kconf_update_bin/*
	%{_libdir}/kde4/*.so
	%{_libdir}/kde4/libexec/kcheckpass
	%{_libdir}/kde4/libexec/kcmdatetimehelper
	%{_libdir}/kde4/libexec/kdm_config
	%{_libdir}/kde4/libexec/kdm_greet
	%{_libdir}/kde4/libexec/kfontprint
	%{_libdir}/kde4/libexec/kio_fonts_helper
	%{_libdir}/kde4/libexec/krootimage
	%{_libdir}/kde4/libexec/krunner_lock
	%{_libdir}/kde4/libexec/test_kcm_xinerama
	%{_libdir}/kde4/plugins/designer/*.so
	%{python_sitelib}/PyKDE4/plasmascript.py*
	%{_libdir}/libkephal.so*
	%{_libdir}/libplasmaclock.so*
	%{_libdir}/libsolidcontrol.so*
	%{_libdir}/libsolidcontrolifaces.so*
	%{_libdir}/libtaskmanager.so*
	%{_libdir}/liblsofui.so*
	%{_libdir}/libprocesscore.so*
	%{_libdir}/libprocessui.so*
	%{_libdir}/libkworkspace.so*
	%{_libdir}/libnepomukquery.so*
	%{_libdir}/libnepomukqueryclient.so*
	%{_libdir}/libkscreensaver.so*
	%{_libdir}/libkdeinit4_kwin.so*
	%{_libdir}/libkwinnvidiahack.so*
	%{_libdir}/libkdecorations.so*
	%{_libdir}/libkwineffects.so*
	%{_libdir}/libkdeinit4_kwin_rules_dialog.so*
	%{_libdir}/libkdeinit4_ksmserver.so*
	%{_libdir}/libkdeinit4_kcminit.so*
	%{_libdir}/libkdeinit4_kcminit_startup.so*
	%{_libdir}/libkhotkeysprivate.so*
	%{_libdir}/libkdeinit4_klipper.so*
	%{_libdir}/libkdeinit4_ksysguard.so*
	%{_libdir}/libksgrd.so*
	%{_libdir}/libkdeinit4_krunner.so*
	%{_libdir}/libkdeinit4_kmenuedit.so*
	%{_libdir}/libplasma_applet-system-monitor.so*
	%{_libdir}/libweather_ion.so*
	%{_libdir}/libkdeinit4_plasma.so*
	%{_libdir}/libkdeinit4_kaccess.so*
	%{_libdir}/libkdeinit4_kxkb.so
	%{_libdir}/libkfontinst.so*
	%{_libdir}/libkfontinstui.so*
	%{_libdir}/strigi/strigita_font.so
	%{_datadir}/applications/kde4/*.desktop
	%{_datadir}/apps/cmake/modules/*.cmake
	%{_datadir}/icons/Oxygen_*/
	%{_datadir}/icons/oxygen/*/*/*.*
	%{_datadir}/icons/hicolor/*/*/*.*
	%{_datadir}/apps/kcontrol/pics/*.png
	%{_datadir}/apps/kconf_update/*.*
	%dir %{_datadir}/apps/solidfakenetbackend
	%{_datadir}/apps/solidfakenetbackend/fakenetworking.xml
	%dir %{_datadir}/apps/systemsettings
	%{_datadir}/apps/systemsettings/systemsettingsui.rc
	%dir %{_datadir}/apps/kwin
	%{_datadir}/apps/kwin/*.*
	%dir %{_datadir}/apps/kwin/default_rules
	%{_datadir}/apps/kwin/default_rules/*.kwinrules
	%dir %{_datadir}/apps/ksplash
	%dir %{_datadir}/apps/ksplash/Themes
	%dir %{_datadir}/apps/ksplash/Themes/Default
	%dir %{_datadir}/apps/ksplash/Themes/Default/1600x1200
	%dir %{_datadir}/apps/ksplash/Themes/Default/1024x768
	%dir %{_datadir}/apps/ksplash/Themes/Default/1280x1024
	%dir %{_datadir}/apps/ksplash/Themes/Default/1920x1200
	%dir %{_datadir}/apps/ksplash/Themes/Default/600x400
	%dir %{_datadir}/apps/ksplash/Themes/Default/800x600
	%{_datadir}/apps/ksplash/Themes/Default/*/*.*
	%dir %{_datadir}/apps/ksplash/Themes/Simple
	%dir %{_datadir}/apps/ksplash/Themes/SimpleSmall
	%dir %{_datadir}/apps/ksplash/Themes/None
	%{_datadir}/apps/ksplash/Themes/*/*.*
	%dir %{_datadir}/apps/khotkeys
	%{_datadir}/apps/khotkeys/*.khotkeys
	%dir %{_datadir}/apps/ksysguard
	%{_datadir}/apps/ksysguard/*.*
	%dir %{_datadir}/apps/powerdevil
	%{_datadir}/apps/powerdevil/*powerdevil*
	%dir %{_datadir}/apps/kwrited
	%{_datadir}/apps/kwrited/kwrited.notifyrc
	%dir %{_datadir}/apps/kmenuedit
	%{_datadir}/apps/kmenuedit/kmenueditui.rc
	%dir %{_datadir}/apps/kmenuedit/icons
	%dir %{_datadir}/apps/kmenuedit/icons/oxygen
	%dir %{_datadir}/apps/kmenuedit/icons/oxygen/22x22
	%dir %{_datadir}/apps/kmenuedit/icons/oxygen/22x22/actions
	%dir %{_datadir}/apps/kmenuedit/icons/oxygen/32x32
	%dir %{_datadir}/apps/kmenuedit/icons/oxygen/32x32/actions
	%{_datadir}/apps/kmenuedit/icons/oxygen/*/actions/*.png
	%{_datadir}/apps/konqsidebartng/virtual_folders/services/fonts.desktop
	%dir %{_datadir}/apps/desktoptheme
	%dir %{_datadir}/apps/desktoptheme/default
	%dir %{_datadir}/apps/desktoptheme/default/widgets
	%{_datadir}/apps/desktoptheme/default/*/*.svgz
	%dir %{_datadir}/apps/desktoptheme/default/calendar
	%dir %{_datadir}/apps/desktoptheme/default/system-monitor
	%dir %{_datadir}/apps/solid
	%dir %{_datadir}/apps/solid/actions
	%{_datadir}/apps/solid/actions/test-predicate-openinwindow.desktop
	%dir %{_datadir}/apps/plasma
	%dir %{_datadir}/apps/plasma/services
	%{_datadir}/apps/plasma/services/*.operations
	%dir %{_datadir}/apps/plasma/dashboard
	%dir %{_datadir}/apps/plasma/dashboard/button
	%dir %{_datadir}/apps/plasma/dashboard/AppleClasses
	%{_datadir}/apps/plasma/dashboard/*/*.js
	%dir %{_datadir}/apps/plasma_scriptengine_ruby
	%{_datadir}/apps/plasma_scriptengine_ruby/*.rb
	%dir %{_datadir}/apps/kcminput 
	%{_datadir}/apps/kcminput/cursor_*.pcf.gz
	%dir %{_datadir}/apps/kcminput/pics
	%{_datadir}/apps/kcminput/pics/mouse*.png
	%dir %{_datadir}/apps/kdm/patterns
	%{_datadir}/apps/kdm/pics/users/*.png
	%dir %{_datadir}/apps/kdm/programs
	%dir %{_datadir}/apps/kdm/themes
	%dir %{_datadir}/apps/kdm/themes/circles
	%dir %{_datadir}/apps/kdm/themes/oxygen
	%{_datadir}/apps/kdm/themes/*/*.*
	%dir %{_datadir}/apps/kdm/sessions
	%{_datadir}/apps/kdm/*/*.*
	%dir %{_datadir}/apps/kaccess
	%{_datadir}/apps/kaccess/kaccess.notifyrc
	%dir %{_datadir}/apps/color-schemes
	%{_datadir}/apps/color-schemes/*.colors
	%dir %{_datadir}/apps/kthememanager
	%dir %{_datadir}/apps/kthememanager/themes
	%dir %{_datadir}/apps/kthememanager/themes/HighContrastDark
	%dir %{_datadir}/apps/kthememanager/themes/HighContrastDark-big
	%dir %{_datadir}/apps/kthememanager/themes/HighContrastLight
	%dir %{_datadir}/apps/kthememanager/themes/HighContrastLight-big
	%dir %{_datadir}/apps/kthememanager/themes/YellowOnBlue
	%dir %{_datadir}/apps/kthememanager/themes/YellowOnBlue-big
	%dir %{_datadir}/apps/kthememanager/themes/KDE_Classic
	%dir %{_datadir}/apps/kthememanager/themes/Keramik
	%dir %{_datadir}/apps/kthememanager/themes/Plastik
	%dir %{_datadir}/apps/kthememanager/themes/Platinum
	%dir %{_datadir}/apps/kthememanager/themes/Sunshine
	%dir %{_datadir}/apps/kthememanager/themes/Redmond
	%{_datadir}/apps/kthememanager/themes/*/*.*
	%dir %{_datadir}/apps/kdisplay
	%dir %{_datadir}/apps/kdisplay/app-defaults
	%{_datadir}/apps/kdisplay/app-defaults/*.ad
	%dir %{_datadir}/apps/kcmkeys
	%{_datadir}/apps/kcmkeys/*.kksrc
	%dir %{_datadir}/apps/kfontinst
	%{_datadir}/apps/kfontinst/kfontviewpart.rc
	%dir %{_datadir}/apps/kfontinst/icons
	%dir %{_datadir}/apps/kfontinst/icons/oxygen
	%dir %{_datadir}/apps/kfontinst/icons/oxygen/16x16
	%dir %{_datadir}/apps/kfontinst/icons/oxygen/16x16/actions
	%dir %{_datadir}/apps/kfontinst/icons/oxygen/22x22
	%dir %{_datadir}/apps/kfontinst/icons/oxygen/22x22/actions
	%dir %{_datadir}/apps/kfontinst/icons/oxygen/scalable
	%dir %{_datadir}/apps/kfontinst/icons/oxygen/scalable/actions
	%{_datadir}/apps/kfontinst/icons/oxygen/*/*/*.*
	%dir %{_datadir}/apps/kfontview
	%{_datadir}/apps/kfontview/kfontviewui.rc
	%dir %{_datadir}/apps/doc
	%dir %{_datadir}/apps/doc/kdm
	%doc %{_datadir}/apps/doc/kdm/README
	%{_datadir}/apps/doc/kdm/greeter.dtd
	%dir %{_datadir}/apps/plasma_scriptengine_python
	%{_datadir}/apps/plasma_scriptengine_python/*.py*
	%{_datadir}/autostart/*.desktop
	%{_datadir}/config.kcfg/*.kcfg
	%{_datadir}/dbus-1/interfaces/*.xml
	%{_datadir}/dbus-1/services/*.service
	%dir %{_datadir}/kde4/services/solidbackends
	%dir %{_datadir}/kde4/services/ScreenSavers
	%dir %{_datadir}/kde4/services/kwin
	%{_datadir}/kde4/services/*.*
	%{_datadir}/kde4/services/*/*.*
	%{_datadir}/kde4/servicetypes/*.desktop
	%{_datadir}/sounds/pop.wav
	%{_datadir}/wallpapers
