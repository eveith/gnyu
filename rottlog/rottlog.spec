Name: rottlog
Version: 0.72.1
Release: 2.0ev
Summary: A system tool that rotates, compresses and archives logfiles
URL: http://www.gnu.org/software/rottlog
Group: System Environment/Base
License: GPL-3
Vendor: GNyU-Linux
Source: ftp://ftp.gnu.org/gnu/rottlog/rottlog-%{version}.tar.gz
BuildArch: noarch
BuildRequires: sed, make, texinfo, findutils, util-linux-ng, bzip2, gzip
Requires: bash, coreutils, util-linux-ng, findutils, bzip2, gzip
Provides: logrotate

%description
This is a powerful BASH script to archive/rotate system logs. It have almost
all features of RedHat, SuSE and Debian logrotate, adding many other.
It's very easy to use and understand. Using Meta Variables and another
rotation algorithm it is possible to rotate logs in a way that a file rotated
once is never touched again before its deletion, making log rotation much more
compatible with host-based intrusion detection schemes like aide. 


%prep
%setup -q


%build
LOCK_FILE='%{_localstatedir}/lock/rottlog' %configure
%{__make} %{?_smp_mflags}
%{__make} check


%install
for i in '%{_bindir}' '%{_localstatedir}/lock'; do
	%{__mkdir_p} "%{buildroot}${i}"
done

%{__fakeroot} %{__make} install DESTDIR='%{buildroot}' \
	bindir='%{buildroot}%{_bindir}' \
	ROTT_STATDIR='%{buildroot}%{_localstatedir}/lib/rottlog' \
	ROTT_ETCDIR='%{buildroot}%{_sysconfdir}/rottlog'

# Install logrotate-to-rottlog converter
%{__install} src/Log2Rot '%{buildroot}%{_bindir}/log2rot'

# Provide old logrotate directories for compatibility
%{__mkdir_p} %{buildroot}/etc/logrotate.d

# Create rottlog configuratation files and directories
%{__mkdir_p} '%{buildroot}%{_sysconfdir}/rottlog'
%{__touch} '%{buildroot}%{_sysconfdir}'/rottlog/{rc,daily,weekly,monthly,custom}

%{__touch} '%{buildroot}%{_localstatedir}/lock/rottlog'

# Make sure rottlog is started every day by installing a file to cron.daily
%{__mkdir_p} '%{buildroot}%{_sysconfdir}/cron.daily'
%{__cat} << __END__ > '%{buildroot}%{_sysconfdir}/cron.daily/rottlog'
#!/bin/sh

[[ -r '%{_sysconfdir}logrott/rc' ]] || exit 1
%{_bindir}/logrott
__END__

[[ -e %{buildroot}/%{_infodir}/dir ]] \
    && %{__rm} -f %{buildroot}/%{_infodir}/dir


%post
update-info-dir


%postun
update-info-dir


%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog README* NEWS TODO VERSION rc/
%attr(0700, root, root) %dir %{_sysconfdir}/logrotate.d
%attr(0700, root, root) %dir %{_sysconfdir}/rottlog
%attr(0660, root, adm) %ghost %config(noreplace) %{_sysconfdir}/rottlog/rc
%attr(0660, root, adm) %ghost %config(noreplace) %{_sysconfdir}/rottlog/daily
%attr(0660, root, adm) %ghost %config(noreplace) %{_sysconfdir}/rottlog/weekly
%attr(0660, root, adm) %ghost %config(noreplace) %{_sysconfdir}/rottlog/monthly
%attr(0660, root, adm) %ghost %config(noreplace) %{_sysconfdir}/rottlog/custom
%attr(0700, root, root) %{_sysconfdir}/cron.daily/rottlog
%attr(0750, root, adm) %{_bindir}/rottlog
%{_bindir}/log2rot
%doc %{_infodir}/rottlog.info*
%ghost %{_localstatedir}/lock/rottlog
%dir %{_localstatedir}/lib/rottlog
