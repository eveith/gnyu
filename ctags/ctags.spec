Name: ctags
Version: 5.8
Release: 1.0ev
Summary: Generates an index of language objects found in source code
URL: http://ctags.sourceforge.net
Group: Development/Tools
License: GPL-2
Vendor: GNyU-Linux
Source: http://prdownloads.sourceforge.net/ctags/ctags-%{version}.tar.gz
BuildRequires: make, gcc

%description
Ctags generates an index (or tag) file of language objects found in source
files that allows these items to be quickly and easily located by a text
editor or other utility. A tag signifies a language object for which an index
entry is available (or, alternatively, the index entry created for that
object). 
Tag generation is supported for the following languages: 
Assembler, AWK, ASP, BETA, Bourne/Korn/Zsh Shell, C, C++, COBOL, Eiffel,
Fortran, Java, Lisp, Lua, Make, Pascal, Perl, PHP, Python, REXX, Ruby, S-Lang,
Scheme, Tcl, Vim, and YACC.



%prep
	%setup -q


%build
	%configure
	%{__make} %{?_smp_mflags}


%install
	%{makeinstall} DESTDIR='%{buildroot}'


%files
	%defattr(-, root, root)
	%doc COPYING README MAINTAINERS NEWS FAQ EXTENDING.html
	%{_bindir}/ctags
	%doc %{_mandir}/man1/ctags.1*
