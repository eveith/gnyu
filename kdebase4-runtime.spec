Name: kdebase4-runtime
Version: 4.2.1
Release: 2ev
Summary: KDE Desktop Applications such as the panel or the login manager
URL: http://www.kde.org/
Group: User Interface/Desktops
License: GPL-2, LGPL-2.1, FDL-1.2
Vendor: GNyU-Linux
Source: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdebase-runtime-%{version}.tar.bz2
BuildRequires: cmake >= 2.4.5, make, gcc-g++, qt4 >= 4.2.0, automoc4 >= 0.8.87
BuildRequires: kdelibs4 = %{version}
BuildRequires: glib2, soprano, perl, qimageblitz >= 0.0.4
BuildRequires: phonon >= 4.3.0, openexr, clucene-core, samba-libs, bzip2
BuildRequires: xine-lib
BuildRequires: libX11, libICE, libSM, libXext, libXcomposite, libxkbfile,
BuildRequires: libXScrnSaver, libXft
Requires: dbus

%description
KDE Workspace consisting of what is the desktop. This means it includes
Plasma, i. e. desktop and panels, the KDM login manager, and so on.


%prep
%setup -q -T -c -a0 -n 'kdebase-%{version}'
%{__mkdir_p} 'kdebase-runtime-%{version}-obj'


%build
pushd 'kdebase-runtime-%{version}-obj'
%{cmake} \
	-DKDE_DISTRIBUTION_TEXT='%{vendor}' \
	-DCONFIG_INSTALL_DIR='%{_sysconfdir}/kde4' \
	-DSYSCONF_INSTALL_DIR='%{_sysconfdir}/kde4' \
	-DMAN_INSTALL_DIR='%{_mandir}' \
	-DQT_QMAKE_EXECUTABLE:FILEPATH='%{_libdir}/qt4/bin/qmake' \
	'../kdebase-runtime-%{version}'
%{__make} %{?_smp_mflags}
popd


%install
pushd 'kdebase-runtime-%{version}-obj'
%{__make} install DESTDIR='%{buildroot}'
popd
%{__rm} '%{buildroot}/%{_datadir}/icons/hicolor/index.theme'


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc 'kdebase-runtime-%{version}'/COPYING*
%doc %{_datadir}/doc/HTML/en/*
%config %{_sysconfdir}/kde4/emoticons.knsrc
%config %{_sysconfdir}/kde4/icons.knsrc
%config %{_sysconfdir}/kde4/khotnewstuff.knsrc
%config %{_sysconfdir}/kde4/kshorturifilterrc
%dir %{_sysconfdir}//kde4/xdg/menus
%config %{_sysconfdir}/kde4/xdg/menus/kde-information.menu
%{_bindir}/kcmshell4
%{_bindir}/kde-cp
%{_bindir}/kde-mv
%{_bindir}/kde-open
%{_bindir}/kde4
%{_bindir}/kde4-menu
%{_bindir}/kdebugdialog
%{_bindir}/kfile4
%{_bindir}/khelpcenter
%{_bindir}/khotnewstuff4
%{_bindir}/kiconfinder
%{_bindir}/kioclient
%{_bindir}/kmimetypefinder
%{_bindir}/knotify4
%{_bindir}/kquitapp
%{_bindir}/kreadconfig
%{_bindir}/kstart
%{_bindir}/ksvgtopng
%{_bindir}/ktraderclient
%{_bindir}/ktrash
%{_bindir}/kuiserver
%{_bindir}/kwalletd
%{_bindir}/kwriteconfig
%{_bindir}/nepomukserver
%{_bindir}/nepomukservicestub
%{_bindir}/solid-hardware
%{_libdir}/kde4/*.so
%{_libdir}/kde4/libexec/*
%dir %{_libdir}/kde4/plugins/phonon_platform
%{_libdir}/kde4/plugins/phonon_platform/kde.so
%dir %{_libdir}/kde4/plugins/styles
%{_libdir}/kde4/plugins/styles/oxygen.so
%{_libdir}/libkdeinit4*.so*
%{_libdir}/libkwalletbackend.so*
%dir %{_libdir}/kconf_update_bin
%dir %{_libdir}/kconf_update_bin/*_update
%{_libdir}/strigi/strigiindex_sopranobackend.so
%doc %{_mandir}/man1/kdesu.1*
%{_datadir}/applications/kde4/*.desktop
%{_datadir}/apps/cmake/modules/*.cmake
%dir %{_datadir}/apps/kde
%{_datadir}/apps/kde/kde.notifyrc
%dir %{_datadir}/apps/nepomuk/ontologies
%{_datadir}/apps/nepomuk/ontologies/*.*
%dir %{_datadir}/apps/nepomukstorage
%dir %{_datadir}/apps/nepomukstrigiservice
%{_datadir}/apps/nepomuk*/*.notifyrc
%dir %{_datadir}/apps/kcmlocale
%dir %{_datadir}/apps/kcmlocale/pics
%{_datadir}/apps/kcmlocale/pics/background.png
%dir %{_datadir}/apps/ksmserver
%dir %{_datadir}/apps/ksmserver/windowmanagers
%{_datadir}/apps/ksmserver/windowmanagers/*.desktop
%dir %{_datadir}/apps/kio_bookmarks
%dir %{_datadir}/apps/kio_info
%{_datadir}/apps/kio_info/kde-info2html
%dir %{_datadir}/apps/kio_desktop
%{_datadir}/apps/kio_desktop/DesktopLinks/Home.desktop
%dir %{_datadir}/apps/kio_desktop/DesktopLinks
%dir %{_datadir}/apps/kio_thumbnail
%dir %{_datadir}/apps/kio_thumbnail/pics
%{_datadir}/apps/kio_thumbnail/pics/thumbnailfont_7x4.png
%dir %{_datadir}/apps/kio_finger
%dir %{_datadir}/apps/kio_man
%{_datadir}/apps/kio_*/*.*
%dir %{_datadir}/apps/konqueror/dirtree
%dir %{_datadir}/apps/konqueror/dirtree/remote
%{_datadir}/apps/konqueror/dirtree/remote/smb-network.desktop
%dir %{_datadir}/apps/remoteview
%dir %{_datadir}/apps/libphonon
%dir %{_datadir}/apps/phonon
%dir %{_datadir}/apps/kcm_phonon
%{_datadir}/apps/kcm_phonon/listview-background.png
%dir %{_datadir}/apps/drkonqi
%dir %{_datadir}/apps/drkonqi/presets
%dir %{_datadir}/apps/drkonqi/pics
%{_datadir}/apps/drkonqi/pics/konqi.png
%dir %{_datadir}/apps/drkonqi/debuggers
%{_datadir}/apps/drkonqi/*/*rc
%{_datadir}/apps/kcm_componentchooser/*.desktop
%{_datadir}/apps/kconf_update/*.upd
%dir %{_datadir}/apps/khelpcenter
%dir %{_datadir}/apps/khelpcenter/plugins
%dir %{_datadir}/apps/khelpcenter/plugins/Applications
%dir %{_datadir}/apps/khelpcenter/plugins/Manpages
%dir %{_datadir}/apps/khelpcenter/plugins/Tutorials
%dir %{_datadir}/apps/khelpcenter/plugins/Scrollkeeper
%dir %{_datadir}/apps/khelpcenter/searchhandlers
%dir %{_datadir}/apps/khelpcenter/searchhandlers/htdig
%{_datadir}/apps/khelpcenter/searchhandlers/htdig/htdig_long.html
%{_datadir}/apps/kstyle/themes/oxygen.themerc
%{_datadir}/apps/libphonon/hardwaredatabase
%{_datadir}/apps/phonon/phonon.notifyrc
%{_datadir}/apps/remoteview/smb-network.desktop
%{_datadir}/autostart/nepomukserver.desktop
%{_datadir}/apps/khelpcenter/*.*
%{_datadir}/apps/khelpcenter/plugins/Applications/.directory
%{_datadir}/apps/khelpcenter/plugins/Manpages/.directory
%{_datadir}/apps/khelpcenter/plugins/Manpages/man?.desktop
%{_datadir}/apps/khelpcenter/plugins/Scrollkeeper/.directory
%{_datadir}/apps/khelpcenter/plugins/Scrollkeeper/scrollkeeper.desktop
%{_datadir}/apps/khelpcenter/plugins/Tutorials/.directory
%{_datadir}/apps/khelpcenter/plugins/Tutorials/*.desktop
%{_datadir}/apps/khelpcenter/plugins/*.desktop
%{_datadir}/apps/khelpcenter/searchhandlers/*.desktop
%{_datadir}/apps/desktoptheme/default/colors
%{_datadir}/apps/desktoptheme/default/metadata.desktop
%dir %{_datadir}/apps/desktoptheme/default/dialogs
%dir %{_datadir}/apps/desktoptheme/default/opaque
%dir %{_datadir}/apps/desktoptheme/default/opaque/widgets
%dir %{_datadir}/apps/desktoptheme/default/opaque/dialogs
%{_datadir}/apps/desktoptheme/default/opaque/*/*.*
%dir %{_datadir}/apps/desktoptheme/default/*/*.*
%{_datadir}/config.kcfg/khelpcenter.kcfg
%dir %{_datadir}/desktop-directories
%{_datadir}/desktop-directories/*.directory
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/services/*.service
%dir %{_datadir}/emoticons/kde4
%{_datadir}/emoticons/kde4/*.*
%{_datadir}/kde4/services/*.*
%{_datadir}/kde4/services/kded/*.desktop
%{_datadir}/kde4/servicetypes/*.desktop
%dir %{_datadir}/kde4/services/searchproviders
%{_datadir}/kde4/services/searchproviders/*.desktop
%{_datadir}/icons/default.kde4
%{_datadir}/icons/oxygen/
%{_datadir}/icons/hicolor/*/apps/knetattach.*
%dir %{_datadir}/locale/l10n                                                                                                                              
%dir %{_datadir}/locale/l10n/C                                                                                                                            
%dir %{_datadir}/locale/l10n/ad                                                                                                                           
%dir %{_datadir}/locale/l10n/ae                                                                                                                           
%dir %{_datadir}/locale/l10n/af                                                                                                                           
%dir %{_datadir}/locale/l10n/ag                                                                                                                           
%dir %{_datadir}/locale/l10n/ai                                                                                                                           
%dir %{_datadir}/locale/l10n/al                                                                                                                           
%dir %{_datadir}/locale/l10n/am                                                                                                                           
%dir %{_datadir}/locale/l10n/an                                                                                                                           
%dir %{_datadir}/locale/l10n/ao                                                                                                                           
%dir %{_datadir}/locale/l10n/ar                                                                                                                           
%dir %{_datadir}/locale/l10n/as                                                                                                                           
%dir %{_datadir}/locale/l10n/at                                                                                                                           
%dir %{_datadir}/locale/l10n/au                                                                                                                           
%dir %{_datadir}/locale/l10n/aw                                                                                                                           
%dir %{_datadir}/locale/l10n/ax                                                                                                                           
%dir %{_datadir}/locale/l10n/az                                                                                                                           
%dir %{_datadir}/locale/l10n/ba                                                                                                                           
%dir %{_datadir}/locale/l10n/bb                                                                                                                           
%dir %{_datadir}/locale/l10n/bd                                                                                                                           
%dir %{_datadir}/locale/l10n/be                                                                                                                           
%dir %{_datadir}/locale/l10n/bf                                                                                                                           
%dir %{_datadir}/locale/l10n/bg                                                                                                                           
%dir %{_datadir}/locale/l10n/bh                                                                                                                           
%dir %{_datadir}/locale/l10n/bi                                                                                                                           
%dir %{_datadir}/locale/l10n/bj                                                                                                                           
%dir %{_datadir}/locale/l10n/bm                                                                                                                           
%dir %{_datadir}/locale/l10n/bn                                                                                                                           
%dir %{_datadir}/locale/l10n/bo                                                                                                                           
%dir %{_datadir}/locale/l10n/br                                                                                                                           
%dir %{_datadir}/locale/l10n/bs                                                                                                                           
%dir %{_datadir}/locale/l10n/bt                                                                                                                           
%dir %{_datadir}/locale/l10n/bw                                                                                                                           
%dir %{_datadir}/locale/l10n/by                                                                                                                           
%dir %{_datadir}/locale/l10n/bz                                                                                                                           
%dir %{_datadir}/locale/l10n/ca                                                                                                                           
%dir %{_datadir}/locale/l10n/cc                                                                                                                           
%dir %{_datadir}/locale/l10n/cd                                                                                                                           
%dir %{_datadir}/locale/l10n/cf                                                                                                                           
%dir %{_datadir}/locale/l10n/cg                                                                                                                           
%dir %{_datadir}/locale/l10n/ch                                                                                                                           
%dir %{_datadir}/locale/l10n/ci                                                                                                                           
%dir %{_datadir}/locale/l10n/ck                                                                                                                           
%dir %{_datadir}/locale/l10n/cl                                                                                                                           
%dir %{_datadir}/locale/l10n/cm                                                                                                                           
%dir %{_datadir}/locale/l10n/cn                                                                                                                           
%dir %{_datadir}/locale/l10n/co                                                                                                                           
%dir %{_datadir}/locale/l10n/cr                                                                                                                           
%dir %{_datadir}/locale/l10n/cu                                                                                                                           
%dir %{_datadir}/locale/l10n/cv                                                                                                                           
%dir %{_datadir}/locale/l10n/cx                                                                                                                           
%dir %{_datadir}/locale/l10n/cy                                                                                                                           
%dir %{_datadir}/locale/l10n/cz                                                                                                                           
%dir %{_datadir}/locale/l10n/de                                                                                                                           
%dir %{_datadir}/locale/l10n/dj                                                                                                                           
%dir %{_datadir}/locale/l10n/dk                                                                                                                           
%dir %{_datadir}/locale/l10n/dm                                                                                                                           
%dir %{_datadir}/locale/l10n/do                                                                                                                           
%dir %{_datadir}/locale/l10n/dz                                                                                                                           
%dir %{_datadir}/locale/l10n/ec                                                                                                                           
%dir %{_datadir}/locale/l10n/ee                                                                                                                           
%dir %{_datadir}/locale/l10n/eg                                                                                                                           
%dir %{_datadir}/locale/l10n/eh                                                                                                                           
%dir %{_datadir}/locale/l10n/er                                                                                                                           
%dir %{_datadir}/locale/l10n/es                                                                                                                           
%dir %{_datadir}/locale/l10n/et                                                                                                                           
%dir %{_datadir}/locale/l10n/fi                                                                                                                           
%dir %{_datadir}/locale/l10n/fj                                                                                                                           
%dir %{_datadir}/locale/l10n/fk                                                                                                                           
%dir %{_datadir}/locale/l10n/fm                                                                                                                           
%dir %{_datadir}/locale/l10n/fo                                                                                                                           
%dir %{_datadir}/locale/l10n/fr                                                                                                                           
%dir %{_datadir}/locale/l10n/ga                                                                                                                           
%dir %{_datadir}/locale/l10n/gb                                                                                                                           
%dir %{_datadir}/locale/l10n/gd                                                                                                                           
%dir %{_datadir}/locale/l10n/ge                                                                                                                           
%dir %{_datadir}/locale/l10n/gh                                                                                                                           
%dir %{_datadir}/locale/l10n/gi                                                                                                                           
%dir %{_datadir}/locale/l10n/gl                                                                                                                           
%dir %{_datadir}/locale/l10n/gm                                                                                                                           
%dir %{_datadir}/locale/l10n/gn                                                                                                                           
%dir %{_datadir}/locale/l10n/gp                                                                                                                           
%dir %{_datadir}/locale/l10n/gq                                                                                                                           
%dir %{_datadir}/locale/l10n/gr                                                                                                                           
%dir %{_datadir}/locale/l10n/gt                                                                                                                           
%dir %{_datadir}/locale/l10n/gu                                                                                                                           
%dir %{_datadir}/locale/l10n/gw                                                                                                                           
%dir %{_datadir}/locale/l10n/gy                                                                                                                           
%dir %{_datadir}/locale/l10n/hk                                                                                                                           
%dir %{_datadir}/locale/l10n/hn                                                                                                                           
%dir %{_datadir}/locale/l10n/hr                                                                                                                           
%dir %{_datadir}/locale/l10n/ht                                                                                                                           
%dir %{_datadir}/locale/l10n/hu                                                                                                                           
%dir %{_datadir}/locale/l10n/id                                                                                                                           
%dir %{_datadir}/locale/l10n/ie                                                                                                                           
%dir %{_datadir}/locale/l10n/il                                                                                                                           
%dir %{_datadir}/locale/l10n/in                                                                                                                           
%dir %{_datadir}/locale/l10n/iq                                                                                                                           
%dir %{_datadir}/locale/l10n/ir                                                                                                                           
%dir %{_datadir}/locale/l10n/is                                                                                                                           
%dir %{_datadir}/locale/l10n/it                                                                                                                           
%dir %{_datadir}/locale/l10n/jm                                                                                                                           
%dir %{_datadir}/locale/l10n/jo                                                                                                                           
%dir %{_datadir}/locale/l10n/jp                                                                                                                           
%dir %{_datadir}/locale/l10n/ke                                                                                                                           
%dir %{_datadir}/locale/l10n/kg                                                                                                                           
%dir %{_datadir}/locale/l10n/kh                                                                                                                           
%dir %{_datadir}/locale/l10n/ki                                                                                                                           
%dir %{_datadir}/locale/l10n/km                                                                                                                           
%dir %{_datadir}/locale/l10n/kn                                                                                                                           
%dir %{_datadir}/locale/l10n/kp                                                                                                                           
%dir %{_datadir}/locale/l10n/kr                                                                                                                           
%dir %{_datadir}/locale/l10n/kw                                                                                                                           
%dir %{_datadir}/locale/l10n/ky                                                                                                                           
%dir %{_datadir}/locale/l10n/kz                                                                                                                           
%dir %{_datadir}/locale/l10n/la                                                                                                                           
%dir %{_datadir}/locale/l10n/lb                                                                                                                           
%dir %{_datadir}/locale/l10n/lc                                                                                                                           
%dir %{_datadir}/locale/l10n/li                                                                                                                           
%dir %{_datadir}/locale/l10n/lk                                                                                                                           
%dir %{_datadir}/locale/l10n/lr                                                                                                                           
%dir %{_datadir}/locale/l10n/ls                                                                                                                           
%dir %{_datadir}/locale/l10n/lt                                                                                                                           
%dir %{_datadir}/locale/l10n/lu                                                                                                                           
%dir %{_datadir}/locale/l10n/lv                                                                                                                           
%dir %{_datadir}/locale/l10n/ly                                                                                                                           
%dir %{_datadir}/locale/l10n/ma                                                                                                                           
%dir %{_datadir}/locale/l10n/mc                                                                                                                           
%dir %{_datadir}/locale/l10n/md                                                                                                                           
%dir %{_datadir}/locale/l10n/me                                                                                                                           
%dir %{_datadir}/locale/l10n/mg                                                                                                                           
%dir %{_datadir}/locale/l10n/mh                                                                                                                           
%dir %{_datadir}/locale/l10n/mk                                                                                                                           
%dir %{_datadir}/locale/l10n/ml                                                                                                                           
%dir %{_datadir}/locale/l10n/mm                                                                                                                           
%dir %{_datadir}/locale/l10n/mn                                                                                                                           
%dir %{_datadir}/locale/l10n/mo                                                                                                                           
%dir %{_datadir}/locale/l10n/mq                                                                                                                           
%dir %{_datadir}/locale/l10n/mr                                                                                                                           
%dir %{_datadir}/locale/l10n/ms                                                                                                                           
%dir %{_datadir}/locale/l10n/mt                                                                                                                           
%dir %{_datadir}/locale/l10n/mu                                                                                                                           
%dir %{_datadir}/locale/l10n/mv                                                                                                                           
%dir %{_datadir}/locale/l10n/mw                                                                                                                           
%dir %{_datadir}/locale/l10n/mx                                                                                                                           
%dir %{_datadir}/locale/l10n/my                                                                                                                           
%dir %{_datadir}/locale/l10n/mz                                                                                                                           
%dir %{_datadir}/locale/l10n/na                                                                                                                           
%dir %{_datadir}/locale/l10n/nc                                                                                                                           
%dir %{_datadir}/locale/l10n/ne                                                                                                                           
%dir %{_datadir}/locale/l10n/nf                                                                                                                           
%dir %{_datadir}/locale/l10n/ng                                                                                                                           
%dir %{_datadir}/locale/l10n/ni                                                                                                                           
%dir %{_datadir}/locale/l10n/nl                                                                                                                           
%dir %{_datadir}/locale/l10n/no                                                                                                                           
%dir %{_datadir}/locale/l10n/np                                                                                                                           
%dir %{_datadir}/locale/l10n/nr                                                                                                                           
%dir %{_datadir}/locale/l10n/nu                                                                                                                           
%dir %{_datadir}/locale/l10n/nz                                                                                                                           
%dir %{_datadir}/locale/l10n/om                                                                                                                           
%dir %{_datadir}/locale/l10n/pa                                                                                                                           
%dir %{_datadir}/locale/l10n/pe                                                                                                                           
%dir %{_datadir}/locale/l10n/pf                                                                                                                           
%dir %{_datadir}/locale/l10n/pg                                                                                                                           
%dir %{_datadir}/locale/l10n/ph                                                                                                                           
%dir %{_datadir}/locale/l10n/pk                                                                                                                           
%dir %{_datadir}/locale/l10n/pl                                                                                                                           
%dir %{_datadir}/locale/l10n/pm                                                                                                                           
%dir %{_datadir}/locale/l10n/pn                                                                                                                           
%dir %{_datadir}/locale/l10n/pr                                                                                                                           
%dir %{_datadir}/locale/l10n/ps                                                                                                                           
%dir %{_datadir}/locale/l10n/pt                                                                                                                           
%dir %{_datadir}/locale/l10n/pw                                                                                                                           
%dir %{_datadir}/locale/l10n/py                                                                                                                           
%dir %{_datadir}/locale/l10n/qa                                                                                                                           
%dir %{_datadir}/locale/l10n/ro                                                                                                                           
%dir %{_datadir}/locale/l10n/rs                                                                                                                           
%dir %{_datadir}/locale/l10n/ru                                                                                                                           
%dir %{_datadir}/locale/l10n/rw
%dir %{_datadir}/locale/l10n/sa
%dir %{_datadir}/locale/l10n/sb
%dir %{_datadir}/locale/l10n/sc
%dir %{_datadir}/locale/l10n/sd
%dir %{_datadir}/locale/l10n/se
%dir %{_datadir}/locale/l10n/sg
%dir %{_datadir}/locale/l10n/sh
%dir %{_datadir}/locale/l10n/si
%dir %{_datadir}/locale/l10n/sk
%dir %{_datadir}/locale/l10n/sl
%dir %{_datadir}/locale/l10n/sm
%dir %{_datadir}/locale/l10n/sn
%dir %{_datadir}/locale/l10n/so
%dir %{_datadir}/locale/l10n/sr
%dir %{_datadir}/locale/l10n/st
%dir %{_datadir}/locale/l10n/sv
%dir %{_datadir}/locale/l10n/sy
%dir %{_datadir}/locale/l10n/sz
%dir %{_datadir}/locale/l10n/tc
%dir %{_datadir}/locale/l10n/td
%dir %{_datadir}/locale/l10n/tg
%dir %{_datadir}/locale/l10n/th
%dir %{_datadir}/locale/l10n/tj
%dir %{_datadir}/locale/l10n/tk
%dir %{_datadir}/locale/l10n/tl
%dir %{_datadir}/locale/l10n/tm
%dir %{_datadir}/locale/l10n/tn
%dir %{_datadir}/locale/l10n/to
%dir %{_datadir}/locale/l10n/tp
%dir %{_datadir}/locale/l10n/tr
%dir %{_datadir}/locale/l10n/tt
%dir %{_datadir}/locale/l10n/tv
%dir %{_datadir}/locale/l10n/tw
%dir %{_datadir}/locale/l10n/tz
%dir %{_datadir}/locale/l10n/ua
%dir %{_datadir}/locale/l10n/ug
%dir %{_datadir}/locale/l10n/us
%dir %{_datadir}/locale/l10n/uy
%dir %{_datadir}/locale/l10n/uz
%dir %{_datadir}/locale/l10n/va
%dir %{_datadir}/locale/l10n/vc
%dir %{_datadir}/locale/l10n/ve
%dir %{_datadir}/locale/l10n/vg
%dir %{_datadir}/locale/l10n/vi
%dir %{_datadir}/locale/l10n/vn
%dir %{_datadir}/locale/l10n/vu
%dir %{_datadir}/locale/l10n/wf
%dir %{_datadir}/locale/l10n/ws
%dir %{_datadir}/locale/l10n/ye
%dir %{_datadir}/locale/l10n/za
%dir %{_datadir}/locale/l10n/zm
%dir %{_datadir}/locale/l10n/zw
%{_datadir}/locale/en_US/entry.desktop
%{_datadir}/locale/l10n/*.desktop
%{_datadir}/locale/l10n/*/*.*
%{_datadir}/sounds/*.*
