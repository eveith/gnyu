Name: doxygen
Version: 1.6.3
Release: 2.0ev
Summary: A documentation system for programing languages
URL: http://www.doxygen.org
Group: Development/Tools
License: GPL-2
Vendor: GNyU-Linux
Source: ftp://ftp.stack.nl/pub/users/dimitri/%{name}-%{version}.src.tar.gz
BuildRequires: sed, flex, bison, make, perl, python, gcc-g++
BuildRequires: libstdc++, graphviz >= 1.8.10

%description
Doxygen is a cross-platform, JavaDoc-like documentation system for C++, C,
Objective-C, C#, Java, IDL, Python, and PHP. Doxygen can be used to generate
an on-line class browser (in HTML) and/or an off-line reference manual (in
LaTeX or RTF) from a set of source files. Doxygen can also be configured to
extract the code-structure from undocumented source files. This includes
dependency graphs, class diagrams and hyperlinked source code. This type of
information can be very useful to quickly find your way in large source
distributions.


%prep
%setup -q -n '%{name}-%{version}'


%build
CFLAGS=${CFLAGS:-%{optflags}}
CXXFLAGS=${CXXFLAGS:-%{optflags}}
export CFLAGS CXXFLAGS

./configure \
	--release \
	--shared \
	--prefix '%{_prefix}' \
	--docdir '%{_docdir}'
echo "TMAKE_CXXFLAGS += ${CFLAGS}" >> .tmakeconfig
%{__make} %{?_smp_mflags}
%{__make} doc


%install
%{__make} install INSTALL='%{buildroot}%{_prefix}'


%files
%defattr(-, root, root)
%doc LICENSE LANGUAGE* README* VERSION PLATFORMS 
%{_bindir}/doxygen
%{_bindir}/doxytag
%doc %{_mandir}/man1/doxygen.1*
%doc %{_mandir}/man1/doxytag.1*
