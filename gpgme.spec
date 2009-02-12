Name: gpgme
Version: 1.1.8
Release: 3ev
Summary: A library designed to make access to GnuPG easier for applications
URL: http://www.gnupg.org/related_software/gpgme/
Group: System Environment/Libraries
License: LGPL
Vendor: GNyU-Linux
Source: ftp://ftp.gnupg.org/gcrypt/gpgme/gpgme-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, libgpg-error >= 1.4, gnupg >= 1.3.0, gnupg2 >= 2.0.4
BuildRequires: pth, glib2 >= 2.0.0

%description
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG easier
for applications. It provides a High-Level Crypto API for encryption,
decryption, signing, signature verification and key management. Currently it
uses GnuPG as its backend but the API isn't restricted to this engine; in fact
we have already developed a backend for CMS (S/MIME).
Because the direct use of GnuPG from an application can be a complicated
programming task, it is suggested that all software should try to use GPGME
instead. This way bug fixes or improvements can be done at a central place and
every application benefits from this.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR="${RPM_BUILD_ROOT}"

[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
%{__ldconfig}
update-info-dir

%postun
%{__ldconfig}
update-info-dir


%files
%defattr(-, root, root)
%doc AUTHORS COPYING* README* ChangeLog NEWS THANKS TODO VERSION
%{_bindir}/gpgme-config
%{_libdir}/libgpgme*.*
%{_includedir}/gpgme.h
%{_datadir}/aclocal/gpgme.m4
%doc %{_infodir}/gpgme.info*
%{_datadir}/common-lisp/source/gpgme/
