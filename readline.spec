Name: readline
Version: 6.1
Release: 2.0ev
Summary: A set of methods for applications that allow users to edit command line
URL: http://cnswww.cns.cwru.edu/php/chet/readline/rltop.html
Group: System Environment/Libraries
License: GPL-3
Vendor: GNyU-Linux
Source: ftp://ftp.gnu.org/gnu/readline/readline-%{version}.tar.gz
Patch1: %{name}-%{version}-001.patch
BuildRequires: make, gcc, ncurses

%description
The Readline library provides a set of functions for use by applications that
allow users to edit command lines as they are typed in. Both Emacs and vi
editing modes are available. The Readline library includes additional
functions to maintain a list of previously-entered command lines, to recall
and perhaps reedit those lines, and perform csh-like history expansion on
previous commands.


%prep
%setup -q
%patch1 -p0


%build
%configure \
	--libdir='/%{_lib}' \
	--enable-multibyte \
	--with-curses
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && %{__rm} -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
%{__ldconfig}
update-info-dir


%postun
%{__ldconfig}
update-info-dir


%files
%defattr(-, root, root)
%doc CHANGELOG CHANGES COPYING MANIFEST NEWS README USAGE
%doc examples
%doc %{_infodir}/history.info*
%doc %{_infodir}/readline.info*
%doc %{_infodir}/rluserman.info*
%doc %{_mandir}/man3/history.3*
%doc %{_mandir}/man3/readline.3*
%dir %{_includedir}/readline
%{_includedir}/readline/*.h
%dir %{_datadir}/readline
%{_datadir}/readline/*.c
/%{_lib}/libreadline.*
/%{_lib}/libhistory.*
