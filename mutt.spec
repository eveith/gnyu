Name: mutt
Version: 1.5.17
Release: 1ev
Summary: A console MUA (Mail User Agent)
URL: http://www.mutt.org/
Group: Applications/Internet
License: GPL
Vendor: MSP Slackware
Source: ftp://ftp.mutt.org/mutt/devel/mutt-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, ncurses, openssl, cyrus-sasl

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
	--enable-pop \
	--enable-imap \
	--with-ssl \
	--with-sasl
make %{_smp_mflags}


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"
%find_lang mutt
rm -rf ${RPM_BUILD_ROOT}/%{_docdir}/mutt


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files -f mutt.lang
%defattr(-, root, root)
%doc ABOUT-NLS BEWARE ChangeLog* COPYRIGHT NEWS OPS* PATCHES README* TODO
%doc UPDATING doc/*.txt doc/*.html
%config(noreplace) /etc/Muttrc
/etc/Muttrc.dist
%config(noreplace) /etc/mime.types
/etc/mime.types.dist
%{_bindir}/flea
%{_bindir}/mutt
%{_bindir}/muttbug
%{_bindir}/pgpewrap
%{_bindir}/pgpring
%{_bindir}/smime_keys
%{_mandir}/man1/flea.1.gz
%{_mandir}/man1/mutt.1.gz
%{_mandir}/man1/mutt_dotlock.1.gz
%{_mandir}/man1/muttbug.1.gz
%{_mandir}/man5/mbox.5.gz
%{_mandir}/man5/mmdf.5.gz
%{_mandir}/man5/muttrc.5.gz
