Name: ncurses
Version: 5.7
Release: 2.1
Summary: A CRT screen handling and optimization package.
License: distributable
Group: System Environment/Libraries
URL: http://www.gnu.org/software/ncurses
Source0: ftp://ftp.gnu.org/pub/gnu/ncurses/ncurses-%{version}.tar.gz
Source3: resetall.sh
BuildRequires: grep, gawk, make, gcc, gcc-g++
BuildRequires: eglibc-devel, kernel-headers, libstdc++-devel
%define includedirw %{_includedir}/ncursesw

%description
The curses library routines are a terminal-independent method of updating
character screens with reasonable optimization.  The ncurses (new curses)
library is a freely distributable replacement for the discontinued 4.4 BSD
classic curses library.


%package -n libncurses5
Summary: The new curses text user interface library
Group: System Environment/Libraries

%description -n libncurses5
The curses library routines are a terminal-independent method of updating
character screens with reasonable optimization. This ncurses (new curses)
package contains the standard TUI (text user interface) libraries.


%package -n libncursesw5
Summary: The wide-character ncurses text user interface library
Group: System Envinronment/Libraries

%description -n libncursesw5
The curses library routines are a terminal-independent method of updating
character screens with reasonable optimization. This ncurses (new curses)
package contains the wide-character TUI (text user interface) libraries,
allowing internationalized programs that make use of the not-so standard
glyphs like Kanji and others.


%package terminfo
Summary: Information on several well-known terminal types
Group: System Environment/Base

%description terminfo
This package contains terminfo data files to support the most common types of
terminal, including ansi, dumb, linux, rxvt, screen, sun, vt100, vt102, vt220,
vt52, and xterm.


%package devel
Summary: Header files for developing NCurses-based programs
Group: Development/Libraries
Requires: libncurses5 = %{version}-%{release}
Requires: libncursesw5 = %{version}-%{release}

%description devel
The curses library routines are a terminal-independent method of updating
character screens with reasonable optimization. This package contains the
development headers needed when creating programs that make active use of
ncurses. It also brings the API documentation via manpages.



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
%{__mkdir_p} '%{buildroot}%{_libdir}'
%{__mkdir_p} '%{buildroot}%{_datadir}'
%{__mkdir_p} '%{buildroot}%{_includedir}'

pushd 'widec'
%{__make} install includedir='%{_includedir}/ncurses'
%{__mkdir_p} '%{buildroot}%{includedirw}'
%{__mv} '%{buildroot}%{_includedir}/ncurses'/* '%{buildroot}%{includedirw}'
popd

pushd 'narrowc'
%{__make} install includedir='%{_includedir}/ncurses'
popd

%{__ln_s} '%{_datadir}/terminfo/l/linux' \
	'%{buildroot}%{_datadir}/terminfo/c/console'
%{__ln_s} '%{_includedir}/ncurses/curses.h' \
	'%{buildroot}%{_includedir}/ncurses.h'

# Narrow char version is still the default; copy headers to include root dir
for header in curses.h unctrl.h eti.h form.h menu.h panel.h term.h
do
	%{__ln_s} "ncurses/${header}" "%{buildroot}%{_includedir}/${header}"
done

# Backwards compatibility with old curses library names
%{__ln_s} -f libncurses.a '%{buildroot}%{_libdir}/libcurses.a'
%{__ln_s} -f libncursesw.a '%{buildroot}%{_libdir}/libcursesw.a'

# Install old termcap file
%{__mkdir_p} '%{buildroot}%{_sysconfdir}'
%{__install} misc/terminfo.src '%{buildroot}%{_sysconfdir}/termcap'

# "Resetall" script
%{__install} -c '%{SOURCE3}' '%{buildroot}%{_bindir}/resetall'


%post -n libncurses5 -p %{__ldconfig}
%postun -n libncurses5 -p %{__ldconfig}
%post -n libncursesw5 -p %{__ldconfig}
%postun -n libncursesw5 -p %{__ldconfig}


%files
%defattr(-,root,root)
%doc README ANNOUNCE doc/html/announce.html
%attr(0755, root, root) %{_bindir}/resetall
%{_bindir}/captoinfo
%{_bindir}/clear
%{_bindir}/infocmp
%{_bindir}/infotocap
%{_bindir}/reset
%{_bindir}/tic
%{_bindir}/toe
%{_bindir}/tput
%{_bindir}/tset
%doc %{_mandir}/man1/captoinfo.1m*
%doc %{_mandir}/man1/clear.1*
%doc %{_mandir}/man1/infocmp.1m*
%doc %{_mandir}/man1/infotocap.1m*
%doc %{_mandir}/man1/reset.1*
%doc %{_mandir}/man1/tic.1m*
%doc %{_mandir}/man1/toe.1m*
%doc %{_mandir}/man1/tput.1*
%doc %{_mandir}/man1/tset.1*


%files terminfo
%defattr(-,root,root)
%doc README ANNOUNCE doc/html/announce.html
%config %attr(0644, root, root) %{_sysconfdir}/termcap
%dir %{_datadir}/terminfo
%{_datadir}/terminfo/*
%dir %{_datadir}/tabset
%{_datadir}/tabset/*
%{_libdir}/terminfo


%files -n libncurses5
%defattr(-,root,root)
%doc README ANNOUNCE doc/html/announce.html
%{_libdir}/libcurses.so
%{_libdir}/libncurses.so
%{_libdir}/libncurses.so.5*
%{_libdir}/libform.so
%{_libdir}/libform.so.5*
%{_libdir}/libmenu.so
%{_libdir}/libmenu.so.5*
%{_libdir}/libpanel.so
%{_libdir}/libpanel.so.5*


%files -n libncursesw5
%defattr(-,root,root)
%doc README ANNOUNCE doc/html/announce.html
%{_libdir}/libncursesw.so
%{_libdir}/libncursesw.so.5*
%{_libdir}/libformw.so
%{_libdir}/libformw.so.5*
%{_libdir}/libmenuw.so
%{_libdir}/libmenuw.so.5*
%{_libdir}/libpanelw.so
%{_libdir}/libpanelw.so.5*


%files devel
%defattr(-,root,root)
%doc README ANNOUNCE doc/html/announce.html
%doc test
%doc doc/html/hackguide.html
%doc doc/html/ncurses-intro.html
%doc c++/README*
%{_bindir}/ncurses5-config
%{_bindir}/ncursesw5-config
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
%{_libdir}/lib*.a
%doc %{_mandir}/man3/*.3x*
%doc %{_mandir}/man5/term.5*
%doc %{_mandir}/man5/terminfo.5*
%doc %{_mandir}/man7/term.7*
