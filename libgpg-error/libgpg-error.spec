Name: libgpg-error
Version: 1.6
Release: 2ev
Summary: A helper library that provides a common set of error codes
URL: http://www.gnupg.org/related_software/libgpg-error/index.html
Group: System Environment/Libraries
License: LGPL
Vendor: MSP Slackware
Source: ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: coreutils, grep, sed, make, gcc, bison, gawk

%description
Libgpg-error is a small library that defines common error values for all GnuPG
components. Among these are GPG, GPGSM, GPGME, GPG-Agent, libgcrypt, Libksba,
DirMngr, Pinentry, SmartCard Daemon and possibly more in the future.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%find_lang libgpg-error


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files -f libgpg-error.lang
%defattr(-, root, root)
%doc COPYING* ABOUT-NLS AUTHORS ChangeLog* NEWS README THANKS VERSION
%{_libdir}/libgpg-error*.*
%{_bindir}/gpg-error*
%{_includedir}/gpg-error.h
%{_datadir}/aclocal/gpg-error.m4
%{_datadir}/common-lisp/source/gpg-error/
