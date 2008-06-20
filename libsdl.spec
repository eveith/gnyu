Name: libsdl
Version: 1.2.12
Release: 1ev
Summary: A library that gives portable low-level access for multimedia applications
URL: http://www.libsdl.org/
Group: System Environment/Libraries
License: LGPL
Vendor: MSP Slackware
Source: http://www.libsdl.org/release/SDL-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, alsa-lib, pth, svgalib
Requires: alsa-libs, pth

%description
SDL is a library that allows you portable low-level access to a video
framebuffer, audio output, mouse, and keyboard. With SDL, it is easy to write
portable games which run on many different platforms.


%prep
%setup -q -n SDL-%{version}


%build
%configure \
	--enable-libc \
	--enable-audio \
	--enable-video \
	--enable-events \
	--enable-joystick \
	--enable-cdrom \
	--enable-threads \
	--enable-timers \
	--enable-files \
	--enable-loadso \
	--enable-cpuinfo \
	--enable-assembly \
	--disable-oss \
	--enable-alsa \
	--enable-alsa-shared \
	--disable-esd \
	--disable-pulseaudio \
	--disable-arts \
	--disable-nas \
	--enable-diskaudio \
	--enable-dummyaudio \
	--disable-mintaudio \
	--disable-ipod \
	--disable-video-photon \
	--disable-video-carbon \
	--disable-video-cocoa \
	--disable-video-ps2gs \
	--disable-video-aalib \
	--disable-video-qtopia \
	--enable-input-events \
	--disable-input-tslib \
	--enable-pth \
	--enable-pthreads \
	--enable-sdl-dlopen \
	--disable-atari-ldg
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
%doc README* BUGS Borland* COPYING CREDITS TODO VisualC* Watcom*
%{_bindir}/sdl-config
%{_libdir}/libSDL*.*
%{_libdir}/pkgconfig/sdl.pc
%{_includedir}/SDL/
%{_mandir}/*/*.*
%{_datadir}/aclocal/sdl.m4
