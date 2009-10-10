Name: mplayer
Version: 20091010
Release: 2ev
Summary: A multimedia player
URL: http://www.mplayerhq.hu
Group: Applications/Multimedia
License: GPL-2
Vendor: GNyU-Linux
Source0: http://www.mplayerhq.hu/MPlayer/releases/mplayer-checkout-snapshot.tar.bz2
Source1: http://www.mplayerhq.hu/MPlayer/skins/Blue-1.7.tar.bz2
BuildRequires: pkg-config, make, gcc
BuildRequires: samba-libs
BuildRequires: libX11, libXScrnSaver, libXext, libXv, libXvMC
BuildRequires: libXxf86vm, libXxf86dga
BuildRequires: mesalib
BuildRequires: libpng, libmng, zlib, libjpeg, libungif, bzip2
BuildRequires: libsdl >= 1.2.1, alsa-lib >= 1.0.0
BuildRequires: cdparanoia
BuildRequires: freetype >= 2.1.8, fontconfig, fribidi >= 0.10.4
BuildRequires: libmad, libogg, libvorbis, speex >= 1.1, libtheora
BuildRequires: liba52, xvidcore, lame
BuildRequires: gtk2, glib2
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
pushd mplayer-checkout-*
./configure \
	--prefix="%{_prefix}" \
	--bindir="%{_bindir}" \
	--datadir="%{_datadir}/mplayer" \
	--mandir="%{_mandir}" \
	--confdir='%{_sysconfdir}/mplayer' \
	--libdir="%{_libdir}" \
	--enable-mencoder \
	--enable-gui \
	--enable-largefiles \
	--disable-linux-devfs \
	--disable-termcap \
	--disable-termios \
	--disable-arts \
	--disable-esd \
	--disable-jack \
	--disable-openal \
	--disable-nas \
	--disable-sgiaudio \
	--enable-runtime-cpudetection \
	--enable-cross-compile \
	--cc="%{_target_platform}-gcc" \
	--target="%{_target}" \
	--extra-cflags="${CFLAGS:-%{optflags}} -I%{_includedir}/cdda" \
	--win32codecsdir="%{_libdir}/win32" \
	--realcodecsdir="%{_libdir}/real"
%{__make} %{?_smp_mflags}
popd


%install
pushd mplayer-checkout-*
%{__make} install DESTDIR="${RPM_BUILD_ROOT}"
popd

# Create and touch some extra dirs and files for the package
%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/mplayer' \
	'%{buildroot}/%{_datadir}/mplayer/skins'
%{__touch} '%{buildroot}/%{_sysconfdir}/mplayer/mplayer.conf'

# Install standard skin
%{__cp} -r Blue "${RPM_BUILD_ROOT}/%{_datadir}/mplayer/skins"
pushd "${RPM_BUILD_ROOT}/%{_datadir}/mplayer/skins"
%{__ln_s} Blue default
popd


%post
%{__ldconfig}


%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc mplayer-checkout-*/AUTHORS
%doc mplayer-checkout-*/README
%doc mplayer-checkout-*/Changelog
%doc mplayer-checkout-*/DOCS
%doc mplayer-checkout-*/LICENSE
%dir %{_sysconfdir}/mplayer
%ghost %config(noreplace) %{_sysconfdir}/mplayer/mplayer.conf
%{_bindir}/mplayer
%{_bindir}/gmplayer
%{_bindir}/mencoder
%doc %{_mandir}/man1/mencoder.1*
%doc %{_mandir}/man1/mplayer.1*
%{_datadir}/pixmaps/mplayer.xpm
%{_datadir}/applications/mplayer.desktop
%dir %{_datadir}/mplayer
%dir %{_datadir}/mplayer/skins
%{_datadir}/mplayer/skins/default
%{_datadir}/mplayer/skins/Blue/
