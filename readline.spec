Name: readline
Version: 5.2
Release: 1ev
Summary: A set of methods for applications that allow users to edit command line
URL: http://cnswww.cns.cwru.edu/php/chet/readline/rltop.html
Group: System Environment/Libraries
License: GPL-2
Vendor: MSP Slackware
Source: ftp://ftp.gnu.org/gnu/readline/readline-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, ncurses

%description
The Readline library provides a set of functions for use by applications that
allow users to edit command lines as they are typed in. Both Emacs and vi
editing modes are available. The Readline library includes additional
functions to maintain a list of previously-entered command lines, to recall
and perhaps reedit those lines, and perform csh-like history expansion on
previous commands.


%prep
%setup -q


%build
%configure \
	--with-curses
%{__make} %{_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'

[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && %{__rm} -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
/sbin/ldconfig
update-info-dir

%postun
/sbin/ldconfig
update-info-dir


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc CHANGELOG CHANGES COPYING MANIFEST NEWS README USAGE
%{_includedir}/readline/
%doc %{_infodir}/history.info*
%doc %{_infodir}/readline.info*
%doc %{_infodir}/rluserman.info*
%{_libdir}/libreadline.*
%{_libdir}/libhistory.*
%doc %{_mandir}/man3/history.3*
%doc %{_mandir}/man3/readline.3*
