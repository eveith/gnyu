Name: aspell
Version: 0.60.5
Release: 1ev
Summary: An intelligent spell checker
URL: http://aspell.net/
Group: Applications/Text
License: LGPL
Vendor: MSP Slackware
Source0: ftp://ftp.gnu.org/gnu/aspell/aspell-%{version}.tar.gz
Source1: ftp://ftp.gnu.org/gnu/aspell/dict/de/aspell6-de-20030222-1.tar.bz2
Source2: ftp://ftp.gnu.org/gnu/aspell/dict/de-alt/aspell6-de-alt-2.1-1.tar.bz2
Source3: ftp://ftp.gnu.org/gnu/aspell/dict/en/aspell6-en-6.0-0.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: gcc-g++, make >= 3.79.1, libstdc++, ncurses

%description
GNU Aspell is a spell checker designed to eventually replace Ispell. It can
either be used as a library or as an independent spell checker. Its main
feature is that it does a superior job of suggesting possible replacements for
a misspelled word than just about any other spell checker out there for the
English language. Unlike Ispell, Aspell can also easily check documents in
UTF-8 without having to use a special dictionary. Aspell will also do its best
to respect the current locale setting. Other advantages over Ispell include
support for using multiple dictionaries at once and intelligently handling
personal dictionaries when more than one Aspell process is open at once.


%prep
%setup -q -a 0
# %setup -q -a 1 -a 2 -a 3


%build
%configure
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR="${RPM_BUILD_ROOT}"
%{__rm} -f %{buildroot}/%{_infodir}/dir
%find_lang aspell


%post
/sbin/ldconfig
update-info-dir

%postun
/sbin/ldconfig
update-info-dir


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files -f aspell.lang
%defattr(-, root, root)
%doc ABOUT-NLS COPYING README TODO
%{_bindir}/aspell
%{_bindir}/aspell-import
%{_bindir}/precat
%{_bindir}/preunzip
%{_bindir}/prezip
%{_bindir}/prezip-bin
%{_bindir}/pspell-config
%{_bindir}/run-with-aspell
%{_bindir}/word-list-compress
%{_includedir}/aspell.h
%{_includedir}/pspell/
%{_infodir}/aspell-dev.info.gz
%{_infodir}/aspell.info.gz
%{_libdir}/aspell-*/
%{_libdir}/libaspell.*
%{_libdir}/libpspell.*
%{_mandir}/man1/aspell-import.1*
%{_mandir}/man1/aspell.1*
%{_mandir}/man1/prezip-bin.1*
%{_mandir}/man1/pspell-config.1*
%{_mandir}/man1/run-with-aspell.1*
%{_mandir}/man1/word-list-compress.1*
