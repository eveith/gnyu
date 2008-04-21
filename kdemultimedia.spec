Name: kdemultimedia
Version: 3.5.6
Release: 1ev
Summary: Various multimedia applications for the KDE desktop
URL: http://www.kde.org/
Group: User Interface/Desktops
License: GPL, Artistic
Vendor: MSP Slackware
Source: http://download.kde.org/stable/%{version}/src/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-g++, qt3 >= 3.3.2, fontconfig, ghostscript, perl
BuildRequires: zlib >= 1.1, libxml2 >= 2.4.8, libxslt >= 1.0.7, mesalib, pcre
BuildRequires: libjpeg, freetype >= 2.0.0, alsa-lib, cdrecord, libXfixes
BuildRequires: cdparanoia, lame, vorbis-tools, libvorbis, libflac >= 1.0.3
BuildRequires: libmad, libaudiofile, taglib, libtheora, libXv, libXext, taglib
BuildRequires: libX11, libXau, libXdmcp, libart, libXxf86dga, libXxf86misc

%description
* noatun: a multimedia player for sound and movies, very extensible due to
          it's plugin interface
* aktion: a player specialiced on movies, needs xanim
* kaudiocreator: CD ripper and audio encoder frontend.
* kaboodle: light media player
* kmid: A standalone and embeddable midi player, includes a karaoke-mode
* kmidi: midi player, can use sound patch files and create a WAV file
* kmix: the audio mixer as a standalone program and Kicker applet
* kscd: A CD player with an interface to the internet CDDB database
* krec: A recording frontend using aRts



%prep
%setup -q


%build
%configure \
	--disable-debug \
	--disable-warnings \
	--enable-final \
	--with-alsa \
	--with-cdparanoia \
	--with-lame \
	--with-taglib \
	--with-audiofile \
	--without-akode \
	--without-musicbrainz \
	--without-gstreamer \
	--with-theora \
	--with-flac \
	--with-kscd-cdda \
	--without-xine \
	--with-extra-includes=%{_includedir}/cdda
make %{_smp_mflags}


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"


[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc README COPYING* 
%doc %{_datadir}/doc/HTML/en/*
/etc/xdg/menus/applications-merged/kde-multimedia-music.menu
%{_bindir}/artsbuilder
%{_bindir}/artscontrol
%{_bindir}/juk
%{_bindir}/kaboodle
%{_bindir}/kaudiocreator
%{_bindir}/kmid
%{_bindir}/kmix
%{_bindir}/kmixctrl
%{_bindir}/krec
%{_bindir}/kscd
%{_bindir}/midisend
%{_bindir}/mpeglibartsplay
%{_bindir}/noatun
%{_bindir}/workman2cddb.pl
%{_bindir}/yaf-cdda
%{_bindir}/yaf-mpgplay
%{_bindir}/yaf-splay
%{_bindir}/yaf-tplay
%{_bindir}/yaf-vorbis
%{_bindir}/yaf-yuv
%{_includedir}/*.h
%{_includedir}/arts/*.h
%{_includedir}/arts/*.idl
%{_includedir}/libkcddb/
%{_includedir}/mpeglib/
%{_includedir}/mpeglib_artsplug/
%{_includedir}/noatun/
%{_libdir}/*.*
%{_libdir}/kde3/*.*
%{_libdir}/mcop/*.mcop*
%{_libdir}/mcop/Arts/*.mcop*
%{_libdir}/mcop/Arts/*/*.mcop*
%{_libdir}/mcop/Noatun/
%{_datadir}/applications/kde/*.desktop
%{_datadir}/apps/artsbuilder/
%{_datadir}/apps/artscontrol/
%{_datadir}/apps/juk/
%{_datadir}/apps/kaboodle/
%{_datadir}/apps/kappfinder/apps/Multimedia/*.desktop
%{_datadir}/apps/kaudiocreator/
%{_datadir}/apps/kconf_update/*
%{_datadir}/apps/kicker/applets/*.desktop
%{_datadir}/apps/kmid/
%{_datadir}/apps/kmix/
%{_datadir}/apps/konqueror/servicemenus/*.desktop
%{_datadir}/apps/krec/
%{_datadir}/apps/kscd/
%{_datadir}/apps/noatun/
%{_datadir}/apps/profiles/
%{_datadir}/icons/*/*/*/*.png
%{_datadir}/icons/*/*/*/*.svgz
%{_datadir}/mimelnk/*/*.desktop
%{_datadir}/services/*.*
%{_datadir}/servicetypes/*.desktop
%{_datadir}/autostart/restore_kmix_volumes.desktop
%{_datadir}/config.kcfg/*.kcfg
%{_datadir}/desktop-directories/kde-multimedia-music.directory
