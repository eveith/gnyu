Name: ncurses
Version: 5.7
Release: 2ev
Summary: A CRT screen handling and optimization package.
License: distributable
Group: System Environment/Libraries
Vendor: GNyU-Linux
URL: http://www.gnu.org/software/ncurses/
Source0: ftp://ftp.gnu.org/pub/gnu/ncurses/ncurses-%{version}.tar.gz
Source3: ncurses-resetall.sh
BuildRequires: gcc, gcc-g++, make
BuildRoot: %{_tmppath}/%{name}-root
%define includedirw %{_includedir}/ncursesw

%description
The curses library routines are a terminal-independent method of
updating character screens with reasonable optimization.  The ncurses
(new curses) library is a freely distributable replacement for the
discontinued 4.4 BSD classic curses library.


%prep
%setup -q


%build
# We build two versions: One with UTF-8 support and a classic one without.
%{__mkdir} narrowc widec

pushd 'narrowc'
%{__ln_s} ../configure .
%configure \
	--with-shared \
	--with-cxx \
	--without-ada \
	--with-ospeed=unsigned \
	--without-gpm \
	--enable-sigwinch \
	--enable-hard-tabs \
	--enable-xmc-glitch \
	--enable-colorfgbg \
	--with-install-prefix="${RPM_BUILD_ROOT}" \
	--with-chtype=long
%{__make} %{?_smp_mflags}
popd

pushd 'widec'
%{__ln_s} ../configure .
%configure \
	--with-shared \
	--with-cxx \
	--without-ada \
	--with-ospeed=unsigned \
	--without-gpm \
	--enable-sigwinch \
	--enable-hard-tabs \
	--enable-xmc-glitch \
	--enable-colorfgbg \
	--enable-widec \
	--with-install-prefix="${RPM_BUILD_ROOT}" \
	--with-chtype=long
%{__make} %{?_smp_mflags}
popd


%install
[[ '%{buildroot}' != '/' ]] && %{__rm_rf} '%{buildroot}'
%{__mkdir_p} '%{buildroot}/%{_libdir}'
%{__mkdir_p} '%{buildroot}/%{_datadir}'
%{__mkdir_p} '%{buildroot}/%{_includedir}'

pushd 'widec'
%{__fakeroot} %{__make} install includedir='%{_includedir}/ncurses'
%{__mkdir_p} %{buildroot}/%{includedirw}
mv ${RPM_BUILD_ROOT}%{_includedir}/ncurses/* ${RPM_BUILD_ROOT}%{includedirw}
popd

pushd 'narrowc'
%{__fakeroot} %{__make} install includedir='%{_includedir}/ncurses'
popd

%{__ln_s} '%{_datadir}/terminfo/l/linux' \
	'%{buildroot}/%{_datadir}/terminfo/c/console'
%{__ln_s} '%{_includedir}/ncurses/curses.h' \
	'%{buildroot}/%{_includedir}/ncurses.h'

# Narrow char version is still the default; copy headers to include root dir
for header in curses.h unctrl.h eti.h form.h menu.h panel.h term.h
do
	%{__ln_s} -f "ncurses/${header}" "%{buildroot}/%{_includedir}/${header}"
done

# Backwards compatibility with old curses library names
%{__ln_s} -f libncurses.a '%{buildroot}/%{_libdir}/libcurses.a'
%{__ln_s} -f libncursesw.a '%{buildroot}/%{_libdir}/libcursesw.a'

# Install old termcap file
%{__mkdir_p} '%{buildroot}/%{_sysconfdir}'
%{__install} misc/terminfo.src '%{buildroot}/%{_sysconfdir}/termcap'

# "Resetall" script
%{__install} -c '%{SOURCE3}' '%{buildroot}/%{_bindir}/resetall'


%post
%{__ldconfig}

%postun
%{__ldconfig}


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm_rf} '%{buildroot}'


%files
%defattr(-,root,root)
%doc README ANNOUNCE doc/html/announce.html
%doc test
%doc doc/html/hackguide.html
%doc doc/html/ncurses-intro.html
%doc c++/README*
%config %attr(0644, root, root) %{_sysconfdir}/termcap
%attr(0755, root, root) %{_bindir}/resetall
%{_bindir}/captoinfo
%{_bindir}/clear
%{_bindir}/infocmp
%{_bindir}/infotocap
%{_bindir}/ncurses5-config
%{_bindir}/ncursesw5-config
%{_bindir}/reset
%{_bindir}/tic
%{_bindir}/toe
%{_bindir}/tput
%{_bindir}/tset
%{_datadir}/terminfo
%{_datadir}/tabset
%dir %{_includedir}/ncurses
%dir %{_includedir}/ncursesw
%{_includedir}/curses.h
%{_includedir}/ncurses.h
%{_includedir}/eti.h
%{_includedir}/form.h
%{_includedir}/menu.h
%{_includedir}/panel.h
%{_includedir}/term.h
%{_includedir}/unctrl.h
%{_includedir}/ncurses*/curses.h
%{_includedir}/ncurses*/cursesapp.h
%{_includedir}/ncurses*/cursesf.h
%{_includedir}/ncurses*/cursesm.h
%{_includedir}/ncurses*/cursesp.h
%{_includedir}/ncurses*/cursesw.h
%{_includedir}/ncurses*/cursslk.h
%{_includedir}/ncurses*/eti.h
%{_includedir}/ncurses*/etip.h
%{_includedir}/ncurses*/form.h
%{_includedir}/ncurses*/menu.h
%{_includedir}/ncurses*/nc_tparm.h
%{_includedir}/ncurses*/ncurses.h
%{_includedir}/ncurses*/ncurses_dll.h
%{_includedir}/ncurses*/panel.h
%{_includedir}/ncurses*/term.h
%{_includedir}/ncurses*/term_entry.h
%{_includedir}/ncurses*/termcap.h
%{_includedir}/ncurses*/tic.h
%{_includedir}/ncurses*/unctrl.h
%{_libdir}/terminfo
%{_libdir}/lib*curses*.*
%{_libdir}/libform*
%{_libdir}/libmenu*
%{_libdir}/libpanel*
%{_mandir}/man1/captoinfo.1m*
%{_mandir}/man1/clear.1*
%{_mandir}/man1/infocmp.1m*
%{_mandir}/man1/infotocap.1m*
%{_mandir}/man1/reset.1*
%{_mandir}/man1/tic.1m*
%{_mandir}/man1/toe.1m*
%{_mandir}/man1/tput.1*
%{_mandir}/man1/tset.1*
%doc %{_mandir}/man3/*.3x*
%doc %{_mandir}/man5/term.5*
%doc %{_mandir}/man5/terminfo.5*
%doc %{_mandir}/man7/term.7*
