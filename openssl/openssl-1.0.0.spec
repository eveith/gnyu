Name: openssl
Version: 1.0.0d
%define soversion %(echo %{version} | %{__sed} -e 's,[a-z],,g')
Release: 1.0
Summary: A free SSL implementation and toolkit
URL: http://www.openssl.org
Group: System Environment/Libraries
License: BSD
Source: http://www.openssl.org/source/openssl-%{version}.tar.gz
BuildRequires: sed, perl > 5.0, make, gcc
BuildRequires: eglibc-devel, kernel-headers, zlib-devel

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


%package -n libssl%{soversion}
Summary: SSL shared libraries
Group: System Environment/Libraries

%description -n libssl%{soversion}
libssl and libcrypto shared libraries needed by openssh and other programs
that make use of OpenSSL as its cryptographic library.


%package devel
Summary: OpenSSL development headers
Group: Development/Libraries
Requires: pkg-config

%description devel
Contains header files and pkg-config information for linking against the
OpenSSL libraries. It also offers documentation for development.


%prep
%setup -q


%build
./config \
	--prefix='%{_prefix}' \
	--openssldir='%{_sysconfdir}/ssl' \
	threads \
	shared \
	zlib-dynamic \
	"${CFLAGS:-$RPM_OPT_FLAGS}"
%{__make} %{?_smp_mflags}
%{__make} test


%install
%{__make} install INSTALL_PREFIX="${RPM_BUILD_ROOT}"

# Relocate some stuff that is placed in silly places
%{__mkdir_p} '%{buildroot}%{_sbindir}' '%{buildroot}%{_mandir}'
%{__mv} '%{buildroot}/etc/ssl/man'/* '%{buildroot}%{_mandir}'
%{__mv} '%{buildroot}/etc/ssl/misc'/* '%{buildroot}%{_sbindir}'
%{__rm} -fr '%{buildroot}/etc/ssl/man' '%{buildroot}/etc/ssl/misc'

# Rename manpages to avoid collisions
pushd '%{buildroot}/%{_mandir}'
for i in 1 3 5 7
do
	cd "man${i}"
	for f in *.${i}*
	do
		basename="${f%.*}"
		extension="${f##*.}"
		if [[ "${extension}" =~ ^[0-9]+$ ]]
		then
			%{__mv} -v "${f}" "${basename}.${extension}ssl"
			if [[ ! -L "${basename}.${extension}ssl" ]]
			then
				%{__bzip2} -z9 "${basename}.${extension}ssl"
			fi
		else
			%{__mv} -v "${f}" "${basename}ssl.${extension}"
		fi
	done

	# Now for the links
	for f in *.${i}*
	do
		[[ -L "${f}" ]] || continue
		t=$(readlink "${f}")
		%{__rm} "${f}"
		%{__ln_s} "${t}ssl.bz2" "${f}"
	done
	cd ..
done
popd


%post -n libssl%{soversion} -p %{__ldconfig}
%postun -n libssl%{soversion} -p %{__ldconfig}


%files
%defattr(-, root, root)
%doc CHANGES* FAQ LICENSE README* NEWS PROBLEMS VMS 
%dir %{_sysconfdir}/ssl
%dir %attr(0711, root, root) %{_sysconfdir}/ssl/certs
%dir %attr(0711, root, root) %{_sysconfdir}/ssl/private
%config(noreplace) %attr(0644, root, root) %{_sysconfdir}/ssl/openssl.cnf
%{_bindir}/openssl
%{_bindir}/c_rehash
%attr(0700, root, root) %{_sbindir}/CA.pl
%attr(0700, root, root) %{_sbindir}/CA.sh
%{_sbindir}/c_hash
%{_sbindir}/c_info
%{_sbindir}/c_issuer
%{_sbindir}/c_name
%{_sbindir}/tsget
%doc %{_mandir}/man1/*ssl*
%doc %{_mandir}/man5/*ssl*
%doc %{_mandir}/man7/*ssl*


%files -n libssl%{soversion}
%defattr(-, root, root)
%doc CHANGES* FAQ LICENSE README* NEWS PROBLEMS VMS 
%{_libdir}/libssl.so.%{soversion}
%{_libdir}/libcrypto.so.%{soversion}
%dir %{_libdir}/engines
%{_libdir}/engines/*.so


%files devel
%defattr(-, root, root)
%doc CHANGES* FAQ LICENSE README* NEWS PROBLEMS VMS 
%doc doc demos
%doc %{_mandir}/man3/*ssl*
%dir %{_includedir}/openssl
%{_includedir}/openssl/*.h
%{_libdir}/libssl.so
%{_libdir}/libssl.a
%{_libdir}/libcrypto.so
%{_libdir}/libcrypto.a
%{_libdir}/pkgconfig/libcrypto.pc
%{_libdir}/pkgconfig/libssl.pc
%{_libdir}/pkgconfig/openssl.pc
