Name: docbook-xsl
Version: 1.71.1
Release: 1ev
Summary: XSL stylesheets for DocBook
URL: http://www.docbook.org/
Group: Applications/Text
License: Distributable
Vendor: GNyU-Linux
Source: http://downloads.sourceforge.net/docbook/docbook-xsl-%{version}.tar.bz2
BuildArch: noarch
Requires(pre): libxml2
Requires(post): libxml2

%description
The DocBook XSL Stylesheets package contains XSL stylesheets. These are useful
for performing transformations on XML DocBook files.


%prep
	%setup -q


%build
	exit 0

%install
	%{__install} -v -d -m 0755 \
		'%{buildroot}/%{_datadir}/xml/docbook/xsl-stylesheets-%{version}'
	%{__cp} -v -R VERSION common eclipse extensions fo highlighting html \
		     htmlhelp images javahelp lib manpages params profiling \
	         slides template tools website wordml xhtml \
		'%{buildroot}/%{_datadir}/xml/docbook/xsl-stylesheets-%{version}'

%post
if [[ "${1}" -eq 1 ]]
then
	if [[ ! -e '%{_sysconfdir}/xml/catalog' ]]
	then
		xmlcatalog --noout --create '%{_sysconfdir}/xml/catalog'
	fi

	xmlcatalog --noout --add "rewriteSystem" \
			   "http://docbook.sourceforge.net/release/xsl/1.71.1" \
			   "%{_datadir}/xml/docbook/xsl-stylesheets-1.71.1" \
		%{_sysconfdir}/xml/catalog
	xmlcatalog --noout --add "rewriteURI" \
			   "http://docbook.sourceforge.net/release/xsl/1.71.1" \
			   "%{_datadir}/xml/docbook/xsl-stylesheets-1.71.1" \
		%{_sysconfdir}/xml/catalog
	xmlcatalog --noout --add "rewriteSystem" \
			   "http://docbook.sourceforge.net/release/xsl/current" \
			   "%{_datadir}/xml/docbook/xsl-stylesheets-1.71.1" \
		%{_sysconfdir}/xml/catalog
	xmlcatalog --noout --add "rewriteURI" \
			   "http://docbook.sourceforge.net/release/xsl/current" \
			   "%{_datadir}/xml/docbook/xsl-stylesheets-1.71.1" \
		%{_sysconfdir}/xml/catalog
fi


%postun
if [[ "${1}" -eq 0 ]]
then
	xmlcatalog --noout --remove "rewriteURI" \
			   "http://docbook.sourceforge.net/release/xsl/current" \
			   "%{_datadir}/xml/docbook/xsl-stylesheets-1.71.1" \
		%{_sysconfdir}/xml/catalog
	xmlcatalog --noout --remove "rewriteSystem" \
			   "http://docbook.sourceforge.net/release/xsl/current" \
			   "%{_datadir}/xml/docbook/xsl-stylesheets-1.71.1" \
		%{_sysconfdir}/xml/catalog
	xmlcatalog --noout --remove "rewriteURI" \
			   "http://docbook.sourceforge.net/release/xsl/1.71.1" \
			   "%{_datadir}/xml/docbook/xsl-stylesheets-1.71.1" \
		%{_sysconfdir}/xml/catalog
	xmlcatalog --noout --remove "rewriteSystem" \
			   "http://docbook.sourceforge.net/release/xsl/1.71.1" \
			   "%{_datadir}/xml/docbook/xsl-stylesheets-1.71.1" \
		%{_sysconfdir}/xml/catalog
fi


%files
	%defattr(-, root, root)
	%doc README RELEASE-NOTES* NEWS*
	%dir %{_datadir}/xml/docbook/xsl-stylesheets-%{version}
	%{_datadir}/xml/docbook/xsl-stylesheets-%{version}/*
