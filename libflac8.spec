Name: libflac
Version: 1.1.2
Release: 1ev
Summary: Cross-Platform Audio Output Library
URL: http://www.vorbis.com/
Group: System Environment/Libraries
License: GPL
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: http://downloads.xiph.org/releases/flac/flac-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc-core, libogg >= 1.1.2, gcc-g++, libtool
BuildRequires: nasm, autoconf
Requires: libogg >= 1.1.2
Provides: libtool(%{_libdir}/libOggFLAC.la) libtool(%{_libdir}/libFLAC++.la)
Provides: libtool(%{_libdir}/libFLAC.la) libtool(%{_libdir}/libOggFLAC.la)

%description
Libao is a cross-platform audio output library.  It currently supports
ESD, aRts, ALSA, OSS, *BSD and Solaris.
This package provides plug-ins for OSS, ESD, aRts, and ALSA (0.9).  You will
need to install the supporting libraries for any plug-ins you want to use
in order for them to work.


%prep
%setup -q -n flac-%{version}


%build
%configure --with-ogg=%{_prefix}
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
%doc README AUTHORS COPYING* 
%doc %{_datadir}/doc/flac-%{version}/
%{_bindir}/flac
%{_bindir}/metaflac
%{_includedir}/FLAC++/
%{_includedir}/FLAC/
%{_includedir}/OggFLAC++/
%{_includedir}/OggFLAC/
%{_libdir}/libFLAC++.*
%{_libdir}/libFLAC.*
%{_libdir}/libOggFLAC++.*
%{_libdir}/libOggFLAC.*
%{_mandir}/man1/flac.1*
%{_mandir}/man1/metaflac.1*
%{_datadir}/aclocal/libFLAC++.m4
%{_datadir}/aclocal/libFLAC.m4
%{_datadir}/aclocal/libOggFLAC++.m4
%{_datadir}/aclocal/libOggFLAC.m4
