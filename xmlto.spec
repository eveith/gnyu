Name: xmlto
Version: 0.0.22
Release: 1ev
Summary: Converts Docbook or XML-FO into other formats (HTML, man, PDF, ...)
URL: https://fedorahosted.org/xmlto/
Group: Applications/Markup
License: GPL-2
Vendor: GNyU-Linux
Source: https://fedorahosted.org/releases/x/m/xmlto/xmlto-%{version}.tar.bz2
BuildRequires: make, flex, libxml2, libxslt, gcc
BuildRequires: docbook-xml >= 4.2, docbook-xsl

%description
xmlto is a front-end to an XSL toolchain. It chooses an appropriate stylesheet
for the conversion you want and applies it using an external XSL-T processor.
It also performs any necessary post-processing


%prep
	%setup -q


%build
	%configure 
	%{__make}


%install
	%{__make} install DESTDIR='%{buildroot}'


%files
	%defattr(-, root, root)
	%doc README AUTHORS ChangeLog COPYING NEWS THANKS
	%{_bindir}/xmlif
	%{_bindir}/xmlto
	%doc %{_mandir}/man1/xmlif.1*
	%doc %{_mandir}/man1/xmlto.1*
	%dir %{_datadir}/xmlto
	%dir %{_datadir}/xmlto/format
	%dir %{_datadir}/xmlto/format/docbook
	%dir %{_datadir}/xmlto/format/fo
	%dir %{_datadir}/xmlto/format/xhtml1
	%{_datadir}/xmlto/xmlto.mak
	%{_datadir}/xmlto/format/*/*
