Name: libtheora
Version: 1.0
Epoch: 1
Release: 2ev
Summary: A video codec that builds upon On2's VP3 codec
URL: http://www.theora.org/
Group: System Environment/Libraries
License: BSD
Vendor: GNyU-Linux
Source: http://downloads.xiph.org/releases/theora/%{name}-%{version}.tar.gz
BuildRequires: make, pkg-config, gcc, doxygen
BuildRequires: libogg >= 1.1, libvorbis >= 1.0.1, libsdl >= 0.11.0, libpng

%description
Theora is a video codec being developed by the Xiph.Org Foundation as part of
their Ogg project. Based upon On2 Technologies' VP3 codec, and christened by
On2 as the successor in VP3's lineage, Theora is targeted at competing with
MPEG-4 video (e.g., H.264, Xvid and DivX), RealVideo, Windows Media Video, and
similar lower-bitrate video compression schemes.
While VP3 is patented technology, On2 has irrevocably given royalty-free
license of the VP3 patents to everyone, letting anyone use Theora and other
VP3-derived codecs for any purpose.
In the Ogg multimedia framework, Theora provides a video layer, while Vorbis
usually acts as the audio layer. Speex, FLAC, and OggPCM may also act as audio
layers.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR="${RPM_BUILD_ROOT}"


%post
%{__ldconfig}


%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc AUTHORS CHANGES README COPYING LICENSE doc/libtheora
%{_includedir}/theora
%{_libdir}/libtheora*.*
%{_libdir}/pkgconfig/theora.pc
%{_libdir}/pkgconfig/theoradec.pc
%{_libdir}/pkgconfig/theoraenc.pc
%dir %{_datadir}/doc/%{name}-%{version}
%doc %{_datadir}/doc/%{name}-%{version}/*
