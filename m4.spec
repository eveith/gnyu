Name: m4
Version: 1.4.8
Release: 1ev
Summary: The GNU m4 macro processor
URL: http://www.gnu.org/software/m4
Group: Development/Languages
License: GPL
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: ftp://ftp.gnu.org/gnu/m4/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: gcc-core, make >= 3.79.1
Requires: /sbin/install-info

%description
GNU M4 is an implementation of the traditional Unix macro processor. It is
mostly SVR4 compatible although it has some extensions (for example, handling
more than 9 positional parameters to macros). GNU m4 also has built-in
functions for including files, running shell commands, doing arithmetic, etc.
GNU M4 is a macro processor in the sense that it copies its input to the
output expanding macros as it goes. Macros are either builtin or user-defined
and can take any number of arguments. Besides just doing macro expansion m4
has builtin functions for including named files, running UNIX commands, doing
integer arithmetic, manipulating text in various ways, recursion etc... m4 can
be used either as a front-end to a compiler or as a macro processor in its own
right.


%prep
%setup -q


%build
%configure
make


%install
make install DESTDIR="$RPM_BUILD_ROOT"
rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir


%post
/sbin/ldconfig
/sbin/install-info %{_infodir}/m4.info.gz %{_infodir}/dir

%postun
/sbin/ldconfig
/sbin/install-info --delete %{_infodir}/m4.info.gz %{_infodir}/dir


%clean
rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-, root, root)
%doc AUTHORS BACKLOG COPYING ChangeLog* NEWS README THANKS TODO
%{_bindir}/m4
%{_infodir}/m4.info*
%{_mandir}/man1/m4.1*
