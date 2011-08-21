Name: augeas
Version: 0.9.0
Release: 1.0
Summary: Programatically changing of configuration files
URL: http://augeas.net
Group: Configuration Management
License: LGPL-2.1
Source: http://augeas.net/download/augeas-%{version}.tar.gz
BuildRequires: grep, sed, make
BuildRequires: gcc
BuildRequires: eglibc-devel


%description
A library for programmatically editing configuration files. Augeas
parses configuration files into a tree structure, which it exposes
through its public API. Changes made through the API are written back
to the initially read files.
The transformation works very hard to preserve comments and formatting
details. It is controlled by ``lens'' definitions that describe the
file format and the transformation into a tree.


%files
%defattr(-, root, root)
%doc AUTHORS COPYING NEWS README
%{_bindir}/augtool
%{_bindir}/augparse
%{_bindir}/fadot

%doc %{_mandir}/man1/augparse.1*
%doc %{_mandir}/man1/augtool.1*


%package devel
Summary: Augeas development files
License: LGPL-2.1
Group: Configuration Management/Development
Requires: %{name} = %{version}-%{release}


%description devel
A library for programmatically editing configuration files. Augeas
parses configuration files into a tree structure, which it exposes
through its public API. Changes made through the API are written back
to the initially read files.
The transformation works very hard to preserve comments and formatting
details. It is controlled by ``lens'' definitions that describe the
file format and the transformation into a tree.
This package contains the files necessary to develop applications that make
use of Augeas, or to compile and link code using it.


%files devel
%defattr(-, root, root)
%doc AUTHORS COPYING HACKING

%{_includedir}/augeas.h
%{_includedir}/fa.h

%{_libdir}/libaugeas.a
%{_libdir}/libaugeas.la
%{_libdir}/libaugeas.so
%{_libdir}/libfa.a
%{_libdir}/libfa.la
%{_libdir}/libfa.so

%{_libdir}/pkgconfig/augeas.pc


%package -n libaugeas0
Summary: Augeas shared library
Group: Configuration Management/Libraries
License: LGPL-2.1


%description -n libaugeas0
A library for programmatically editing configuration files. Augeas
parses configuration files into a tree structure, which it exposes
through its public API. Changes made through the API are written back
to the initially read files.


%files -n libaugeas0
%defattr(-, root, root)
%doc COPYING AUTHORS

%{_libdir}/libaugeas.so.0*
%{_libdir}/libfa.so.1*


%post -n libaugeas0 -p %{__ldconfig}
%postun -n libaugeas0 -p %{__ldconfig}


%package lenses
Summary: Official set of lenses for use by libaugeas0
License: LGPL-2.1
Group: Configuration Mangement
Requires: %{name} = %{version}-%{release}
 

%description lenses
Augeas parses configuration files described in lenses into a tree
structure, which it exposes through its public API. Lenses are the
building blocks of the file <-> tree transformation. The transformation
is controlled by ``lens'' definitions that describe the file format and
mapping of its contents into a tree. This package includes the official
set of lenses.


%files lenses
%defattr(-, root, root)
%dir %{_datadir}/augeas
%dir %{_datadir}/augeas/lenses
%dir %{_datadir}/augeas/lenses/dist
%{_datadir}/augeas/lenses/dist/*.aug


%package lenses-tests
Summary: Tests for official Augeas lenses
License: LGPL-2.1
Group: Configuration Mangement
Requires: %{name} = %{version}-%{release}
Requires: %{name}-lenses = %{version}-%{release}
 

%description lenses-tests
Set of tests for official Augeas lenses. These can be used when
modifying the official lenses, or when creating new ones.


%files lenses-tests
%defattr(-, root, root)
%dir %{_datadir}/augeas/lenses/dist/tests
%{_datadir}/augeas/lenses/dist/tests/*.aug


%package lenses-vim
Summary: Augeas lenses sytanx support for the VIm editor
Group: Editors/Support
License: LGPL-2.1
Requires: vim


%description lenses-vim
Augeas parses configuration files through descriptions stored in so-called
lenses. This package provides supplementary files for the VIm editor for
syntax highlighting and other file-type functions.


%files lenses-vim
%defattr(-, root, root)
%{_datadir}/vim/vimfiles/ftdetect/augeas.vim
%{_datadir}/vim/vimfiles/syntax/augeas.vim


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%check
%{__make} check ||:
