Name: doxygen
Version: 1.5.1
Release: 1ev
Summary: A documentation system for programing languages
URL: http://www.doxygen.org/
Group: Development/Tools
License: GPL
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: ftp://ftp.stack.nl/pub/users/dimitri/%{name}-%{version}.src.tar.gz
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: perl, make >= 3.79.1, gcc-g++, libstdc++, mktemp, qt3, sed
BuildRequires: flex, bison, graphviz >= 2.8

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
%setup -q -n %{name}-%{version}

# We don't build for windows.
rm -f src/unistd.h


%build
./configure --release --shared --with-doxywizard \
	--prefix %{_prefix} --docdir %{_docdir}
sed -i "s/\(TMAKE_CFLAGS_RELEASE\s*=\s*\).*/\1${RPM_OPT_FLAGS}/" \
	tmake/lib/*/tmake.conf
make
make doc	

%install
make install INSTALL="${RPM_BUILD_ROOT}/%{_prefix}"
rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir


%post

%postun


%clean
rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-, root, root)
%doc LICENSE LANGUAGE* README* VERSION PLATFORMS 
%{_bindir}/doxygen
%{_bindir}/doxytag
%{_bindir}/doxywizard
%{_mandir}/man1/doxygen.1*
%{_mandir}/man1/doxytag.1*
%{_mandir}/man1/doxywizard.1*
