Name: libflac
Version: 1.2.1
Release: 2ev
Summary: Cross-Platform Audio Output Library: Free Lossless Audio Codec
URL: http://www.vorbis.com/
Group: System Environment/Libraries
License: GPL
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: http://downloads.xiph.org/releases/flac/flac-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc, gcc-g++, nasm >= 0.98.30, pkg-config
BuildRequires: libogg >= 1.1.2
Requires: pkg-config

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
