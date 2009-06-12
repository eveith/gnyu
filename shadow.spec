Name: shadow
Version: 4.1.4.1
Release: 2ev
Summary: The Shadow Password Suite
URL: http://pkg-shadow.alioth.debian.org/
Group: System Environment/Base
License: BSD
Vendor: GNyU-Linux
Source0: ftp://pkg-shadow.alioth.debian.org/pub/pkg-shadow/%{name}-%{version}.tar.bz2
Source1: shadow-pam-chage
Source2: shadow-pam-chgpasswd
Source3: shadow-pam-chpasswd
Source4: shadow-pam-groupadd
Source5: shadow-pam-groupdel
Source6: shadow-pam-groupmems
Source7: shadow-pam-groupmod
Source8: shadow-pam-login
Source9: shadow-pam-newusers
Source10: shadow-pam-passwd
Source11: shadow-pam-su
Source12: shadow-pam-useradd
Source13: shadow-pam-usermod
Source14: shadow-login.defs
Source15: shadow-useradd.default
Source16: shadow-pam-chfn
Source17: shadow-pam-chsh
Source18: shadow-pam-userdel
Source19: shadow-limits
Source20: shadow-login.access
Patch1: %{name}-4.0.18.1-useradd-usermod.patch
BuildRequires: make, gcc, libpam, libutempter, gettext

%description
The Shadow Password Suite is an integral part of every modern Unix system. It
incorporates a way to store passwords locally in a shadow password file that
exists alongside the old and traditionall /etc/passwd file. The shadow
passwords are no longer directly stored in /etc/password, but in /etc/shadow,
a file which only the super user can read. Shadow also provides additional
functionality such as password expiration.

This package provides the "shadow" library used for reading/writing the shadow
files and understanding its entries. It also offers tools to query information
from it. To actually maintain shadow accounts, you will have to install a
tools suite like the one provided by the "shadow-utils" or "pwdutils" package.


%package su
Summary: The Substitute User ("su") command from the Shadow package
Group: System Environment/Base
Requires: shadow = %{version}-%{release}
Conflicts: shadow < %{version}

%description su
"su" (short for Substitute User) is a utility that allows an user to become
another or root during a login session. 


%package login
Summary: The Login program
Group: System Environment/Base
Requires: shadow = %{version}-%{release}
Conflicts: shadow < %{version}

%description login
login is used to establish a new session with the system. It is normally
invoked automatically by responding to the login: prompt on the user’s
terminal.


%package utils
Summary: Utilities to manage shadow accounts in local flatfiles
Group: System Environment/Base
Requires: shadow = %{version}
Conflicts: pwdutils

%description utils
These are additional utilities required to manage, add and remove shadow user
and group accounts. It contains passwd, useradd, userdel, usermod; groupadd, 
groupdel and groupmod binaries to manage passwords, user and group information
from the console.

These programs are not network capable and cannot be used to manage accounts
stored in NIS/NIS+ or LDAP databases. If you wish to manage these, install the
pwduitls package, which provides the same plus NIS/NIS+/LDAP support.


%prep
	%setup -q


%build
	%configure \
		--with-libpam \
		--without-selinux \
		--disable-rpath \
		--enable-shadowgrp \
		--with-nscd \
		--with-sha-crypt
	%{__make} %{?_smp_mflags}


%install
	%{__fakeroot} %{__make} install DESTDIR='%{buildroot}'
	%find_lang shadow


	# Install pam config files
	%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/pam.d'
	for source in '%{SOURCE1}' '%{SOURCE2}' '%{SOURCE3}' '%{SOURCE4}' \
			'%{SOURCE5}' '%{SOURCE6}' '%{SOURCE7}' '%{SOURCE8}' \
			'%{SOURCE9}' '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}' \
			'%{SOURCE13}' '%{SOURCE16}' '%{SOURCE17}' '%{SOURCE18}'
	do
		stripped_name=$(echo $source \
			| %{__sed} "s,${RPM_SOURCE_DIR}/\?shadow-pam-,,")
		%{__cp} "${source}" \
			"%{buildroot}/%{_sysconfdir}/pam.d/${stripped_name}"
	done

	%{__touch} '%{buildroot}/%{_sysconfdir}/suauth'
	%{__cp} '%{SOURCE19}' '%{buildroot}/%{_sysconfdir}/limits'

	# Relocate some files to make them available at boot time
	%{__mkdir_p} '%{buildroot}/bin'
	%{__mkdir_p} '%{buildroot}/sbin'
	%{__mv} '%{buildroot}/%{_bindir}/login' '%{buildroot}/bin'
	%{__mv} '%{buildroot}/%{_bindir}/su' '%{buildroot}/bin'
	%{__mv} '%{buildroot}/%{_bindir}/groups' '%{buildroot}/bin'
	%{__mv} '%{buildroot}/%{_sbindir}/nologin' '%{buildroot}/sbin'

	# Install the libshadow library. Dunno why it isn't automatically
	# installed anymore.
	%{__mkdir_p} '%{buildroot}/%{_lib}'
	%{__cp} lib/.libs/libshadow.{la,a} '%{buildroot}/%{_lib}'
	

	%{__mkdir_p} '%{buildroot}/%{_sysconfdir}'
	%{__touch} '%{buildroot}/%{_sysconfdir}/shadow'
	%{__touch} '%{buildroot}/%{_sysconfdir}/shadow-'
	%{__touch} '%{buildroot}/%{_sysconfdir}/gshadow'
	%{__touch} '%{buildroot}/%{_sysconfdir}/gshadow-'
	%{__cp} '%{SOURCE14}' '%{buildroot}/%{_sysconfdir}/login.defs'
	%{__cp} '%{SOURCE20}' '%{buildroot}/%{_sysconfdir}/login.access'

	%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/default'
	%{__cp} '%{SOURCE15}' '%{buildroot}/%{_sysconfdir}/default/useradd'


%post
	%{__ldconfig}


%postun
	%{__ldconfig}


%files -f shadow.lang
%defattr(-, root, root)
%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/login.defs
%ghost %config(noreplace) %attr(0400, root, root) %{_sysconfdir}/shadow
%ghost %config(noreplace) %attr(0600, root, root) %{_sysconfdir}/shadow-
%ghost %config(noreplace) %attr(0400, root, root) %{_sysconfdir}/gshadow
%ghost %config(noreplace) %attr(0600, root, root) %{_sysconfdir}/gshadow-
%dir %{_sysconfdir}/default
/%{_lib}/libshadow.*
/bin/groups
%attr(0711, root, root) /sbin/nologin
%{_bindir}/faillog
%{_bindir}/lastlog
%doc %{_mandir}/man1/groups.1*
%doc %{_mandir}/man3/getspnam.3*
%doc %{_mandir}/man3/shadow.3*
%doc %{_mandir}/man5/faillog.5*
%doc %{_mandir}/man5/gshadow.5*
%doc %{_mandir}/man5/shadow.5*
%doc %{_mandir}/man8/faillog.8*
%doc %{_mandir}/man8/lastlog.8*
%doc %{_mandir}/man8/nologin.8*
%doc %{_mandir}/*/man1/groups.1*
%doc %{_mandir}/*/man3/getspnam.3*
%doc %{_mandir}/*/man3/shadow.3*
%doc %{_mandir}/*/man5/faillog.5*
%doc %{_mandir}/*/man5/gshadow.5*
%doc %{_mandir}/*/man5/shadow.5*
%doc %{_mandir}/*/man8/faillog.8*
%doc %{_mandir}/*/man8/lastlog.8*
%doc %{_mandir}/*/man8/nologin.8*


%files login
%defattr(-, root, root)
%attr(0600, root, root) %config(noreplace) %{_sysconfdir}/limits
%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/login.access
%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/pam.d/login
%attr(0711, root, root) /bin/login
%doc %{_mandir}/man1/login.1*
%doc %{_mandir}/man5/login.defs.5*
%doc %{_mandir}/*/man1/login.1*
%doc %{_mandir}/*/man5/limits.5*
%doc %{_mandir}/*/man5/login.access.5*
%doc %{_mandir}/*/man5/login.defs.5*
%doc %{_mandir}/*/man5/porttime.5*


%files su
%defattr(-, root, root)
%ghost %config(noreplace) %{_sysconfdir}/suauth
%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/pam.d/su
%attr(4711, root, root) /bin/su
%doc %{_mandir}/man1/su.1*
%doc %{_mandir}/man5/suauth.5*
%doc %{_mandir}/*/man1/su.1*
%doc %{_mandir}/*/man5/suauth.5*


%files utils
%defattr(-, root, root)
%attr(0640, root, root) %config(noreplace) %{_sysconfdir}/default/useradd
%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/pam.d/chage
%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/pam.d/chfn
%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/pam.d/chsh
%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/pam.d/chgpasswd
%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/pam.d/chpasswd
%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/pam.d/groupadd
%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/pam.d/groupdel
%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/pam.d/groupmems
%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/pam.d/groupmod
%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/pam.d/newusers
%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/pam.d/passwd
%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/pam.d/useradd
%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/pam.d/userdel
%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/pam.d/usermod
%attr(4711, root, root) %{_bindir}/chage
%attr(4711, root, root) %{_bindir}/chfn
%attr(4711, root, root) %{_bindir}/chsh
%attr(4711, root, root) %{_bindir}/expiry
%attr(4711, root, root) %{_bindir}/gpasswd
%attr(4711, root, root) %{_bindir}/newgrp
%attr(4711, root, root) %{_bindir}/passwd
%{_bindir}/sg
%attr(0710, root, root) %{_sbindir}/chgpasswd
%attr(0710, root, root) %{_sbindir}/chpasswd
%attr(0710, root, root) %{_sbindir}/groupadd
%attr(0710, root, root) %{_sbindir}/groupdel
%attr(0710, root, root) %{_sbindir}/groupmems
%attr(0710, root, root) %{_sbindir}/groupmod
%attr(0710, root, root) %{_sbindir}/grpck
%attr(0710, root, root) %{_sbindir}/grpconv
%attr(0710, root, root) %{_sbindir}/grpunconv
%attr(0710, root, root) %{_sbindir}/logoutd
%attr(0710, root, root) %{_sbindir}/newusers
%attr(0710, root, root) %{_sbindir}/pwck
%attr(0710, root, root) %{_sbindir}/pwconv
%attr(0710, root, root) %{_sbindir}/pwunconv
%attr(0710, root, root) %{_sbindir}/useradd
%attr(0710, root, root) %{_sbindir}/userdel
%attr(0710, root, root) %{_sbindir}/usermod
%attr(0710, root, root) %{_sbindir}/vigr
%attr(0710, root, root) %{_sbindir}/vipw
%doc %{_mandir}/man1/chage.1*
%doc %{_mandir}/man1/chfn.1*
%doc %{_mandir}/man1/chsh.1*
%doc %{_mandir}/man1/expiry.1*
%doc %{_mandir}/man1/gpasswd.1*
%doc %{_mandir}/man1/newgrp.1*
%doc %{_mandir}/man1/passwd.1*
%doc %{_mandir}/man1/sg.1*
%doc %{_mandir}/man5/passwd.5*
%doc %{_mandir}/man8/chgpasswd.8*
%doc %{_mandir}/man8/chpasswd.8*
%doc %{_mandir}/man8/groupadd.8*
%doc %{_mandir}/man8/groupdel.8*
%doc %{_mandir}/man8/groupmems.8*
%doc %{_mandir}/man8/groupmod.8*
%doc %{_mandir}/man8/grpck.8*
%doc %{_mandir}/man8/grpconv.8*
%doc %{_mandir}/man8/grpunconv.8*
%doc %{_mandir}/man8/logoutd.8*
%doc %{_mandir}/man8/newusers.8*
%doc %{_mandir}/man8/pwck.8*
%doc %{_mandir}/man8/pwconv.8*
%doc %{_mandir}/man8/pwunconv.8*
%doc %{_mandir}/man8/useradd.8*
%doc %{_mandir}/man8/userdel.8*
%doc %{_mandir}/man8/usermod.8*
%doc %{_mandir}/man8/vigr.8*
%doc %{_mandir}/man8/vipw.8*
%doc %{_mandir}/*/man1/chage.1*
%doc %{_mandir}/*/man1/chfn.1*
%doc %{_mandir}/*/man1/chsh.1*
%doc %{_mandir}/*/man1/expiry.1*
%doc %{_mandir}/*/man1/gpasswd.1*
%doc %{_mandir}/*/man1/newgrp.1*
%doc %{_mandir}/*/man1/passwd.1*
%doc %{_mandir}/*/man1/sg.1*
%doc %{_mandir}/*/man5/passwd.5*
%doc %{_mandir}/*/man8/chgpasswd.8*
%doc %{_mandir}/*/man8/chpasswd.8*
%doc %{_mandir}/*/man8/groupadd.8*
%doc %{_mandir}/*/man8/groupdel.8*
%doc %{_mandir}/*/man8/groupmems.8*
%doc %{_mandir}/*/man8/groupmod.8*
%doc %{_mandir}/*/man8/grpck.8*
%doc %{_mandir}/*/man8/grpconv.8*
%doc %{_mandir}/*/man8/grpunconv.8*
%doc %{_mandir}/*/man8/logoutd.8*
%doc %{_mandir}/*/man8/newusers.8*
%doc %{_mandir}/*/man8/pwck.8*
%doc %{_mandir}/*/man8/pwconv.8*
%doc %{_mandir}/*/man8/pwunconv.8*
%doc %{_mandir}/*/man8/useradd.8*
%doc %{_mandir}/*/man8/userdel.8*
%doc %{_mandir}/*/man8/usermod.8*
%doc %{_mandir}/*/man8/vigr.8*
%doc %{_mandir}/*/man8/vipw.8*
