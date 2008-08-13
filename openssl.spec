Name: openssl
Version: 0.9.8g
Release: 1ev
Summary: A free SSL implementation and toolkit
URL: http://www.openssl.org/
Group: System Environment/Libraries
License: BSD
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: http://www.openssl.org/source/%{name}-%{version}.tar.gz
Patch0: %{name}-0.9.8-gcc42.patch
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: perl >= 5, make >= 3.79.1, gcc-core, sed, bc
Requires: zlib

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
#%patch0 -p1


%build
./config \
	--prefix=%{_prefix} \
	--openssldir=/etc/ssl \
	threads \
	shared \
	zlib-dynamic \
	$RPM_OPT_FLAGS
make %{_smp_mflags}
make test


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"

make INSTALL_PREFIX="$RPM_BUILD_ROOT" install

rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir

# Relocate some stuff that is placed in silly places

mkdir -p ${RPM_BUILD_ROOT}/%{_sbindir}
mkdir -p ${RPM_BUILD_ROOT}/%{_mandir}
mv -v ${RPM_BUILD_ROOT}/etc/ssl/man/* ${RPM_BUILD_ROOT}/%{_mandir}
mv -v ${RPM_BUILD_ROOT}/etc/ssl/misc/* ${RPM_BUILD_ROOT}/%{_sbindir}
rm -vfr ${RPM_BUILD_ROOT}/etc/ssl/man ${RPM_BUILD_ROOT}/etc/ssl/misc


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-, root, root)
%doc CHANGES* ChangeLog* FAQ LICENSE README* NEWS PROBLEMS VMS 
%dir /etc/ssl
%dir /etc/ssl/certs
%dir /etc/ssl/private
%config(noreplace) /etc/ssl/openssl.cnf
%{_bindir}/openssl
%{_bindir}/c_rehash
%{_libdir}/engines/
%{_libdir}/pkgconfig/libcrypto.pc
%{_libdir}/pkgconfig/libssl.pc
%{_libdir}/pkgconfig/openssl.pc
%{_libdir}/libssl.*
%{_libdir}/libcrypto.*
%{_includedir}/openssl/
%attr(0755, root, root) %{_sbindir}/CA.pl
%attr(0755, root, root) %{_sbindir}/CA.sh
%{_sbindir}/c_hash
%{_sbindir}/c_info
%{_sbindir}/c_issuer
%{_sbindir}/c_name
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_mandir}/man5/*
%{_mandir}/man7/*
