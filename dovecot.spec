Name: dovecot
Version: 1.1.9
Release: 1ev
Summary: A very secure and robust IMAP server
URL: http://www.dovecot.org/
Group: Networking/Servers/IMAP
License: MIT, LGPL-2
Vendor: GNyU-Linux
Source0: http://www.dovecot.org/releases/1.1/dovecot-%{version}.tar.gz
Source1: %{name}-dovecot.ii
BuildRequires: make, gcc, cyrus-sasl, openssl, libcap2, libpam
BuildRequires(install): ucspi-tcp
Requires: ucspi-tcp

%description
Dovecot is an open source IMAP and POP3 server that is written primarly with
security in mind. It is fast, simple to set up and has a small memory
footprint. Dovecot supprts reading mails from Maildir and mbox and maintains
its indexes transparently. Thus, it maintains compatibility without giving up
on performance.


%prep
%setup -q


%build
%configure \
	--with-passwd \
	--with-nss \
	--with-passwd-file \
	--with-shadow \
	--with-pam \
	--with-checkpassword \
	--with-zlib \
	--with-bzlib \
	--with-ssl=openssl \
	--with-ssldir='%{_sysconfdir}/ssl' \
	--with-rundir='%{_localstatedir}/run/dovecot' \
	--with-statedir='' \
	--with-pop3d \
	--with-docs
%{__make} %{?_smp_mflags}


%install
%{__make_install} DESTDIR='%{buildroot}'

# Documentation is always installed in %{_datadir}/doc, but we want to be
# flexible
%{__rm_rf} '%{buildroot}/%{_datadir}/doc'

%{__rm} -f '%{buildroot}/%{_sysconfdir}'/*-example.conf
%{__touch} '%{buildroot}/%{_sysconfdir}/dovecot.conf'
%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/ssl/certs'
%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/ssl/private'
%{__touch} '%{buildroot}/%{_sysconfdir}/ssl/certs/dovecot.pem'
%{__touch} '%{buildroot}/%{_sysconfdir}/ssl/private/dovecot.pem'

# Install ifile
%install_ifile '%{SOURCE1}' daemon/dovecot.i


%postun
if [[ "${1}" -eq 0 ]]
then
	for i in daemon/dovecot/pop3 daemon/dovecot/imap daemon/dovecot
	do
		ngc -d "${i}"
		ng-update delete "${i}" default
	done
fi > /dev/null 2>&1
exit 0


%files
%defattr(-, root, root)
%doc COPYING* AUTHORS ChangeLog dovecot-example.conf NEWS README TODO doc/wiki
%doc doc/*.txt doc/*.conf doc/*.cnf doc/solr-schema.xml doc/mkcert.sh
%ghost %config %{_sysconfdir}/ssl/certs/dovecot.pem
%ghost %config %{_sysconfdir}/ssl/private/dovecot.pem
%ghost %attr(0600, root, root) %config %{_sysconfdir}/dovecot.conf
%attr(0700, root, root) %{_sysconfdir}/initng/daemon/dovecot.i
%{_sbindir}/dovecot
%{_sbindir}/dovecotpw
%dir %{_libdir}/dovecot
%dir %{_libdir}/dovecot/auth
%dir %{_libdir}/dovecot/imap
%{_libdir}/dovecot/imap/*
%dir %{_libdir}/dovecot/lda
%{_libdir}/dovecot/lda/*
%dir %{_libdir}/dovecot/pop3
%{_libdir}/dovecot/pop3/*
%{_libdir}/dovecot/lib01_acl_plugin.*
%{_libdir}/dovecot/lib02_lazy_expunge_plugin.*
%{_libdir}/dovecot/lib10_quota_plugin.*
%{_libdir}/dovecot/lib11_trash_plugin.*
%{_libdir}/dovecot/lib20_convert_plugin.*
%{_libdir}/dovecot/lib20_expire_plugin.*
%{_libdir}/dovecot/lib20_fts_plugin.*
%{_libdir}/dovecot/lib20_mail_log_plugin.*
%{_libdir}/dovecot/lib20_mbox_snarf_plugin.*
%{_libdir}/dovecot/lib20_zlib_plugin.*
%{_libdir}/dovecot/lib21_fts_squat_plugin.*
%dir %{_libexecdir}/dovecot
%{_libexecdir}/dovecot/checkpassword-reply
%{_libexecdir}/dovecot/convert-tool
%{_libexecdir}/dovecot/deliver
%{_libexecdir}/dovecot/dict
%{_libexecdir}/dovecot/dovecot-auth
%{_libexecdir}/dovecot/expire-tool
%{_libexecdir}/dovecot/gdbhelper
%{_libexecdir}/dovecot/idxview
%{_libexecdir}/dovecot/imap
%{_libexecdir}/dovecot/imap-login
%{_libexecdir}/dovecot/listview
%{_libexecdir}/dovecot/logview
%{_libexecdir}/dovecot/maildirlock
%{_libexecdir}/dovecot/pop3
%{_libexecdir}/dovecot/pop3-login
%{_libexecdir}/dovecot/rawlog
%{_libexecdir}/dovecot/ssl-build-param
