Name: asciidoc
Version: 8.4.5
Release: 1ev
Summary: A presentable text document format
URL: http://www.methods.co.nz/asciidoc/
Group: Applications/Markup
License: GPL-2
Vendor: GNyU-Linux
Source: http://sourceforge.net/projects/asciidoc/files/%{name}/%{name}-%{version}.tar.gz
BuildRequires: make, python >= 2.5.2
BuildArch: noarch
Requires: python >= 2.5.2

%description
AsciiDoc is a text document format for writing short documents, articles,
books and UNIX man pages. AsciiDoc files can be translated to HTML and DocBook
markups using the asciidoc(1) command.
AsciiDoc is highly configurable: both the AsciiDoc source file syntax and the
backend output markups (which can be almost any type of SGML/XML markup) can
be customized and extended by the user.


%prep
	%setup -q


%build
	%configure
	%{__make} %{?_smp_mflags}


%install
	%{__make} install DESTDIR='%{buildroot}'

	[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
		&& %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%files
	%defattr(-, root, root)
	%doc README* BUGS* CHANGELOG* COPYING COPYRIGHT
	%dir %{_sysconfdir}/asciidoc
	%config %{_sysconfdir}/asciidoc/*.conf
	%{_sysconfdir}/asciidoc/dblatex/
	%{_sysconfdir}/asciidoc/docbook-xsl/
	%{_sysconfdir}/asciidoc/filters/
	%{_sysconfdir}/asciidoc/images/
	%{_sysconfdir}/asciidoc/javascripts/
	%{_sysconfdir}/asciidoc/stylesheets/
	%{_bindir}/asciidoc.py
	%{_bindir}/asciidoc
	%{_bindir}/a2x
	%doc %{_mandir}/man1/a2x.1*
	%doc %{_mandir}/man1/asciidoc.1*
