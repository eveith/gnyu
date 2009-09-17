Name: libgsf
Version: 1.14.15
Release: 2ev
Summary: Read and write OLE and Zip files
URL: ftp://ftp.gnome.org/pub/GNOME/sources/libgsf
Group: System Environment/Libraries
License: GPL-2
Vendor: GNyU-Linux
Source: ftp://ftp.gnome.org/pub/GNOME/sources/libgsf/1.14/libgsf-%{version}.tar.bz2
BuildRequires: pkg-config >= 0.9.0, make >= 3.79.1, gcc, gettext, intltool
BuildRequires: perl, perl-XML-Parser
BuildRequires: zlib >= 1.1.3, bzip2, glib2

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
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR="${RPM_BUILD_ROOT}"
%find_lang libgsf


%post
%{__ldconfig}


%postun
%{__ldconfig}


%files -f libgsf.lang
%defattr(-, root, root)
%doc AUTHORS BUGS COPYING* HACKING NEWS README TODO
%doc %{_datadir}/gtk-doc/html/gsf/*
%dir %{_datadir}/gtk-doc/html/gsf
%{_bindir}/gsf
%{_bindir}/gsf-vba-dump
%{_includedir}/libgsf-1/
%{_libdir}/libgsf-1.*
%{_libdir}/pkgconfig/libgsf-1.pc
%doc %{_mandir}/man1/gsf-office-thumbnailer.1*
%doc %{_mandir}/man1/gsf-vba-dump.1*
%doc %{_mandir}/man1/gsf.1*
