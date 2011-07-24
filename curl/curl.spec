Name: curl
Version: 7.21.7
Release: 1.0
Summary: A command line tool and library for client-side URL transfers
URL: http://curl.haxx.se/
Group: Network/Applications
License: MIT
Vendor: GNyU-Linux
Source: http://curl.haxx.se/download/curl-%{version}.tar.bz2
BuildRequires: grep, sed, make, pkg-config, perl
BuildRequires: gcc
BuildRequires: eglibc-devel
BuildRequires: zlib-devel
BuildRequires: openssl-devel

%description
curl and libcurl is a tool for transferring files using URL syntax. It
supports HTTP, HTTPS, FTP, FTPS, SCP, SFTP, TFTP, DICT, TELNET, LDAP, and
FILE, as well as HTTP-post, HTTP-put, cookies, FTP upload, resumed transfers,
passwords, port numbers, SSL certificates, Kerberos, and proxies. It is
powered by libcurl, the client-side URL transfer library. There are bindings
to libcurl for over 30 languages and environments.


%files
%defattr(-, root, root)
%doc CHANGES COPYING README RELEASE-NOTES 
%{_bindir}/curl*
%doc %{_mandir}/man1/curl.1*


%package devel
Summary: cURL development files
Group: Network/Development
Requires: %{name} = %{version}-%{release}
Requires: pkg-config


%description devel
curl and libcurl is a tool for transferring files using URL syntax. This
package includes header files, a pkg-config .pc and API documentation needed
for developing programs that make use of cURL.


%files devel
%defattr(-, root, root)
%doc CHANGES COPYING README RELEASE-NOTES 
%doc %{_mandir}/man1/curl-config.1*
%doc %{_mandir}/man3/*curl*.3*

%dir %{_includedir}/curl
%{_includedir}/curl/*.h

%{_libdir}/pkgconfig/libcurl.pc
%{_libdir}/libcurl.so
%{_libdir}/libcurl.a
%{_libdir}/libcurl.la


%package -n libcurl4
Summary: cURL network transfer library
Group: Network/Libraries


%description -n libcurl4
The cURL library is a software for transfering files using URL syntax.


%files -n libcurl4
%defattr(-, root, root)
%doc COPYING CHANGES README
%{_libdir}/libcurl.so.4*


%post -n libcurl4 -p %{__ldconfig}
%postun -n libcurl4 -p %{__ldconfig}


%prep
%setup -q


%build
%configure \
	--enable-thread \
	--enable-manual \
	--with-ipv6
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'


%check
%{__make} check ||:
