Name: libmatroska
Version: 0.8.1
Release: 2ev
Summary: A C++ library to parse the Matroska audio/video container format
URL: http://www.matroska.org/
Group: System Environment/Libraries
License: LGPL
Vendor: GNyU-Linux
Source: http://dl.matroska.org/downloads/%{name}/%{name}-%{version}.tar.bz2
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
%{__make} %{?_smp_mflags} \
    CXX="${CXX:-%{_target_platform}-g++}" \
    CXXFLAGS="${CXXFLAGS:-%{optflags}}" \
    prefix="%{_prefix}" \
    staticlib sharedlib
popd


%install
pushd 'make/linux'
%{__make} \
    CXX="${CXX:-%{_target_platform}-g++}" \
    CXXFLAGS="${CXXFLAGS:-%{optflags}}" \
    prefix="%{buildroot}/%{_prefix}" \
    install
popd


%post
%{__ldconfig}


%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc LICENSE.LGPL
%dir %{_includedir}/matroska
%{_includedir}/matroska/*.h
%dir %{_includedir}/matroska/c
%{_includedir}/matroska/c/*.h
%{_libdir}/libmatroska.*
