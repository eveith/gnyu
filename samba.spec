Name: samba
Version: 3.4.2
Release: 3ev
Summary: SMB and CIFS file exchange client tools and server
URL: http://www.samba.org/
Group: System Environment/Daemons
License: GPL-3
Vendor: GNyU-Linux
Source0: http://www.samba.org/samba/ftp/stable/samba-%{version}.tar.gz
Source1: %{name}-smbd.i
Source2: %{name}-nmbd.i
Source3: %{name}-winbindd.i
BuildRequires: pkg-config >= 0.9.0, make, gcc, perl
BuildRequires: readline, libattr, libutempter, libcap2, libacl
BuildRequires: libpam, gnutls, openldap-libs, heimdal-libs
BuildRequires: cups, perl-Net-LDAP, zlib, openssl, popt
Requires: samba-libs = %{version}

%description
A common file exchange format in the windows world is SMB and its successor,
CIFS. The Samba suite (SaMBa is a play on the abbreviation SMB, which stands
for Server Message Block) allows a Unix machine to mount windows shares,
authenticate against a Windows server, and so forth. In short it aims to
integrate the Unix machine into a Microsoft Windows network.
The Samba Server and its daemons enable a machine to be part of a Windows
domain or even replace a Windows NT 4.0 primary domain controller, depending 
on the configuration settings made.


%package libs
Summary: SMB and CIFS client libraries
Group: System Environment/Libraries

%description libs
A common file exchange format in the windows world is SMB and its successor,
CIFS. The Samba suite (SaMBa is a play on the abbreviation SMB, which stands
for Server Message Block) allows a Unix machine to provide shares that windows
machines can mount, an authentication server or even a Primary Domain
Controller that can replace a Windows NT machine. 
Providing client services can be fairly simple by using these libraries. Many
frontends do not depend on the Samba Server itself, but the routines found in
the Samba client libraries (or short libsmbclient).


%package swat
Summary: A utility to configure Samba from the browser
Group: System Environment/Daemons
Requires: samba = %{version}, ucspi-tcp

%description swat
A common file exchange format in the windows world is SMB and its successor,
CIFS. The %{name} package provides the server and all tools neccessary to act
as a SMB/CIFS client and/or server. However, configuration can be tricky.
That's why the people at smaba.org wrote SWAT, the Samba Web Administration
Tool. It is a standalone HTTP service listining on port 901.


%prep
%setup -q


%build
pushd source3
%configure \
	--enable-shared \
	--enable-static \
	--enable-swat \
	--enable-cups \
	--with-fhs \
	--with-privatedir='%{_sysconfdir}/samba/private' \
	--with-lockdir='%{_localstatedir}/lock' \
	--with-piddir='%{_localstatedir}/run/samba' \
	--with-pammodulesdir='/%{_lib}/security' \
	--with-swatdir='%{_datadir}/swat' \
	--with-configdir='%{_sysconfdir}/samba' \
	--with-mandir='%{_mandir}' \
	--with-ldap \
	--with-cifsmount \
	--with-pam \
	--with-pam_smbpass \
	--with-quotas \
	--with-sys-quotas \
	--with-utmp \
	--with-libsmbclient \
	--with-libsmbsharemodes \
	--enable-gnutls \
	--with-acl-support \
	--with-aio-support \
	--with-sendfile-support \
	--with-winbind
%{__make} %{?_smp_mflags}
popd


%install
pushd source3
%{__make} install DESTDIR='%{buildroot}'
%find_lang pam_winbind
popd

%{__mkdir_p} '%{buildroot}/etc/samba/private'
%{__touch} '%{buildroot}/etc/samba/smb.conf'

%{__mkdir_p} '%{buildroot}/%{_localstatedir}/lock/winbindd_privileged'
%{__mkdir_p} '%{buildroot}/%{_localstatedir}/lock/printing'

for lock in winbindd_privileged/pipe winbindd_idmap.tdb winbindd_cache.tdb \
		account_policy.tdb brlock.tdb browse.dat connections.tdb gencache.tdb \
		group_mapping.tdb locking.tdb login_cache.tdb messages.tdb \
		netsamlogon_cache.tdb ntdrivers.tdb ntprinters.tdb registry.tdb \
		sessionid.tdb share_info.tdb wins.dat
do
	%{__touch} "%{buildroot}/%{_localstatedir}/lock/${lock}"
done

# Install InitNG service files
%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/initng/daemon'
for i in '%{SOURCE1}' '%{SOURCE2}' '%{SOURCE3}'
do
	newname=$(echo "${i}" | %{__sed} 's,^.*%{name}-\(.*\.i\),\1,')
	%{__cat} "$i" | %{__sed} \
		-e 's,@smbd@,%{_sbindir}/smbd,g' \
		-e 's,@nmbd@,%{_sbindir}/nmbd,g' \
		-e 's,@winbindd@,%{_sbindir}/winbindd,g' \
	> "%{buildroot}/etc/initng/daemon/${newname}"
done


%post
%{__ldconfig}


%preun
if [[ "${1}" -eq 0 ]]
then
	for i in smbd winbindd nmbd
	do
		ngc -d daemon/"${i}" > /dev/null 2>&1
		ng-update del "${i}" default > /dev/null 2>&1
	done > /dev/null 2>&1
fi
exit 0


%postun
%{__ldconfig}


%post libs
%{__ldconfig}


%postun libs 
%{__ldconfig}


%files -f source3/pam_winbind.lang
%defattr(-, root, root)
%doc README WHATSNEW* Roadmap COPYING MAINTAINERS Read-Manifest-Now
%doc examples/ docs/*
%dir %{_sysconfdir}/samba
%dir %{_sysconfdir}/samba/private
%ghost %config(noreplace) %{_sysconfdir}/samba/smb.conf
%attr(0700, root, root) %{_sysconfdir}/initng/daemon/*.i
/%{_lib}/security/*.so
%{_bindir}/eventlogadm
%{_bindir}/findsmb
%{_bindir}/ldbadd
%{_bindir}/ldbdel
%{_bindir}/ldbedit
%{_bindir}/ldbmodify
%{_bindir}/ldbrename
%{_bindir}/ldbsearch
%{_bindir}/net
%{_bindir}/nmblookup
%{_bindir}/ntlm_auth
%{_bindir}/pdbedit
%{_bindir}/profiles
%{_bindir}/rpcclient
%{_bindir}/sharesec
%{_bindir}/smbcacls
%{_bindir}/smbcontrol
%{_bindir}/smbcquotas
%{_bindir}/smbpasswd
%{_bindir}/smbspool
%{_bindir}/smbstatus
%{_bindir}/tdb*
%{_bindir}/testparm
%{_bindir}/wbinfo
%{_sbindir}/nmbd
%{_sbindir}/smbd
%{_sbindir}/swat
%{_sbindir}/winbindd
%dir %{_libdir}/samba
%{_libdir}/samba/lowcase.dat
%{_libdir}/samba/upcase.dat
%{_libdir}/samba/valid.dat
%dir %{_libdir}/samba/auth
%{_libdir}/samba/auth/script.so
%dir %{_libdir}/samba/charset
%{_libdir}/samba/charset/*.so
%dir %{_libdir}/samba/vfs
%{_libdir}/samba/vfs/*.so
%doc %{_mandir}/man1/findsmb.*
%doc %{_mandir}/man1/ldbadd.1*
%doc %{_mandir}/man1/ldbdel.1*
%doc %{_mandir}/man1/ldbedit.1*
%doc %{_mandir}/man1/ldbmodify.1*
%doc %{_mandir}/man1/ldbrename.1*
%doc %{_mandir}/man1/ldbsearch.1*
%doc %{_mandir}/man1/log2pcap.1*
%doc %{_mandir}/man1/nmblookup.1*
%doc %{_mandir}/man1/ntlm_auth.1*
%doc %{_mandir}/man1/profiles.1*
%doc %{_mandir}/man1/rpcclient.1*
%doc %{_mandir}/man1/sharesec.1*
%doc %{_mandir}/man1/smbcacls.1*
%doc %{_mandir}/man1/smbcontrol.1*
%doc %{_mandir}/man1/smbcquotas.1*
%doc %{_mandir}/man1/smbstatus.1*
%doc %{_mandir}/man1/testparm.1*
%doc %{_mandir}/man1/vfstest.1*
%doc %{_mandir}/man1/wbinfo.1*
%doc %{_mandir}/man5/lmhosts.5*
%doc %{_mandir}/man5/smb.conf.5*
%doc %{_mandir}/man5/smbpasswd.5*
%doc %{_mandir}/man7/libsmbclient.7*
%doc %{_mandir}/man7/samba.7*
%doc %{_mandir}/man7/winbind_krb5_locator.7*
%doc %{_mandir}/man8/cifs.upcall.8*
%doc %{_mandir}/man8/eventlogadm.8*
%doc %{_mandir}/man8/net.*
%doc %{_mandir}/man8/nmbd.*
%doc %{_mandir}/man8/pam_winbind.8*
%doc %{_mandir}/man8/pdbedit.8*
%doc %{_mandir}/man8/smbd.*
%doc %{_mandir}/man8/smbpasswd.*
%doc %{_mandir}/man8/smbspool.8*
%doc %{_mandir}/man8/tdb*.8*
%doc %{_mandir}/man8/vfs_*.8*
%doc %{_mandir}/man8/winbindd.*
%{_bindir}/smbclient
%{_bindir}/smbget
%{_bindir}/smbtar
%{_bindir}/smbtree
%{_sbindir}/mount.*
%{_sbindir}/umount.*
%doc %{_mandir}/man1/smbclient.*
%doc %{_mandir}/man1/smbget.*
%doc %{_mandir}/man1/smbtar.*
%doc %{_mandir}/man1/smbtree.*
%doc %{_mandir}/man5/smbgetrc.*
%doc %{_mandir}/man8/*mount.*
%dir %attr(0755, root, root) %{_localstatedir}/lock/printing
%dir %attr(0750, root, root) %{_localstatedir}/lock/winbindd_privileged
%ghost %config(noreplace missingok) %{_localstatedir}/lock/winbindd_privileged/pipe
%ghost %config(noreplace missingok) %{_localstatedir}/lock/winbindd_idmap.tdb
%ghost %config(noreplace missingok) %{_localstatedir}/lock/winbindd_cache.tdb
%ghost %config(noreplace missingok) %{_localstatedir}/lock/account_policy.tdb
%ghost %config(noreplace missingok) %{_localstatedir}/lock/brlock.tdb
%ghost %config(noreplace missingok) %{_localstatedir}/lock/browse.dat
%ghost %config(noreplace missingok) %{_localstatedir}/lock/connections.tdb
%ghost %config(noreplace missingok) %{_localstatedir}/lock/gencache.tdb
%ghost %config(noreplace missingok) %{_localstatedir}/lock/group_mapping.tdb
%ghost %config(noreplace missingok) %{_localstatedir}/lock/locking.tdb
%ghost %config(noreplace missingok) %{_localstatedir}/lock/login_cache.tdb
%ghost %config(noreplace missingok) %{_localstatedir}/lock/messages.tdb
%ghost %config(noreplace missingok) %{_localstatedir}/lock/netsamlogon_cache.tdb
%ghost %config(noreplace missingok) %{_localstatedir}/lock/ntdrivers.tdb
%ghost %config(noreplace missingok) %{_localstatedir}/lock/ntprinters.tdb
%ghost %config(noreplace missingok) %{_localstatedir}/lock/registry.tdb
%ghost %config(noreplace missingok) %{_localstatedir}/lock/sessionid.tdb
%ghost %config(noreplace missingok) %{_localstatedir}/lock/share_info.tdb
%ghost %config(noreplace missingok) %{_localstatedir}/lock/wins.dat


%files libs
%defattr(-, root, root)
%{_includedir}/libsmbclient.h
%{_includedir}/netapi.h
%{_includedir}/smb_share_modes.h
%{_includedir}/talloc.h
%{_includedir}/tdb.h
%{_includedir}/wbclient.h
%{_libdir}/libnetapi.*
%{_libdir}/libsmbclient.*
%{_libdir}/libsmbsharemodes.*
%{_libdir}/libtalloc.*
%{_libdir}/libtdb.*
%{_libdir}/libwbclient.*
%doc %{_mandir}/man7/libsmbclient.7*
%doc %{_mandir}/man8/idmap_*.8*


%files swat
%defattr(-, root, root)
%{_sbindir}/swat
%{_datadir}/swat/
%{_libdir}/samba/*.msg
%doc %{_mandir}/man8/swat.8*
