Name: kdebase4
Version: 4.3.1
Release: 7ev
Summary: KDE Base Applications: "What Runs The Desktop"
URL: http://www.kde.org/
Group: User Interface/Desktops
License: GPL-2, LGPL-2.1, FDL-1.2
Vendor: GNyU-Linux
Source: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdebase-%{version}.tar.bz2
BuildRequires: cmake >= 2.6.2, make, flex, bison, gcc-g++, perl, gettext
BuildRequires: libX11, libSM, libICE, libXrender, libXt, libxkbfile
BuildRequires: qt4 >= 4.5.0, automoc4 >= 0.9.88
BuildRequires: kdelibs4 = %{version}, kdebase4-workspace = %{version}
BuildRequires: strigi, glib2, zlib, mesalib, pciutils
Requires: dbus, kdebase4-workspace >= %{version}, kdebase4-runtime >= %{version}
Obsoletes: kdebase < %{version}

%description
KDE Base Applications consists of what runs on the desktop.  This module isn't a
complete collection of essential applications that a user would expect on a 
desktop (such as e-mail and calculator).  This packages is the basic set of
applications beyond the workspace that KDE applications can assume are installed.


%prep
	%setup -q -T -c -a0 -n 'kdebase-%{version}'
	%{__mkdir_p} 'kdebase-%{version}-obj'


%build
	pushd 'kdebase-%{version}-obj'
	%{cmake} \
		-DKDE_DISTRIBUTION_TEXT='%{vendor}' \
		-DCONFIG_INSTALL_DIR='%{_sysconfdir}/kde4' \
		-DMAN_INSTALL_DIR='%{_mandir}' \
		-DQT_QMAKE_EXECUTABLE:FILEPATH='%{_libdir}/qt4/bin/qmake' \
		-DWITH_RAW1394:BOOL=OFF \
		'../kdebase-%{version}'
	%{__make} %{?_smp_mflags}
	popd


%install
	pushd 'kdebase-%{version}-obj'
	%{__make} install DESTDIR='%{buildroot}'
	popd


%post
	%{__ldconfig}


%postun
	%{__ldconfig}


%files
	%defattr(-, root, root)
	%doc 'kdebase-%{version}/README' 'kdebase-%{version}/AUTHORS'
	%doc 'kdebase-%{version}'/COPYING*
	%doc %{_datadir}/doc/HTML/en/*
	%config %{_sysconfdir}/kde4/konqsidebartng.rc
	%{_bindir}/dolphin
	%{_bindir}/kappfinder
	%{_bindir}/kbookmarkmerger
	%{_bindir}/kdepasswd
	%{_bindir}/kdialog
	%{_bindir}/keditbookmarks
	%{_bindir}/kfind
	%{_bindir}/kfmclient
	%{_bindir}/kinfocenter
	%{_bindir}/konqueror
	%{_bindir}/konsole
	%{_bindir}/konsoleprofile
	%{_bindir}/kwrite
	%{_bindir}/nspluginscan
	%{_bindir}/nspluginviewer
	%{_includedir}/knewmenu.h
	%{_includedir}/konq*.h
	%{_includedir}/libkonq*.h
	%{_libdir}/kde4/dolphinpart.so
	%{_libdir}/kde4/konq*.so
	%{_libdir}/kde4/kcm*.so
	%{_libdir}/kde4/lib*.so
	%{_libdir}/kde4/plasma_applet_folderview.so
	%{_libdir}/kde4/kded_*.so
	%{_libdir}/kde4/khtmlkttsdplugin.so
	%{_libdir}/libdolphinprivate.so*
	%{_libdir}/libkdeinit4_*.so
	%{_libdir}/libkonq*.so*
	%{_libdir}/libkonsoleprivate.so*
	%doc %{_mandir}/man1/kappfinder.1*
	%doc %{_mandir}/man1/kfind.1*
	%doc %{_mandir}/man1/kbookmarkmerger.1*
	%dir %{_datadir}/applications/kde4
	%{_datadir}/applications/kde4/*.desktop
	%dir %{_datadir}/apps/dolphin
	%{_datadir}/apps/dolphin/dolphinui.rc
	%dir %{_datadir}/apps/dolphinpart
	%{_datadir}/apps/dolphinpart/dolphinpart.rc
	%dir %{_datadir}/apps/dolphinpart/kpartplugins
	%{_datadir}/apps/dolphinpart/kpartplugins/*.*
	%dir %{_datadir}/apps/kappfinder
	%dir %{_datadir}/apps/kappfinder/apps
	%dir %{_datadir}/apps/kappfinder/apps/Editors
	%dir %{_datadir}/apps/kappfinder/apps/Internet
	%dir %{_datadir}/apps/kappfinder/apps/Internet/Terminal
	%dir %{_datadir}/apps/kappfinder/apps/Toys
	%dir %{_datadir}/apps/kappfinder/apps/Development
	%dir %{_datadir}/apps/kappfinder/apps/Graphics
	%dir %{_datadir}/apps/kappfinder/apps/System
	%dir %{_datadir}/apps/kappfinder/apps/System/Terminal
	%dir %{_datadir}/apps/kappfinder/apps/Utilities
	%dir %{_datadir}/apps/kappfinder/apps/Utilities/XUtilities
	%dir %{_datadir}/apps/kappfinder/apps/Office
	%dir %{_datadir}/apps/kappfinder/apps/Multimedia
	%dir %{_datadir}/apps/kappfinder/apps/Games
	%dir %{_datadir}/apps/kappfinder/apps/Games/Arcade
	%dir %{_datadir}/apps/kappfinder/apps/Games/Board
	%dir %{_datadir}/apps/kappfinder/apps/Games/Card
	%dir %{_datadir}/apps/kappfinder/apps/Games/Emulators
	%dir %{_datadir}/apps/kappfinder/apps/Games/TacticStrategy
	%dir %{_datadir}/apps/kappfinder/apps/Games/Roguelikes
	%{_datadir}/apps/kappfinder/apps/*/*.desktop
	%{_datadir}/apps/kappfinder/apps/*/*/*.desktop
	%dir %{_datadir}/apps/kbookmark
	%{_datadir}/apps/kbookmark/directory_bookmarkbar.desktop
	%dir %{_datadir}/apps/kcmcss
	%{_datadir}/apps/kcmcss/template.css
	%dir %{_datadir}/apps/kcmusb
	%{_datadir}/apps/kcmusb/usb.ids
	%{_datadir}/apps/kconf_update/*.*
	%dir %{_datadir}/apps/kcontrol
	%dir %{_datadir}/apps/kcontrol/pics
	%{_datadir}/apps/kcontrol/pics/*.png
	%dir %{_datadir}/apps/kdm
	%dir %{_datadir}/apps/kdm/pics
	%dir %{_datadir}/apps/kdm/pics/users
	%{_datadir}/apps/kdm/pics/users/*.png
	%dir %{_datadir}/apps/keditbookmarks
	%{_datadir}/apps/keditbookmarks/keditbookmarks*.rc
	%dir %{_datadir}/apps/kinfocenter
	%{_datadir}/apps/kinfocenter/kinfocenterui.rc
	%dir %{_datadir}/apps/kinfocenter/about
	%{_datadir}/apps/kinfocenter/about/*.*
	%dir %{_datadir}/apps/konqsidebartng
	%dir %{_datadir}/apps/konqsidebartng/entries
	%dir %{_datadir}/apps/konqsidebartng/dirtree
	%dir %{_datadir}/apps/konqsidebartng/add
	%dir %{_datadir}/apps/konqsidebartng/virtual_folders
	%dir %{_datadir}/apps/konqsidebartng/virtual_folders/remote
	%dir %{_datadir}/apps/konqsidebartng/virtual_folders/remote/ftp
	%dir %{_datadir}/apps/konqsidebartng/virtual_folders/remote/web
	%dir %{_datadir}/apps/konqsidebartng/virtual_folders/services
	%dir %{_datadir}/apps/konqsidebartng/websidebar
	%{_datadir}/apps/konqsidebartng/*/*.desktop
	%{_datadir}/apps/konqsidebartng/*/*/*.desktop
	%{_datadir}/apps/konqsidebartng/.*
	%{_datadir}/apps/konqsidebartng/websidebar/websidebar.html
	%{_datadir}/apps/konqsidebartng/*/.*
	%{_datadir}/apps/konqsidebartng/*/*/.*
	%{_datadir}/apps/konqsidebartng/*/*/*/*.desktop
	%{_datadir}/apps/konqsidebartng/*/*/*/.directory
	%dir %{_datadir}/apps/konqueror
	%{_datadir}/apps/konqueror/konqueror.rc
	%dir %{_datadir}/apps/konqueror/pics
	%dir %{_datadir}/apps/konqueror/profiles
	%{_datadir}/apps/konqueror/profiles/*
	%dir %{_datadir}/apps/konqueror/about
	%{_datadir}/apps/konqueror/*/*.*
	%dir %{_datadir}/apps/konsole
	%{_datadir}/apps/konsole/*.*
	%dir %{_datadir}/apps/kwrite
	%{_datadir}/apps/kwrite/kwriteui.rc
	%dir %{_datadir}/apps/khtml
	%dir %{_datadir}/apps/khtml/kpartplugins
	%{_datadir}/apps/khtml/kpartplugins/khtml*.*
	%dir %{_datadir}/autostart
	%{_datadir}/autostart/konqy_preload.desktop
	%dir %{_datadir}/config.kcfg
	%dir %{_datadir}/apps/plugin
	%{_datadir}/apps/plugin/nspluginpart.rc
	%{_datadir}/config.kcfg/*.kcfg
	%{_datadir}/dbus-1/interfaces/*.xml
	%{_datadir}/icons/hicolor/*/*/*.*
	%{_datadir}/icons/oxygen
	%{_datadir}/kde4/services/*.desktop
	%{_datadir}/kde4/servicetypes/*.desktop
	%dir %{_datadir}/kde4/services/useragentstrings
	%dir %{_datadir}/kde4/services/ServiceMenus
	%{_datadir}/kde4/services/*/*.desktop
	%dir %{_datadir}/templates
	%{_datadir}/templates/*.desktop
	%dir %{_datadir}/templates/.source
	%{_datadir}/templates/.source/*.*
