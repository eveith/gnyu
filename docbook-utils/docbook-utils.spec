Name: docbook-utils
Version: 0.6.14
Release: 1ev
Summary: Shell scripts for managing DocBook documents
URL: ftp://sources.redhat.com/pub/docbook-tools/new-trials/
Group: Applications/Text
License: GPL
Vendor: MSP Slackware
Source0: ftp://sources.redhat.com/pub/docbook-tols/new-trials/SOURCES/%{name}-%{version}.tar.gz
Source1: db2html
Source2: gdp-both.dsl
Patch0: docbook-utils-spaces.patch
Buildroot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch
BuildRequires: perl-SGMLSpm, openjade, docbook-style-dsssl
Requires: docbook-style-dsssl >= 1.72, docbook-dtds, perl-SGMLSpm >= 1.03ii,
Requires: which, perl
Obsoletes: stylesheets
Provides: stylesheets

%description
This package contains scripts are for easy conversion from DocBook
files to other formats (for example, HTML, RTF, and PostScript), and
for comparing SGML files.


%package pdf
Summary: A script for converting DocBook documents to PDF format.
URL: ftp://sources.redhat.com/pub/docbook-tools/new-trials/
Group: Applications/Text
Requires: jadetex >= 2.5
Requires: docbook-utils = %{version}
Requires: tetex-dvips
Obsoletes: stylesheets-db2pdf
Provides: stylesheets-db2pdf

%description pdf
This package contains a script for converting DocBook documents to
PDF format.


%prep
%setup -q
%patch0 -p1 -b .spaces


%build
%configure
%{__make}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__mkdir_p} %{buildroot}/{%{_bindir},%{_mandir}/man1,/tmp}
%{__make_install} \
	DESTDIR='%{buildroot}' \
	prefix='%{_prefix}' \
	mandir='%{_mandir}' \
	docdir=/tmp

pushd '%{buildroot}/%{_bindir}'
for util in dvi html pdf ps rtf
do
	%{__ln_s} "docbook2${util}" "db2${util}"
done
popd

pushd '%{buildroot}/%{_mandir}/man1'
for util in dvi html pdf ps rtf
do
	%{__ln_s} jw.1.gz "db2${util}.1.gz"
done
popd

# db2html is not just a symlink, as it has to create the output directory
%{__rm} -f '%{buildroot}/%{_bindir}/db2html'
%{__install} -c -m 0755 %{SOURCE1} '%{buildroot}/%{_bindir}/db2html'
%{__install} -c -m 0644 %{SOURCE2} \
	'%{buildroot}/%{_datadir}/sgml/docbook/utils-%{version}/docbook-utils.dsl'

%{__rm} -rf '%{buildroot}/tmp'


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc README COPYING TODO
%{_bindir}/jw
%{_bindir}/docbook2html
%{_bindir}/docbook2man
%{_bindir}/docbook2rtf
%{_bindir}/docbook2tex
%{_bindir}/docbook2texi
%{_bindir}/docbook2txt
%{_bindir}/db2html
%{_bindir}/db2rtf
%{_bindir}/sgmldiff
%{_datadir}/sgml/docbook/utils-%{version}
%{_mandir}/*/db2dvi.*
%{_mandir}/*/db2html.*
%{_mandir}/*/db2ps.*
%{_mandir}/*/db2rtf.*
%{_mandir}/*/docbook2html.*
%{_mandir}/*/docbook2rtf.*
%{_mandir}/*/docbook2man.*
%{_mandir}/*/docbook2tex.*
%{_mandir}/*/docbook2texi.*
%{_mandir}/*/jw.*
%{_mandir}/*/sgmldiff.*
%{_mandir}/*/*-spec.*

%files pdf
%defattr (-,root,root)
%{_bindir}/docbook2pdf
%{_bindir}/docbook2dvi
%{_bindir}/docbook2ps
%{_bindir}/db2dvi
%{_bindir}/db2pdf
%{_bindir}/db2ps
%{_mandir}/*/db2pdf.*
%{_mandir}/*/docbook2pdf.*
%{_mandir}/*/docbook2dvi.*
%{_mandir}/*/docbook2ps.*
