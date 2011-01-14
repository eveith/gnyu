Name: libsdlmixer
Version: 1.2.8
Release: 2ev
Summary: A multichannel sample and music mixer
URL: http://www.libsdl.org/projects/SDL_mixer/
Group: System Environment/Libraries
License: GPL-2
Vendor: GNyU-Linux
Source: http://www.libsdl.org/projects/SDL_mixer/release/SDL_mixer-%{version}.tar.gz
BuildRequires: make, gcc, libsdl >= 1.2.10, libvorbis

%description
SDL_mixer is a sample multi-channel audio mixer library. 
It supports any number of simultaneously playing channels of 16 bit
stereo audio, plus a single channel of music, mixed by the popular
MikMod MOD, Timidity MIDI, Ogg Vorbis, and SMPEG MP3 libraries.


%prep
%setup -q -n 'SDL_mixer-%{version}'


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
%doc CHANGES COPYING README
%{_includedir}/SDL/SDL_mixer.h
%{_libdir}/libSDL_mixer*.*
