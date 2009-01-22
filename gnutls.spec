Name: gnutls
Version: 2.6.3
Release: 3ev
Summary: An Open Source implementation of TLS 1.0 Internet protocol (RFC 2246)
URL: http://www.gnu.org/software/gnutls/
Group: System Environment/Libraries
License: LGPL-2.1
Vendor: GNyU-Linux
Source: ftp://ftp.gnutls.org/pub/gnutls/%{name}-%{version}.tar.bz2
BuildRequires: make, gcc, gcc-g++, gettext, libstdc++
BuildRequires: libgcrypt, zlib, libgpg-error, readline, ncurses

%description
GnuTLS is a project that aims to develop a library which provides a secure 
layer, over a reliable transport layer. Currently the GnuTLS library implements
the proposed standards by the IETF's TLS working group.
Quoting from the TLS protocol specification:
"The TLS protocol provides communications privacy over the Internet. The 
protocol allows client/server applications to communicate in a way that is 
designed to prevent eavesdropping, tampering, or message forgery."


%prep
%setup -q


%build
%configure \
	--disable-rpath \
	--with-included-libtasn1 \
	--with-included-libcfg 
%{__make} %{?_smp_mflags}


%install
%{__make_install} DESTDIR='%{buildroot}'
%{find_lang} gnutls

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files -f gnutls.lang
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS COPYING COPYING.LIB README NEWS THANKS doc/*.pdf
%{_bindir}/certtool
%{_bindir}/gnutls-cli
%{_bindir}/gnutls-cli-debug
%{_bindir}/gnutls-serv
%{_bindir}/libgnutls-config
%{_bindir}/libgnutls-extra-config
%{_bindir}/[ps][sr][kp]tool
%{_includedir}/gnutls/
%doc %{_infodir}/gnutls*
%{_libdir}/libgnutls-extra.*
%{_libdir}/libgnutls-openssl.*
%{_libdir}/libgnutls.*
%{_libdir}/libgnutlsxx.*
%{_libdir}/pkgconfig/gnutls.pc
%{_libdir}/pkgconfig/gnutls-extra.pc
%doc %{_mandir}/man1/gnutls-cli*.1*
%doc %{_mandir}/man1/gnutls-serv.1*
%doc %{_mandir}/man1/*tool.1*
%doc %{_mandir}/man3/gnutls_*.3*
%{_datadir}/aclocal/libgnutls.m4
%{_datadir}/aclocal/libgnutls-extra.m4
