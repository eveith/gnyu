Name: nss
Version: 3.12.4
Release: 1ev
Summary: A library supporting a set of network security standards
URL: http://www.mozilla.org/projects/security/pki/nss
Group: System Environment/Libraries
License: GPL-2/MPL/LGPL-2.1
Vendor: GNyU-Linux
Source: ftp://ftp.mozilla.org/pub/mozilla.org/security/nss/releases/NSS_3_12_4_RTM/src/nss-%{version}-with-nspr-4.8.tar.gz
BuildRequires: make, gcc, pkg-config >= 0.9.0

%description
Network Security Services (NSS) is a set of libraries designed to support
cross-platform development of security-enabled client and server applications.
Applications built with NSS can support SSL v2 and v3, TLS, PKCS #5, PKCS #7,
PKCS #11, PKCS #12, S/MIME, X.509 v3 certificates, and other security
standards.


%prep
	%setup -q -n 'nss-%{version}-with-nspr-4.8'


%build
	pushd 'mozilla/security/nss'
	%{__make} %{?_smp_mflags} \
		BUILD_OPT=1 \
		XCFLAGS="${CFLAGS:-%{optflags}}" \
		CC="${CC:-%{_target_platform}-gcc}" \
		nss_build_all
	popd


%install
	%{__mkdir_p} '%{buildroot}/%{_libdir}'
	for lib in mozilla/dist/*.OBJ/lib/*.so
	do
	  %{__install} -m0755 "${lib}" '%{buildroot}/%{_libdir}'
	done

	#%{__mkdir_p} '%{buildroot}/%{_libdir}/pkgconfig'
	#%{__install} -m0644 ./mozilla/dist/pkgconfig/nss.pc \
	#	'%{buildroot}/%{_libdir}/pkgconfig/nss.pc'

	%{__mkdir_p} '%{buildroot}/%{_includedir}/nss3'
	for header in mozilla/dist/public/nss/*.h
	do
		%{__install} -m0644 "${header}"	'%{buildroot}/%{_includedir}/nss3'
	done


%post
	%{__ldconfig}


%postun
	%{__ldconfig}


%files
	%defattr(-, root, root)
	%dir %{_includedir}/nss3
	%{_includedir}/nss3/*.h
    %{_libdir}/libfreebl3.so
    %{_libdir}/libnspr4.so
    %{_libdir}/libnss3.so
    %{_libdir}/libnssckbi.so
    %{_libdir}/libnssdbm3.so
    %{_libdir}/libnssutil3.so
    %{_libdir}/libplc4.so
    %{_libdir}/libplds4.so
    %{_libdir}/libsmime3.so
    %{_libdir}/libsoftokn3.so
    %{_libdir}/libsqlite3.so
    %{_libdir}/libssl3.so
