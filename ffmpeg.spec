Name: ffmpeg
Version: 2009.02.13
Release: 1ev
Summary: A video and audio format decoder and streaming server
URL: http://ffmpeg.mplayerhq.hu
Group: Applications/Multimedia
License: GPL-2, LGPL-2.1
Vendor: GNyU-Linux
Source: ffmpeg-export-snapshot.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make >= 3.81, gcc
BuildRequires lame, libogg, libvorbis, xvidcore, zlib, x264 >= 0.65
Requires: libavcodec

%description
FFmpeg is a collection of software libraries that can record, convert and
stream digital audio and video in numerous formats. It includes libavcodec
(see extra libavcodec package), an audio/video codec library used by several 
other projects, like XINE, and libavformat, an audio/video container mux and 
demux library. The name of the project comes from the MPEG video standards 
group, together with "FF" for "fast forward".


%package -n libavcodec
Version: %{version}
Summary: An audio/video codec library
Group: System Environment/Libraries
License: GPL-2, LGPL-2.1

%description -n libavcodec
libavcodec is a free software/open source LGPL-licensed library of codecs for
encoding and decoding video and audio data; it is written in the C programming
language. It is part of the FFmpeg-project and many free/open source
applications rely on it.


%prep
%setup -q -n 'ffmpeg-export-%(echo %{version} | %{__sed} "s,\.,-,g")'


%build
# TODO: We will later include libfaad, libfaac, libx264 and liba52!
#	--disable-libx264 \
./configure \
	--prefix="%{_prefix}" \
	--libdir="%{_libdir}" \
	--shlibdir="%{_libdir}" \
	--incdir="%{_includedir}" \
	--mandir="%{_mandir}" \
	--enable-shared \
	--enable-static \
	--enable-gpl \
	--enable-nonfree \
	--enable-postproc \
	--enable-swscale \
	--enable-avfilter \
	--enable-avfilter-lavf \
	--enable-pthreads \
	--disable-libfaac \
	--disable-libfaad \
	--enable-libmp3lame \
	--disable-libnut \
	--disable-libtheora \
	--enable-libvorbis \
	--enable-libx264 \
	--enable-libxvid \
	--cc="${CC:-%{_target_platform}-gcc}" \
	--extra-cflags="${CFLAGS:-%{optflags}}" \
	--arch="%{_target_cpu}" 
%{__make} %{_smp_mflags}
	

%install
%{__make} install DESTDIR="${RPM_BUILD_ROOT}"


%post -n libavcodec
%{__ldconfig}

%postun -n libavcodec
%{__ldconfig}


%files
%defattr(-, root, root)
%doc COPYING* Changelog MAINTAINERS README doc CREDITS
%{_bindir}/ffmpeg
%{_bindir}/ffplay
%{_bindir}/ffserver

%files -n libavcodec
%defattr(-, root, root)
%{_includedir}/*.h
%{_includedir}/postproc/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib*.*
%{_libdir}/vhook
