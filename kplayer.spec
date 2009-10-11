Name: kplayer
Version: 0.6.3
Release: 1ev
Summary: A KDE frontend to MPlayer
URL: http://kplayer.sourceforge.net/
Group: Applications/Multimedia
License: GPL-2
Vendor: MSP Slackware
Source: http://downloads.sourceforge.net/kplayer/kplayer-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: gcc-core, gcc-g++, make, qt3, kdelibs, kdebase, mplayer
BuildRequires: autoconf, automake
BuildRequires: libSM, libICE, libX11, libXau, libXcursor, libXdmcp, libXext
Requires: kdelibs, kdebase, mplayer

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


%build
make -f Makefile.dist
%configure \
	--disable-debug \
	--disable-warnings \
	--enable-final
make %{_smp_mflags}


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"
%find_lang kplayer
[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files -f kplayer.lang
%defattr(-, root, root)
%doc AUTHORS BUGS COPYING* ChangeLog README TODO
%doc %{_datadir}/doc/HTML/*/kplayer
%{_bindir}/kplayer
%{_libdir}/kde3/libkplayerpart.*
%{_datadir}/applications/kde/kplayer.desktop
%{_datadir}/apps/konqueror/servicemenus/kplayer*.desktop
%{_datadir}/apps/kplayer
%{_datadir}/services/kplayerpart.desktop
%{_datadir}/icons/*color/*/apps/kplayer.png
