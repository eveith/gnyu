Name: libsdl
Version: 1.2.13
Release: 1ev
Summary: A library that gives portable low-level access for multimedia apps
URL: http://www.libsdl.org/
Group: System Environment/Libraries
License: LGPL-2
Vendor: GNyU-Linux
Source: http://www.libsdl.org/release/SDL-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: coreutils, grep, sed, make, gcc, alsa-lib, pth, svgalib
BuildRequires: pkg-config

%description
SDL is a library that allows you portable low-level access to a video
framebuffer, audio output, mouse, and keyboard. With SDL, it is easy to write
portable games which run on many different platforms.


%prep
%setup -q -n 'SDL-%{version}'


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
%{__make} %{?_smp_mflags}	


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc README* BUGS Borland* COPYING CREDITS TODO VisualC* Watcom*
%{_bindir}/sdl-config
%{_libdir}/libSDL*.*
%{_libdir}/pkgconfig/sdl.pc
%{_includedir}/SDL/
%doc %{_mandir}/*/*.*
%{_datadir}/aclocal/sdl.m4
