Name: libxml2 
Version: 2.7.3
Release: 4ev
Summary: A library for manipulating XML and HTML resources.
URL: http://www.xmlsoft.org/
Group: System Environment/Libraries
License: MIT
Vendor: GNyU-Linux
Source: ftp://xmlsoft.org/libxml2/%{name}-%{version}.tar.gz
BuildRequires(build,install): make, python, pkg-config
BuildRequires(build): gcc, zlib

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
Schemas is in progress. It includes xmllint, a command line XML validator.


%package python
Summary: Python bindings to libxml2
Requires: libxml2 = %{version}
Group: System Environment/Libraries

%description python
These bindings allow python scripts to use the functions exported by the
libxml2.


%prep
%setup -q


%build
%configure \
	--with-zlib \
	--with-python 
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
(cd doc/examples ; %{__make} clean ; %{__rm} -rf .deps)
%{__rm} -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README Copyright TODO
%doc %{_datadir}/doc/%{name}-%{version}
%doc %{_datadir}/gtk-doc/html/%{name}
%{_bindir}/xml2-config
%{_bindir}/xmlcatalog
%{_bindir}/xmllint
%{_includedir}/libxml2/
%{_libdir}/libxml2.*
%{_libdir}/pkgconfig/libxml-2.0.pc
%{_libdir}/xml2Conf.sh
%doc %{_mandir}/man1/xml2-config.1*
%doc %{_mandir}/man1/xmlcatalog.1*
%doc %{_mandir}/man1/xmllint.1*
%doc %{_mandir}/man3/libxml.3*
%{_datadir}/aclocal/libxml.m4


%files python
%defattr(-, root, root)
%doc %{_datadir}/doc/%{name}-python-%{version}
%{_libdir}/python*/site-packages/drv_libxml2.py
%{_libdir}/python*/site-packages/libxml2.py
%{_libdir}/python*/site-packages/libxml2mod.*
