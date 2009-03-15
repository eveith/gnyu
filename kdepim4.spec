Name: kdepim4
Version: 4.2.1
Release: 2ev
Summary: Personal Information Management suite for KDE
URL: http://www.kde.org/
Group: User Interface/Desktops
License: GPL-2, LGPL-2.1, FDL-1.2
Vendor: GNyU-Linux
Source: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdepim-%{version}.tar.bz2
BuildRequires: cmake >= 2.4.5, make, gcc-g++, qt4 >= 4.2.0, automoc4 >= 0.8.86
BuildRequires: kdelibs4 = %{version}, kdepimlibs4 = %{version}, phonon >= 4.3.0
BuildRequires: perl, boost >= 1.33.1, akonadi, zlib, strigi, gpgme, gnokii, soprano
BuildRequires: libassuan, shared-mime-info, pilot-link, libmal, libxml2
BuildRequires: libXScrnSaver
Obsoletes: kdepim < %{version}

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
%config %{_sysconfdir}/kde4/kres-migratorrc
%config %{_sysconfdir}/kde4/libkleopatrarc
%{_bindir}/akonadi_distlist_resource
%{_bindir}/akonadi_ical_resource
%{_bindir}/akonadi_imaplib_resource
%{_bindir}/akonadi_kabc_resource
%{_bindir}/akonadi_kcal_resource
%{_bindir}/akonadi_knut_resource
%{_bindir}/akonadi_localbookmarks_resource
%{_bindir}/akonadi_maildir_resource
%{_bindir}/akonadi_mailthreader_agent
%{_bindir}/akonadi_nepomuktag_resource
%{_bindir}/akonadi_nepomuk_*_feeder
%{_bindir}/akonadi_nntp_resource
%{_bindir}/akonadi_strigi_feeder
%{_bindir}/akonadi_vcard_resource
%{_bindir}/akonadi_vcarddir_resource
%{_bindir}/akonadiconsole
%{_bindir}/akonaditray
%{_bindir}/akregator
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
%{_bindir}/kode
%{_bindir}/kolabwizard
%{_bindir}/konsolekalendar
%{_bindir}/kontact
%{_bindir}/korgac
%{_bindir}/korganizer
%{_bindir}/kpilot
%{_bindir}/kpilotDaemon
%{_bindir}/kres-migrator
%{_bindir}/ksendemail
%{_bindir}/ktimetracker
%{_bindir}/kung
%{_bindir}/kwatchgnupg
%{_bindir}/kwsdl_compiler
%{_bindir}/kxforms
%{_bindir}/kxml_compiler
%{_bindir}/scalixadmin
%{_bindir}/scalixwizard
%{_bindir}/schematest
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
%{_includedir}/*.h
%{_includedir}/*/*.h
%{_includedir}/*/*/*.h
%{_libdir}/kde4/*.so
%{_libdir}/kde4/plugins/designer/kdepimwidgets.so
%{_libdir}/libakonadi-*.so*
%{_libdir}/libakregator*.so*
%{_libdir}/libgwsoap.so*
%{_libdir}/libimap.so*
%{_libdir}/libkab*.so*
%{_libdir}/libkalarm*.so*
%{_libdir}/libkcal*.so*
%{_libdir}/libkdepim.so*
%{_libdir}/libkgroupware*.so*
%{_libdir}/libkholidays.so*
%{_libdir}/libkleo*.so*
%{_libdir}/libkmail*.so*
%{_libdir}/libknode*.so*
%{_libdir}/libknotes*.so*
%{_libdir}/libkaddressbook*.so*
%{_libdir}/libkocorehelper.so*
%{_libdir}/libkode.so*
%{_libdir}/libkontact*.so*
%{_libdir}/libkorg*.so*
%{_libdir}/libkpgp.so*
%{_libdir}/libkpilot*.so*
%{_libdir}/libkschema.so*
%{_libdir}/libksieve.so*
%{_libdir}/libkslox.so*
%{_libdir}/libkxmlcommon.so*
%{_libdir}/libmaildir.so*
%{_libdir}/libmimelib.so*
%{_libdir}/libschema.so*
%{_libdir}/libkschemawidgets.so*
%{_libdir}/libwscl.so*
%{_libdir}/libwsdl.so*
%{_libdir}/strigi/strigiea_ics.so
%{_libdir}/strigi/strigiea_vcf.so
%doc %{_mandir}/man1/kabcclient.1*
%{_datadir}/applications/kde4/*.desktop
%{_datadir}/apps/cmake/modules/*.cmake
%dir %{_datadir}/apps/kxforms
%{_datadir}/apps/kxforms/kxformsui.rc
%dir %{_datadir}/apps/akonadiconsole
%{_datadir}/apps/akonadiconsole/akonadiconsoleui.rc
%dir %{_datadir}/apps/akonadi
%dir %{_datadir}/apps/akonadi/plugins
%dir %{_datadir}/apps/akonadi/plugins/serializer
%{_datadir}/apps/akonadi/plugins/serializer/*.desktop
%{_datadir}/akonadi/agents/*.desktop
%{_datadir}/apps/nepomuk/ontologies/n?o.*
%dir %{_datadir}/apps/kleopatra/pics
%{_datadir}/apps/kleopatra/pics/*.*
%dir %{_datadir}/apps/akregator_onlinesync_plugin
%{_datadir}/apps/akregator_onlinesync_plugin/akregator_onlinesync_plugin.rc
%dir %{_datadir}/apps/kjots
%{_datadir}/apps/kjots/*.rc
%dir %{_datadir}/apps/kaddressbook/icons/oxygen
%dir %{_datadir}/apps/kaddressbook/icons/oxygen/16x16
%dir %{_datadir}/apps/kaddressbook/icons/oxygen/16x16/apps
%{_datadir}/apps/kaddressbook/icons/*/*/apps/*.*
%{_datadir}/apps/kconf_update/*.*
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
%dir %{_datadir}/apps/korgac/icons/oxygen
%dir %{_datadir}/apps/korgac/icons/oxygen/22x22
%dir %{_datadir}/apps/korgac/icons/oxygen/22x22/actions
%{_datadir}/apps/korgac/icons/oxygen/*/actions/*.*
%dir %{_datadir}/apps/kontact/ksettingsdialog
%{_datadir}/apps/kontact/ksettingsdialog/*.setdlg
%dir %{_datadir}/apps/kdepimwidgets
%dir %{_datadir}/apps/kdepimwidgets/pics
%{_datadir}/apps/kdepimwidgets/pics/*.png
%dir %{_datadir}/apps/libkdepim
%dir %{_datadir}/apps/libkdepim/about
%{_datadir}/apps/libkdepim/about/*.*
%dir %{_datadir}/apps/libkholidays
%{_datadir}/apps/libkholidays/*
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
%dir %{_datadir}/apps/kpilot
%dir %{_datadir}/apps/kpilot/kpilotui.rc
%dir %{_datadir}/apps/kontact
%{_datadir}/apps/kontact/kontactui.rc
%dir %{_datadir}/apps/kontact/about
%{_datadir}/apps/kontact/about/*.*
%dir %{_datadir}/apps/kontactsummary
%{_datadir}/apps/kontactsummary/kontactsummary_part.rc
%dir %{_datadir}/akonadi
%dir %{_datadir}/akonadi/agents
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
