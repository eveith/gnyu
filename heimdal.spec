Name: heimdal
Version: 1.2.1
Release: 2ev 
Summary: A Kerberos V implementation (client and server programs)
URL: http://www.h5l.org/
Group: System Environment/Libraries
License: BSD
Vendor: GNyU-Linux
Source0: http://www.h5l.org/dist/src/heimdal-%{version}.tar.gz
Source1: %{name}-profile.sh
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, pkg-config, gcc, bison
BuildRequires: openssl, openldap-libs, db >= 4.5, readline
Provides: kerberos5, krb5
Requires: %{name}-libs = %{version}-%{release}
%define krb_prefix %{_prefix}/heimdal

%description
	Heimdal is an implementation of Kerberos 5 that aims to be protocol compatible
	with existing implementations and RFC 1510. It is also reasonably compatible
	with the M.I.T Kerberos V5 API, supports Kerberos V5 over GSS-API (RFC 1964),
	includes a number of important and useful applications (rsh, telnet, popper,
	etc.), and is backwards compatible with Kerberos V4.
	This package contains Kerberos-enabled client programs, such as telnet, and
	their corresponding server daemons.


%package libs
Summary: Libraries for Kerberos-V-enabled software
Group: System Environment/Libraries
Provides: kerberos5, kerberos5-gssapi, kerberos5-libs, krb5-libs

%description libs
Kerberos is a network authentication system. The krb5-libs package
contains the shared libraries needed by Kerberos 5. If you are using
Kerberos, you need to install this package.


%package kdc
Group: System Environment/Daemons
Summary: Kerberos V key distribution centre
Requires: %{name}-libs = %{version}

%description kdc
This package includes the KDC (key distribution centre) server,
which is designed to run on a secure computer and keeps track
of users passwords. This is done using the Kerberos protocol in
such a way that the server computers do not need to know user's
passwords.
Heimdal is a free implementation of the Kerberos V protocol, that aims to be
compatible with MIT's kerberos software.


%package kcm
Group: System Environment/Daemons
Summary: Kerberos V key caching management
Requires: %{name}-libs = %{version}-%{release}

%description kcm
This package includes the KCM daemon.
The kcm daemon can hold the credentials for all users in the system.
Access control is done with Unix-like permissions.  The daemon checks the
access on all operations based on the uid and gid of the user.  The
tickets are renewed as long as is permitted by the KDC's policy.
Heimdal is a free implementation of the Kerberos V protocol, that aims to be
compatible with MIT's kerberos software.


%package servers
Group: System Environment/Daemons
Summary: Kerberos-V-enabled network service daemons
Requires: %{name}-%{libs} = %{version}

%description servers
Heimdal is a free implementation of Kerberos 5 that aims to be compatible 
with MIT Kerberos. 
This package includes servers such as telnetd and ftpd that have been
compiled with Heimdal support.


%prep
%setup -q


%build
%configure \
	--bindir='%{krb_prefix}/bin' \
	--sbindir='%{krb_prefix}/sbin' \
	--mandir='%{krb_prefix}/man' \
	--datadir='%{krb_prefix}/share' \
	--libexecdir='%{krb_prefix}/libexec' \
	--enable-pthread-support 
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

# Per-login profile script to add (man-) path
%{__mkdir_p} '%{buildroot}/etc/profile.d'
%{__cat} < '%{SOURCE1}' | %{__m2rpath} \
	> '%{buildroot}/etc/profile.d/%{name}.sh'

%{__mkdir_p} '%{buildroot}/%{_sysconfdir}'
%{__touch} '%{buildroot}/%{_sysconfdir}/krb5.conf'

# Delete doublettes
%{__rm} -rf '%{buildroot}/%{krb_prefix}/man'/cat?


%post libs
%{__ldconfig}
update-info-dir

%postun libs
%{__ldconfig}
update-info-dir


%files
%defattr(-, root, root)
%doc ChangeLog* NEWS README TODO*
%dir %{krb_prefix}/bin
%{krb_prefix}/bin/afslog
%{krb_prefix}/bin/ftp
%{krb_prefix}/bin/gss
%{krb_prefix}/bin/hxtool
%{krb_prefix}/bin/idn-lookup
%{krb_prefix}/bin/kauth
%{krb_prefix}/bin/kdestroy
%{krb_prefix}/bin/kf
%{krb_prefix}/bin/kgetcred
%{krb_prefix}/bin/kinit
%{krb_prefix}/bin/klist
%{krb_prefix}/bin/kpasswd
%{krb_prefix}/bin/kswitch
%{krb_prefix}/bin/kx
%{krb_prefix}/bin/login
%{krb_prefix}/bin/otpprint
%{krb_prefix}/bin/pagsh
%{krb_prefix}/bin/pfrom
%{krb_prefix}/bin/rcp
%{krb_prefix}/bin/rsh
%{krb_prefix}/bin/rxtelnet
%{krb_prefix}/bin/rxterm
%{krb_prefix}/bin/string2key
%{krb_prefix}/bin/telnet
%{krb_prefix}/bin/tenletxr
%{krb_prefix}/bin/verify_krb5_conf
%{krb_prefix}/bin/xnlock
%dir %{krb_prefix}/sbin
%{krb_prefix}/sbin/ktutil
%attr(4755, root, root) %{krb_prefix}/bin/otp
%attr(4755, root, root) %{krb_prefix}/bin/su
%dir %{krb_prefix}/libexec
%{krb_prefix}/libexec/kimpersonate
%{krb_prefix}/libexec/popper
%{krb_prefix}/libexec/ftpd
%{krb_prefix}/libexec/kdigest
%{krb_prefix}/libexec/rshd
%{krb_prefix}/libexec/telnetd
%dir %{krb_prefix}/man
%dir %{krb_prefix}/man/man1
%doc %{krb_prefix}/man/man1/afslog.1*
%doc %{krb_prefix}/man/man1/ftp.1*
%doc %{krb_prefix}/man/man1/kauth.1*
%doc %{krb_prefix}/man/man1/kdestroy.1*
%doc %{krb_prefix}/man/man1/kf.1*
%doc %{krb_prefix}/man/man1/kgetcred.1*
%doc %{krb_prefix}/man/man1/kimpersonate.1*
%doc %{krb_prefix}/man/man1/kinit.1*
%doc %{krb_prefix}/man/man1/klist.1*
%doc %{krb_prefix}/man/man1/kpasswd.1*
%doc %{krb_prefix}/man/man1/kx.1*
%doc %{krb_prefix}/man/man1/login.1*
%doc %{krb_prefix}/man/man1/otp.1*
%doc %{krb_prefix}/man/man1/otpprint.1*
%doc %{krb_prefix}/man/man1/pagsh.1*
%doc %{krb_prefix}/man/man1/pfrom.1*
%doc %{krb_prefix}/man/man1/rcp.1*
%doc %{krb_prefix}/man/man1/rsh.1*
%doc %{krb_prefix}/man/man1/rxtelnet.1*
%doc %{krb_prefix}/man/man1/rxterm.1*
%doc %{krb_prefix}/man/man1/su.1*
%doc %{krb_prefix}/man/man1/telnet.1*
%doc %{krb_prefix}/man/man1/tenletxr.1*
%doc %{krb_prefix}/man/man1/xnlock.1*
%dir %{krb_prefix}/man/man5
%doc %{krb_prefix}/man/man5/ftpusers.5
%doc %{krb_prefix}/man/man5/login.access.5
%dir %{krb_prefix}/man/man8
%doc %{krb_prefix}/man/man8/ftpd.8
%doc %{krb_prefix}/man/man8/popper.8
%doc %{krb_prefix}/man/man8/rshd.8
%doc %{krb_prefix}/man/man8/telnetd.8
%doc %{krb_prefix}/man/man8/ktutil.8*
%doc %{krb_prefix}/man/man8/string2key.8*
%doc %{krb_prefix}/man/man8/verify_krb5_conf.8*

%files kdc
%defattr(-, root, root)
%dir %{krb_prefix}/sbin
%{krb_prefix}/sbin/iprop-log
%{krb_prefix}/sbin/kadmin
%{krb_prefix}/sbin/kstash
%dir %{krb_prefix}/libexec
%{krb_prefix}/libexec/kdc
%{krb_prefix}/libexec/kfd
%{krb_prefix}/libexec/hprop
%{krb_prefix}/libexec/hpropd
%{krb_prefix}/libexec/ipropd-master
%{krb_prefix}/libexec/ipropd-slave
%{krb_prefix}/libexec/kadmind
%{krb_prefix}/libexec/kpasswdd
%{krb_prefix}/libexec/push
%{krb_prefix}/libexec/kxd
%dir %{krb_prefix}/man
%dir %{krb_prefix}/man/man8
%doc %{krb_prefix}/man/man8/kadmin.8*
%doc %{krb_prefix}/man/man8/kdc.8*
%doc %{krb_prefix}/man/man8/kfd.8*
%doc %{krb_prefix}/man/man8/kstash.8*
%doc %{krb_prefix}/man/man8/hprop.8*
%doc %{krb_prefix}/man/man8/hpropd.8*
%doc %{krb_prefix}/man/man8/iprop.8*
%doc %{krb_prefix}/man/man8/iprop-log.8*
%doc %{krb_prefix}/man/man8/ipropd-master.8*
%doc %{krb_prefix}/man/man8/ipropd-slave.8*
%doc %{krb_prefix}/man/man8/kadmind.8*
%doc %{krb_prefix}/man/man8/kpasswdd.8*
%doc %{krb_prefix}/man/man8/push.8*
%doc %{krb_prefix}/man/man8/kxd.8*
%{_libdir}/libkdc.*
%{_includedir}/kdc*.h

%files kcm
%defattr(-, root, root)
%dir %{krb_prefix}/libexec
%{krb_prefix}/libexec/kcm
%dir %{krb_prefix}/man
%dir %{krb_prefix}/man/man8
%doc %{krb_prefix}/man/man8/kcm.8*

%files libs
%defattr(-, root, root)
%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/krb5.conf
%attr(0755, root, root) %{_sysconfdir}/profile.d/heimdal.sh
%{_includedir}/asn1_err.h
%{_includedir}/base64.h
%{_includedir}/cms_asn1.h
%{_includedir}/der-protos.h
%{_includedir}/der.h
%{_includedir}/digest_asn1.h
%{_includedir}/editline.h
%{_includedir}/getarg.h
%{_includedir}/gssapi.h
%dir %{_includedir}/gssapi
%{_includedir}/gssapi/gkrb5_err.h
%{_includedir}/gssapi/gssapi.h
%{_includedir}/gssapi/gssapi_krb5.h
%{_includedir}/gssapi/gssapi_spnego.h
%{_includedir}/hdb-protos.h
%{_includedir}/hdb.h
%{_includedir}/hdb_asn1.h
%{_includedir}/hdb_err.h
%{_includedir}/heim_asn1.h
%{_includedir}/heim_err.h
%{_includedir}/heimntlm-protos.h
%{_includedir}/heimntlm.h
%{_includedir}/hex.h
%{_includedir}/hx509-protos.h
%{_includedir}/hx509.h
%{_includedir}/hx509_err.h
%{_includedir}/k524_err.h
%dir %{_includedir}/kadm5
%{_includedir}/kadm5/admin.h
%{_includedir}/kadm5/kadm5-private.h
%{_includedir}/kadm5/kadm5-protos.h
%{_includedir}/kadm5/kadm5_err.h
%{_includedir}/kadm5/private.h
%{_includedir}/kafs.h
%{_includedir}/krb5-private.h
%{_includedir}/krb5-protos.h
%{_includedir}/krb5-types.h
%{_includedir}/krb5.h
%dir %{_includedir}/krb5
%{_includedir}/krb5/locate_plugin.h
%{_includedir}/krb5/windc_plugin.h
%{_includedir}/krb5_asn1.h
%{_includedir}/krb5_ccapi.h
%{_includedir}/krb5_err.h
%{_includedir}/kx509_asn1.h
%{_includedir}/otp.h
%{_includedir}/parse_bytes.h
%{_includedir}/parse_time.h
%{_includedir}/parse_units.h
%{_includedir}/pkcs12_asn1.h
%{_includedir}/pkcs8_asn1.h
%{_includedir}/pkcs9_asn1.h
%{_includedir}/pkinit_asn1.h
%{_includedir}/resolve.h
%{_includedir}/rfc2459_asn1.h
%{_includedir}/roken-common.h
%{_includedir}/roken.h
%dir %{_includedir}/roken
%{_includedir}/roken/glob.h
%{_includedir}/roken/vis.h
%{_includedir}/rtbl.h
%{_includedir}/sl.h
%{_includedir}/wind.h
%{_includedir}/wind_err.h
%{_includedir}/xdbm.h
%doc %{_infodir}/heimdal.info*
%doc %{_infodir}/hx509.info
%{_libdir}/libasn1.*
%{_libdir}/libeditline.*
%{_libdir}/libgssapi.*
%{_libdir}/libhdb.*
%{_libdir}/libheimntlm.*
%{_libdir}/libhx509.*
%{_libdir}/libkadm5clnt.*
%{_libdir}/libkadm5srv.*
%{_libdir}/libkafs.*
%{_libdir}/libkrb5.*
%{_libdir}/libotp.*
%{_libdir}/libroken.*
%{_libdir}/libsl.*
%{_libdir}/libwind.*
%{_libdir}/windc.*
%{_libdir}/pkgconfig/heimdal-gssapi.pc
%dir %{krb_prefix}
%dir %{krb_prefix}/bin
%{krb_prefix}/bin/krb5-config
%dir %{krb_prefix}/man
%dir %{krb_prefix}/man/man1
%doc %{krb_prefix}/man/man1/krb5-config.1*
%dir %{krb_prefix}/man/man3
%doc %{krb_prefix}/man/man3/*.3*
%dir %{krb_prefix}/man/man5
%doc %{krb_prefix}/man/man5/mech.5*
%doc %{krb_prefix}/man/man5/krb5.conf.5*
%doc %{krb_prefix}/man/man5/qop.5*
%dir %{krb_prefix}/man/man8
%doc %{krb_prefix}/man/man8/kerberos.8*
