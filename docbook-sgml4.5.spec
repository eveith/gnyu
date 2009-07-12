Name: docbook-sgml4.5
Version: 4.5
Release: 1ev
Summary: Document Type Definitions for Docbook SGML
URL: http://www.docbook.org/
Group: Applications/Text
License: Distributable
Vendor: GNyU-Linux
Source: http://www.docbook.org/sgml/%{version}/docbook-%{version}.zip
BuildArch: noarch
Provides: docbook-sgml = %{version}
Requires(pre): sgml-common
Requires(post): sgml-common

%description
The DocBook SGML DTD package contains document type definitions for
verification of SGML data files against the DocBook rule set. These are useful
for structuring books and software documentation to a standard allowing you to
utilize transformations already written for that standard.


%prep
	%setup -q -c
	%{__sed} -i -e '/ISO 8879/d' -e '/gml/d' 'docbook.cat'


%build
	exit 0


%install
	%{__install} -v -d '%{buildroot}/%{_datadir}/sgml/docbook/sgml-dtd-4.5'
	%{__install} -v 'docbook.cat' \
		'%{buildroot}/%{_datadir}/sgml/docbook/sgml-dtd-4.5/catalog'
	%{__cp} -v -af *.dtd *.mod *.dcl \
		'%{buildroot}/%{_datadir}/sgml/docbook/sgml-dtd-4.5'
	%{__cat} >> '%{buildroot}/%{_datadir}/sgml/docbook/sgml-dtd-4.5/catalog' << "EOF"
  -- Begin Single Major Version catalog changes --

PUBLIC "-//OASIS//DTD DocBook V4.4//EN" "docbook.dtd"
PUBLIC "-//OASIS//DTD DocBook V4.3//EN" "docbook.dtd"
PUBLIC "-//OASIS//DTD DocBook V4.2//EN" "docbook.dtd"
PUBLIC "-//OASIS//DTD DocBook V4.1//EN" "docbook.dtd"
PUBLIC "-//OASIS//DTD DocBook V4.0//EN" "docbook.dtd"

  -- End Single Major Version catalog changes --
EOF


%post
if [[ "${1}" -eq 1 ]]
then
	install-catalog --add '%{_sysconfdir}/sgml/sgml-docbook-dtd-4.5.cat' \
		'%{_datadir}/sgml/docbook/sgml-dtd-4.5/catalog'
	install-catalog --add '%{_sysconfdir}/sgml/sgml-docbook-dtd-4.5.cat' \
		'%{_sysconfdir}/sgml/sgml-docbook.cat'
fi


%postun
if [[ "${1}" -eq 0 ]]
then
	install-catalog --remove '%{_sysconfdir}/sgml/sgml-docbook-dtd-4.5.cat' \
		'%{_sysconfdir}/sgml/sgml-docbook.cat'
	install-catalog --remove '%{_sysconfdir}/sgml/sgml-docbook-dtd-4.5.cat' \
		'%{_datadir}/sgml/docbook/sgml-dtd-4.5/catalog'
fi


%files
	%defattr(-, root, root)
	%doc README
	%dir %{_datadir}/sgml/docbook/sgml-dtd-4.5
	%{_datadir}/sgml/docbook/sgml-dtd-4.5/catalog
	%{_datadir}/sgml/docbook/sgml-dtd-4.5/*.dtd
	%{_datadir}/sgml/docbook/sgml-dtd-4.5/*.mod
	%{_datadir}/sgml/docbook/sgml-dtd-4.5/*.dcl
