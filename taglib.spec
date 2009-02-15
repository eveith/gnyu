Name: taglib
Version: 1.4
Release: 1ev
Summary: An audio meta data (tag) reading and modification library.
URL: http://developer.kde.org/~wheeler/taglib/
Group: System Environment/Libraries
License: LGPL
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: http://developer.kde.org/~wheeler/files/src/taglib-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc-g++
Provides: libtool(%{_libdir}/libtag.la), libtool(%{_libdir}/libtag_c.la)

%description
TagLib is a library for reading and editing the meta data of several popular
audio formats. It supports both ID3v1 and ID3v2 for MP3 files, Ogg Vorbis
comments and ID3 tags, and Vorbis comments in FLAC files.


%prep
%setup -q


%build
%configure \
	--disable-debug --disable-warnings --enable-final --enable-pch
make


%install
make install DESTDIR="$RPM_BUILD_ROOT"
rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-, root, root)
%doc README AUTHORS COPYING ChangeLog TODO
%{_bindir}/taglib-config
%{_includedir}/taglib/
%{_libdir}/libtag.*
%{_libdir}/libtag_c.*
%{_libdir}/pkgconfig/taglib.pc
