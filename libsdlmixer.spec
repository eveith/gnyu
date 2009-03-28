Name: libsdlmixer
Version: 1.2.8
Release: 1ev
Summary: A multichannel sample and music mixer
URL: http://www.libsdl.org/projects/SDL_mixer/
Group: System Environment/Libraries
License: GPL-2
Vendor: MSP Slackware
Source: http://www.libsdl.org/projects/SDL_mixer/release/SDL_mixer-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, libsdl >= 1.2, libvorbis

%description
SDL_mixer is a sample multi-channel audio mixer library. 
It supports any number of simultaneously playing channels of 16 bit
stereo audio, plus a single channel of music, mixed by the popular
MikMod MOD, Timidity MIDI, Ogg Vorbis, and SMPEG MP3 libraries.


%prep
%setup -q -n SDL_mixer-%{version}


%build
%configure \
	--enable-music-ogg
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
%doc CHANGES COPYING README
%{_includedir}/SDL/SDL_mixer.h
%{_libdir}/libSDL_mixer*.*
