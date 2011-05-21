Name: neon
Version: 0.29.6
Release: 1.0
Summary: A HTTP and WebDAV client library
URL: http://www.webdav.org/neon/
Group: System Environment/Libraries
License: LGPL-2
Source: http://www.webdav.org/neon/neon-%{version}.tar.gz
BuildRequires: grep, sed, make >= 3.79.1, gcc
BuildRequires: pkg-config >= 0.18
BuildRequires: eglibc-devel
BuildRequires: openssl-devel >= 0.9.7, expat-devel, zlib-devel
Requires: libneon27 = %{version}-%{release}

%description
neon is an HTTP and WebDAV client library, with a C interface. Featuring: 
 - High-level interface to HTTP and WebDAV methods (PUT, GET, HEAD etc) 
 - Low-level interface to HTTP request handling, to allow implementing new
   methods easily. 
 - persistent connections 
 - RFC2617 basic and digest authentication (including auth-int, md5-sess) 
 - Proxy support (including basic/digest authentication) 
 - SSL/TLS support using OpenSSL (including client certificate support) 
 - Generic WebDAV 207 XML response handling mechanism 
 - XML parsing using the expat or libxml parsers 
 - Easy generation of error messages from 207 error responses 
 - WebDAV resource manipulation: MOVE, COPY, DELETE, MKCOL. 
 - WebDAV metadata support: set and remove properties, query any set of
   properties (PROPPATCH/PROPFIND). 
 - autoconf macros supplied for easily embedding neon directly inside an
   application source tree.


%package devel
Summary: Development Headers for neon
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
neon is an HTTP and WebDAV client library, with a C interface. This package
offers API documentation, development headers and other files you'll need when
building applications that make use of neon.


%package -n libneon27
Summary: A HTTP and WebDAV client library
Group: System Environment/Libraries

%description
neon is an HTTP and WebDAV client library, with a C interface. Featuring: 
 - High-level interface to HTTP and WebDAV methods (PUT, GET, HEAD etc) 
 - Low-level interface to HTTP request handling, to allow implementing new
   methods easily. 
 - persistent connections 
 - RFC2617 basic and digest authentication (including auth-int, md5-sess) 
 - Proxy support (including basic/digest authentication) 
 - SSL/TLS support using OpenSSL (including client certificate support) 
 - Generic WebDAV 207 XML response handling mechanism 
 - XML parsing using the expat or libxml parsers 
 - Easy generation of error messages from 207 error responses 
 - WebDAV resource manipulation: MOVE, COPY, DELETE, MKCOL. 
 - WebDAV metadata support: set and remove properties, query any set of
   properties (PROPPATCH/PROPFIND). 
 - autoconf macros supplied for easily embedding neon directly inside an
   application source tree.


%prep
%setup -q


%build
%configure \
    --disable-debug \
    --enable-shared \
    --with-ssl=openssl \
    --with-expat
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%{__rm} -f '%{buildroot}%{_infodir}/dir'
%find_lang neon


%post -n libneon27 -p %{__ldconfig}
%postun -n libneon27 -p %{__ldconfig}


%files
%defattr(-, root, root)
%doc AUTHORS BUGS ChangeLog* NEWS README THANKS TODO src/COPYING.LIB


%files -n libneon27 -f neon.lang
%defattr(-, root, root)
%doc AUTHORS BUGS ChangeLog* NEWS README THANKS TODO src/COPYING.LIB
%{_libdir}/libneon.so.27*


%files devel
%defattr(-, root, root)
%doc AUTHORS BUGS ChangeLog* NEWS README THANKS TODO src/COPYING.LIB
%dir %{_datadir}/doc/neon-%{version}
%dir %{_datadir}/doc/neon-%{version}/html
%doc %{_datadir}/doc/neon-%{version}/html/*
%{_bindir}/neon-config
%{_libdir}/libneon.so
%{_libdir}/libneon.la
%{_libdir}/libneon.a
%{_libdir}/pkgconfig/neon.pc
%dir %{_includedir}/neon
%{_includedir}/neon/*.h
%doc %{_mandir}/man1/neon-config.1*
%doc %{_mandir}/man3/ne_*.3*
%doc %{_mandir}/man3/neon.3*
