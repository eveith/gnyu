Name: raptor
Version: 1.4.18
Release: 1ev
Summary: A RDF parser library for Redland
URL: http://www.librdf.org/
Group: System Environment/Libraries
License: LGPL-2.1/Apache-2
Vendor: GNyU-Linux
Source: http://download.librdf.org/source/raptor-%{version}.tar.gz
BuildRequires: make, gcc, pkg-config, zlib, libxml2, curl

%description
Raptor is the RDF Parser Toolkit for Redland that provides a set of
Resource Description Framework (RDF) parsers and serializers,
generating RDF triples from the following syntaxes: RDF/XML,
N-Triples, TRiG, Turtle, RSS tag soup including all versions of RSS,
Atom 1.0 and 0.3, GRDDL and microformats for HTML, XHTML and XML. The
serializing RDF triples to syntaxes are: RDF/XML, RSS 1.0, Atom 1.0,
N-Triples, XMP, Turtle, GraphViz DOT and JSON.


%prep
%setup -q


%build
%configure \
	--enable-release
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc README NEWS NOTICE LICENSE*.txt COPYING* AUTHORS ChangeLog*
%{_bindir}/raptor-config
%{_bindir}/rapper
%{_includedir}/raptor.h
%{_libdir}/libraptor.*
%{_libdir}/pkgconfig/raptor.pc
%doc %{_mandir}/man1/raptor-config.1*
%doc %{_mandir}/man1/rapper.1*
%doc %{_mandir}/man3/libraptor.3*
%doc %{_datadir}/gtk-doc/html/raptor/*
