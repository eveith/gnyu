Name: libsdl
Version: 1.2.13
Release: 2ev
Summary: A library that gives portable low-level access for multimedia apps
URL: http://www.libsdl.org/
Group: System Environment/Libraries
License: LGPL-2
Vendor: GNyU-Linux
Source: http://www.libsdl.org/release/SDL-%{version}.tar.gz
BuildRequires: make, gcc, alsa-lib >= 0.9.0
BuildRequires: libICE, libSM, libX11, libXext, libXrender, libXrandr
BuildRequires: mesalib, libusb, pth, 
BuildRequires: pkg-config

%description
SDL is a library that allows you portable low-level access to a video
framebuffer, audio output, mouse, and keyboard. With SDL, it is easy to write
portable games which run on many different platforms.


%prep
%setup -q -n 'SDL-%{version}'


%build
%configure \
	--disable-oss \
	--enable-alsa \
	--enable-alsa-shared \
	--disable-esd \
	--disable-arts \
	--disable-nas \
	--disable-mintaudio \
	--disable-ipod \
	--disable-video-photon \
	--disable-video-carbon \
	--disable-video-cocoa \
	--disable-video-svga \
	--disable-video-ps2gs \
	--disable-video-aalib \
	--disable-video-qtopia \
	--disable-input-tslib \
	--enable-sdl-dlopen \
	--disable-atari-ldg \
	--disable-video-x11-xinerama
%{__make} %{?_smp_mflags}	


%install
%{__make} install DESTDIR='%{buildroot}'


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc README* BUGS Borland* COPYING CREDITS TODO VisualC* Watcom*
%{_bindir}/sdl-config
%{_libdir}/libSDL*.*
%{_libdir}/pkgconfig/sdl.pc
%{_includedir}/SDL/
%doc %{_mandir}/*/*.*
%{_datadir}/aclocal/sdl.m4
