Name: readline
Version: 6.2
Release: 3.0
Summary: A set of methods for applications that allow users to edit command line
URL: http://cnswww.cns.cwru.edu/php/chet/readline/rltop.html
Group: System Environment/Libraries
License: GPL-3
Source: ftp://ftp.gnu.org/gnu/readline/readline-%{version}.tar.gz
BuildRequires: grep, make, gcc
BuildRequires: kernel-headers, eglibc-devel, ncurses-devel

%description
The Readline library provides a set of functions for use by applications that
allow users to edit command lines as they are typed in. Both Emacs and vi
editing modes are available. The Readline library includes additional
functions to maintain a list of previously-entered command lines, to recall
and perhaps reedit those lines, and perform csh-like history expansion on
previous commands.
This package contains the GNU Info documentation on both the readline and the
history library. It offers end-user documentation as well as developer
references.


%package -n libreadline6
Summary: A set of methods for applications that allow users to edit command line
Group: System Environment/Libraries

%description -n libreadline6
The Readline library provides a set of functions for use by applications that
allow users to edit command lines as they are typed in. Both Emacs and vi
editing modes are available. The Readline library includes additional
functions to maintain a list of previously-entered command lines, to recall
and perhaps reedit those lines, and perform csh-like history expansion on
previous commands.


%package devel
Summary: Readline development headers
Group: Development/Libraries

%description devel
The Readline library provides a set of functions for use by applications that
allow users to edit command lines as they are typed in.
This package contains the development headers and API reference in the form of
manpages.


%prep
%setup -q


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
update-info-dir


%post -n libreadline6 -p %{__ldconfig}


%postun
update-info-dir


%postun -n libreadline6 -p %{__ldconfig}


%files
%defattr(-, root, root)
%doc CHANGELOG CHANGES COPYING MANIFEST NEWS README USAGE
%doc %{_infodir}/history.info*
%doc %{_infodir}/readline.info*
%doc %{_infodir}/rluserman.info*


%files -n libreadline6
/%{_lib}/libreadline.so.6*
/%{_lib}/libhistory.so.6*


%files devel
%defattr(-, root, root)
%doc CHANGELOG CHANGES COPYING MANIFEST NEWS README USAGE
%doc examples
%doc %{_mandir}/man3/history.3*
%doc %{_mandir}/man3/readline.3*
%dir %{_includedir}/readline
%{_includedir}/readline/*.h
/%{_lib}/libhistory.a
/%{_lib}/libreadline.so
/%{_lib}/libreadline.a
/%{_lib}/libhistory.so
%dir %{_datadir}/readline
%{_datadir}/readline/*.c
