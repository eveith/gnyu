Name: rottlog
Version: 0.70beta3
Release: 1ev
Summary: A system tool that rotates, compresses and archives logfiles
URL: http://www.gnu.org/software/rottlog/
Group: System Environment/Base
License: GPL
Vendor: MSP Slackware
Source: http://savannah.gnu.org/download/%{name}/%{name}-%{version}.tar.gz
BuildArch: noarch
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: make, coreutils, texinfo, sed
Requires: /bin/sh, bash, coreutils
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
%configure
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'

%{__mkdir_p} %{buildroot}/%{_bindir}
%{__make_install} DESTDIR='%{buildroot}' \
	sbindir='%{buildroot}/%{_sbindir}' \
	bindir='%{buildroot}/%{_bindir}' \
	sysconfdir='%{buildroot}/%{_sysconfdir}' \
	ROTT_ETCDIR='%{buildroot}/%{_sysconfdir}/rottlog' \
	ROTT_STATDIR='%{buildroot}/%{_localstatedir}/rottlog'

# Install logrotate-to-rottlog converter
%{__install} -m0755 src/Log2Rot %{buildroot}/%{_bindir}/log2rot

# Provide old logrotate directories for compatibility
%{__mkdir_p} %{buildroot}/etc/logrotate.d

# Create rottlog configuratation files and directories
%{__mkdir_p} %{buildroot}/%{_sysconfdir}/rottlog
touch %{buildroot}/%{_sysconfdir}/rottlog/{rc,daily,weekly,monthly,custom}

# Make sure rottlog is started every day by installing a file to cron.daily
%{__mkdir_p} %{buildroot}/%{_sysconfdir}/cron.daily

%{__cat} << __END__ > %{buildroot}/%{_sysconfdir}/cron.daily/rottlog
#!/bin/sh

[[ -r /etc/logrott/rc ]] || exit 1
%{_bindir}/logrott
__END__


# Remove installed info directory file, every system has its own
[[ -e %{buildroot}/%{_infodir}/dir ]] \
    && %{__rm} -f %{buildroot}/%{_infodir}/dir


# Correct links

pushd "$RPM_BUILD_ROOT/%{_bindir}"
for f in custom day month week
do
	rm -f viroot${f}
	ln -sf virottrc virott${f}
done
popd


%post
update-info-dir

%postun
update-info-dir


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog README* NEWS TODO VERSION rc/
/etc/logrotate.d
%attr(0300, root, root) %dir %{_sysconfdir}/rottlog
%{_sysconfdir}/rottlog/sample_*
%ghost %config(noreplace) %{_sysconfdir}/rottlog/rc
%ghost %config(noreplace) %{_sysconfdir}/rottlog/daily
%ghost %config(noreplace) %{_sysconfdir}/rottlog/weekly
%ghost %config(noreplace) %{_sysconfdir}/rottlog/monthly
%ghost %config(noreplace) %{_sysconfdir}/rottlog/custom
%attr(0700, root, root) %{_sysconfdir}/cron.daily/rottlog
%{_bindir}/*rot*
%{_infodir}/rottlog*.info*
%{_mandir}/*/rottlog*.*
