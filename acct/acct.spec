Name: acct
Version: 6.5.5
Release: 0.9
Summary: User-specific process accounting
URL: GPL-3
Group: System Environment/Base
License: http://www.gnu.org/directory/acct.html
Source: http://ftp.gnu.org/gnu/acct/acct-%{version}.tar.gz
BuildRequires: grep, sed, make, gcc
BuildRequires: eglibc-devel, linux-headers
Requires: /sbin/install-info

%description
This package contains the programs necessary for user-specific process
accounting: sa, accton, and lastcomm.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

%{__mkdir_p} '%{buildroot}%{_localstatedir}/log'
%{__touch} '%{buildroot}%{_localstatedir}/log/pacct'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
if [ "$1" -eq 1 ]; then
    /sbin/install-info %{_infodir}/accounting.info* %{_infodir}/dir
fi


%preun
if [ "$1" -eq 0 ]; then
    /sbin/install-info --delete %{_infodir}/accounting.info* %{_infodir}/dir
fi


%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO

%{_bindir}/ac
%{_bindir}/last
%{_bindir}/lastcomm

%{_sbindir}/accton
%{_sbindir}/dump-acct
%{_sbindir}/dump-utmp
%{_sbindir}/sa

%doc %{_infodir}/accounting.info*
%doc %{_mandir}/man1/ac.1*
%doc %{_mandir}/man1/last.1*
%doc %{_mandir}/man1/lastcomm.1*
%doc %{_mandir}/man8/accton.8*
%doc %{_mandir}/man8/dump-utmp.8*
%doc %{_mandir}/man8/sa.8*

%dir %attr(0750, root, root) %{_localstatedir}/log
%ghost %attr(0600, root, root) %{_localstatedir}/log/pacct
