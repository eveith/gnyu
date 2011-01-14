Name: kdepim4
Version: 4.3.2
Release: 7.1ev
Summary: Personal Information Management suite for KDE
URL: http://www.kde.org/
Group: User Interface/Desktops
License: GPL-2, LGPL-2.1, FDL-1.2
Vendor: GNyU-Linux
Source: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdepim-%{version}.tar.bz2
BuildRequires: cmake >= 2.6.2, make, flex, bison, gcc-g++, perl, gettext
BuildRequires: libX11, libSM, libICE, libXrender
BuildRequires: qt4 >= 4.5.0, automoc4 >= 0.9.88
BuildRequires: kdelibs4 = %{version}, kdepimlibs4 = %{version}, phonon >= 4.3.0
BuildRequires: kdelibs4-experimental = %{version}
BuildRequires: boost >= 1.33.1, akonadi, zlib, strigi, gpgme, gnokii, soprano
BuildRequires: libassuan, shared-mime-info, pilot-link, libmal, libxml2
BuildRequires: libXScrnSaver
Obsoletes: kdepim < %{version}
Requires: kdepim4-runtime >= %{version}

%description
KDE PIM is sub project of KDE. Its goal is to provide an application suite to
manage personal information. This includes mail, time, people and more. The
main result is KDE Kontact, KDE's personal information manager.


%prep
	%setup -q -n 'kdepim-%{version}'


%build
	%{cmake} \
		-DQT_QMAKE_EXECUTABLE:FILEPATH='%{_libdir}/qt4/bin/qmake' \
		.
	%{__make} %{?_smp_mflags}


%install
	%{__make} install DESTDIR='%{buildroot}'


%post
	%{__ldconfig}


%postun
	%{__ldconfig}


%files
	%defattr(-, root, root)
	%doc COPYING* MAINTAINERS README*
	%doc %{_datadir}/doc/HTML/en/*
	%config %{_sysconfdir}/kde4/kmail.antispamrc
	%config %{_sysconfdir}/kde4/kmail.antivirusrc
	%config %{_sysconfdir}/kde4/korganizer.knsrc
	%config %{_sysconfdir}/kde4/libkleopatrarc
	%{_bindir}/akregator
	%{_bindir}/akregatorstorageexporter
	%{_bindir}/egroupwarewizard
	%{_bindir}/groupwarewizard
	%{_bindir}/groupwisewizard
	%{_bindir}/ical2vcal
	%{_bindir}/kabc2mutt
	%{_bindir}/kabcclient
	%{_bindir}/kabcdistlistupdater
	%{_bindir}/kaddressbook
	%{_bindir}/kalarm
	%{_bindir}/kalarmautostart
	%{_bindir}/karm
	%{_bindir}/kgpgconf
	%{_bindir}/kjots
	%{_bindir}/kleopatra
	%{_bindir}/kmail
	%{_bindir}/kmail_antivir.sh
	%{_bindir}/kmail_clamav.sh
	%{_bindir}/kmail_fprot.sh
	%{_bindir}/kmail_sav.sh
	%{_bindir}/kmailcvt
	%{_bindir}/knode
	%{_bindir}/knotes
	%{_bindir}/kolabwizard
	%{_bindir}/konsolekalendar
	%{_bindir}/kontact
	%{_bindir}/korgac
	%{_bindir}/korganizer
	%{_bindir}/kpilot
	%{_bindir}/kpilotDaemon
	%{_bindir}/ksendemail
	%{_bindir}/ktimetracker
	%{_bindir}/kwatchgnupg
	%{_bindir}/scalixadmin
	%{_bindir}/scalixwizard
	%{_bindir}/sloxwizard
	%dir %{_includedir}/libkleopatraclient
	%dir %{_includedir}/libkleopatraclient/core
	%dir %{_includedir}/libkleopatraclient/gui
	%dir %{_includedir}/kleo/ui
	%dir %{_includedir}/kpgp
	%dir %{_includedir}/kleo
	%dir %{_includedir}/ksieve
	%dir %{_includedir}/akregator
	%dir %{_includedir}/kmail
	%dir %{_includedir}/kmail/interfaces
	%dir %{_includedir}/kaddressbook
	%dir %{_includedir}/kpilot
	%{_includedir}/*/*.h
	%{_includedir}/*/*/*.h
	%{_libdir}/kde4/*.so
	%{_libdir}/kde4/plugins/designer/kdepimwidgets.so
	%{_libdir}/libakregator*.so*
	%{_libdir}/libgwsoap.so*
	%{_libdir}/libkab*.so*
	%{_libdir}/libkalarm*.so*
	%{_libdir}/libkcal*.so*
	%{_libdir}/libkdepim.so*
	%{_libdir}/libkgroupware*.so*
	%{_libdir}/libkleo*.so*
	%{_libdir}/libkmail*.so*
	%{_libdir}/libknode*.so*
	%{_libdir}/libknotes*.so*
	%{_libdir}/libkaddressbook*.so*
	%{_libdir}/libkontact*.so*
	%{_libdir}/libkorg*.so*
	%{_libdir}/libkpgp.so*
	%{_libdir}/libkpilot*.so*
	%{_libdir}/libksieve.so*
	%{_libdir}/libkslox.so*
	%{_libdir}/libmimelib.so*
	%{_libdir}/strigi/strigiea_ics.so
	%{_libdir}/strigi/strigiea_vcf.so
	%{_datadir}/applications/kde4/*.desktop
	%dir %{_datadir}/apps/kleopatra/pics
	%{_datadir}/apps/kleopatra/pics/*.*
	%dir %{_datadir}/apps/kjots
	%{_datadir}/apps/kjots/*.rc
	%dir %{_datadir}/apps/kaddressbook/icons/oxygen
	%dir %{_datadir}/apps/kaddressbook/icons/oxygen/16x16
	%dir %{_datadir}/apps/kaddressbook/icons/oxygen/16x16/apps
	%{_datadir}/apps/kaddressbook/icons/*/*/apps/*.*
	%{_datadir}/apps/kconf_update/*.*
	%dir %{_datadir}/apps/konsolekalendar
	%dir %{_datadir}/apps/konsolekalendar/pics
	%{_datadir}/apps/konsolekalendar/pics/hi*-apps-konsolekalendar.png
	%dir %{_datadir}/apps/ktimetracker
	%{_datadir}/apps/ktimetracker/ktimetrackerui.rc
	%dir %{_datadir}/apps/ktimetracker/pics
	%{_datadir}/apps/ktimetracker/pics/*.xpm
	%dir %{_datadir}/apps/ktimetracker/icons
	%dir %{_datadir}/apps/ktimetracker/icons/oxygen
	%dir %{_datadir}/apps/ktimetracker/icons/oxygen/16x16
	%dir %{_datadir}/apps/ktimetracker/icons/oxygen/16x16/actions
	%dir %{_datadir}/apps/ktimetracker/icons/oxygen/32x32
	%dir %{_datadir}/apps/ktimetracker/icons/oxygen/32x32/actions
	%dir %{_datadir}/apps/ktimetracker/icons/oxygen/128x128
	%dir %{_datadir}/apps/ktimetracker/icons/oxygen/128x128/actions
	%dir %{_datadir}/apps/ktimetracker/icons/oxygen/48x48
	%dir %{_datadir}/apps/ktimetracker/icons/oxygen/48x48/actions
	%dir %{_datadir}/apps/ktimetracker/icons/oxygen/22x22
	%dir %{_datadir}/apps/ktimetracker/icons/oxygen/22x22/actions
	%dir %{_datadir}/apps/ktimetracker/icons/oxygen/64x64
	%dir %{_datadir}/apps/ktimetracker/icons/oxygen/64x64/actions
	%dir %{_datadir}/apps/ktimetracker/icons/oxygen/scalable
	%dir %{_datadir}/apps/ktimetracker/icons/oxygen/scalable/actions
	%{_datadir}/apps/ktimetracker/icons/oxygen/*/actions/*.*
	%dir %{_datadir}/apps/knotes/icons/oxygen
	%dir %{_datadir}/apps/knotes/icons/oxygen/16x16
	%dir %{_datadir}/apps/knotes/icons/oxygen/16x16/actions
	%{_datadir}/apps/knotes/icons/oxygen/16x16/actions/*.*
	%dir %{_datadir}/apps/kontact/ksettingsdialog
	%{_datadir}/apps/kontact/ksettingsdialog/*.setdlg
	%dir %{_datadir}/apps/kdepimwidgets
	%dir %{_datadir}/apps/kdepimwidgets/pics
	%{_datadir}/apps/kdepimwidgets/pics/*.png
	%dir %{_datadir}/apps/libkdepim
	%dir %{_datadir}/apps/libkdepim/about
	%{_datadir}/apps/libkdepim/about/*.*
	%dir %{_datadir}/apps/kleopatra
	%{_datadir}/apps/kleopatra/kleopatra.rc
	%dir %{_datadir}/apps/kwatchgnupg
	%{_datadir}/apps/kwatchgnupg/kwatchgnupgui.rc
	%dir %{_datadir}/apps/kwatchgnupg/pics
	%{_datadir}/apps/kwatchgnupg/pics/kwatchgnupg*.png
	%dir %{_datadir}/apps/libkleopatra
	%dir %{_datadir}/apps/libkleopatra/pics
	%{_datadir}/apps/libkleopatra/pics/*.png
	%dir %{_datadir}/apps/knode
	%{_datadir}/apps/knode/*rc
	%dir %{_datadir}/apps/knode/pics
	%{_datadir}/apps/knode/pics/*.*
	%dir %{_datadir}/apps/knode/filters
	%{_datadir}/apps/knode/filters/?.fltr
	%{_datadir}/apps/knode/filters/filters.rc
	%dir %{_datadir}/apps/kmail
	%{_datadir}/apps/kmail/*rc
	%{_datadir}/apps/kmail/tips
	%dir %{_datadir}/apps/kmail/pics
	%{_datadir}/apps/kmail/pics/*.*
	%dir %{_datadir}/apps/kmail/plugins
	%dir %{_datadir}/apps/kmail/plugins/bodypartformatter
	%{_datadir}/apps/kmail/plugins/bodypartformatter/*.desktop
	%dir %{_datadir}/apps/kmail/about
	%{_datadir}/apps/kmail/about/*.*
	%dir %{_datadir}/apps/akregator
	%{_datadir}/apps/akregator/*rc
	%dir %{_datadir}/apps/akregator/about
	%{_datadir}/apps/akregator/about/*.*
	%dir %{_datadir}/apps/akregator/pics
	%{_datadir}/apps/akregator/pics/*.png
	%dir %{_datadir}/apps/kalarm
	%{_datadir}/apps/kalarm/kalarmui.rc
	%dir %{_datadir}/apps/kalarm/icons
	%dir %{_datadir}/apps/kalarm/icons/oxygen
	%dir %{_datadir}/apps/kalarm/icons/oxygen/16x16
	%dir %{_datadir}/apps/kalarm/icons/oxygen/16x16/actions
	%dir %{_datadir}/apps/kalarm/icons/oxygen/22x22
	%dir %{_datadir}/apps/kalarm/icons/oxygen/22x22/actions
	%{_datadir}/apps/kalarm/icons/oxygen/*/actions/*.png
	%dir %{_datadir}/apps/kaddressbook
	%{_datadir}/apps/kaddressbook/*rc
	%{_datadir}/apps/kaddressbook/zone.tab
	%dir %{_datadir}/apps/kaddressbook/printing
	%{_datadir}/apps/kaddressbook/printing/*.png
	%dir %{_datadir}/apps/kaddressbook/icons
	%dir %{_datadir}/apps/kaddressbook/pics
	%{_datadir}/apps/kaddressbook/pics/world.jpg
	%dir %{_datadir}/apps/kaddressbook/csv-templates
	%{_datadir}/apps/kaddressbook/csv-templates/*.desktop
	%dir %{_datadir}/apps/kmailcvt
	%dir %{_datadir}/apps/kmailcvt/pics
	%{_datadir}/apps/kmailcvt/pics/step1.png
	%dir %{_datadir}/apps/knotes
	%{_datadir}/apps/knotes/*rc
	%dir %{_datadir}/apps/knotes/icons
	%dir %{_datadir}/apps/korganizer
	%{_datadir}/apps/korganizer/*.rc
	%{_datadir}/apps/korganizer/tips
	%dir %{_datadir}/apps/korganizer/sounds
	%{_datadir}/apps/korganizer/sounds/*.wav
	%dir %{_datadir}/apps/korgac
	%dir %{_datadir}/apps/korgac/icons
	%dir %{_datadir}/apps/korgac/icons/hicolor
	%dir %{_datadir}/apps/korgac/icons/hicolor/22x22
	%dir %{_datadir}/apps/korgac/icons/hicolor/22x22/actions
	%{_datadir}/apps/korgac/icons/hicolor/22x22/actions/korgac.png
	%dir %{_datadir}/apps/kpilot
	%dir %{_datadir}/apps/kpilot/kpilotui.rc
	%dir %{_datadir}/apps/kontact
	%{_datadir}/apps/kontact/kontactui.rc
	%dir %{_datadir}/apps/kontact/about
	%{_datadir}/apps/kontact/about/*.*
	%dir %{_datadir}/apps/kontactsummary
	%{_datadir}/apps/kontactsummary/kontactsummary_part.rc
	%{_datadir}/autostart/*.desktop
	%{_datadir}/config.kcfg/*.kcfg
	%{_datadir}/dbus-1/interfaces/org.kde*.xml
	%{_datadir}/icons/*/*/*/*.*
	%dir %{_datadir}/kde4/services/kontact
	%dir %{_datadir}/kde4/services/kresources/alarms
	%dir %{_datadir}/kde4/services/kresources/knotes
	%dir %{_datadir}/kde4/services/kresources/*/*.desktop
	%dir %{_datadir}/kde4/services/kaddressbook
	%dir %{_datadir}/kde4/services/korganizer
	%dir %{_datadir}/kde4/services/*.desktop
	%dir %{_datadir}/kde4/services/*.protocol
	%dir %{_datadir}/kde4/services/*/*.desktop
	%{_datadir}/kde4/servicetypes/*.desktop
