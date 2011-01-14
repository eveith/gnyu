Name: curl
Version: 7.19.6
Release: 3ev
Summary: A command line tool and library for client-side URL transfers
URL: http://curl.haxx.se/
Group: Applications/Internet
License: MIT
Vendor: GNyU-Linux
Source: http://curl.haxx.se/download/curl-%{version}.tar.bz2
BuildRequires: make, pkg-config, gcc
BuildRequires: zlib, openldap-libs
BuildRequires: openssl, heimdal-libs

%description
curl and libcurl is a tool for transferring files using URL syntax. It
supports HTTP, HTTPS, FTP, FTPS, SCP, SFTP, TFTP, DICT, TELNET, LDAP, and
FILE, as well as HTTP-post, HTTP-put, cookies, FTP upload, resumed transfers,
passwords, port numbers, SSL certificates, Kerberos, and proxies. It is
powered by libcurl, the client-side URL transfer library. There are bindings
to libcurl for over 30 languages and environments.


%prep
%setup -q


%build
%configure \
	--enable-thread \
	--enable-ldaps \
	--enable-manual \
	--with-gssapi
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc CHANGES COPYING README RELEASE-NOTES 
%{_bindir}/curl*
%{_includedir}/curl/
%{_libdir}/libcurl.*
%{_libdir}/pkgconfig/libcurl.pc
%doc %{_mandir}/man1/curl.1*
%doc %{_mandir}/man1/curl-config.1*
%doc %{_mandir}/man3/*curl*.3*
