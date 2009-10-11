Name: kplayer
Version: 0.7
Release: 2ev
Summary: A KDE frontend to MPlayer
URL: http://kplayer.sourceforge.net
Group: Applications/Multimedia
License: GPL-3
Vendor: GNyU-Linux
Source: http://downloads.sourceforge.net/kplayer/kplayer-%{version}.tar.bz2
BuildRequires: cmake >= 2.6.2, pkg-config, make, gcc-g++, perl
BuildRequires: qt4, kdelibs4, kdebase4
BuildRequires: libX11
BuildRequires: mplayer

%description
KPlayer is a KDE multimedia player. With KPlayer you can easily play a wide
variety of video and audio files and streams using a rich and friendly
interface that follows KDE standards. 
Features include:
- video, audio and subtitle playback from file, URL, DVD, VCD, audio CD, TV,
DVB, and KDE I/O Slaves;
- volume, contrast, brightness, hue and saturation controls;
- zooming, full screen and fixed aspect options;
- status and progress display and seeking;
- multimedia library to organize your media files and streams;
- configuration dialog;
- file properties for setting file specific options.


%prep
%setup -q

# Fix link issue against -lx11
%{__sed} -i \
	's:target_link_libraries(kplayerpart :target_link_libraries(kplayerpart \${X11_LIBRARIES} :' \
		kplayer/CMakeLists.txt


%build
%{cmake} .
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR="${RPM_BUILD_ROOT}"
%find_lang kplayer


%files -f kplayer.lang
%defattr(-, root, root)
%doc AUTHORS BUGS COPYING* ChangeLog README TODO
%doc %{_datadir}/doc/HTML/*/*
%{_bindir}/kplayer
%{_libdir}/kde4/libkplayerpart.so
%{_datadir}/applications/kde4/kplayer.desktop
%{_datadir}/apps/konqueror/servicemenus/kplayer-*.desktop
%dir %{_datadir}/apps/kplayer
%{_datadir}/apps/kplayer/COPYING
%{_datadir}/apps/kplayer/input.conf
%{_datadir}/apps/kplayer/*.rc
%dir %{_datadir}/apps/kplayer/icons
%dir %{_datadir}/apps/kplayer/icons/hicolor
%dir %{_datadir}/apps/kplayer/icons/hicolor/*
%dir %{_datadir}/apps/kplayer/icons/hicolor/*/actions
%{_datadir}/apps/kplayer/icons/hicolor/*/actions/*.png
%{_datadir}/icons/hicolor/*/apps/kplayer.png
%{_datadir}/kde4/services/kplayerpart.desktop
