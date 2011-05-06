Name: expat
Version: 2.0.1
Release: 1.0
Summary: An stream-oriented XML parser
URL: http://www.expat.org
Group: Applications/XML
License: BSD
Source: http://sourceforge.net/projects/expat/files/expat/%{version}/expat-%{version}.tar.gz
BuildRequires: grep, sed, make, gcc, gcc-g++
BuildRequires: eglibc-devel, libstdc++-devel

%description
This is Expat, a C library for parsing XML, written by James Clark.
Expat is a stream-oriented XML parser.  This means that you register
handlers with the parser before starting the parse.  These handlers
are called when the parser discovers the associated structures in the
document being parsed.  A start tag is an example of the kind of
structures for which you may register handlers.


%package devel
Summary: Development Headers for Expat
Group: Development/Libraries

%description devel
This is Expat, a C library for parsing XML, written by James Clark.
Expat is a stream-oriented XML parser.  This means that you register
handlers with the parser before starting the parse.  These handlers
are called when the parser discovers the associated structures in the
document being parsed.  A start tag is an example of the kind of
structures for which you may register handlers.


%package -n libexpat1
Summary: A stream-oriented XML parser library
Group: System Environment/Libraries

%description -n libexpat1
This is Expat, a C library for parsing XML, written by James Clark.
Expat is a stream-oriented XML parser.  This means that you register
handlers with the parser before starting the parse.  These handlers
are called when the parser discovers the associated structures in the
document being parsed.  A start tag is an example of the kind of
structures for which you may register handlers.


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
%{__make} check


%post -n libexpat1 -p %{__ldconfig}
%postun -n libexpat1 -p %{__ldconfig}


%files
%defattr(-, root, root)
%doc README COPYING MANIFEST Changes
%{_bindir}/xmlwf
%doc %{_mandir}/man1/xmlwf.1*


%files devel
%defattr(-, root, root)
%doc README COPYING MANIFEST Changes
%doc doc examples
%{_libdir}/libexpat.so
%{_libdir}/libexpat.la
%{_libdir}/libexpat.a
%{_includedir}/expat.h
%{_includedir}/expat_external.h


%files -n libexpat1
%defattr(-, root, root)
%doc README COPYING MANIFEST Changes
%{_libdir}/libexpat.so.1*
