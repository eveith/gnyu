Name: libmatroska
Version: 0.8.1
Release: 1ev
Summary: A C++ library to parse the Matroska audio/video container format
URL: http://www.matroska.org/
Group: System Environment/Libraries
License: LGPL
Vendor: MSP Slackware
Source: http://dl.matroska.org/downloads/%{name}/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-g++, libebml

%description
The Matroska Multimedia Container is an open standard free Container format, a
file format that can hold an unlimited number of video, audio, picture or
subtitle tracks inside a single file. It is intended to serve as a
universal format for storing common multimedia content, like movies or TV
shows. Matroska is similar in concept to other containers like AVI, MP4 or
ASF, but is completely open source. Matroska file types are .MKV for video
(and audio) and .MKA for audio-only files respectively.
Matroska is an English word derived from the Russian word Матрёшка
(transliterated as Matryoshka). Which is pronounced as: mat + ros (as in
albatross OR as in metros) + ka (as in Alaska). Simply stated, the term
Matroska means 'nesting doll' (the common eastern European egg shaped doll
within a doll). This is a play on the container (media within a form of
media/Doll Within a Doll) aspect of the Matryoshka as it is a container for
visual and audio data.


%prep
%setup -q


%build
pushd 'make/linux'
make \
    CXX="%{_target_platform}-g++" \
    CXXFLAGS="$RPM_OPT_FLAGS" \
    prefix="%{_prefix}" \
    staticlib sharedlib
popd


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
pushd 'make/linux'
make \
    CXX="%{_target_platform}-gcc" \
    CXXFLAGS="$RPM_OPT_FLAGS" \
    prefix="${RPM_BUILD_ROOT}/%{_prefix}" \
    install
popd

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
%doc LICENSE.LGPL
%{_includedir}/matroska/
%{_libdir}/libmatroska.*
