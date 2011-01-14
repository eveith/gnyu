Name: procmail
Version: 3.22
Release: 1ev
Summary: A mail processing suite
URL: http://www.procmail.org/
Group: Applications/Mail
License: GPL-2
Vendor: GNyU-Linux
Source: http://www.procmail.org/procmail-%{version}.tar.gz
BuildRequires: make, gcc

%description
Procmail is a mail delivery agent (MDA) or mail filter, a program to process
incoming emails on a computer


%prep
	%setup -q


%build
	echo -e "\n" | %{__make} \
		CFLAGS0="${CFLAGS:-%{optflags}}" \
		CC="${CC:-%{_target_platform}-gcc}"


%install
	%{__mkdir_p} '%{buildroot}/%{_sysconfdir}'
	%{__mkdir_p} '%{buildroot}/%{_bindir}'
	%{__mkdir_p} '%{buildroot}/%{_mandir}'/man{1,5}
	%{__cp} new/lockfile new/procmail new/formail new/mailstat \
		'%{buildroot}/%{_bindir}'
	%{__cp} new/*.1 '%{buildroot}/%{_mandir}/man1'
	%{__cp} new/*.5 '%{buildroot}/%{_mandir}/man5'
	%{__touch} '%{buildroot}/%{_sysconfdir}/procmailrc'


%files
	%defattr(-, root, root)
	%doc COPYING FAQ FEATURES HISTORY KNOWN_BUGS README
	%doc examples/
	%ghost %config %{_sysconfdir}/procmailrc
	%attr(0755, root, root) %{_bindir}/formail
	%attr(0755, root, root) %{_bindir}/lockfile
	%attr(0755, root, root) %{_bindir}/mailstat
	%attr(0755, root, root) %{_bindir}/procmail
	%doc %{_mandir}/man1/formail.1*
	%doc %{_mandir}/man1/lockfile.1*
	%doc %{_mandir}/man1/procmail.1*
	%doc %{_mandir}/man5/procmailex.5*
	%doc %{_mandir}/man5/procmailrc.5*
	%doc %{_mandir}/man5/procmailsc.5*
