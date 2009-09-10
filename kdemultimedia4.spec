name: kdemultimedia4
Version: 4.3.1
Release: 5ev
Summary: Multimedia applications for KDE 4
URL: http://www.kde.org/
Group: User Interface/Desktops
License: GPL-2, LGPL-2.1, FDL-1.2
Vendor: GNyU-Linux
Source: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdemultimedia-%{version}.tar.bz2
BuildRequires: cmake >= 2.6.2, make, flex, bison, gcc-g++, perl, gettext
BuildRequires: libX11, libSM, libICE, libXrender, libXt, libxkbfile, libxcb
BuildRequires: qt4 >= 4.5.0, automoc4 >= 0.9.88, phonon >= 4.3.0
BuildRequires: kdelibs4 = %{version}, kdelibs4-experimental = %{version}
BuildRequires: alsa-lib, xine-lib, taglib >= 1.5, libvorbis, libogg, libflac
BuildRequires: cdparanoia
Obsoletes: kdemultimedia < %{version}

%description
This package contains various multimedia-related applications for KDE 4. More
specificly:
   * dragonplayer: Video Player is a very simple Phonon-based media player.
   * kmix: the audio mixer as a standalone program and Kicker applet
   * kscd: A CD player with an interface to the internet CDDB database
The following are libraries and plugins that are building the core
infrastructure of above applications:
   * strigi-analyzer: provide meta information about sound files
   * libkcddb: a library for retrieving and sending cddb information


%prep
	%setup -q -n 'kdemultimedia-%{version}'


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
	%doc AUTHORS README COPYING*
	%doc %{_datadir}/doc/HTML/en/*
	%config %{_sysconfdir}/kde4/dragonplayerrc
	%{_bindir}/dragon
	%{_bindir}/juk
	%{_bindir}/kmix
	%{_bindir}/kmixctrl
	%{_bindir}/mplayerthumbsconfig
	%{_includedir}/audiocdencoder.h
	%{_includedir}/libkcddb/
	%{_includedir}/libkcompactdisc/
	%{_libdir}/kde4/dragonpart.so
	%{_libdir}/kde4/kcm_*.so
	%{_libdir}/kde4/kio_audiocd.so
	%{_libdir}/kde4/libaudiocd_encoder_flac.so
	%{_libdir}/kde4/libaudiocd_encoder_lame.so
	%{_libdir}/kde4/libaudiocd_encoder_vorbis.so
	%{_libdir}/kde4/libaudiocd_encoder_wav.so
	%{_libdir}/kde4/videopreview.so
	%{_libdir}/libaudiocdplugins.so*
	%{_libdir}/libkcddb.so*
	%{_libdir}/libkcompactdisc.so*
	%{_libdir}/libkdeinit4_kmix*.so
	%{_datadir}/applications/kde4/*.desktop
	%dir %{_datadir}/apps/dragonplayer
	%{_datadir}/apps/dragonplayer/*.*
	%dir %{_datadir}/apps/juk
	%{_datadir}/apps/juk/*rc
	%dir %{_datadir}/apps/juk/pics
	%{_datadir}/apps/juk/pics/*.png
	%{_datadir}/apps/kconf_update/*.*
	%dir %{_datadir}/apps/kmix
	%{_datadir}/apps/kmix/kmixui.rc
	%dir %{_datadir}/apps/kmix/pics
	%{_datadir}/apps/kmix/pics/*.png
	%dir %{_datadir}/apps/kmix/profiles
	%{_datadir}/apps/kmix/profiles/*.xml
	%{_datadir}/apps/konqsidebartng/virtual_folders/services/audiocd.desktop
	%{_datadir}/apps/solid/actions/dragonplayer-opendvd.desktop
	%dir %{_datadir}/apps/videothumbnail
	%{_datadir}/apps/videothumbnail/sprocket-*.png
	%{_datadir}/autostart/*.desktop
	%{_datadir}/config.kcfg/*.kcfg
	%{_datadir}/dbus-1/interfaces/org.kde.*.xml
	%{_datadir}/icons/*/*/*/*.*
	%{_datadir}/kde4/services/*.*
	%{_datadir}/kde4/services/ServiceMenus/*.desktop
