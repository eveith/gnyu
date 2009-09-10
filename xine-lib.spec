Name: xine-lib
Version: 1.1.16.3
Release: 4ev
Summary: A audio and video decoder and playback library
URL: http://www.xine-project.org/
Group: System Environment/Libraries
License: GPL-2, LGPL-2
Vendor: GNyU-Linux
Source: http://prdownloads.sourceforge.net/xine/%{name}-%{version}.tar.bz2
BuildRequires: make, gcc, gcc-g++, gettext >= 0.16.1, perl
BuildRequires: libavcodec
BuildRequires: libogg, libvorbis, libtheora, speex, libflac
BuildRequires: libmad, libmng, alsa-lib
BuildRequires: freetype, fontconfig, gtk2
BuildRequires: samba-libs
BuildRequires: zlib, mesalib, libsdl
BuildRequires: libX11, libXext, libXv, libXvMC, libxcb >= 1.0

%description
xine is a free (gpl-licensed) high-performance, portable and reusable
multimedia playback engine. xine itself is a shared library with an easy to
use, yet powerful API which is used by many applications for smooth video
playback and video processing purposes.


%prep
%setup -q


%build
%configure \
	--with-external-ffmpeg \
	--disable-rpath \
	--enable-ipv6 \
	--enable-opengl \
	--disable-xshm \
	--enable-xv \
	--disable-oss \
	--disable-gnomevfs \
	--enable-mmap \
	--enable-antialiasing \
	--enable-w32dll \
	--with-x \
	--with-vorbis \
	--with-theora \
	--with-speex \
	--with-libflac \
	--with-freetype \
	--with-fontconfig \
	--with-alsa \
	--without-arts \
	--without-esound \
	--without-fusionsound \
	--without-jack \
	--with-w32-path='%{_libdir}/win32' \
	--disable-xinerama \
	--with-external-libmad
%{__make} %{?_smp_mflags}
	


%install
%{__make} install DESTDIR='%{buildroot}'
%{__mkdir_p} '%{buildroot}/%{_libdir}/win32'
%find_lang libxine1


%post
%{__ldconfig}


%postun
%{__ldconfig}


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
