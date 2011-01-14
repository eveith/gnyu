Name: kdelibs4
Version: 4.3.2
Release: 7ev
Summary: Base libraries for KDE-based applcations
URL: http://www.kde.org/
Group: User Interface/Desktops
License: GPL-2, LGPL-2, BSD
Vendor: GNyU-Linux
Source: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdelibs-%{version}.tar.bz2
BuildRequires: cmake >= 2.6.2, make, flex, bison, gcc-g++, perl, gettext
BuildRequires: libX11, libSM, libICE, libXrender
BuildRequires: qt4 >= 4.5.0, automoc4 >= 0.9.88
BuildRequires: zlib, bzip2, openssl, mesalib, libacl, libutempter 
BuildRequires: strigi >= 0.6.3, soprano >= 2.1.68
BuildRequires: pcre, libxslt, libxml2, hal, heimdal-libs
BuildRequires: shared-mime-info >= 0.23, enchant, aspell
BuildRequires: openexr, libpng, libjpeg, libungif
Requires: hicolor-icon-theme, shared-mime-info >= 0.23

%description
Libraries for the K Desktop Environment (KDE):
This package includes libraries that are central to the development and
execution of a KDE program, as well as internationalization files for these
libraries, misc HTML documentation, theme modules, and regression tests.


%prep
	%setup -q -T -c -a0 -n 'kdelibs-%{version}'
	%{__mkdir_p} 'kdelibs-%{version}-obj'


%build
	pushd 'kdelibs-%{version}-obj'
	%{cmake} \
		-DKDE_DISTRIBUTION_TEXT='%{vendor}' \
		-DCONFIG_INSTALL_DIR='%{_sysconfdir}/kde4' \
		-DMAN_INSTALL_DIR='%{_mandir}' \
		-DQT_QMAKE_EXECUTABLE:FILEPATH='%{_libdir}/qt4/bin/qmake' \
		'../kdelibs-%{version}'
	%{__make} %{?_smp_mflags}
	popd


%install
	pushd 'kdelibs-%{version}-obj'
	%{__make} install DESTDIR="${RPM_BUILD_ROOT}"
	popd

	%{__mv} '%{buildroot}/%{_prefix}/etc'/* '%{buildroot}/%{_sysconfdir}'
	%{__rm} -rf '%{buildroot}/%{_prefix}/etc'


%post
	%{__ldconfig}
	update-mime-database '%{_datadir}/mime' > /dev/null 2>&1
	exit 0


%postun
	%{__ldconfig}
	update-mime-database '%{_datadir}/mime' > /dev/null 2>&1
	exit 0


%files
	%defattr(-, root, root)
	%doc 'kdelibs-%{version}/AUTHORS' 'kdelibs-%{version}/CONFLICTS' 
	%doc 'kdelibs-%{version}'/COPYING* 'kdelibs-%{version}/DEBUG'
	%doc 'kdelibs-%{version}/KDE4PORTING.html' 'kdelibs-%{version}/README'
	%doc 'kdelibs-%{version}/TODO'
	%doc %{_datadir}/doc/HTML/en/*
	%dir %{_sysconfdir}/kde4
	%dir %{_sysconfdir}/kde4/colors
	%dir %{_sysconfdir}/kde4/ui
	%{_sysconfdir}/kde4/*.codes
	%{_sysconfdir}/kde4/colors/*.colors
	%{_sysconfdir}/kde4/katemoderc
	%{_sysconfdir}/kde4/kdebug.areas
	%{_sysconfdir}/kde4/kdebugrc
	%{_sysconfdir}/kde4/ksslcalist
	%{_sysconfdir}/kde4/plasmoids.knsrc
	%{_sysconfdir}/kde4/ui/ui_standards.rc
	%{_sysconfdir}/xdg/menus/applications.menu
	%{_bindir}/checkXML
	%{_bindir}/kbuildsycoca4
	%{_bindir}/kconfig_compiler
	%{_bindir}/kcookiejar4
	%{_bindir}/kde4-config
	%{_bindir}/kded4
	%{_bindir}/kdeinit4
	%{_bindir}/kdeinit4_shutdown
	%{_bindir}/kdeinit4_wrapper
	%{_bindir}/kjs
	%{_bindir}/kjscmd
	%{_bindir}/kross
	%{_bindir}/kshell4
	%{_bindir}/kunittestmodrunner
	%{_bindir}/kwrapper4
	%{_bindir}/makekdewidgets
	%{_bindir}/meinproc4
	%{_bindir}/nepomuk-rcgen
	%{_bindir}/preparetips
	%{_includedir}/*.h
	%dir %{_includedir}/kjs
	%{_includedir}/kjs/*.h
	%dir %{_includedir}/sonnet
	%{_includedir}/sonnet/*.h
	%dir %{_includedir}/kio
	%{_includedir}/kio/*.h
	%dir %{_includedir}/dom
	%{_includedir}/dom/*.h
	%dir %{_includedir}/kdesu
	%{_includedir}/kdesu/*.h
	%dir %{_includedir}/solid
	%{_includedir}/solid/*.h
	%dir %{_includedir}/kunittest
	%{_includedir}/kunittest/*.h
	%dir %{_includedir}/knewstuff2
	%{_includedir}/knewstuff2/*.h
	%dir %{_includedir}/knewstuff2/core
	%{_includedir}/knewstuff2/core/*.h
	%dir %{_includedir}/knewstuff2/ui
	%{_includedir}/knewstuff2/ui/*.h
	%dir %{_includedir}/kparts
	%{_includedir}/kparts/*.h
	%dir %{_includedir}/ksettings
	%{_includedir}/ksettings/*.h
	%dir %{_includedir}/threadweaver
	%{_includedir}/threadweaver/*.h
	%dir %{_includedir}/ktexteditor
	%{_includedir}/ktexteditor/*.h
	%dir %{_includedir}/kmediaplayer
	%{_includedir}/kmediaplayer/*.h
	%dir %{_includedir}/khexedit
	%{_includedir}/khexedit/*.h
	%dir %{_includedir}/dnssd
	%{_includedir}/dnssd/*.h
	%dir %{_includedir}/kross
	%dir %{_includedir}/kross/core
	%{_includedir}/kross/core/*.h
	%dir %{_includedir}/kross/ui
	%{_includedir}/kross/ui/*.h
	%dir %{_includedir}/plasma
	%{_includedir}/plasma/*.h
	%dir %{_includedir}/plasma/widgets
	%{_includedir}/plasma/widgets/*.h
	%dir %{_includedir}/plasma/scripting
	%{_includedir}/plasma/scripting/*.h
	%{_includedir}/KDE/
	%{_includedir}/kgenericfactory.tcc
	%dir %{_includedir}/nepomuk
	%{_includedir}/nepomuk/*.h
	%dir %{_libdir}/kde4
	%{_libdir}/kde4/*.so
	%{_libdir}/kde4/libexec/
	%{_libdir}/kde4/plugins/
	%{_libdir}/libkdefakes.*
	%{_libdir}/libkdecore.*
	%{_libdir}/libkdeui.*
	%{_libdir}/libkpty.*
	%{_libdir}/libkdesu.*
	%{_libdir}/libkjs.*
	%{_libdir}/libkjsapi.*
	%{_libdir}/libkjsembed.*
	%{_libdir}/libkio.*
	%{_libdir}/libkntlm.*
	%{_libdir}/libsolid.*
	%{_libdir}/libkdeinit4_kded4.*
	%{_libdir}/libkdeinit4_kbuildsycoca4.*
	%{_libdir}/libkde3support.*
	%{_libdir}/libkunittest.*
	%{_libdir}/libkfile.*
	%{_libdir}/libkdeinit4_kconf_update.*
	%{_libdir}/libkdeinit4_kio_http_cache_cleaner.*
	%{_libdir}/libknewstuff2.*
	%{_libdir}/libkparts.*
	%{_libdir}/libkutils.*
	%{_libdir}/libkdeinit4_klauncher.*
	%{_libdir}/libthreadweaver.*
	%{_libdir}/libkhtml.*
	%{_libdir}/libktexteditor.*
	%{_libdir}/libkmediaplayer.*
	%{_libdir}/libkimproxy.*
	%{_libdir}/libknotifyconfig.*
	%{_libdir}/libkdnssd.*
	%{_libdir}/libkrosscore.*
	%{_libdir}/libkrossui.*
	%{_libdir}/libplasma.*
	%{_libdir}/libnepomuk.*
	%{_datadir}/apps/LICENSES
	%dir %{_datadir}/apps/cmake
	%dir %{_datadir}/apps/cmake/modules
	%{_datadir}/apps/cmake/modules/*.*
	%dir %{_datadir}/apps/kdeui
	%dir %{_datadir}/apps/kdeui/pics
	%dir %{_datadir}/apps/kdeui/about
	%{_datadir}/apps/kdeui/*/*.*
	%dir %{_datadir}/apps/kcharselect
	%{_datadir}/apps/kcharselect/kcharselect-data
	%dir %{_datadir}/apps/kconf_update
	%{_datadir}/apps/kconf_update/*.*
	%dir %{_datadir}/apps/kssl
	%{_datadir}/apps/kssl/ca-bundle.crt
	%dir %{_datadir}/apps/proxyscout
	%{_datadir}/apps/proxyscout/proxyscout.notifyrc
	%dir %{_datadir}/apps/ksgmltools2
	%dir %{_datadir}/apps/ksgmltools2/customization
	%doc %{_datadir}/apps/ksgmltools2/customization/README
	%{_datadir}/apps/ksgmltools2/customization/*.x?l
	%dir %{_datadir}/apps/ksgmltools2/customization/af
	%dir %{_datadir}/apps/ksgmltools2/customization/af/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/bg
	%dir %{_datadir}/apps/ksgmltools2/customization/bg/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/ca
	%dir %{_datadir}/apps/ksgmltools2/customization/ca/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/cs
	%dir %{_datadir}/apps/ksgmltools2/customization/cs/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/da
	%dir %{_datadir}/apps/ksgmltools2/customization/da/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/de
	%dir %{_datadir}/apps/ksgmltools2/customization/de/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/dtd
	%dir %{_datadir}/apps/ksgmltools2/customization/el
	%dir %{_datadir}/apps/ksgmltools2/customization/el/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/en-GB
	%dir %{_datadir}/apps/ksgmltools2/customization/en-GB/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/en
	%dir %{_datadir}/apps/ksgmltools2/customization/en/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/eo
	%dir %{_datadir}/apps/ksgmltools2/customization/eo/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/es
	%dir %{_datadir}/apps/ksgmltools2/customization/es/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/et
	%dir %{_datadir}/apps/ksgmltools2/customization/et/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/fi
	%dir %{_datadir}/apps/ksgmltools2/customization/fi/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/fo
	%dir %{_datadir}/apps/ksgmltools2/customization/fo/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/fr
	%dir %{_datadir}/apps/ksgmltools2/customization/fr/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/gl
	%dir %{_datadir}/apps/ksgmltools2/customization/gl/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/he
	%dir %{_datadir}/apps/ksgmltools2/customization/he/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/hu
	%dir %{_datadir}/apps/ksgmltools2/customization/hu/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/id
	%dir %{_datadir}/apps/ksgmltools2/customization/id/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/it
	%dir %{_datadir}/apps/ksgmltools2/customization/it/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/ja
	%dir %{_datadir}/apps/ksgmltools2/customization/ja/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/ko
	%dir %{_datadir}/apps/ksgmltools2/customization/ko/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/lt
	%dir %{_datadir}/apps/ksgmltools2/customization/lt/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/nds
	%dir %{_datadir}/apps/ksgmltools2/customization/nds/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/nl
	%dir %{_datadir}/apps/ksgmltools2/customization/nl/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/nn
	%dir %{_datadir}/apps/ksgmltools2/customization/nn/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/no
	%dir %{_datadir}/apps/ksgmltools2/customization/no/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/obsolete
	%dir %{_datadir}/apps/ksgmltools2/customization/pl
	%dir %{_datadir}/apps/ksgmltools2/customization/pl/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/pt-BR
	%dir %{_datadir}/apps/ksgmltools2/customization/pt-BR/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/pt
	%dir %{_datadir}/apps/ksgmltools2/customization/pt/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/ro
	%dir %{_datadir}/apps/ksgmltools2/customization/ro/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/ru
	%dir %{_datadir}/apps/ksgmltools2/customization/ru/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/sk
	%dir %{_datadir}/apps/ksgmltools2/customization/sk/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/sl
	%dir %{_datadir}/apps/ksgmltools2/customization/sl/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/sr
	%dir %{_datadir}/apps/ksgmltools2/customization/sr/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/sr@latin
	%dir %{_datadir}/apps/ksgmltools2/customization/sr@latin/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/sv
	%dir %{_datadir}/apps/ksgmltools2/customization/sv/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/th
	%dir %{_datadir}/apps/ksgmltools2/customization/th/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/tr
	%dir %{_datadir}/apps/ksgmltools2/customization/tr/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/uk
	%dir %{_datadir}/apps/ksgmltools2/customization/uk/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/wa
	%dir %{_datadir}/apps/ksgmltools2/customization/wa/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/xh
	%dir %{_datadir}/apps/ksgmltools2/customization/xh/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/xsl
	%doc %{_datadir}/apps/ksgmltools2/customization/xsl/README
	%dir %{_datadir}/apps/ksgmltools2/customization/xx
	%dir %{_datadir}/apps/ksgmltools2/customization/xx/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/zh-CN
	%dir %{_datadir}/apps/ksgmltools2/customization/zh-CN/entities
	%dir %{_datadir}/apps/ksgmltools2/customization/zh-TW
	%dir %{_datadir}/apps/ksgmltools2/customization/zh-TW/entities
	%{_datadir}/apps/ksgmltools2/customization/*/*.*
	%{_datadir}/apps/ksgmltools2/customization/*/entities/*.docbook
	%dir %{_datadir}/apps/ksgmltools2/docbook
	%doc %{_datadir}/apps/ksgmltools2/docbook/README.kde
	%dir %{_datadir}/apps/ksgmltools2/docbook/xml-dtd-4.1.2
	%dir %{_datadir}/apps/ksgmltools2/docbook/xml-dtd-4.1.2/ent
	%{_datadir}/apps/ksgmltools2/docbook/xml-dtd-4.1.2/*.*
	%{_datadir}/apps/ksgmltools2/docbook/xml-dtd-4.1.2/ent/*.*
	%dir %{_datadir}/apps/ksgmltools2/docbook/xml-dtd-4.2
	%dir %{_datadir}/apps/ksgmltools2/docbook/xml-dtd-4.2/ent
	%doc %{_datadir}/apps/ksgmltools2/docbook/xml-dtd-4.2/README
	%{_datadir}/apps/ksgmltools2/docbook/xml-dtd-4.2/*.*
	%{_datadir}/apps/ksgmltools2/docbook/xml-dtd-4.2/ent/*.*
	%dir %{_datadir}/apps/ksgmltools2/docbook/xsl
	%doc %{_datadir}/apps/ksgmltools2/docbook/xsl/README
	%doc %{_datadir}/apps/ksgmltools2/docbook/xsl/VERSION
	%doc %{_datadir}/apps/ksgmltools2/docbook/xsl/WhatsNew
	%dir %{_datadir}/apps/ksgmltools2/docbook/xsl/common
	%dir %{_datadir}/apps/ksgmltools2/docbook/xsl/html
	%dir %{_datadir}/apps/ksgmltools2/docbook/xsl/images
	%dir %{_datadir}/apps/ksgmltools2/docbook/xsl/images/callouts
	%{_datadir}/apps/ksgmltools2/docbook/xsl/images/callouts/*.*
	%dir %{_datadir}/apps/ksgmltools2/docbook/xsl/lib
	%dir %{_datadir}/apps/ksgmltools2/docbook/xsl/manpages
	%dir %{_datadir}/apps/ksgmltools2/docbook/xsl/params
	%{_datadir}/apps/ksgmltools2/docbook/xsl/*/*.*
	%dir %{_datadir}/apps/khtml
	%{_datadir}/apps/khtml/*.*
	%{_datadir}/apps/khtml/domain_info
	%dir %{_datadir}/apps/khtml/css
	%{_datadir}/apps/khtml/css/*.css
	%dir %{_datadir}/apps/knewstuff
	%dir %{_datadir}/apps/knewstuff/pics
	%{_datadir}/apps/knewstuff/pics/*.png
	%dir %{_datadir}/apps/kjava
	%{_datadir}/apps/kjava/kjava.*
	%{_datadir}/apps/kjava/pluginsinfo
	%dir %{_datadir}/apps/kcm_componentchooser
	%{_datadir}/apps/kcm_componentchooser/*.desktop
	%dir %{_datadir}/apps/kdewidgets
	%dir %{_datadir}/apps/kdewidgets/pics
	%{_datadir}/apps/kdewidgets/pics/*.png
	%dir %{_datadir}/apps/katepart
	%{_datadir}/apps/katepart/*.rc
	%dir %{_datadir}/apps/katepart/syntax
	%{_datadir}/apps/katepart/syntax/*.*
	%dir %{_datadir}/apps/katepart/script
	%{_datadir}/apps/katepart/script/*.js
	%dir %{_datadir}/apps/ktexteditor_insertfile
	%dir %{_datadir}/apps/ktexteditor_kdatatool
	%{_datadir}/apps/ktexteditor_*/*.rc
	%dir %{_datadir}/apps/nepomuk
	%dir %{_datadir}/apps/nepomuk/pics
	%{_datadir}/apps/nepomuk/pics/rating.png
	%{_datadir}/dbus-1/interfaces/org.freedesktop.PowerManagement.Inhibit.xml
	%{_datadir}/dbus-1/interfaces/org.freedesktop.PowerManagement.xml
	%{_datadir}/dbus-1/interfaces/org.kde.JobView.xml
	%{_datadir}/dbus-1/interfaces/org.kde.JobViewServer.xml
	%{_datadir}/dbus-1/interfaces/org.kde.KCookieServer.xml
	%{_datadir}/dbus-1/interfaces/org.kde.KDirNotify.xml
	%{_datadir}/dbus-1/interfaces/org.kde.KHTMLPart.xml
	%{_datadir}/dbus-1/interfaces/org.kde.KIMIface.xml
	%{_datadir}/dbus-1/interfaces/org.kde.KLauncher.xml
	%{_datadir}/dbus-1/interfaces/org.kde.KMediaPlayer.xml
	%{_datadir}/dbus-1/interfaces/org.kde.KPasswdServer.xml
	%{_datadir}/dbus-1/interfaces/org.kde.KSpeech.xml
	%{_datadir}/dbus-1/interfaces/org.kde.KWallet.xml
	%{_datadir}/dbus-1/interfaces/org.kde.Solid.Networking.Client.xml
	%{_datadir}/dbus-1/interfaces/org.kde.kded.xml
	%{_datadir}/dbus-1/interfaces/org.kde.kio.FileUndoManager.xml
	%{_datadir}/icons/hicolor/*/actions/presence_*.png
	%dir %{_datadir}/kde4
	%dir %{_datadir}/kde4/services
	%{_datadir}/kde4/services/*.protocol
	%{_datadir}/kde4/services/*.desktop
	%dir %{_datadir}/kde4/services/qimageioplugins
	%dir %{_datadir}/kde4/services/kded
	%{_datadir}/kde4/services/*/*.desktop
	%dir %{_datadir}/kde4/servicetypes
	%{_datadir}/kde4/servicetypes/*.desktop
	%{_datadir}/mime/packages/kde.xml
	%{_datadir}/locale/all_languages
	%doc %{_mandir}/man1/kdecmake.1*
	%doc %{_mandir}/man1/checkXML.1*
	%doc %{_mandir}/man1/makekdewidgets.1*
	%doc %{_mandir}/man1/kde4-config.1*
	%doc %{_mandir}/man1/kjs.1*
	%doc %{_mandir}/man1/kjscmd.1*
	%doc %{_mandir}/man1/kross.1*
	%doc %{_mandir}/man8/kbuildsycoca4.8*
	%doc %{_mandir}/man8/kcookiejar4.8*
	%doc %{_mandir}/man8/kdeinit4.8*
	%doc %{_mandir}/man8/meinproc4.8*
	%doc %{_mandir}/man8/kded4.8*
	%doc %{_mandir}/man7/kdeoptions.7*
	%doc %{_mandir}/man7/qtoptions.7*
