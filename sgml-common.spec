Name: sgml-common
Version: 0.6.3
Release: 3ev
Summary: Base ISO character entities and utilities for SGML and XML
URL: ftp://sources.redhat.com/pub/docbook-tools/
Group: Applications/Text 
License: Distributable
Vendor: GNyU-Linux
Source: ftp://sources.redhat.com/pub/docbook-tools/new-trials/SOURCES/%{name}-%{version}.tgz
Patch0: %{name}-automake-manpath-error.patch
BuildRequires: make
Buildarch: noarch

%description
This package includes a set of characters symbolic names
("character entities") used by SGML and XML documents of many types,
very basic utilities to allow manipulation of SGML
"centralized catalogs", and the "SGML declaration" of XML.


%prep
%setup -q
%patch0 -p1


%build
%{__aclocal}
%{__automake} --add-missing
%{__autoconf}
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install install-man DESTDIR='%{buildroot}'
%{__touch} %{buildroot}/%{_sysconfdir}/sgml/{sgml-ent,sgml-docbook}.cat


%post
if [[ "${1}" -eq 1 ]]
then
	install-catalog --add '%{_sysconfdir}/sgml/sgml-ent.cat' \
		'%{_datadir}/sgml/sgml-iso-entities-8879.1986/catalog'
	install-catalog --add '%{_sysconfdir}/sgml/sgml-docbook.cat' \
		'%{_sysconfdir}/sgml/sgml-ent.cat'
fi


%preun
if [[ "${1}" -eq 0 ]]
then
	install-catalog --remove '%{_sysconfdir}/sgml/sgml-ent.cat' \
		'%{_datadir}/sgml/sgml-iso-entities-8879.1986/catalog'
	install-catalog --remove '%{_sysconfdir}/sgml/sgml-docbook.cat' \
		'%{_sysconfdir}/sgml/sgml-ent.cat'
fi


%files
%defattr(-, root, root)
%doc %{_docdir}/%{name}-%{version}
%config %{_sysconfdir}/sgml/sgml.conf
%ghost %config %{_sysconfdir}/sgml/sgml-ent.cat
%ghost %config %{_sysconfdir}/sgml/sgml-docbook.cat
%{_bindir}/install-catalog
%{_bindir}/sgmlwhich
%doc %{_mandir}/man8/install-catalog.8*
%{_datadir}/sgml/*
