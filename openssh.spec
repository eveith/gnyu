Name: openssh
Version: 4.7p1
Release: 1ev
Summary: The Secure SHell clients and libraries
URL: http://www.openssh.org/
Group: Applications/Communications
License: BSD/MIT
Vendor: MSP Slackware
Source0: ftp://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/%{name}-%{version}.tar.gz
Source1: openssh-sshd.i
Source2: openssh-sshd.pam
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc-core, libpam, zlib, openssl >= 0.9.8, sed
%define _sshd_uid 504
%define _sshd_gid 51

%description
OpenSSH is a FREE version of the SSH connectivity tools that technical users
of the Internet rely on. Users of telnet, rlogin, and ftp may not realize that
their password is transmitted across the Internet unencrypted, but it is.
OpenSSH encrypts all traffic (including passwords) to effectively eliminate
eavesdropping, connection hijacking, and other attacks. Additionally, OpenSSH
provides secure tunneling capabilities and several authentication methods, and
supports all SSH protocol versions.


%package server
Summary: OpenSSH server side applications
Group: System Environment/Daemons
Requires: openssh = %{version}, zlib, libpam, openssl >= 0.9.8

%description server
This package includes the server side applications for the OpenSSH suite, like
the sftp-server and sshd.


%prep
%setup -q

if ! id sshd > /dev/null 2>&1
then
	touch .REMOVE_SSHD_USER
	groupadd -g %{_sshd_gid} sshd
	useradd -g sshd -u %{_sshd_uid} -s /sbin/nologin -d /var/empty sshd
fi


%build
%configure \
	--sysconfdir=/etc/ssh \
	--with-cflags="$RPM_OPT_FLAGS" \
	--with-cppflags="$RPM_OPT_FLAGS" \
	--with-md5-passwords \
	--with-pam \
	--with-mantype=man \
	--with-rand-helper \
	--with-privsep-path=/%{_var}/empty \
	--with-privsep-user=sshd
make %{_smp_mflags}

%install
[[ "$RPM_BUILD_ROOT" != "/" ]] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"

rm -vf "$RPM_BUILD_ROOT"/"%{_infodir}"/dir

# Install OpenSSH pam control file

mkdir -p "$RPM_BUILD_ROOT"/etc/pam.d
cp %{SOURCE2} "$RPM_BUILD_ROOT"/etc/pam.d/sshd

# Install OpenSSH service file

mkdir -p "$RPM_BUILD_ROOT"/etc/initng/daemon
cat "%{SOURCE1}" \
	| sed \
		-e 's,@sshd@,%{_sbindir}/sshd,g' \
		-e 's,@ssh-keygen@,%{_bindir}/ssh-keygen,g' \
	> "$RPM_BUILD_ROOT"/etc/initng/daemon/sshd.i

# Privilege separation needs a directory
mkdir -p "$RPM_BUILD_ROOT"/%{_var}/empty

# Touch ghost files
for file in ssh_host_dsa_key ssh_host_dsa_key.pub \
		ssh_host_key ssh_host_key.pub ssh_host_rsa_key \
		ssh_host_rsa_key.pub
do
	touch "$RPM_BUILD_ROOT"/etc/ssh/"$file"
done


%pre server
groupadd -g %{_sshd_gid} sshd > /dev/null 2>&1 || :
useradd -g %{_sshd_gid} -u %{_sshd_uid} -s /sbin/nologin -d /var/empty sshd \
	> /dev/null 2>&1 || :


%preun server
if [ "$1" = '0' ]
then
	ngc -d daemon/sshd/generate_keys > /dev/null 2>&1 ||:
	ngc -d daemon/sshd > /dev/null 2>&1 || :
	ng-update del daemon/sshd > /dev/null 2>&1 || :
fi

%post server
if ngc -s | grep -q 'daemon/sshd'
then
	ngc -d daemon/sshd/generate_keys > /dev/null 2>&1 ||:
	ngc -r daemon/sshd > /dev/null 2>&1 || :
fi
/sbin/ldconfig

%postun server
if [ "$1" = '0' ] 
then
	userdel sshd > /dev/null 2>&1 || :
	groupdel sshd > /dev/null 2>&1 || :
fi
/sbin/ldconfig

%post
/sbin/ldconfig

%postun 
/sbin/ldconfig


%clean
[[ "$RPM_BUILD_ROOT" != "/" ]] && rm -rf "$RPM_BUILD_ROOT"
if [ -e '.REMOVE_SSHD_USER' ]
then
	userdel sshd > /dev/null 2>&1
	groupdel sshd > /dev/null 2>&1
fi
exit 0


%files
%defattr(-, root, root)
%doc LICENCE README* CREDITS ChangeLog* RFC* WARNING* TODO 
%dir /etc/ssh
%attr(0644, root, root) %config(noreplace) /etc/ssh/ssh_config
%config /etc/ssh/ssh_prng_cmds
/etc/ssh/moduli
%{_datadir}/Ssh.bin
%{_bindir}/ssh
%{_bindir}/slogin
%{_bindir}/scp
%{_bindir}/ssh-add
%{_bindir}/ssh-agent
%{_bindir}/ssh-keygen
%{_bindir}/ssh-keyscan
%{_bindir}/sftp
%{_mandir}/man1/scp.1.gz
%{_mandir}/man1/ssh-agent.1.gz
%{_mandir}/man1/ssh-keygen.1.gz
%{_mandir}/man1/ssh-keyscan.1.gz
%{_mandir}/man1/ssh.1.gz
%{_mandir}/man1/ssh-add.1.gz
%{_mandir}/man1/slogin.1.gz
%{_mandir}/man5/ssh_config.5.gz
%{_mandir}/man8/ssh-keysign.8.gz
%{_mandir}/man8/ssh-rand-helper.8.gz
%{_mandir}/man8/sftp-server.8.gz
%{_libexecdir}/ssh-keysign
%{_libexecdir}/ssh-rand-helper


%files server
/etc/initng/daemon/sshd.i
%dir /etc/ssh
%config(noreplace) /etc/pam.d/sshd
%ghost %config(noreplace) /etc/ssh/ssh_host_*key*
%attr(0600, root, root) %config(noreplace) /etc/ssh/sshd_config
%{_libexecdir}/sftp-server
%{_sbindir}/sshd
%{_mandir}/man5/sshd_config.5.gz
%{_mandir}/man1/sftp.1.gz
%{_mandir}/man8/sshd.8.gz
%dir /%{_var}/empty
