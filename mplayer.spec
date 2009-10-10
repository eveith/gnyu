Name: mplayer
Version: 1.0rc1
Release: 1ev
Summary: A multimedia player
URL: http://www.mplayerhq.hu/
Group: Applications/Multimedia
License: GPL-2
Vendor: MSP Slackware
Source0: http://www.mplayerhq.hu/MPlayer/releases/MPlayer-%{version}.tar.bz2
Source1: http://www.mplayerhq.hu/MPlayer/skins/Blue-1.7.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, gtk2, samba-libs, libavcodec
BuildRequires: xvidcore, libogg, libvorbis, libtheora, freetype, fontconfig
BuildRequires: libjpeg, libpng, zlib, x264, libfame, alsa-lib
Requires: gtk2
Obsoletes: gmplayer

%description
MPlayer is a movie player which runs on many systems (see the documentation).
It plays most MPEG/VOB, AVI, Ogg/OGM, VIVO, ASF/WMA/WMV, QT/MOV/MP4,
RealMedia, Matroska, NUT, NuppelVideo, FLI, YUV4MPEG, FILM, RoQ, PVA files,
supported by many native, XAnim, and Win32 DLL codecs. You can watch VideoCD,
SVCD, DVD, 3ivx, DivX 3/4/5 and even WMV movies.
Another great feature of MPlayer is the wide range of supported output
drivers. It works with X11, Xv, DGA, OpenGL, SVGAlib, fbdev, AAlib, DirectFB,
but you can use GGI, SDL (and this way all their drivers), VESA (on every VESA
compatible card, even without X11!) and some low level card-specific drivers
(for Matrox, 3Dfx and ATI), too! Most of them support software or hardware
scaling, so you can enjoy movies in fullscreen. MPlayer supports displaying
through some hardware MPEG decoder boards, such as the Siemens DVB, DXR2 and
DXR3/Hollywood+.
MPlayer has an onscreen display (OSD) for status information, nice big
antialiased shaded subtitles and visual feedback for keyboard controls.
European/ISO 8859-1,2 (Hungarian, English, Czech, etc), Cyrillic and Korean
fonts are supported along with 12 subtitle formats (MicroDVD, SubRip, OGM,
SubViewer, Sami, VPlayer, RT, SSA, AQTitle, JACOsub, PJS and our own: MPsub).
DVD subtitles (SPU streams, VOBsub and Closed Captions) are supported as well.


%prep
%setup -q -c -a0 -a1


%build
pushd "MPlayer-%{version}"
./configure \
	--prefix="%{_prefix}" \
	--bindir="%{_bindir}" \
	--datadir="%{_datadir}/mplayer" \
	--mandir="%{_mandir}" \
	--confdir=/etc/mplayer \
	--libdir="%{_libdir}" \
	--enable-mencoder \
	--enable-gui \
	--enable-largefiles \
	--disable-linux-devfs \
	--disable-termcap \
	--disable-termios \
	--disable-lirc \
	--disable-lircc \
	--disable-joystick \
	--enable-vm \
	--enable-xf86keysym \
	--disable-radio \
	--disable-radio-capture \
	--disable-radio-v4l2 \
	--disable-tv \
	--disable-tv-v4l1 \
	--disable-tv-v4l2 \
	--disable-tv-bsdbt848 \
	--disable-pvr \
	--disable-rtc \
	--enable-network \
	--disable-winsock2 \
	--enable-smb \
	--disable-live \
	--disable-dvdnav \
	--enable-dvdread \
	--disable-mpdvdkit \
	--enable-cdparanoia \
	--enable-bitmap-font \
	--enable-freetype \
	--enable-unrarlib \
	--disable-menu \
	--enable-sortsub \
	--disable-fribidi \
	--disable-enca \
	--disable-macosx \
	--disable-maemo \
	--disable-macosx-finder-support \
	--disable-macosx-bundle \
	--enable-inet6 \
	--enable-gethostbyname2 \
	--enable-ftp \
	--disable-vstream \
	--enable-pthreads \
	--enable-ass \
	--disable-rpath \
	--disable-gif \
	--enable-png \
	--enable-jpeg \
	--disable-libcdio \
	--disable-liblzo \
	--enable-win32 \
	--enable-qtx \
	--enable-xanim \
	--enable-real \
	--enable-xvid \
	--disable-x264 \
	--disable-nut \
	--enable-libavutil \
	--enable-libavcodec \
	--enable-libavformat \
	--enable-libpostproc \
	--enable-libavutil_so \
	--enable-libavcodec_so \
	--enable-libavformat_so \
	--enable-libpostproc_so \
	--enable-libavcodec_mpegaudio_hp \
	--disable-libfame \
	--enable-tremor-internal \
	--disable-tremor-low \
	--disable-tremor-external \
	--enable-libvorbis \
	--disable-speex \
	--enable-theora \
	--disable-faad-external \
	--enable-faad-internal \
	--disable-faac \
	--disable-ladspa \
	--disable-libdv \
	--enable-mad \
	--disable-toolame \
	--disable-twolame \
	--disable-xmms \
	--enable-mp3lib \
	--enable-liba52 \
	--disable-libdts \
	--enable-libmpeg2 \
	--disable-musepack \
	--enable-gl \
	--disable-sdl \
	--disable-aa \
	--disable-caca \
	--disable-ggi \
	--disable-ggiwmh \
	--disable-directx \
	--disable-dxr2 \
	--disable-dxr3 \
	--disable-ivtv \
	--disable-dvdnav \
	--disable-dvdread \
	--disable-xmga \
	--enable-xv \
	--enable-xvmc \
	--enable-vm \
	--enable-xinerama \
	--enable-x11 \
	--disable-fbdev \
	--disable-mlib \
	--disable-3dfx \
	--disable-tdfxfb \
	--disable-s3fb \
	--disable-directfb \
	--disable-zr \
	--disable-bl \
	--disable-tdfxvid \
	--disable-tga \
	--enable-md5sum \
	--enable-pnm \
	--enable-alsa \
	--disable-ossaudio \
	--disable-arts \
	--disable-esd \
	--disable-polyp \
	--disable-jack \
	--disable-openal \
	--disable-nas \
	--disable-sgiaudio \
	--disable-win32waveout \
	--disable-select \
	--enable-runtime-cpudetection \
	--enable-cross-compile \
	--cc="%{_target_platform}-gcc" \
	--target="%{_target}" \
	--with-extraincdir="%{_includedir}/cdda" \
	--with-win32libdir="%{_libdir}/win32" \
	--with-xanimlibdir="%{_libdir}/xanim" \
	--with-reallibdir="%{_libdir}/real"
# (After --enable-freetype) --enable-fontconfig \
make %{_smp_mflags}
popd


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"

pushd "MPlayer-%{version}"
make install DESTDIR="$RPM_BUILD_ROOT"
popd

# Create and touch some extra dirs and files for the package

pushd "$RPM_BUILD_ROOT"
mkdir -p etc/mplayer ./%{_datadir}/mplayer/skins
touch etc/mplayer/mplayer.conf
popd

# Install standard skin

cp -r Blue "${RPM_BUILD_ROOT}/%{_datadir}/mplayer/skins"
pushd "${RPM_BUILD_ROOT}/%{_datadir}/mplayer/skins"
ln -sf Blue default
popd


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc "MPlayer-%{version}/AUTHORS" "MPlayer-%{version}/ChangeLog" 
%doc "MPlayer-%{version}/Copyright" "MPlayer-%{version}/DOCS"
%doc "MPlayer-%{version}/LICENSE" "MPlayer-%{version}/README"
%dir /etc/mplayer
%ghost %config(noreplace) /etc/mplayer/mplayer.conf
%{_bindir}/mplayer
%{_bindir}/gmplayer
%{_bindir}/mencoder
%{_libdir}/libdha.*
%{_libdir}/mplayer/
%{_mandir}/man1/mencoder.1*
%{_mandir}/man1/mplayer.1*
%{_datadir}/pixmaps/mplayer.xpm
%{_datadir}/applications/mplayer.desktop
%dir %{_datadir}/mplayer
%{_datadir}/mplayer/skins
