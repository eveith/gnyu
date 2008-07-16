Name: gnupg2
Version: 2.0.3
Release: 1ev
Summary: The version of GnuPG supporting OpenPGP and S/MIME
URL: http://www.gnupg.org/
Group: Applications/Text
License: GPL
Vendor: MSP Slackware
Source: ftp://ftp.gnupg.org/gcrypt/gnupg/gnupg-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, libgpg-error, libassuan, libksba, libgcrypt
BuildRequires: zlib, bzip2, openldap-libs
Requires: libgpg-error, libksba, libgcrypt, zlib, bzip2, openldap-libs

%description
GnuPG is GNU's tool for secure communication and data storage.  It can
be used to encrypt data and to create digital signatures.  It includes
an advanced key management facility and is compliant with the proposed
OpenPGP Internet standard as described in RFC2440 and the S/MIME
standard as described by several RFCs.
GnuPG 2.0 is the stable version of GnuPG integrating support for
OpenPGP and S/MIME.  It does not conflict with an installed 1.4
OpenPGP-only version.


%prep
%setup -q -n gnupg-%{version}


%build
%configure
make


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"

%find_lang gnupg2


[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
/sbin/ldconfig
/sbin/install-info --info-dir=%{_infodir} %{_infodir}/gnupg.info.gz

%postun
/sbin/ldconfig
/sbin/install-info --info-dir=%{_infodir} %{_infodir}/gnupg.info.gz


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files -f gnupg2.lang
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS COPYING ChangeLog NEWS README* VERSION TODO THANKS
%{_bindir}/*
%{_sbindir}/*
%{_datadir}/gnupg/
%{_mandir}/*/*.?*
%{_libexecdir}/*
%{_infodir}/gnupg.info*
