Name: libxml2 
Version: 2.7.8
Release: 1.0
Summary: A library for manipulating XML and HTML resources.
URL: http://www.xmlsoft.org/
Group: System Environment/Libraries
License: MIT
Source: ftp://xmlsoft.org/libxml2/%{name}-%{version}.tar.gz
BuildRequires: grep, sed, pkg-config, make
BuildRequires: gcc, gettext-tools
BuildRequires: eglibc-devel, zlib-devel
BuildRequires: python-devel


%description
Libxml2 is the XML C library developed for the Gnome project. The library code
is portable (to Linux, Unix, Windows, embedded systems, etc.) and modular;
most of the extensions can be compiled out. Libxml2 implements a number of
existing standards related to markup languages, including the XML standard,
Namespaces in XML, XML Base, Relax NG, RFC 2396, XPath, XPointer, HTML4,
XInclude, SGML Catalogs, and XML Catalogs. In most cases, libxml tries to
implement the specifications in a relatively strict way. To some extent, it
provides support for the following specifications, but doesn't claim to
implement them: DOM, FTP client, HTTP client, and SAX2. Support for W3C XML
Schemas is in progress.


%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README Copyright TODO
%{_libdir}/libxml2.so.2*


%post -p %{__ldconfig}
%postun -p %{__ldconfig}


%package tools
Summary: XML-related tools from libxml2
Group: Data Processing/XML
Requires: libxml2 = %{version}-%{release}


%description tools
Libxml2 is the XML C library developed for the Gnome project. The library code
is portable (to Linux, Unix, Windows, embedded systems, etc.) and modular;
most of the extensions can be compiled out. Libxml2 implements a number of
existing standards related to markup languages, including the XML standard,
Namespaces in XML, XML Base, Relax NG, RFC 2396, XPath, XPointer, HTML4,
XInclude, SGML Catalogs, and XML Catalogs. In most cases, libxml tries to
implement the specifications in a relatively strict way. To some extent, it
provides support for the following specifications, but doesn't claim to
implement them: DOM, FTP client, HTTP client, and SAX2. Support for W3C XML
Schemas is in progress. It includes xmllint, a command line XML validator.



%files tools
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README Copyright TODO

%{_bindir}/xmlcatalog
%{_bindir}/xmllint
%doc %{_mandir}/man1/xmlcatalog.1*
%doc %{_mandir}/man1/xmllint.1*


%package devel
Summary: libxml2 Development Files
Group: Development/Libraries
Requires: libxml2 = %{version}-%{release}


%description devel
Libxml2 is the XML C library developed for the Gnome project. This package
contains header files, API documentation and other files needed for
developing, compiling and linking applications that make use of libxml2.


%files devel
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README Copyright TODO
%doc %{_datadir}/doc/%{name}-%{version}
%doc %{_datadir}/gtk-doc/html/%{name}

%{_bindir}/xml2-config

%dir %{_includedir}/libxml2
%dir %{_includedir}/libxml2/libxml
%{_includedir}/libxml2/libxml/*.h

%{_libdir}/libxml2.so
%{_libdir}/libxml2.la
%{_libdir}/libxml2.a
%{_libdir}/pkgconfig/libxml-2.0.pc
%{_libdir}/xml2Conf.sh

%doc %{_mandir}/man1/xml2-config.1*
%doc %{_mandir}/man3/libxml.3*

%{_datadir}/aclocal/libxml.m4



%package python
Summary: Python bindings to libxml2
Requires: libxml2 = %{version}
Group: System Environment/Libraries


%description python
These bindings allow python scripts to use the functions exported by the
libxml2.


%files python
%defattr(-, root, root)
%doc %{_datadir}/doc/%{name}-python-%{version}
%{_libdir}/python*/site-packages/drv_libxml2.py
%{_libdir}/python*/site-packages/libxml2.py
%{_libdir}/python*/site-packages/libxml2mod.*


%prep
%setup -q


%build
%configure \
	--with-zlib \
	--with-python \
    --with-fexceptions \
    --with-history \
    --enable-ipv6 \
    --with-sax1 \
    --with-regexps \
    --with-threads \
    --with-reader \
    --with-http
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
(cd doc/examples ; %{__make} clean ; %{__rm} -rf .deps)
%{__rm} -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%check
%{__make} -k check ||:
