Name: openssl0.9.8
Version: 0.9.8j
Release: 5ev
Summary: A free SSL implementation and toolkit
URL: http://www.openssl.org/
Group: System Environment/Libraries
License: BSD
Vendor: GNyU-Linux
Source: http://www.openssl.org/source/openssl-%{version}.tar.gz
Patch0: %{name}-gcc42.patch
Buildroot: %{_tmppath}/%{name}-root
BuildRequires(build,install): make, perl
BuildRequires(build): bc, gcc
BuildRequires: pkg-config
Provides: openssl = %{version}-%{release}
Obsoletes: openssl < %{version}, openssl098

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
%setup -q -n 'openssl-%{version}'


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
%{__fakeroot} %{__make} install INSTALL_PREFIX="${RPM_BUILD_ROOT}"

# Relocate some stuff that is placed in silly places
%{__mkdir_p} '%{buildroot}/%{_sbindir}' '%{buildroot}/%{_mandir}'
%{__mv} '%{buildroot}/etc/ssl/man'/* '%{buildroot}/%{_mandir}'
%{__mv} '%{buildroot}/etc/ssl/misc'/* '%{buildroot}/%{_sbindir}'
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


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc CHANGES* FAQ LICENSE README* NEWS PROBLEMS VMS 
%doc doc demos
%dir %{_sysconfdir}/ssl
%dir %attr(0711, root, root) %{_sysconfdir}/ssl/certs
%dir %attr(0711, root, root) %{_sysconfdir}/ssl/private
%config(noreplace) %attr(0644, root, root) %{_sysconfdir}/ssl/openssl.cnf
%{_bindir}/openssl
%{_bindir}/c_rehash
%{_libdir}/engines/
%{_libdir}/pkgconfig/libcrypto.pc
%{_libdir}/pkgconfig/libssl.pc
%{_libdir}/pkgconfig/openssl.pc
%{_libdir}/libssl.*
%{_libdir}/libcrypto.*
%{_libdir}/fips_premain.c
%{_libdir}/fips_premain.c.sha1
%{_includedir}/openssl/
%attr(0700, root, root) %{_sbindir}/CA.pl
%attr(0700, root, root) %{_sbindir}/CA.sh
%{_sbindir}/c_hash
%{_sbindir}/c_info
%{_sbindir}/c_issuer
%{_sbindir}/c_name
%doc %{_mandir}/man1/*ssl*
%doc %{_mandir}/man3/*ssl*
%doc %{_mandir}/man5/*ssl*
%doc %{_mandir}/man7/*ssl*
