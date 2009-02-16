Name: x264
Version: 20090213
%define rev 2245
Release: 2ev
Summary: A library for de- or encoding H.264 video
URL: http://www.videolan.org/developers/x264.html
Group: System Environment/Libraries
License: GPL-2
Vendor: GNyU-Linux
Source: ftp://ftp.videolan.org/pub/videolan/x264/snapshots/x264-snapshot-%{version}-%{rev}.tar.bz2
BuildRequires: make, gcc, pkg-config
Requires: pkg-config

%description
x264 is a free software library for encoding H.264/MPEG-4 AVC video streams.
Written from scratch by Loren Merritt, Laurent Aimar, Eric Petit, Min Chen,
Justin Clay, Måns Rullgård, Radek Czyz, Alex Izvorski, Alex Wright, and
Christian Heine, it is released under the terms of the GNU General Public
License.


%prep
%setup -q -n 'x264-snapshot-%{version}-%{rev}'


%build
./configure \
	--disable-asm \
	--enable-shared \
	--extra-cflags="${CFLAGS:-%{optflags}} -O4" \
	--host="%{_target_platform}"
%{__make} %{?_smp_mflags} CC="${CC:-%{_target_platform}-gcc}"


%install
%{__make} install \
	DESTDIR='%{buildroot}' \
	bindir='%{_bindir}' \
	libdir='%{_libdir}' \
	includedir='%{_includedir}'


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc AUTHORS COPYING
%{_bindir}/x264
%{_includedir}/x264.h
%{_libdir}/libx264*.*
%{_libdir}/pkgconfig/x264.pc
