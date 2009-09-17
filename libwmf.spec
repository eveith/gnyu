Name: libwmf
Version: 0.2.8.4
Release: 1ev
Summary: A library to read and write WMF files
URL: http://wvware.sourceforge.net/
Group: System Environment/Libraries
License: LGPL
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: http://downloads.sourceforge.net/wvware/libwmf-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc-core, expat, libjpeg, gtk2, freetype >= 2.0.0
BuildRequires: zlib, ghostscript
Requires: expat, libjpeg, gtk2, freetype >= 2.0.0, zlib, ghostscript
Provides: libtool(%{_libdir}/libwmflite.la), libtool(%{_libdir}/libwmf.la)
Provides: libtool(%{_libdir}/gtk-2.0/2.10.0/loaders/io-wmf.la)

%description
libwmf is a library to convert Microsoft's WMF (Windows Metafile) format to
something useful. Bindings exist to convert them to onscreen X graphics, to
the png format, and to fig and eps.


%prep
%setup -q


%build
%configure
make


%install
make install DESTDIR="$RPM_BUILD_ROOT" 
rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir

# Remove not correctly installed docs

rm -rf ${RPM_BUILD_ROOT}/%{_datadir}/doc


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-, root, root)
%doc AUTHORS COPYING CREDITS ChangeLog* README NEWS TODO
%doc doc/*.html doc/*.png doc/html/
%{_bindir}/libwmf-config
%{_bindir}/wmf2eps
%{_bindir}/wmf2fig
%{_bindir}/wmf2svg
%{_bindir}/wmf2gd
%{_bindir}/wmf2x
%{_bindir}/libwmf-fontmap
%{_includedir}/libwmf/
%{_libdir}/libwmf*.*
%{_libdir}/gtk-2.0/2.10.0/loaders/io-wmf.*
%{_datadir}/libwmf/
