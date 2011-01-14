Name: libgcrypt
Version: 1.4.0
Release: 1ev
Summary: A general-pourpose cryptographic library
URL: http://www.gnu.org/directory/security/libgcrypt.html
Group: System Environment/Libraries
License: LGPL
Vendor: MSP Slackware
Source: ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, libgpg-error >= 0.5

%description
This is a general purpose cryptographic library based on the code from GnuPG.
It provides functions for all cryptograhic building blocks: symmetric ciphers
(AES, DES, Blowfish, CAST5, Twofish, Arcfour), hash algorithms (MD4, MD5,
RIPE-MD160, SHA-1, TIGER-192), MACs (HMAC for all hash algorithms), public key
algorithms (RSA, ElGamal, DSA), large integer functions, random numbers and a
lot of supporting functions. 


%prep
%setup -q


%build
%configure \
	--with-capabilities
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'

[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
/sbin/ldconfig
update-info-dir

%postun
/sbin/ldconfig
update-info-dir


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc AUTHORS COPYING* BUGS ChangeLog README* NEWS THANKS VERSION TODO
%{_bindir}/dumpsexp
%{_bindir}/libgcrypt-config
%{_libdir}/libgcrypt.*
%{_includedir}/gcrypt*.h
%{_infodir}/gcrypt.info*
%{_datadir}/aclocal/libgcrypt.m4
