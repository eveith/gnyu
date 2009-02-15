Name: taglib
Version: 1.5
Release: 2ev
Summary: An audio meta data (tag) reading and modification library
URL: http://developer.kde.org/~wheeler/taglib/
Group: System Environment/Libraries
License: LGPL-2/MPL-1.1
Vendor: GNyU-Linux
Source: http://developer.kde.org/~wheeler/files/src/taglib-%{version}.tar.gz
BuildRequires: make >= 3.79.1, gcc-g++, pkg-config, zlib
Requires: pkg-config

%description
TagLib is a library for reading and editing the meta data of several popular
audio formats. It supports both ID3v1 and ID3v2 for MP3 files, Ogg Vorbis
comments and ID3 tags, and Vorbis comments in FLAC files.


%prep
%setup -q


%build
%configure \
	--disable-debug \
	--disable-warnings
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR="${RPM_BUILD_ROOT}"


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc COPYING* doc/* examples
%{_bindir}/taglib-config
%{_includedir}/taglib/
%{_libdir}/libtag.*
%{_libdir}/libtag_c.*
%{_libdir}/pkgconfig/taglib.pc
%{_libdir}/pkgconfig/taglib_c.pc
