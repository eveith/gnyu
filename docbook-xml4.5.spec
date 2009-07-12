Name: docbook-xml4.5
Version: 4.5
Release: 2ev
Summary: Document Type Definitions for Docbook (XML format)
URL: http://www.docbook.org/
Group: Applications/Text
License: Distributable
Vendor: GNyU-Linux
Source: ftp://ftp.linux.ee/pub/gentoo/distfiles/distfiles/docbook-xml-%{version}.zip
BuildArch: noarch
Requires: libxml2
Provides: docbook-xml = %{version}

%description
The DocBook XML DTD-4.5 package contains document type definitions for
verification of XML data files against the DocBook rule set. These are useful
for structuring books and software documentation to a standard allowing you to
utilize transformations already written for that standard.


%prep
	%setup -q -c


%build
	exit 0


%install
	%{__install} -v -d -m 0755 \
		'%{buildroot}/%{_datadir}/xml/docbook/xml-dtd-4.5'
	%{__cp} -v -af 'docbook.cat' *.dtd ent/ *.mod \
		'%{buildroot}/%{_datadir}/xml/docbook/xml-dtd-4.5'


%post
if [[ "${1}" -eq 1 ]]
then
	if [[ ! -e '%{_sysconfdir}/xml/docbook' ]]
	then
		xmlcatalog --noout --create '%{_sysconfdir}/xml/docbook'
	fi
	xmlcatalog --noout --add "public" \
		"-//OASIS//DTD DocBook XML V4.5//EN" \
		"http://www.oasis-open.org/docbook/xml/4.5/docbookx.dtd" \
		%{_sysconfdir}/xml/docbook
	xmlcatalog --noout --add "public" \
		"-//OASIS//DTD DocBook XML CALS Table Model V4.5//EN" \
		"file://%{_datadir}/xml/docbook/xml-dtd-4.5/calstblx.dtd" \
		%{_sysconfdir}/xml/docbook
	xmlcatalog --noout --add "public" \
		"-//OASIS//DTD XML Exchange Table Model 19990315//EN" \
		"file://%{_datadir}/xml/docbook/xml-dtd-4.5/soextblx.dtd" \
		%{_sysconfdir}/xml/docbook
	xmlcatalog --noout --add "public" \
		"-//OASIS//ELEMENTS DocBook XML Information Pool V4.5//EN" \
		"file://%{_datadir}/xml/docbook/xml-dtd-4.5/dbpoolx.mod" \
		%{_sysconfdir}/xml/docbook
	xmlcatalog --noout --add "public" \
		"-//OASIS//ELEMENTS DocBook XML Document Hierarchy V4.5//EN" \
		"file://%{_datadir}/xml/docbook/xml-dtd-4.5/dbhierx.mod" \
		%{_sysconfdir}/xml/docbook
	xmlcatalog --noout --add "public" \
		"-//OASIS//ELEMENTS DocBook XML HTML Tables V4.5//EN" \
		"file://%{_datadir}/xml/docbook/xml-dtd-4.5/htmltblx.mod" \
		%{_sysconfdir}/xml/docbook
	xmlcatalog --noout --add "public" \
		"-//OASIS//ENTITIES DocBook XML Notations V4.5//EN" \
		"file://%{_datadir}/xml/docbook/xml-dtd-4.5/dbnotnx.mod" \
		%{_sysconfdir}/xml/docbook
	xmlcatalog --noout --add "public" \
		"-//OASIS//ENTITIES DocBook XML Character Entities V4.5//EN" \
		"file://%{_datadir}/xml/docbook/xml-dtd-4.5/dbcentx.mod" \
		%{_sysconfdir}/xml/docbook
	xmlcatalog --noout --add "public" \
		"-//OASIS//ENTITIES DocBook XML Additional General Entities V4.5//EN" \
		"file://%{_datadir}/xml/docbook/xml-dtd-4.5/dbgenent.mod" \
		%{_sysconfdir}/xml/docbook
	xmlcatalog --noout --add "rewriteSystem" \
		"http://www.oasis-open.org/docbook/xml/4.5" \
		"file://%{_datadir}/xml/docbook/xml-dtd-4.5" \
		%{_sysconfdir}/xml/docbook
	xmlcatalog --noout --add "rewriteURI" \
		"http://www.oasis-open.org/docbook/xml/4.5" \
		"file://%{_datadir}/xml/docbook/xml-dtd-4.5" \
		%{_sysconfdir}/xml/docbook
	xmlcatalog --noout --add "delegatePublic" \
		"-//OASIS//ENTITIES DocBook XML" \
		"file://%{_sysconfdir}/xml/docbook" \
		%{_sysconfdir}/xml/catalog
	xmlcatalog --noout --add "delegatePublic" \
		"-//OASIS//DTD DocBook XML" \
		"file://%{_sysconfdir}/xml/docbook" \
		%{_sysconfdir}/xml/catalog
	xmlcatalog --noout --add "delegateSystem" \
		"http://www.oasis-open.org/docbook/" \
		"file://%{_sysconfdir}/xml/docbook" \
		%{_sysconfdir}/xml/catalog
	xmlcatalog --noout --add "delegateURI" \
		"http://www.oasis-open.org/docbook/" \
		"file://%{_sysconfdir}/xml/docbook" \
		%{_sysconfdir}/xml/catalog

	for DTDVERSION in 4.1.2 4.2 4.3 4.4
	do
	  xmlcatalog --noout --add "public" \
		"-//OASIS//DTD DocBook XML V$DTDVERSION//EN" \
		"http://www.oasis-open.org/docbook/xml/$DTDVERSION/docbookx.dtd" \
		%{_sysconfdir}/xml/docbook
	  xmlcatalog --noout --add "rewriteSystem" \
		"http://www.oasis-open.org/docbook/xml/$DTDVERSION" \
		"file:///usr/share/xml/docbook/xml-dtd-4.5" \
		%{_sysconfdir}/xml/docbook
	  xmlcatalog --noout --add "rewriteURI" \
		"http://www.oasis-open.org/docbook/xml/$DTDVERSION" \
		"file:///usr/share/xml/docbook/xml-dtd-4.5" \
		%{_sysconfdir}/xml/docbook
	  xmlcatalog --noout --add "delegateSystem" \
		"http://www.oasis-open.org/docbook/xml/$DTDVERSION/" \
		"file://%{_sysconfdir}/xml/docbook" \
		%{_sysconfdir}/xml/catalog
	  xmlcatalog --noout --add "delegateURI" \
		"http://www.oasis-open.org/docbook/xml/$DTDVERSION/" \
		"file://%{_sysconfdir}/xml/docbook" \
		%{_sysconfdir}/xml/catalog
	done
fi


%postun
if [[ "${1}" -eq 0 ]]
then
	for DTDVERSION in 4.1.2 4.2 4.3 4.4
	do
	  xmlcatalog --noout --remove "delegateURI" \
		"http://www.oasis-open.org/docbook/xml/$DTDVERSION/" \
		"file://%{_sysconfdir}/xml/docbook" \
		%{_sysconfdir}/xml/catalog
	  xmlcatalog --noout --remove "delegateSystem" \
		"http://www.oasis-open.org/docbook/xml/$DTDVERSION/" \
		"file://%{_sysconfdir}/xml/docbook" \
		%{_sysconfdir}/xml/catalog
	  xmlcatalog --noout --remove "rewriteURI" \
		"http://www.oasis-open.org/docbook/xml/$DTDVERSION" \
		"file:///usr/share/xml/docbook/xml-dtd-4.5" \
		%{_sysconfdir}/xml/docbook
	  xmlcatalog --noout --remove "rewriteSystem" \
		"http://www.oasis-open.org/docbook/xml/$DTDVERSION" \
		"file:///usr/share/xml/docbook/xml-dtd-4.5" \
		%{_sysconfdir}/xml/docbook
	  xmlcatalog --noout --remove "public" \
		"-//OASIS//DTD DocBook XML V$DTDVERSION//EN" \
		"http://www.oasis-open.org/docbook/xml/$DTDVERSION/docbookx.dtd" \
		%{_sysconfdir}/xml/docbook
	done

	xmlcatalog --noout --remove "delegateURI" \
		"http://www.oasis-open.org/docbook/" \
		"file://%{_sysconfdir}/xml/docbook" \
		%{_sysconfdir}/xml/catalog
	xmlcatalog --noout --remove "delegateSystem" \
		"http://www.oasis-open.org/docbook/" \
		"file://%{_sysconfdir}/xml/docbook" \
		%{_sysconfdir}/xml/catalog
	xmlcatalog --noout --remove "delegatePublic" \
		"-//OASIS//DTD DocBook XML" \
		"file://%{_sysconfdir}/xml/docbook" \
		%{_sysconfdir}/xml/catalog
	xmlcatalog --noout --remove "delegatePublic" \
		"-//OASIS//ENTITIES DocBook XML" \
		"file://%{_sysconfdir}/xml/docbook" \
		%{_sysconfdir}/xml/catalog
	xmlcatalog --noout --remove "rewriteURI" \
		"http://www.oasis-open.org/docbook/xml/4.5" \
		"file://%{_datadir}/xml/docbook/xml-dtd-4.5" \
		%{_sysconfdir}/xml/docbook
	xmlcatalog --noout --remove "rewriteSystem" \
		"http://www.oasis-open.org/docbook/xml/4.5" \
		"file://%{_datadir}/xml/docbook/xml-dtd-4.5" \
		%{_sysconfdir}/xml/docbook
	xmlcatalog --noout --remove "public" \
		"-//OASIS//ENTITIES DocBook XML Additional General Entities V4.5//EN" \
		"file://%{_datadir}/xml/docbook/xml-dtd-4.5/dbgenent.mod" \
		%{_sysconfdir}/xml/docbook
	xmlcatalog --noout --remove "public" \
		"-//OASIS//ENTITIES DocBook XML Character Entities V4.5//EN" \
		"file://%{_datadir}/xml/docbook/xml-dtd-4.5/dbcentx.mod" \
		%{_sysconfdir}/xml/docbook
	xmlcatalog --noout --remove "public" \
		"-//OASIS//ENTITIES DocBook XML Notations V4.5//EN" \
		"file://%{_datadir}/xml/docbook/xml-dtd-4.5/dbnotnx.mod" \
		%{_sysconfdir}/xml/docbook
	xmlcatalog --noout --remove "public" \
		"-//OASIS//ELEMENTS DocBook XML HTML Tables V4.5//EN" \
		"file://%{_datadir}/xml/docbook/xml-dtd-4.5/htmltblx.mod" \
		%{_sysconfdir}/xml/docbook
	xmlcatalog --noout --remove "public" \
		"-//OASIS//ELEMENTS DocBook XML Document Hierarchy V4.5//EN" \
		"file://%{_datadir}/xml/docbook/xml-dtd-4.5/dbhierx.mod" \
		%{_sysconfdir}/xml/docbook
	xmlcatalog --noout --remove "public" \
		"-//OASIS//ELEMENTS DocBook XML Information Pool V4.5//EN" \
		"file://%{_datadir}/xml/docbook/xml-dtd-4.5/dbpoolx.mod" \
		%{_sysconfdir}/xml/docbook
	xmlcatalog --noout --remove "public" \
		"-//OASIS//DTD XML Exchange Table Model 19990315//EN" \
		"file://%{_datadir}/xml/docbook/xml-dtd-4.5/soextblx.dtd" \
		%{_sysconfdir}/xml/docbook
	xmlcatalog --noout --remove "public" \
		"-//OASIS//DTD DocBook XML CALS Table Model V4.5//EN" \
		"file://%{_datadir}/xml/docbook/xml-dtd-4.5/calstblx.dtd" \
		%{_sysconfdir}/xml/docbook
	xmlcatalog --noout --remove "public" \
		"-//OASIS//DTD DocBook XML V4.5//EN" \
		"http://www.oasis-open.org/docbook/xml/4.5/docbookx.dtd" \
		%{_sysconfdir}/xml/docbook
fi


%files
	%defattr(-, root, root)
	%dir %{_datadir}/xml/docbook/xml-dtd-4.5
	%{_datadir}/xml/docbook/xml-dtd-4.5/docbook.cat
	%{_datadir}/xml/docbook/xml-dtd-4.5/*.dtd
	%{_datadir}/xml/docbook/xml-dtd-4.5/*.mod
	%{_datadir}/xml/docbook/xml-dtd-4.5/ent/
