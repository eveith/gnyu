Name: libgpg-error
Version: 1.4
Release: 1ev
Summary: A helper library that provides a common set of error codes
URL: http://www.gnupg.org/related_software/libgpg-error/index.html
Group: System Environment/Libraries
License: LGPL
Vendor: MSP Slackware
Source: ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, bison, gawk
Provides: libtool(%{_libdir}/libgpg-error.la)

%description
Libgpg-error is a small library that defines common error values for all GnuPG
components. Among these are GPG, GPGSM, GPGME, GPG-Agent, libgcrypt, Libksba,
DirMngr, Pinentry, SmartCard Daemon and possibly more in the future.


%prep
%setup -q


%build
%configure
make


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"

%find_lang libgpg-error

[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files -f libgpg-error.lang
%defattr(-, root, root)
%doc COPYING* ABOUT-NLS AUTHORS ChangeLog* NEWS README THANKS VERSION
%{_libdir}/libgpg-error*.*
%{_bindir}/gpg-error*
%{_includedir}/gpg-error.h
%{_datadir}/aclocal/gpg-error.m4
%{_datadir}/common-lisp/source/gpg-error/
