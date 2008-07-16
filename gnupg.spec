Name: gnupg
Version: 1.4.7
Release: 1ev
Summary: GNU Utility for data encryption and digital signatures
URL: http://www.gnupg.org/
Group: Applications/Text
License: GPL
Vendor: MSP Slackware
Source: ftp://ftp.gnupg.org/gcrypt/gnupg/gnupg-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, gettext, zlib, openldap-libs, zlib, libusb
Requires: zlib, libusb

%description
GnuPG (GNU Privacy Guard) is a GNU utility for encrypting data and
creating digital signatures. GnuPG has advanced key management
capabilities and is compliant with the proposed OpenPGP Internet
standard described in RFC-2440.  Since GnuPG doesn't use any patented
algorithms, it is not compatible with some versions of PGP 2 which use
only the patented IDEA algorithm.  See
http://www.gnupg.org/why-not-idea.html for information on using IDEA
if the patent does not apply to you and you need to be compatible with
these versions of PGP 2.


%prep
%setup -q


%build
%configure \
	--enable-noexecstack
make


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"
%find_lang %{name}

[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"
rm -f "${RPM_BUILD_ROOT}/%{_datadir}/gnupg/FAQ"
rm -f "${RPM_BUILD_ROOT}/%{_datadir}/gnupg/faq.html"


%post
/sbin/install-info %{_infodir}/gpg.info %{_infodir}/dir 2>/dev/null || :
/sbin/install-info %{_infodir}/gpgv.info %{_infodir}/dir 2>/dev/null || :

%preun
if [ $1 = 0 ]; then
   /sbin/install-info --delete %{_infodir}/gpg.info \
        %{_infodir}/dir 2>/dev/null || :
   /sbin/install-info --delete %{_infodir}/gpgv.info \
        %{_infodir}/dir 2>/dev/null || :
fi


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"
rm -f gnupg.lang


%files -f gnupg.lang
%defattr(-, root, root)
%doc INSTALL AUTHORS COPYING NEWS README THANKS TODO PROJECTS doc/DETAILS
%doc doc/FAQ doc/faq.html doc/HACKING doc/OpenPGP doc/samplekeys.asc
%doc %attr (0755,root,root) tools/convert-from-106
%dir %{_datadir}/gnupg
%config %{_datadir}/gnupg/options.skel
%{_mandir}/man1/*
%{_mandir}/man7/*
%{_infodir}/gnupg1.info*
%attr (4755,root,root) %{_bindir}/gpg
%{_bindir}/gpgv
%{_bindir}/gpgsplit
%{_bindir}/gpg-zip
%{_libexecdir}/gnupg/
