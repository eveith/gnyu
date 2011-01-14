Name: pinentry
Version: 0.7.6
Release: 3ev
Summary: A Ncurses TUI to read passphrases and PIN number in a secure manner
URL: http://www.gnupg.org/related_software/pinentry/index.en.html
Group: Applications/Text
License: GPL-2
Vendor: GNyU-Linux
Source: ftp://ftp.gnupg.org/gcrypt/pinentry/%{name}-%{version}.tar.gz
BuildRequires(build,install): make
BuildRequires(build): gcc, gtk2, qt3, qt4, ncurses, libcap2, libstdc++
Provides: pinentry-curses

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


%package qt3
Summary: A Qt UI to read passphrases and PIN numbers in a secure manner
Group: Applications/Text
Requires: pinentry = %{version}
Obsoletes: %{name}-qt

%description qt3
"Pinentry" is a simple dialogue program that allows GnuPG to read passphrases
and PIN numbers in a secure manner. It is called by other programs to decrypt
data, e. g. e-mails or files.  This version uses the Qt 3 toolkit; there is
also a version for the newer Qt 4 toolkit, one using GTK+2 and one based on
Ncurses for the console.


%package qt4
Summary: A Qt-4 UI to read passphrases and PIN numbers in a secure manner
Group: Applications/Text
Requires: pinentry = %{version}

%description qt4
"Pinentry" is a simple dialogue program that allows GnuPG to read passphrases
and PIN numbers in a secure manner. It is called by other programs to decrypt
data, e. g. e-mails or files.  This version uses the Qt 4 toolkit; there is
also a version using the older Qt 3.x library, GTK+2 and one based on Ncurses
for the console.
  

%prep
	%setup -q

	# Make the qt4 version build with Qt-4.5.
	%{__sed} -i -e \
		's,#elif Q_MOC_OUTPUT_REVISION != 59,#elif Q_MOC_OUTPUT_REVISION < 59,' \
		qt4/*.moc


%build
	%configure \
		--enable-pinentry-curses \
		--enable-fallback-curses \
		--disable-pinentry-gtk \
		--enable-pinentry-gtk2 \
		--enable-pinentry-qt \
		--enable-pinentry-qt4
	%{__make} %{?_smp_mflags}


%install
	%{__make} install DESTDIR='%{buildroot}'

	# No default pinentry. :-)
	%{__rm} -f '%{buildroot}/%{_bindir}/pinentry'


%files
	%defattr(-, root, root)
	%doc AUTHORS ChangeLog COPYING NEWS README* THANKS TODO
	%{_bindir}/pinentry-curses
	%doc %{_infodir}/pinentry.info*


%files qt3
	%defattr(-, root, root)
	%doc AUTHORS ChangeLog COPYING NEWS README* THANKS TODO
	%{_bindir}/pinentry-qt


%files qt4
	%defattr(-, root, root)
	%doc AUTHORS ChangeLog COPYING NEWS README* THANKS TODO
	%{_bindir}/pinentry-qt4


%files gtk2
	%defattr(-, root, root)
	%doc AUTHORS ChangeLog COPYING NEWS README* THANKS TODO
	%{_bindir}/pinentry-gtk-2
