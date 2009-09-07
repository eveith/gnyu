Name: libtheora
Version: 1.0alpha7
Release: 1ev
Summary: A video codec that builds upon On2's VP3 codec
URL: http://www.theora.org/
Group: System Environment/Libraries
License: GPL
Vendor: MSP Slackware
Source: http://downloads.xiph.org/releases/theora/%{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, libogg >= 1.1
Requires: libogg >= 1.1

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
make %{_smp_mflags}


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"

[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"
rm -rf "${RPM_BUILD_ROOT}/%{_datadir}/doc/%{name}-%{version}"


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc AUTHORS CHANGES README COPYING LICENSE doc/libtheora
%{_includedir}/theora
%{_libdir}/libtheora*.*
%{_libdir}/pkgconfig/theora.pc
