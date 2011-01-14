Name: gnupg2
Version: 2.0.13
Release: 4ev
Summary: The version of GnuPG supporting OpenPGP and S/MIME
URL: http://www.gnupg.org/
Group: Applications/Text
License: GPL-3
Vendor: GNyU-Linux
Source: ftp://ftp.gnupg.org/gcrypt/gnupg/gnupg-%{version}.tar.bz2
BuildRequires(build,install): make, gettext
BuildRequires(build): gcc, libgpg-error >= 1.4, libassuan >= 1.0.4
BuildRequires(build): libksba >= 1.0.2, libgcrypt >= 1.4.0
BuildRequires(build): zlib, bzip2, openldap-libs, pth >= 1.3.7, readline

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
%setup -q -n 'gnupg-%{version}'


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make_install} DESTDIR='%{buildroot}'
%find_lang gnupg2
%{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
%{__ldconfig}
update-info-dir


%postun
%{__ldconfig}
update-info-dir


%files -f gnupg2.lang
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS COPYING ChangeLog NEWS README* VERSION TODO THANKS
%doc doc/examples
%{_bindir}/gpg-agent                             
%{_bindir}/gpg-connect-agent                     
%{_bindir}/gpg2                                  
%{_bindir}/gpgconf                               
%{_bindir}/gpgkey2ssh                            
%{_bindir}/gpgparsemail                          
%{_bindir}/gpgsm                                 
%{_bindir}/gpgsm-gencert.sh                      
%{_bindir}/gpgv2                                 
%{_bindir}/kbxutil                               
%{_bindir}/scdaemon                              
%{_bindir}/watchgnupg
%{_sbindir}/*
%{_datadir}/gnupg/
%doc %{_mandir}/man1/gpg-agent.1*
%doc %{_mandir}/man1/gpg-connect-agent.1*
%doc %{_mandir}/man1/gpg-preset-passphrase.1*
%doc %{_mandir}/man1/gpg-zip.1
%doc %{_mandir}/man1/gpg2.1*
%doc %{_mandir}/man1/gpgconf.1*
%doc %{_mandir}/man1/gpgparsemail.1*
%doc %{_mandir}/man1/gpgsm-gencert.sh.1*
%doc %{_mandir}/man1/gpgsm.1*
%doc %{_mandir}/man1/gpgv2.1*
%doc %{_mandir}/man1/scdaemon.1*
%doc %{_mandir}/man1/symcryptrun.1*
%doc %{_mandir}/man1/watchgnupg.1*
%doc %{_mandir}/man8/applygnupgdefaults.8*
%doc %{_mandir}/man8/addgnupghome.8*
%{_libexecdir}/*
%doc %{_infodir}/gnupg.info*
%dir %{_datadir}/doc/gnupg
%doc %{_datadir}/doc/gnupg/*
