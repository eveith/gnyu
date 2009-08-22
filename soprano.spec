Name: soprano
Version: 2.3.0
Release: 3ev
Summary: An interface library between Qt 4 and RDF storage solutions
URL: http://soprano.sourceforge.net/
Group: System Environment/Libraries
License: GPL-2
Vendor: GNyU-Linux
Source: http://downloads.sourceforge.net/soprano/soprano-%{version}.tar.bz2
BuildRequires: cmake >= 2.6.2, pkg-config, make, gcc-g++
BuildRequires: qt4 >= 4.4.0, dbus
BuildRequires: redland >= 1.0.5, clucene-core >= 0.9.19

%description
Soprano (formally known as QRDF) is a library which provides a nice Qt
interface to RDF storage solutions. It has a modular structure which
allows to  replace the actual RDF storage implementation used.
Soprano has the following features:
* Full context (i.e. named graph) support
* Plugin structure for extensibility.
* Backend plugins for:
  - Redland
  - Sesame2
* Parser and serializer plugins for:
  - raptor (rdf+xml, turtle, trig, nTriples)
  - nQuads
* A server and client lib which allows a simple remote
  Soprano server.
* SPARQL http enpoint support
* Simple sopranod server application.
* Simple command line tool to perform commands on models in
  a Soprano server (sopranocmd)
* Rule-based Forward inference engine.
* Full-text index based on CLucene which indexes all literal
  statements (i.e. those statements with a literal object node)
* Hierarchical architecture which allows to stack multiple filter models
  on top of an RDF storage.


%prep
%setup -q


%build
%{cmake} \
	-DQT_QMAKE_EXECUTABLE:FILEPATH='%{_libdir}/qt4/bin/qmake' \
	.
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
%doc AUTHORS ChangeLog COPYING* README TODO
%{_bindir}/onto2vocabularyclass
%{_bindir}/sopranocmd
%{_bindir}/sopranod
%dir %{_includedir}/Soprano
%{_includedir}/Soprano/*
%dir %{_includedir}/soprano
%{_includedir}/soprano/*
%{_libdir}/libsoprano.*
%{_libdir}/libsopranoclient.*
%{_libdir}/libsopranoindex.*
%{_libdir}/libsopranoserver.*
%dir %{_libdir}/soprano
%{_libdir}/soprano/*.so
%{_libdir}/pkgconfig/soprano.pc
%{_datadir}/dbus-1/interfaces/org.soprano.Model.xml
%{_datadir}/dbus-1/interfaces/org.soprano.NodeIterator.xml
%{_datadir}/dbus-1/interfaces/org.soprano.QueryResultIterator.xml
%{_datadir}/dbus-1/interfaces/org.soprano.Server.xml
%{_datadir}/dbus-1/interfaces/org.soprano.StatementIterator.xml
%dir %{_datadir}/soprano
%{_datadir}/soprano/*
%{_datadir}/apps/cmake/modules/SopranoAddOntology.cmake
