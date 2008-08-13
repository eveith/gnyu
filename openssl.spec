Name: openssl
Version: 0.9.8h
Release: 2ev
Summary: A free SSL implementation and toolkit
URL: http://www.openssl.org/
Group: System Environment/Libraries
License: BSD
Vendor: GNyU-Linux
Source: http://www.openssl.org/source/%{name}-%{version}.tar.gz
Patch0: %{name}-0.9.8-gcc42.patch
Buildroot: %{_tmppath}/%{name}-root
BuildRequires(build,install): make, perl
BuildRequires(build): bc, gcc
Provides: openssl098 = %{version}-%{release}

%description
The OpenSSL Project is a collaborative effort to develop a robust,
commercial-grade, fully featured, and Open Source toolkit implementing the
Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS v1)
protocols as well as a full-strength general purpose cryptography library.
The project is managed by a worldwide community of volunteers that use the
Internet to communicate, plan, and develop the OpenSSL toolkit and its
related documentation.
OpenSSL is based on the excellent SSLeay library developed from Eric A. Young
and Tim J. Hudson.  The OpenSSL toolkit is licensed under a dual-license (the
OpenSSL license plus the SSLeay license) situation, which basically means
that you are free to get and use it for commercial and non-commercial
purposes as long as you fulfill the conditions of both licenses.

OpenSSL is the base of many SSL/TLS enabled programs and should be installed
on every system.


%prep
%setup -q


%build
./config \
	--prefix='%{_prefix}' \
	--openssldir='%{_sysconfdir}/ssl' \
	threads \
	shared \
	zlib-dynamic \
	"${RPM_OPT_FLAGS}"
%{__make} %{?_smp_mflags}
%{__make} test


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} INSTALL_PREFIX="${RPM_BUILD_ROOT}"

rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir

# Relocate some stuff that is placed in silly places
%{__mkdir_p} '%{buildroot}/%{_sbindir}' '%{buildroot}/%{_mandir}'
%{__mv} '%{buildroot}/etc/ssl/man'/* '%{buildroot}/%{_mandir}'
%{__mv} '%{buildroot}/etc/ssl/misc'/* '%{buildroot}/%{_sbindir}'
%{__rm} -fr '%{buildroot}/etc/ssl/man' '%{buildroot}/etc/ssl/misc'


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc CHANGES* ChangeLog* FAQ LICENSE README* NEWS PROBLEMS VMS 
%doc doc demos
%dir %{_sysconfdir}/ssl
%dir %attr(0711, root, root) %{_sysconfdir}/ssl/certs
%dir %attr(0700, root, root) %{_sysconfdir}/ssl/private
%config(noreplace) %attr(0644, root, root) %{_sysconfdir}/ssl/openssl.cnf
%{_bindir}/openssl
%{_bindir}/c_rehash
%{_libdir}/engines/
%{_libdir}/pkgconfig/libcrypto.pc
%{_libdir}/pkgconfig/libssl.pc
%{_libdir}/pkgconfig/openssl.pc
%{_libdir}/libssl.*
%{_libdir}/libcrypto.*
%{_includedir}/openssl/
%attr(0700, root, root) %{_sbindir}/CA.pl
%attr(0700, root, root) %{_sbindir}/CA.sh
%{_sbindir}/c_hash
%{_sbindir}/c_info
%{_sbindir}/c_issuer
%{_sbindir}/c_name
%doc %{_mandir}/man1/*
%doc %{_mandir}/man3/*
%doc %{_mandir}/man5/*
%doc %{_mandir}/man7/*
