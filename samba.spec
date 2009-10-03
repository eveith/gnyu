Name: samba
Version: 3.2.0
Release: 2ev
Summary: SMB and CIFS file exchange client tools and server
URL: http://www.samba.org/
Group: System Environment/Daemons
License: GPL-3
Vendor: GNyU-Linux
Source0: http://www.samba.org/samba/ftp/stable/samba-%{version}.tar.gz
Source1: %{name}-smbd.i
Source2: %{name}-nmbd.i
Source3: %{name}-winbindd.i
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires(build,install): coreutils, grep, sed
BuildRequires(build): make, gcc, openldap-libs, libattr, libacl, popt, libpam
BuildRequires(build): heimdal-libs, cups, libcap2, ncurses, readline, zlib
BuildRequires(build): openssl
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
pushd source
%configure \
	--enable-shared \
	--enable-static \
	--enable-swat \
	--enable-cups \
	--with-fhs \
	--with-privatedir=%{_sysconfdir}/samba/private \
	--with-lockdir=%{_localstatedir}/lock \
	--with-piddir=%{_localstatedir}/run/samba \
	--with-pammodulesdir=/%{_lib}/security \
	--with-swatdir=%{_datadir}/swat \
	--with-configdir=%{_sysconfdir}/samba \
	--with-mandir=%{_mandir} \
	--with-ldap \
	--with-cifsmount \
	--with-pam \
	--with-pam_smbpass \
	--with-quotas \
	--with-sys-quotas \
	--with-utmp \
	--with-ads \
	--with-libmsrpc \
	--with-libaddns \
	--with-libsmbclient \
	--with-libsmbsharemodes \
	--with-acl-support \
	--with-aio-support \
	--with-sendfile-support \
	--with-winbind
%{__make} %{?_smp_mflags}
popd


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'

pushd source
%{__make_install} DESTDIR='%{buildroot}'
popd

%{__mkdir_p} '%{buildroot}/etc/samba/private'
touch '%{buildroot}/etc/samba/smb.conf'
%{__mkdir_p} '%{buildroot}/%{_localstatedir}/lock/winbindd_privileged'
%{__mkdir_p} '%{buildroot}/%{_localstatedir}/lock/printing'
touch '%{buildroot}/%{_localstatedir}/lock/winbindd_privileged/pipe'
touch '%{buildroot}/%{_localstatedir}/lock/winbindd_idmap.tdb'
touch '%{buildroot}/%{_localstatedir}/lock/winbindd_cache.tdb'
touch '%{buildroot}/%{_localstatedir}/lock/account_policy.tdb'
touch '%{buildroot}/%{_localstatedir}/lock/brlock.tdb'
touch '%{buildroot}/%{_localstatedir}/lock/browse.dat'
touch '%{buildroot}/%{_localstatedir}/lock/connections.tdb'
touch '%{buildroot}/%{_localstatedir}/lock/gencache.tdb'
touch '%{buildroot}/%{_localstatedir}/lock/group_mapping.tdb'
touch '%{buildroot}/%{_localstatedir}/lock/locking.tdb'
touch '%{buildroot}/%{_localstatedir}/lock/login_cache.tdb'
touch '%{buildroot}/%{_localstatedir}/lock/messages.tdb'
touch '%{buildroot}/%{_localstatedir}/lock/netsamlogon_cache.tdb'
touch '%{buildroot}/%{_localstatedir}/lock/ntdrivers.tdb'
touch '%{buildroot}/%{_localstatedir}/lock/ntprinters.tdb'
touch '%{buildroot}/%{_localstatedir}/lock/registry.tdb'
touch '%{buildroot}/%{_localstatedir}/lock/sessionid.tdb'
touch '%{buildroot}/%{_localstatedir}/lock/share_info.tdb'
touch '%{buildroot}/%{_localstatedir}/lock/wins.dat'


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
/sbin/ldconfig

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
/sbin/ldconfig

%post libs
/sbin/ldconfig

%postun libs 
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc README WHATSNEW* Roadmap COPYING MAINTAINERS Read-Manifest-Now
%doc examples/ docs/*
%dir %{_sysconfdir}/samba
%dir %{_sysconfdir}/samba/private
%ghost %config(noreplace) %{_sysconfdir}/samba/smb.conf
%{_sysconfdir}/initng/daemon/*.i
/%{_lib}/security/*.so
%{_bindir}/eventlogadm
%{_bindir}/findsmb
%{_bindir}/ldbadd
%{_bindir}/ldbdel
%{_bindir}/ldbedit
%{_bindir}/ldbmodify
%{_bindir}/ldbsearch
%{_bindir}/net
%{_bindir}/nmblookup
%{_bindir}/ntlm_auth
%{_bindir}/pdbedit
%{_bindir}/profiles
%{_bindir}/rpcclient
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
%{_libdir}/upcase.dat
%{_libdir}/lowcase.dat
%{_libdir}/valid.dat
%{_libdir}/charset/
%{_libdir}/auth/
%{_libdir}/vfs/
%doc %{_mandir}/man1/findsmb.*
%doc %{_mandir}/man1/ldbadd.1*
%doc %{_mandir}/man1/ldbdel.1*
%doc %{_mandir}/man1/ldbedit.1*
%doc %{_mandir}/man1/ldbmodify.1*
%doc %{_mandir}/man1/ldbsearch.1*
%doc %{_mandir}/man1/log2pcap.*
%doc %{_mandir}/man1/nmblookup.*
%doc %{_mandir}/man1/ntlm_auth.*
%doc %{_mandir}/man1/profiles.*
%doc %{_mandir}/man1/rpcclient.*
%doc %{_mandir}/man1/smbcacls.*
%doc %{_mandir}/man1/smbcontrol.*
%doc %{_mandir}/man1/smbcquotas.*
%doc %{_mandir}/man1/smbstatus.*
%doc %{_mandir}/man1/testparm.*
%doc %{_mandir}/man1/vfstest.*
%doc %{_mandir}/man1/wbinfo.*
%doc %{_mandir}/man5/lmhosts.*
%doc %{_mandir}/man5/smb.conf.*
%doc %{_mandir}/man5/smbpasswd.5*
%doc %{_mandir}/man7/libsmbclient.*
%doc %{_mandir}/man7/pam_winbind.*
%doc %{_mandir}/man7/samba.*
%doc %{_mandir}/man8/eventlogadm.*
%doc %{_mandir}/man8/net.*
%doc %{_mandir}/man8/nmbd.*
%doc %{_mandir}/man8/pdbedit.*
%doc %{_mandir}/man8/smbd.*
%doc %{_mandir}/man8/smbpasswd.*
%doc %{_mandir}/man8/smbspool.*
%doc %{_mandir}/man8/swat.*
%doc %{_mandir}/man8/tdb*.*
%doc %{_mandir}/man8/vfs_*.*
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
%{_includedir}/*.h
%{_libdir}/*.so*
%{_libdir}/*.a
%doc %{_mandir}/man7/libsmbclient.*
%doc %{_mandir}/man8/idmap_*.*

%files swat
%defattr(-, root, root)
%{_sbindir}/swat
%{_datadir}/swat/
%{_libdir}/*.msg
%doc %{_mandir}/man8/swat.8*
