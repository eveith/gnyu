Name: neon
Version: 0.28.5
Release: 3ev
Summary: A HTTP and WebDAV client library
URL: http://www.webdav.org/neon/
Group: System Environment/Libraries
License: LGPL-2
Vendor: GNyU-Linux
Source: http://www.webdav.org/neon/neon-%{version}.tar.gz
BuildRequires: make >= 3.79.1, gcc, expat, zlib, gnutls, heimdal-libs

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
		--with-expat \
		--with-ssl=gnutls
	%{__make} %{?_smp_mflags}


%install
	%{__make} install DESTDIR='%{buildroot}'
	%{__rm} -f '%{buildroot}/%{_infodir}/dir'
	%find_lang neon


%post -p %{__ldconfig}
%postun -p %{__ldconfig}


%files -f neon.lang
	%defattr(-, root, root)
	%doc AUTHORS BUGS ChangeLog* NEWS README THANKS TODO src/COPYING.LIB
	%doc %{_datadir}/doc/%{name}-%{version} 
	%{_bindir}/neon-config
	%{_includedir}/neon/
	%{_libdir}/libneon*.*
	%{_libdir}/pkgconfig/neon.pc
	%doc %{_mandir}/man1/neon-config.1*
	%doc %{_mandir}/man3/ne_*.*
	%doc %{_mandir}/man3/neon.3*
