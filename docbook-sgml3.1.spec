Name: docbook-sgml3.1
Version: 3.1
Release: 1ev
Summary: Document Type Definitions for Docbook SGML
URL: http://www.docbook.org/
Group: Applications/Text
License: Distributable
Vendor: GNyU-Linux
Source: http://www.docbook.org/sgml/3.1/docbk31.zip
BuildArch: noarch
Requires(pre): sgml-common
Requires(post): sgml-common

%description
The DocBook SGML DTD package contains document type definitions for
verification of SGML data files against the DocBook rule set. These are useful
for structuring books and software documentation to a standard allowing you to
utilize transformations already written for that standard.


%prep
	%setup -q -c
	%{__sed} -i -e '/ISO 8879/d' \
	    -e 's|DTDDECL "-//OASIS//DTD DocBook V3.1//EN"|SGMLDECL|g' \
	    'docbook.cat'


%build
	exit 0


%install
	%{__install} -v -d -m 0755 \
		'%{buildroot}/%{_datadir}/sgml/docbook/sgml-dtd-3.1'
	%{__install} -v 'docbook.cat' \
		'%{buildroot}/%{_datadir}/sgml/docbook/sgml-dtd-3.1/catalog'
	%{__cp} -v -af *.dtd *.mod *.dcl \
		'%{buildroot}/%{_datadir}/sgml/docbook/sgml-dtd-3.1'
	%{__cat} >> '%{buildroot}/%{_datadir}/sgml/docbook/sgml-dtd-3.1/catalog' << "EOF"
  -- Begin Single Major Version catalog changes --

PUBLIC "-//Davenport//DTD DocBook V3.0//EN" "docbook.dtd"

  -- End Single Major Version catalog changes --
EOF


%post
if [[ "${1}" -eq 1 ]]
then
	install-catalog --add '%{_sysconfdir}/sgml/sgml-docbook-dtd-3.1.cat' \
		'%{_datadir}/sgml/docbook/sgml-dtd-3.1/catalog'
	install-catalog --add '%{_sysconfdir}/sgml/sgml-docbook-dtd-3.1.cat' \
		'%{_sysconfdir}/sgml/sgml-docbook.cat'
fi


%postun
if [[ "${1}" -eq 0 ]]
then
	install-catalog --remove '%{_sysconfdir}/sgml/sgml-docbook-dtd-3.1.cat' \
		'%{_datadir}/sgml/sgml-docbook.cat'
	install-catalog --remove '%{_sysconfdir}/sgml/sgml-docbook-dtd-3.1.cat' \
		'%{_datadir}/sgml/docbook/sgml-dtd-3.1/catalog'
fi


%files
	%defattr(-, root, root)
	%doc ChangeLog *.txt
	%dir %{_datadir}/sgml/docbook/sgml-dtd-3.1
	%{_datadir}/sgml/docbook/sgml-dtd-3.1/catalog
	%{_datadir}/sgml/docbook/sgml-dtd-3.1/*.*
