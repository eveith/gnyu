Name: libflac8
Version: 1.2.1
Release: 2ev
Summary: Cross-Platform Audio Output Library: Free Lossless Audio Codec
URL: http://www.vorbis.com/
Group: System Environment/Libraries
License: LGPL-2.1, GPL-2
Vendor: GNyU-Linux
Source: http://downloads.xiph.org/releases/flac/flac-%{version}.tar.gz
BuildRequires: pkgconfig >= 0.9.0, make, gcc, gcc-g++, nasm >= 0.98.30
BuildRequires: libogg >= 1.1.2, libvorbis
Requires: pkg-config
Provides: libflac = %{version}

%description
Libao is a cross-platform audio output library.  It currently supports
ESD, aRts, ALSA, OSS, *BSD and Solaris.
This package provides plug-ins for OSS, ESD, aRts, and ALSA (0.9).  You will
need to install the supporting libraries for any plug-ins you want to use
in order for them to work.


%prep
%setup -q -n 'flac-%{version}'


%build
%configure \
	--disable-xmms-plugin
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc README AUTHORS COPYING* 
%doc %{_datadir}/doc/flac-%{version}/
%{_bindir}/flac
%{_bindir}/metaflac
%{_includedir}/FLAC++/
%{_includedir}/FLAC/
%{_libdir}/libFLAC++.*
%{_libdir}/libFLAC.*
%{_libdir}/pkgconfig/flac.pc
%{_libdir}/pkgconfig/flac++.pc
%doc %{_mandir}/man1/flac.1*
%doc %{_mandir}/man1/metaflac.1*
%{_datadir}/aclocal/libFLAC++.m4
%{_datadir}/aclocal/libFLAC.m4
