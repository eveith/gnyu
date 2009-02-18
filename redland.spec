Name: redland
Version: 1.0.8
Release: 1ev
Summary: Provides a RDF API and triple stores
URL: http://librdf.org/
Group: System Environment/Libraries
License: LGPL-2.1/Apache-2.0
Vendor: GNyU-Linux
Source: http://download.librdf.org/source/redland-%{version}.tar.gz
BuildRequires: make, gcc, pkg-config, raptor, rasqal, db, openssl, mysql-libs
BuildRequires: sqlite

%description
Redland is a set of free software C libraries that provide support for the 
Resource Description Framework (RDF).
   * Modular, object based libraries and APIs for manipulating the RDF graph,
     triples, URIs and Literals.
   * Storage for graphs in memory and persistently with Sleepycat/Berkeley DB,
     MySQL 3-5, PostgreSQL, AKT Triplestore, SQLite, files or URIs.
   * Support for multiple syntaxes for reading and writing RDF as RDF/XML, 
     N-Triples and Turtle Terse RDF Triple Language, RSS and Atom syntaxes via 
     the Raptor RDF Parser Library.
   * Querying with SPARQL and RDQL using the Rasqal RDF Query Library.
   * Data aggregation and recording provenance support with Redland contexts.
   * Portable, fast and with no known memory leaks.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc README LICENSE*.txt COPYING* AUTHORS ChangeLog NOTICE NEWS TODO
%doc %{_datadir}/gtk-doc/html/redland
%{_bindir}/rdfproc
%{_bindir}/redland-config
%{_bindir}/redland-db-upgrade
%{_includedir}/librdf.h
%{_includedir}/redland.h
%{_includedir}/rdf_*.h
%{_libdir}/librdf.*
%{_libdir}/pkgconfig/redland.pc
%doc %{_mandir}/man1/rdfproc.1*
%doc %{_mandir}/man1/redland-config.1*
%doc %{_mandir}/man1/redland-db-upgrade.1*
%doc %{_mandir}/man3/redland.3*
%dir %{_datadir}/redland
%{_datadir}/redland/Redland.i
%{_datadir}/redland/mysql-v[12].ttl
