Name: libgsf
Version: 1.14.3
Release: 1ev
Summary: Read and write OLE and Zip files.
URL: ftp://ftp.gnome.org/pub/GNOME/sources/libgsf/
Group: System Environment/Libraries
License: LGPL
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: ftp://ftp.gnome.org/pub/GNOME/sources/libgsf/1.14/libgsf-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc-core
BuildRequires: glib2, zlib >= 1.1.3, libxml2 >= 2.4.16
Requires: glib2, zlib >= 1.1.3, libxml2 >= 2.4.16
Provides: libtool(%{_libdir}/libgsf-1.la)

%description
The GNOME Structured File Library is a utility library for reading and writing
structured file formats. Support for MS OLE2 streams is complete, as is zip
import. There is also support for document metadata and some initial work on
decompressing VBA streams in OLE files for future conversion to other
languages. This library replaces libole2 and is used in gnumeric, mrproject,
abiword, libwv2, koffice. It is also part of the AAF format.


%prep
%setup -q


%build
%configure
make


%install
make install DESTDIR="$RPM_BUILD_ROOT"
rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir

%find_lang libgsf


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
rm -rf ${RPM_BUILD_ROOT}


%files -f libgsf.lang
%defattr(-, root, root)
%doc AUTHORS BUGS COPYING* HACKING NEWS README TODO
%doc %{_datadir}/gtk-doc/html/gsf/
%{_bindir}/gsf
%{_bindir}/gsf-vba-dump
%{_includedir}/libgsf-1/
%{_libdir}/libgsf-1.*
%{_libdir}/pkgconfig/libgsf-1.pc
%{_mandir}/man1/gsf-office-thumbnailer.1.gz
