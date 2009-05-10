Name: pinentry
Version: 0.7.5
Release: 2ev
Summary: A Ncurses TUI to read passphrases and PIN number in a secure manner
URL: http://www.gnupg.org/related_software/pinentry/index.en.html
Group: Applications/Text
License: GPL-2
Vendor: GNyU-Linux
Source: ftp://ftp.gnupg.org/gcrypt/pinentry/%{name}-%{version}.tar.gz
BuildRequires(build,install): make
BuildRequires(build): gcc, gtk2, qt3, ncurses, libcap2, libstdc++

%description
"Pinentry" is a simple dialogue program that allows GnuPG to read passphrases
and PIN numbers in a secure manner. It is called by other programs to decrypt
data, e. g. e-mails or files.
The original version uses Ncurses and has a TUI (text user interface). There
are also versions using graphical toolkits: GTK+ and Qt.


%package gtk2
Summary: A GTK+2 UI to read passphrases and PIN numbers in a secure manner
Group: Applications/Text
Requires: pinentry = %{version}

%description gtk2
"Pinentry" is a simple dialogue program that allows GnuPG to read passphrases
and PIN numbers in a secure manner. It is called by other programs to decrypt
data, e. g. e-mails or files.
This version uses the GTK+2; there is also a version using Qt and one based
on Ncurses for the console.


%package qt
Summary: A Qt UI to read passphrases and PIN numbers in a secure manner
Group: Applications/Text
Requires: pinentry = %{version}

%description qt
"Pinentry" is a simple dialogue program that allows GnuPG to read passphrases
and PIN numbers in a secure manner. It is called by other programs to decrypt
data, e. g. e-mails or files.
This version uses the Qt; there is also a version using GTK+2 and one based
on Ncurses for the console.


%prep
	%setup -q


%build
	%configure \
		--enable-pinentry-curses \
		--disable-pinentry-gtk \
		--disable-pinentry-gtk2 \
		--enable-pinentry-qt
	%{__make} %{?_smp_mflags}


%install
	%{__make_install} DESTDIR='%{buildroot}'


%files
	%defattr(-, root, root)
	%doc AUTHORS ChangeLog COPYING NEWS README* THANKS TODO
	%{_bindir}/pinentry-curses
	%doc %{_infodir}/pinentry.info*


%files qt
	%defattr(-, root, root)
	%doc AUTHORS ChangeLog COPYING NEWS README* THANKS TODO
	%{_bindir}/pinentry
	%{_bindir}/pinentry-qt


%files gtk2
	%defattr(-, root, root)
	%doc AUTHORS ChangeLog COPYING NEWS README* THANKS TODO
