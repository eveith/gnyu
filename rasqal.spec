Name: rasqal
Version: 0.9.16
Release: 2ev
Summary: A library for executing RDF queries
URL: http://www.librdf.org/rasqal
Group: System Environment/Libraries
License: LGPL-2.1/Apache-2.0
Vendor: GNyU-Linux
Source: http://download.librdf.org/source/rasqal-%{version}.tar.gz
BuildRequires: pkg-config, make, gcc, flex >= 2.5.33, bison >= 1.28, perl
BuildRequires: raptor >= 1.4.17
BuildRequires: libxml2 >= 2.6.8, pcre >= 3.9, gmp

%description
Rasqal is a free software / Open Source C library that handles Resource
Description Framework (RDF) query syntaxes, query construction and
query execution returning result bindings. The supported query
languages are SPARQL and RDQL.

Rasqal was designed to work closely with the Redland RDF library but is
entirely separate.


%prep
%setup -q


%build
%configure \
	--with-redland=internal
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog* COPYING* LICENSE.txt NEWS NOTICE README
%dir %{_datadir}/gtk-doc/html/rasqal
%doc %{_datadir}/gtk-doc/html/rasqal/*
%{_bindir}/rasqal-config
%{_bindir}/roqet
%{_includedir}/rasqal
%{_libdir}/librasqal.*
%{_libdir}/pkgconfig/rasqal.pc
%doc %{_mandir}/man1/rasqal-config.1*
%doc %{_mandir}/man1/roqet.1*
%doc %{_mandir}/man3/librasqal.3*
