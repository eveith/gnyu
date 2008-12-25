Name: fcron
Version: 3.0.4
Release: 1ev
Summary: An enhanced cron daemon to schedule the execution of commands
URL: http://fcron.free.fr/
Group: System Environment/Base
License: GPL-2
Vendor: GNyU-Linux
Source0: http://fcron.free.fr/archives/fcron-%{version}.src.tar.gz
Source1: %{name}-fcron.i
Source2: %{name}-fcron.pamd
Source3: %{name}-fcrontab.pamd
Patch0: fcron-fcrontab_shell_error.diff
BuildRequires: make >= 3.79.1, libpam, gcc
Requires: %{_bindir}/sendmail, %{_bindir}/vim

%define _cron_uid 16
%define _cron_gid 29

%description
Fcron is a periodical command scheduler which aims at replacing vixie cron, so
it implements most of its functionality. It does not assume that your system
is running either all the time or regularly: you can, for instance, tell fcron
to execute tasks every x hours y minutes of system uptime or to do a job only
once in a specified interval of time. You can also set a nice value to a job,
run it depending on the system load average, and much more.


%prep
%setup -q


%build
%configure \
	--with-editor='%{_bindir}/vim' \
	--with-piddir='%{_localstatedir}/run' \
	--with-spooldir='%{_localstatedir}/spool/cron' \
	--with-pam \
	--without-selinux \
	--without-boot-install \
	--with-fifodir='%{_localstatedir}/tmp' \
	--with-sendmail='%{_bindir}/sendmail' \
	--with-username=cron \
	--with-groupname=cron
%{__make} %{?_smp_mflags}


%install
%{__make_install} DESTDIR='%{buildroot}'

pushd %{buildroot}

# Install service file for fcron
%{__mkdir_p} etc/initng/daemon
%{__cat} < '%{SOURCE1}' | \
	%{__sed} -e 's,@fcron@,%{_sbindir}/fcron,g' \
	> etc/initng/daemon/fcron.i

# We also need pam files, install them here.
%{__mkdir_p} etc/pam.d
[[ etc/pam.conf ]] && %{__rm} -f etc/pam.conf
%{__cat} < '%{SOURCE2}' > etc/pam.d/fcron
%{__cat} < '%{SOURCE3}' > etc/pam.d/fcrontab

# Create the fcron spool directory
%{__mkdir_p} ./%{_localstatedir}/spool/cron

# Link fcrontab to the traditional name to avoid confusion with scripts.
( cd ./%{_bindir}; %{__ln_s} fcrontab crontab; cd - )


# Install fcron config file.

%{__cat} << __EOF__ > etc/fcron.conf
# fcron.conf - Configuration file for fcron(8) and fcrontab(1).
#   See fcron.conf(5) for syntax and explanations.
#
# WARNING : this file must be owned by root:fcron and 640.
#

# The spool directory where fcron stores its files
fcrontabs   =   %{_localstatedir}/spool/cron

# The locations of the pid file and the fifo file
pidfile     =   %{_localstatedir}/run/fcron.pid
fifofile    =   %{_localstatedir}/tmp/fcron.fifo

# allow/deny files to determine which users are allowed to use fcrontab
fcronallow  =   %{_sysconfdir}/fcron.allow
fcrondeny   =   %{_sysconfdir}/fcron.deny

# Location of the programs used by fcron
shell       =   /bin/sh
sendmail    =   %{_bindir}/sendmail

# Location of the default editor for "fcrontab -e"
editor      =   %{_bindir}/vim
__EOF__


# Create /etc/cron.* directories
%{__mkdir_p} ./%{_sysconfdir}/cron.{hourly,daily,weekly}


# Finished. :-)
popd


%pre
if [[ "${1}" -eq 1 ]]
then
	userdel cron
	groupdel cron
	groupadd \
		-g %{_cron_gid} \
		cron
	useradd \
		-g cron \
		-u %{_cron_uid} \
		-s /sbin/nologin  \
		-d %{_localstatedir}/spool/cron \
	  	cron
fi > /dev/null 2>&1
exit 0

%preun
if [[ $1 -eq 0 ]]
then
	ngc -d daemon/fcron > /dev/null 2>&1
	ng-update del daemon/fcron > /dev/null 2>&1
fi
exit 0

%postun
if [[ $1 -eq 0 ]]
then
	userdel cron 
	groupdel cron
fi > /dev/null 2>&1
exit 0


%files
%defattr(-, root, root)
%doc MANIFEST VERSION doc/en doc/fr
%doc %{_datadir}/doc/%{name}-%{version}
%config(noreplace) %attr(0640, root, cron) %{_sysconfdir}/fcron.allow
%config(noreplace) %attr(0640, root, cron) %{_sysconfdir}/fcron.conf
%config(noreplace) %attr(0640, root, cron) %{_sysconfdir}/fcron.deny
%config(noreplace) %{_sysconfdir}/pam.d/fcron*
%attr(0750, root, root) %{_sysconfdir}/initng/daemon/fcron.i
%attr(6111, cron, cron) %{_bindir}/fcrondyn
%attr(4110, root, cron) %{_bindir}/fcronsighup
%attr(6111, cron, cron) %{_bindir}/fcrontab
%attr(6111, cron, cron) %{_bindir}/crontab
%attr(110, root, root) %{_sbindir}/fcron
%doc %{_mandir}/fr/man1/fcrondyn.1*
%doc %{_mandir}/fr/man1/fcrontab.1*
%doc %{_mandir}/fr/man3/bitstring.3*
%doc %{_mandir}/fr/man5/fcron.conf.5*
%doc %{_mandir}/fr/man5/fcrontab.5*
%doc %{_mandir}/fr/man8/fcron.8*
%doc %{_mandir}/man1/fcrondyn.1*
%doc %{_mandir}/man1/fcrontab.1*
%doc %{_mandir}/man3/bitstring.3*
%doc %{_mandir}/man5/fcron.conf.5*
%doc %{_mandir}/man5/fcrontab.5*
%doc %{_mandir}/man8/fcron.8*
%dir %attr(0770, cron, cron) %{_localstatedir}/spool/cron
%dir %{_sysconfdir}/cron.*
