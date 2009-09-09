Name: ffmpeg
Version: 20090909
Release: 1ev
Summary: A video and audio format decoder and streaming server
URL: http://ffmpeg.mplayerhq.hu
Group: Applications/Multimedia
License: GPL-2, LGPL-2.1
Vendor: GNyU-Linux
Source: ffmpeg-%{version}.tar.bz2
BuildRequires: make >= 3.81, pkg-config >= 0.9.0, gcc
BuildRequires: zlib, bzip2, libogg, libvorbis, libtheora, speex, xvidcore
BuildRequires: x264, libmatroska, faad2, libsdl, alsa-lib

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
%setup -q


%build
# TODO: We will later include libfaac and liba52!
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
	--enable-avfilter \
	--enable-avfilter-lavf \
	--enable-bzlib \
	--enable-libfaad \
	--enable-libmp3lame \
	--enable-libtheora \
	--enable-libvorbis \
	--enable-libspeex \
	--enable-libx264 \
	--enable-libxvid \
	--enable-zlib \
	--enable-pthreads \
	--cc="${CC:-%{_target_platform}-gcc}" \
	--extra-cflags="${CFLAGS:-%{optflags}}" \
	--arch="%{_target_cpu}" 
%{__make} %{?_smp_mflags}
	

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
%dir %{_datadir}/ffmpeg
%{_datadir}/ffmpeg/libx264*.ffpreset


%files -n libavcodec
%defattr(-, root, root)
%{_includedir}/*/*.h
%dir %{_includedir}/libavcodec
%dir %{_includedir}/libavdevice
%dir %{_includedir}/libavfilter
%dir %{_includedir}/libavformat
%dir %{_includedir}/libavutil
%dir %{_includedir}/libpostproc
%dir %{_includedir}/libswscale
%{_libdir}/libavcodec.*
%{_libdir}/libavdevice.*
%{_libdir}/libavfilter.*
%{_libdir}/libavformat.*
%{_libdir}/libavutil.*
%{_libdir}/libpostproc.*
%{_libdir}/libswscale.*
%{_libdir}/pkgconfig/libavcodec.pc
%{_libdir}/pkgconfig/libavdevice.pc
%{_libdir}/pkgconfig/libavfilter.pc
%{_libdir}/pkgconfig/libavformat.pc
%{_libdir}/pkgconfig/libavutil.pc
%{_libdir}/pkgconfig/libpostproc.pc
%{_libdir}/pkgconfig/libswscale.pc
