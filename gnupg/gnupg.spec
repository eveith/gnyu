Name: gnupg
Version: 1.4.9
Release: 2ev
Summary: GNU Utility for data encryption and digital signatures
URL: http://www.gnupg.org/
Group: Applications/Text
License: GPL-3
Vendor: GNyU-Linux
Source: ftp://ftp.gnupg.org/gcrypt/gnupg/gnupg-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires(prep,build,install): coreutils
BuildRequires(build,install): make, gettext
BuildRequires(build): gcc, zlib, libusb, openldap-libs
BuildRequires(build): readline, curl, libtermcap

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
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%find_lang %{name}

pushd '%{buildroot}/%{_datadir}/gnupg'
%{__mv} FAQ FAQ-%{version}
%{__mv} faq.html faq-%{version}.html
popd

[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
update-info-dir

%preun
update-info-dir

%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__rm} -f gnupg.lang


%files -f gnupg.lang
%defattr(-, root, root)
%doc INSTALL AUTHORS COPYING NEWS README THANKS TODO PROJECTS doc/DETAILS
%doc doc/FAQ doc/faq.html doc/HACKING doc/OpenPGP doc/samplekeys.asc
%doc %attr (0755,root,root) tools/convert-from-106
%dir %{_datadir}/gnupg
%config %{_datadir}/gnupg/options.skel
%doc %{_datadir}/gnupg/FAQ-%{version}
%doc %{_datadir}/gnupg/faq-%{version}.html
%doc %{_mandir}/man1/*
%doc %{_mandir}/man7/*
%doc %{_infodir}/gnupg1.info*
%attr (4755,root,root) %{_bindir}/gpg
%{_bindir}/gpgv
%{_bindir}/gpgsplit
%{_bindir}/gpg-zip
%{_libexecdir}/gnupg/
