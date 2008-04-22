Name: xine-lib
Version: 1.1.12
Release: 2ev
Summary: A audio and video decoder and playback library
URL: http://www.xinehq.de/
Group: System Environment/Libraries
License: GPL-2, LGPL-2
Vendor: GNyU-Linux
Source: http://prdownloads.sourceforge.net/xine/%{name}-%{version}.tar.bz2
Patch0: %{name}-1.1.1-deepbind-939.patch
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, gcc-g++, libogg, libvorbis, alsa-lib, zlib, freetype
BuildRequires: libflac, samba-libs, libmng, mesalib, libtheora, fontconfig
BuildRequires: gawk, sed, libX11, libXext

%description
xine is a free (gpl-licensed) high-performance, portable and reusable
multimedia playback engine. xine itself is a shared library with an easy to
use, yet powerful API which is used by many applications for smooth video
playback and video processing purposes.


%prep
%setup -q
%patch0 -p1


%build
%configure \
	--disable-mlib \
	--enable-ipv6 \
	--enable-opengl \
	--disable-xshm \
	--enable-xv \
	--disable-aalib \
	--disable-macosx-video \
	--disable-coreaudio \
	--disable-directfb \
	--disable-oss \
	--disable-artstest \
	--disable-gnomevfs \
	--disable-gdkpixbuf \
	--enable-mmap \
	--enable-antialiasing \
	--enable-w32dll \
	--with-x \
	--without-caca \
	--without-sdl \
	--without-pulseaudio \
	--without-dxheaders \
	--with-vorbis \
	--with-theora \
	--without-speex \
	--with-libflac \
	--without-imagemagick \
	--with-freetype \
	--with-fontconfig \
	--with-alsa \
	--without-esound \
	--without-fusionsound \
	--without-jack \
	--with-w32-path='%{_libdir}/win32'
%{__make} %{?_smp_mflags}
	


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%{__mkdir_p} '%{buildroot}/%{_libdir}/win32'
%find_lang libxine1


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files -f libxine1.lang
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS COPYING* CREDITS ChangeLog NEWS README TODO doc
%doc %{_datadir}/doc/xine-lib
# %doc %{_datadir}/doc/xine
%{_bindir}/xine-config
%{_bindir}/xine-list-1.1
%{_libdir}/libxine.*
%{_libdir}/xine/
%{_libdir}/pkgconfig/libxine.pc
%{_mandir}/*/xine*.*
%{_datadir}/aclocal/xine.m4
%{_datadir}/xine/
%{_includedir}/xine.h
%{_includedir}/xine/
%dir %{_libdir}/win32
