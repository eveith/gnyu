Name: findutils
Version: 4.4.2
Release: 1.0
Summary: Utilities for directory searching
URL: http://www.gnu.org/software/findutils
Group: System Environment/Base
License: GPL-3
Source: http://ftp.gnu.org/pub/gnu/findutils/findutils-%{version}.tar.gz
Source1: updatedb.sh
BuildRequires: grep, sed, make, gcc
BuildRequires: eglibc-devel, kernel-headers
BuildRequires: gettext-tools

%description
The GNU Find Utilities are the basic directory searching utilities of the GNU
operating system. These programs are typically used in conjunction with other
programs to provide modular and powerful directory search and file locating
capabilities to other commands.

The tools supplied with this package are:

find - search for files in a directory hierarchy
locate - list files in databases that match a pattern
updatedb - update a file name database
xargs - build and execute command lines from standard input 


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

%find_lang findutils

%{__mkdir_p} '%{buildroot}%{_sysconfdir}/cron.daily'
%{__install} -m 0700 -o root -g root %{SOURCE1} \
    '%{buildroot}%{_sysconfdir}/cron.daily'

%{__touch} '%{buildroot}%{_localstatedir}/locatedb'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%check
%{__make} check


%post
update-info-dir


%postun
update-info-dir


%files -f findutils.lang
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS COPYING ChangeLog README* NEWS THANKS TODO
%attr(0700, root, root) %{_sysconfdir}/cron.daily/updatedb.sh
%{_bindir}/find
%{_bindir}/oldfind
%{_bindir}/locate
%{_bindir}/updatedb
%{_bindir}/xargs
%{_libexecdir}/bigram
%{_libexecdir}/code
%{_libexecdir}/frcode
%doc %{_infodir}/find.info*
%doc %{_infodir}/find-maint.info*
%doc %{_mandir}/man1/find.1*
%doc %{_mandir}/man1/locate.1*
%doc %{_mandir}/man1/updatedb.1*
%doc %{_mandir}/man1/xargs.1*
%doc %{_mandir}/man5/locatedb.5*
%ghost %{_localstatedir}/locatedb
