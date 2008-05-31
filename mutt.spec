Name: mutt
Version: 1.5.18
Release: 2ev
Summary: A console MUA (Mail User Agent)
URL: http://www.mutt.org/
Group: Applications/Internet
License: GPL
Vendor: GNyU-Linux
Source: ftp://ftp.mutt.org/mutt/devel/mutt-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: coreutils, grep, sed, make, gcc, ncurses, openssl, cyrus-sasl
BuildRequires: gpgme, zlib, perl

%description
Mutt is a small but very powerful text-based MIME mail client. It is highly 
configurable, and is well-suited to the mail power user with advanced features
like key bindings, keyboard macros, mail threading, regular expression
searches, and a powerful pattern matching language for selecting groups of
messages.

%prep
%setup -q


%build
%configure \
	--enable-gpgme \
	--enable-pop \
	--enable-imap \
	--with-ssl \
	--with-sasl \
	--without-gdbm \
	--without-qdbm
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%find_lang mutt
%{__rm} -rf '%{buildroot}/%{_docdir}/mutt' '%{buildroot}/%{_datadir}/doc/mutt'


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files -f mutt.lang
%defattr(-, root, root)
%doc ABOUT-NLS BEWARE ChangeLog* COPYRIGHT NEWS OPS* PATCHES README* TODO
%doc UPDATING doc/*.txt doc/*.html
%config(noreplace) %{_sysconfdir}/Muttrc
%{_sysconfdir}/Muttrc.dist
%config(noreplace) %{_sysconfdir}/mime.types
%{_sysconfdir}/mime.types.dist
%{_bindir}/flea
%{_bindir}/mutt
%{_bindir}/muttbug
%{_bindir}/pgpewrap
%{_bindir}/pgpring
%{_bindir}/smime_keys
%{_mandir}/man1/flea.1*
%{_mandir}/man1/mutt.1*
%{_mandir}/man1/mutt_dotlock.1*
%{_mandir}/man1/muttbug.1*
%{_mandir}/man5/mbox.5*
%{_mandir}/man5/mmdf.5*
%{_mandir}/man5/muttrc.5*
