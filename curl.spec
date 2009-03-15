Name: curl
Version: 7.16.2
Release: 1ev
Summary: A command line tool for client-side URL transfers
URL: http://curl.haxx.se/
Group: Applications/Internet
License: MIT
Vendor: MSP Slackware
Source: http://curl.haxx.se/download/curl-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, openssl, zlib
Requires: openssl, zlib
Requires: openssl, zlib
Provides: libtool(%{_libdir}/libcurl.la)

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
	--without-gnutls \
	--enable-thread \
	--disable-ipv6
make %{_smp_mflags}


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc CHANGES COPYING README RELEASE-NOTES 
%{_bindir}/curl*
%{_includedir}/curl/
%{_mandir}/*/*
%{_libdir}/*.*
%{_libdir}/pkgconfig/libcurl.pc
%{_datadir}/curl/
