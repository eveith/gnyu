Name: perl-XML-Parser
Version: 2.36
Release: 1ev
Summary: A Perl module for parsing XML documents
URL: http://search.cpan.org/~msergeant/XML-Parser-%{version}/Parser.pm
Group: System Environment/Libraries
License: Artistic
Vendor: GNyU-Linux
Source: http://search.cpan.org/CPAN/authors/id/M/MS/MSERGEANT/XML-Parser-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: coreutils, perl, make, gcc, expat
BuildArch: noarch

%description
This module provides ways to parse XML documents. It is built on top of 
XML::Parser::Expat, which is a lower level interface to James Clark's expat 
library (and also included in this package). Each call to one of the parsing 
methods creates a new instance of XML::Parser::Expat which is then used to 
parse the document. Expat options may be provided when the XML::Parser object 
is created. These options are then passed on to the Expat object on each parse 
call. They can also be given as extra arguments to the parse methods, in which 
case they override options given at XML::Parser creation time.


%prep
%setup -q -n XML-Parser-%{version}


%build
%{__perl} Makefile.PL
%{__make} %{?_smp_mflags}
%{__make} test


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__fakeroot} %{__make} install_vendor DESTDIR='%{buildroot}'

%{__rm} -f \
    '%{buildroot}/%{perl_archlib}/perllocal.pod' \
    '%{buildroot}/%{perl_vendorarch}/auto/XML/Parser'/{.packlist,Expat.bs}


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc MANIFEST META.yml README Changes
#%{perl_privlib}/Pod/Simple/DumpAsXML.pm
#%{perl_privlib}/Pod/Simple/XMLOutStream.pm
%{perl_vendorarch}/XML/
%{perl_vendorarch}/auto/XML/
%{_mandir}/man3/XML::Parser*.3pm*
#%{_mandir}/man3/Pod::Simple::DumpAsXML.3pm*
#%{_mandir}/man3/Pod::Simple::XMLOutStream.3pm*
