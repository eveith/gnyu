Name: openssh
Version: 5.3p1
Release: 2ev
Summary: The Secure SHell clients and libraries
URL: http://www.openssh.org/
Group: Applications/Communications
License: BSD/MIT
Vendor: GNyU-Linux
Source0: ftp://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/%{name}-%{version}.tar.gz
Source1: openssh-sshd.i
Source2: openssh-sshd.pam
BuildRequires: make >= 3.79.1, gcc, perl
BuildRequires: zlib >= 1.2.3, openssl >= 0.9.6, tcp_wrappers, shadow, libpam
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


%build
	%configure \
		--sysconfdir='%{_sysconfdir}/ssh' \
		--with-cflags="${CFLAGS:-%{optflags}}" \
		--with-cppflags="${CXXFLAGS:-%{optflags}}" \
		--with-tcp-wrappers \
		--with-md5-passwords \
		--with-pam \
		--with-mantype=man \
		--with-ssl-engine \
		--with-privsep-path='/%{_var}/empty' \
		--with-privsep-user=sshd
	%{__make} %{?_smp_mflags}


%install
	%{__make_install} DESTDIR="${RPM_BUILD_ROOT}"

	%{__touch} '%{buildroot}/%{_sysconfdir}/ssh/moduli'

	# Install OpenSSH pam control file
	%{__mkdir_p} "${RPM_BUILD_ROOT}/%{_sysconfdir}/pam.d"
	%{__cp} '%{SOURCE2}' "${RPM_BUILD_ROOT}/%{_sysconfdir}/pam.d/sshd"

	# Install OpenSSH service file
	%{__mkdir_p} "${RPM_BUILD_ROOT}/etc/initng/daemon"
	%{install_ifile '%{SOURCE1}' daemon/sshd.i}

	# Privilege separation needs a directory
	%{__mkdir_p} "${RPM_BUILD_ROOT}/%{_var}/empty"

	# Touch ghost files
	for file in ssh_host_dsa_key ssh_host_dsa_key.pub \
			ssh_host_key ssh_host_key.pub ssh_host_rsa_key \
			ssh_host_rsa_key.pub
	do
		%{__touch} "${RPM_BUILD_ROOT}/etc/ssh/${file}"
	done


%pre server
	if [[ "${1}" -eq 1 ]]
	then
		groupadd \
			-g '%{_sshd_gid}' \
			sshd
		useradd \
			-g '%{_sshd_gid}' \
			-u '%{_sshd_uid}' \
			-s /sbin/nologin
			-d '/%{_var}/empty' \
			sshd
	fi > /dev/null 2>&1
	exit 0


%preun server
	if [[ "${1}" -eq 0 ]]
	then
		%{__ngc} -d daemon/sshd
		ng-update delete daemon/sshd default
	fi > /dev/null 2>&1
	exit 0


%postun server
	if [[ "${1}" -eq 0 ]]
	then
		userdel sshd
		groupdel sshd
	fi > /dev/null 2>&1
	%{__ldconfig}


%post
	%{__ldconfig}


%postun 
	%{__ldconfig}


%files
	%defattr(-, root, root)
	%doc LICENCE README* CREDITS ChangeLog* PROTOCOL* WARNING* TODO 
	%dir %{_sysconfdir}/ssh
	%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/ssh/ssh_config
	%{_sysconfdir}/ssh/moduli
	%{_datadir}/Ssh.bin
	%{_bindir}/ssh
	%{_bindir}/slogin
	%{_bindir}/scp
	%{_bindir}/ssh-add
	%{_bindir}/ssh-agent
	%{_bindir}/ssh-keygen
	%{_bindir}/ssh-keyscan
	%{_bindir}/sftp
	%doc %{_mandir}/man1/scp.1*
	%doc %{_mandir}/man1/ssh-agent.1*
	%doc %{_mandir}/man1/ssh-keygen.1*
	%doc %{_mandir}/man1/ssh-keyscan.1*
	%doc %{_mandir}/man1/ssh.1*
	%doc %{_mandir}/man1/ssh-add.1*
	%doc %{_mandir}/man1/slogin.1*
	%doc %{_mandir}/man5/ssh_config.5*
	%doc %{_mandir}/man8/ssh-keysign.8*
	%doc %{_mandir}/man8/sftp-server.8*
	%attr(4711, root, root) %{_libexecdir}/ssh-keysign


%files server
	%attr(0660, root, root) %{_sysconfdir}/initng/daemon/sshd.i
	%config(noreplace) %{_sysconfdir}/pam.d/sshd
	%ghost %config(noreplace) %{_sysconfdir}/ssh/ssh_host_*key*
	%config %ghost %{_sysconfdir}/ssh/moduli
	%attr(0600, root, root) %config(noreplace) %{_sysconfdir}/ssh/sshd_config
	%{_libexecdir}/sftp-server
	%{_sbindir}/sshd
	%doc %{_mandir}/man5/sshd_config.5*
	%doc %{_mandir}/man5/moduli.5*
	%doc %{_mandir}/man1/sftp.1*
	%doc %{_mandir}/man8/sshd.8*
	%dir /%{_var}/empty
