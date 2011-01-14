Name: bacula
Version: 5.0.1
Release: 1.0ev
Summary: An open-source backup solution
URL: http://www.bacula.org
Group: Applications/Backup
License: GPL-2
Vendor: GNyU-Linux
Source0: https://sourceforge.net/projects/bacula/files/bacula/%{version}/bacula-%{version}.tar.gz
Source1: %{name}-bacula-sd.ii
Source2: %{name}-bacula-dir.ii
Source3: %{name}-bacula-fd.ii
BuildRequires: sed, gawk, grep, make, gcc, gcc-g++, libtool, pkg-config >= 0.20
BuildRequires: python >= 2.2, gettext, gettext-tools, psmisc
BuildRequires: zlib, openssl, mysql-libs, ncurses, readline, libacl, libattr
BuildRequires: qt4 >= 4.2
%define bacula_uid 510
%define bacula_gid 58

%description
Bacula is an open source, enterprise level computer backup system for
heterogeneous networks. It is designed to automate backup tasks that had often
required intervention from a systems administrator or computer operator.
This package contains common software shared by directory, storage and file
daemon alike.


%package director
Summary: Bacula Director
Group: Applications/Backup

%description director
The Bacula Director (bacula-dir) is the heart of a bacula system. It
orchestrates the various tasks, stores file and catalog information and
triggers backup, recovery or verify tasks.


%package storage
Summary: Bacula storage service
Group: Applications/Backup

%description storage
The Bacula Storage Daemon (bacula-fd) constructs the receiving end of a bacula
installation and offers storage space to back up to or restore from. It can
run on the same or a different machine than the director and accesses a wide
range of storage devices, e.g. tapes and DVDs, and supports backing up to a
file system.


%package file
Summary: Bacula File (client) services
Group: Applications/Backup

%description file
Bacula's File Daemon (bacula-fd) makes up the client side of a bacula
installation. It is accessed from a bacula director and sends the files that
are to be backed up to a storage server.


%package bat
Summary: A Qt4 frontend to Bacula (Bacula Administration Tool)
Group: Applications/Backup

%description bat
BAT, the Bacula Administration Tool, is a frontend to bacula's various
services, mostly the director. It helps organizing various bacula tasks, e.g.
manually starting backup, restore or verify procedures. Its feature set is
richer than that of the "bconsole" command.


%prep
%setup -q


%build
%configure \
	--sysconfdir='%{_sysconfdir}/bacula' \
	--with-dir-user=bacula \
	--with-dir-group=bacula \
	--with-sd-user=bacula \
	--with-sd-group=bacula \
	--with-fd-user=root \
	--with-fd-group=root \
	--with-scriptdir='%{_libexecdir}/bacula' \
	--enable-bat \
	--with-mysql \
	--with-working-dir='%{_localstatedir}/lib/bacula/working' \
	--with-bsrdir='%{_localstatedir}/lib/bacula/bsr' \
	--with-log-dir='%{_localstatedir}/log/bacula'
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

# Drop init-like scripts from packages because we use InitNG.
%{__rm} '%{buildroot}%{_libexecdir}/bacula'/{bacula,bacula-ctl-*} ||:
%{__rm} '%{buildroot}%{_sbindir}/bacula' ||:
%{__rm} '%{buildroot}%{_libexecdir}/bacula'/{start,stop}mysql ||:
%{__rm} '%{buildroot}%{_libexecdir}/bacula'/btraceback.* ||:

# Manpages for programs that aren't built
%{__rm} '%{buildroot}%{_mandir}/man1'/bacula-{bwxconsole,tray-monitor}.1* ||:

%{__mkdir_p} '%{buildroot}%{_localstatedir}/lib/bacula'/{working,bsr}
%{__mkdir_p} '%{buildroot}%{_localstatedir}/log/bacula'

%{install_ifile %{SOURCE1} daemon/bacula-sd.i}
%{install_ifile %{SOURCE2} daemon/bacula-dir.i}
%{install_ifile %{SOURCE3} daemon/bacula-fd.i}

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
	&& %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
%{__ldconfig}


%pre
if [[ "${1}" -eq 0 ]]; then
	%{__groupadd} \
		-g '%{bacula_gid}' \
		bacula
	%{__useradd} \
		-u '%{bacula_uid}' \
		-g '%{bacula_gid}' \
		-c 'Bacula Service User' \
		-s /sbin/nologin \
		-d '%{_sysconfdir}/bacula' \
		bacula
fi


%postun
%{__ldconfig}
if [[ "${1}" -eq 0 ]]; then
	%{__userdel} bacula
	%{__groupdel} bacula
fi


%files
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS ChangeLog COPYING COPYRIGHT LICENSE README SUPPORT
%doc technotes examples Patchnotes ReleaseNotes
%config(noreplace) %{_sysconfdir}/bacula/bconsole.conf
%attr(0710, root, root) %{_sbindir}/bconsole
%attr(0710, root, root) %{_sbindir}/bsmtp
%attr(0710, root, root) %{_sbindir}/btraceback
%{_libdir}/bpipe-fd.so
%{_libdir}/libbac.*
%{_libdir}/libbac-%{version}.*
%{_libdir}/libbaccfg.*
%{_libdir}/libbaccfg-%{version}.*
%{_libdir}/libbacfind.*
%{_libdir}/libbacfind-%{version}.*
%{_libdir}/libbacpy.*
%{_libdir}/libbacpy-%{version}.*
%{_libdir}/libbacsql.*
%{_libdir}/libbacsql-%{version}.*
%{_libexecdir}/bacula/bconsole
%{_libexecdir}/bacula/bacula_config
%doc %{_mandir}/man8/bacula.8*
%doc %{_mandir}/man8/bconsole.8*
%doc %{_mandir}/man8/btraceback.8*
%doc %{_mandir}/man1/bsmtp.1*
%dir %{_datadir}/doc/bacula
%dir %{_datadir}/doc/bacula/html
%doc %{_datadir}/doc/bacula/html/*.*
%doc %{_datadir}/doc/bacula/ChangeLog
%doc %{_datadir}/doc/bacula/INSTALL
%doc %{_datadir}/doc/bacula/LICENSE
%doc %{_datadir}/doc/bacula/README
%doc %{_datadir}/doc/bacula/ReleaseNotes
%doc %{_datadir}/doc/bacula/VERIFYING
%doc %{_datadir}/doc/bacula/technotes
%dir %{_localstatedir}/log/bacula
%dir %{_localstatedir}/lib/bacula
%dir %{_localstatedir}/lib/bacula/bsr
%dir %{_localstatedir}/lib/bacula/working


%files storage
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS ChangeLog COPYING COPYRIGHT LICENSE README SUPPORT
%doc technotes examples Patchnotes ReleaseNotes
%attr(0660, bacula, root) %config(noreplace) %{_sysconfdir}/bacula/bacula-sd.conf
%attr(0700, root, root) %{_sysconfdir}/initng/daemon/bacula-sd.i
%attr(0710, bacula, root) %{_sbindir}/bacula-sd
%{_sbindir}/bcopy
%{_sbindir}/bextract
%{_sbindir}/bls
%{_sbindir}/bscan
%{_sbindir}/btape
%doc %{_mandir}/man8/bacula-sd.8*
%doc %{_mandir}/man8/bcopy.8*
%doc %{_mandir}/man8/bextract.8*
%doc %{_mandir}/man8/bls.8*
%doc %{_mandir}/man8/bscan.8*
%doc %{_mandir}/man8/btape.8*
%{_libexecdir}/bacula/disk-changer
%{_libexecdir}/bacula/dvd-handler
%{_libexecdir}/bacula/mtx-changer
%config(noreplace) %{_libexecdir}/bacula/mtx-changer.conf


%files director
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS ChangeLog COPYING COPYRIGHT LICENSE README SUPPORT
%doc technotes examples Patchnotes ReleaseNotes
%attr(0700, root, root) %{_sysconfdir}/initng/daemon/bacula-dir.i
%attr(0660, bacula, root) %config(noreplace) %{_sysconfdir}/bacula/bacula-dir.conf
%attr(0710, bacula, root) %{_sbindir}/bacula-dir
%{_sbindir}/bregex
%{_sbindir}/bwild
%{_sbindir}/dbcheck
%doc %{_mandir}/man8/bacula-dir.8*
%doc %{_mandir}/man8/dbcheck.8*
%{_libexecdir}/bacula/create_bacula_database
%{_libexecdir}/bacula/create_mysql_database
%{_libexecdir}/bacula/delete_catalog_backup
%{_libexecdir}/bacula/drop_bacula_database
%{_libexecdir}/bacula/drop_bacula_tables
%{_libexecdir}/bacula/drop_mysql_database
%{_libexecdir}/bacula/drop_mysql_tables
%{_libexecdir}/bacula/grant_bacula_privileges
%{_libexecdir}/bacula/grant_mysql_privileges
%{_libexecdir}/bacula/make_bacula_tables
%{_libexecdir}/bacula/make_catalog_backup
%{_libexecdir}/bacula/make_catalog_backup.pl
%{_libexecdir}/bacula/make_mysql_tables
%{_libexecdir}/bacula/update_bacula_tables
%{_libexecdir}/bacula/update_mysql_tables
%{_libexecdir}/bacula/query.sql


%files file
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS ChangeLog COPYING COPYRIGHT LICENSE README SUPPORT
%doc technotes examples Patchnotes ReleaseNotes
%attr(0640, root, root) %config %{_sysconfdir}/bacula/bacula-fd.conf
%attr(0700, root, root) %{_sysconfdir}/initng/daemon/bacula-fd.i
%attr(0710, root, root) %{_sbindir}/bacula-fd
%doc %{_mandir}/man8/bacula-fd.8*


%files bat
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS ChangeLog COPYING COPYRIGHT LICENSE README SUPPORT
%doc technotes examples Patchnotes ReleaseNotes
%config(noreplace) %{_sysconfdir}/bacula/bat.conf
%{_sbindir}/bat
%doc %{_mandir}/man1/bat.1*
