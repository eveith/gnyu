Name: shadow
Version: 4.0.18.1
Release: 1ev
Summary: The Shadow Password suite (provides "login" and "su")
URL: ftp://ftp.pld.org.pl
Group: System Environment/Base
License: BSD
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source0: ftp://ftp.pld.org.pl/software/%{name}/%{name}-%{version}.tar.bz2
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
Source15: shadow-default_useradd
Patch1: %{name}-4.0.18.1-useradd-usermod.patch
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make >= 3.79.1, gcc-core, libpam, sed
Requires: libpam
Provides: login, su

%description
The Shadow Suite is important for system login, as it provides the login tool,
"su" (to become another user) and some other tools that are helpful.

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
%patch -P 1 -p1


%build
%configure \
	--with-libpam \
	--without-selinux \
	--disable-rpath \
	--enable-shadowgrp
make %{_smp_mflags}


%install
[[ "$RPM_BUILD_ROOT" != "/" ]] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"

rm -vf "$RPM_BUILD_ROOT"/"%{_infodir}"/dir

%find_lang shadow

# Install pam config files

mkdir -p ${RPM_BUILD_ROOT}/etc/pam.d
for source in %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} \
		%{SOURCE6} %{SOURCE7} %{SOURCE8} %{SOURCE9} %{SOURCE10} %{SOURCE11} \
		%{SOURCE12} %{SOURCE13}
do
	stripped_name=$(echo $source | sed "s,${RPM_SOURCE_DIR}/\?shadow-pam-,,")
	cp $source ${RPM_BUILD_ROOT}/etc/pam.d/$stripped_name
done

# Relocate some files to make them available at boot time

mkdir -p ${RPM_BUILD_ROOT}/{bin,sbin,%{_lib}}
mv "$RPM_BUILD_ROOT"/"%{_bindir}"/{groups,login,su} "$RPM_BUILD_ROOT"/bin
mv "$RPM_BUILD_ROOT"/"%{_sbindir}"/nologin "$RPM_BUILD_ROOT"/sbin
mv "$RPM_BUILD_ROOT"/"%{_libdir}"/* "$RPM_BUILD_ROOT"/"%{_lib}"
[[ "%{_libdir}" != "/%{_lib}" ]] && rm -rf "$RPM_BUILD_ROOT"/"%{_libdir}"

# Install new defaults

mkdir -p "$RPM_BUILD_ROOT"/etc
cp "%{SOURCE14}" "$RPM_BUILD_ROOT"/etc/login.defs
cp "%{SOURCE15}" "$RPM_BUILD_ROOT"/etc/default/useradd


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ "$RPM_BUILD_ROOT" != "/" ]] && rm -rf "$RPM_BUILD_ROOT"


%files -f shadow.lang
%defattr(-, root, root)
%dir /etc/default
%config(noreplace) /etc/login.defs
%config(noreplace) /etc/pam.d/login
%config(noreplace) /etc/pam.d/su
/bin/groups
/bin/login
%attr(4755, root, root) /bin/su
/%{_lib}/libshadow.*
/sbin/nologin
%{_bindir}/faillog
%{_bindir}/lastlog
%{_mandir}/cs/man1/groups.1.gz
%{_mandir}/cs/man1/su.1.gz
%{_mandir}/cs/man5/faillog.5.gz
%{_mandir}/cs/man5/gshadow.5.gz
%{_mandir}/cs/man5/shadow.5.gz
%{_mandir}/cs/man8/faillog.8.gz
%{_mandir}/cs/man8/lastlog.8.gz
%{_mandir}/cs/man8/nologin.8.gz
%{_mandir}/de/man1/groups.1.gz
%{_mandir}/de/man1/login.1.gz
%{_mandir}/es/man1/login.1.gz
%{_mandir}/es/man1/su.1.gz
%{_mandir}/fi/man1/su.1.gz
%{_mandir}/fr/man1/groups.1.gz
%{_mandir}/fr/man1/login.1.gz
%{_mandir}/fr/man1/su.1.gz
%{_mandir}/fr/man3/getspnam.3.gz
%{_mandir}/fr/man3/shadow.3.gz
%{_mandir}/fr/man5/faillog.5.gz
%{_mandir}/fr/man5/gshadow.5.gz
%{_mandir}/fr/man5/login.defs.5.gz
%{_mandir}/fr/man5/shadow.5.gz
%{_mandir}/fr/man5/suauth.5.gz
%{_mandir}/fr/man8/faillog.8.gz
%{_mandir}/fr/man8/lastlog.8.gz
%{_mandir}/hu/man1/groups.1.gz
%{_mandir}/hu/man1/login.1.gz
%{_mandir}/hu/man1/su.1.gz
%{_mandir}/hu/man8/lastlog.8.gz
%{_mandir}/id/man1/login.1.gz
%{_mandir}/it/man1/groups.1.gz
%{_mandir}/it/man1/login.1.gz
%{_mandir}/it/man1/su.1.gz
%{_mandir}/it/man3/getspnam.3.gz
%{_mandir}/it/man3/shadow.3.gz
%{_mandir}/it/man5/faillog.5.gz
%{_mandir}/it/man5/shadow.5.gz
%{_mandir}/it/man8/faillog.8.gz
%{_mandir}/it/man8/lastlog.8.gz
%{_mandir}/ja/man1/groups.1.gz
%{_mandir}/ja/man1/login.1.gz
%{_mandir}/ja/man1/su.1.gz
%{_mandir}/ja/man5/faillog.5.gz
%{_mandir}/ja/man5/login.defs.5.gz
%{_mandir}/ja/man5/shadow.5.gz
%{_mandir}/ja/man5/suauth.5.gz
%{_mandir}/ja/man8/faillog.8.gz
%{_mandir}/ja/man8/lastlog.8.gz
%{_mandir}/ko/man1/groups.1.gz
%{_mandir}/ko/man1/login.1.gz
%{_mandir}/ko/man1/su.1.gz
%{_mandir}/man1/groups.1.gz
%{_mandir}/man1/login.1.gz
%{_mandir}/man1/su.1.gz
%{_mandir}/man3/getspnam.3.gz
%{_mandir}/man3/shadow.3.gz
%{_mandir}/man5/faillog.5.gz
%{_mandir}/man5/gshadow.5.gz
%{_mandir}/man5/limits.5.gz
%{_mandir}/man5/login.access.5.gz
%{_mandir}/man5/login.defs.5.gz
%{_mandir}/man5/porttime.5.gz
%{_mandir}/man5/shadow.5.gz
%{_mandir}/man5/suauth.5.gz
%{_mandir}/man8/faillog.8.gz
%{_mandir}/man8/lastlog.8.gz
%{_mandir}/man8/nologin.8.gz
%{_mandir}/pl/man1/groups.1.gz
%{_mandir}/pl/man1/login.1.gz
%{_mandir}/pl/man1/su.1.gz
%{_mandir}/pl/man5/faillog.5.gz
%{_mandir}/pl/man5/login.defs.5.gz
%{_mandir}/pl/man5/shadow.5.gz
%{_mandir}/pl/man5/suauth.5.gz
%{_mandir}/pl/man8/faillog.8.gz
%{_mandir}/pl/man8/lastlog.8.gz
%{_mandir}/pt_BR/man5/shadow.5.gz
%{_mandir}/ru/man1/groups.1.gz
%{_mandir}/ru/man1/login.1.gz
%{_mandir}/ru/man1/su.1.gz
%{_mandir}/ru/man3/getspnam.3.gz
%{_mandir}/ru/man3/shadow.3.gz
%{_mandir}/ru/man5/faillog.5.gz
%{_mandir}/ru/man5/gshadow.5.gz
%{_mandir}/ru/man5/limits.5.gz
%{_mandir}/ru/man5/login.access.5.gz
%{_mandir}/ru/man5/login.defs.5.gz
%{_mandir}/ru/man5/porttime.5.gz
%{_mandir}/ru/man5/shadow.5.gz
%{_mandir}/ru/man5/suauth.5.gz
%{_mandir}/ru/man8/faillog.8.gz
%{_mandir}/ru/man8/lastlog.8.gz
%{_mandir}/ru/man8/nologin.8.gz
%{_mandir}/sv/man1/groups.1.gz
%{_mandir}/sv/man1/login.1.gz
%{_mandir}/sv/man1/su.1.gz
%{_mandir}/sv/man3/getspnam.3.gz
%{_mandir}/sv/man3/shadow.3.gz
%{_mandir}/sv/man5/faillog.5.gz
%{_mandir}/sv/man5/gshadow.5.gz
%{_mandir}/sv/man5/login.defs.5.gz
%{_mandir}/sv/man5/shadow.5.gz
%{_mandir}/sv/man5/suauth.5.gz
%{_mandir}/sv/man8/faillog.8.gz
%{_mandir}/sv/man8/lastlog.8.gz
%{_mandir}/sv/man8/nologin.8.gz
%{_mandir}/tr/man1/login.1.gz
%{_mandir}/tr/man1/su.1.gz
%{_mandir}/tr/man5/shadow.5.gz
%{_mandir}/zh_CN/man1/su.1.gz
%{_mandir}/zh_TW/man1/su.1.gz


%files utils
%config(noreplace) /etc/default/useradd
%config(noreplace) /etc/pam.d/chage
%config(noreplace) /etc/pam.d/chgpasswd
%config(noreplace) /etc/pam.d/chpasswd
%config(noreplace) /etc/pam.d/groupadd
%config(noreplace) /etc/pam.d/groupdel
%config(noreplace) /etc/pam.d/groupmems
%config(noreplace) /etc/pam.d/groupmod
%config(noreplace) /etc/pam.d/newusers
%config(noreplace) /etc/pam.d/passwd
%config(noreplace) /etc/pam.d/useradd
%config(noreplace) /etc/pam.d/usermod
%attr(4755, root, root) %{_bindir}/chage
%attr(4755, root, root) %{_bindir}/chfn
%attr(4755, root, root) %{_bindir}/chsh
%attr(4755, root, root) %{_bindir}/expiry
%attr(4755, root, root) %{_bindir}/gpasswd
%attr(4755, root, root) %{_bindir}/newgrp
%attr(4755, root, root) %{_bindir}/passwd
%{_bindir}/sg
%{_sbindir}/chgpasswd
%{_sbindir}/chpasswd
%{_sbindir}/groupadd
%{_sbindir}/groupdel
%{_sbindir}/groupmems
%{_sbindir}/groupmod
%{_sbindir}/grpck
%{_sbindir}/grpconv
%{_sbindir}/grpunconv
%{_sbindir}/logoutd
%{_sbindir}/newusers
%{_sbindir}/pwck
%{_sbindir}/pwconv
%{_sbindir}/pwunconv
%{_sbindir}/useradd
%{_sbindir}/userdel
%{_sbindir}/usermod
%{_sbindir}/vigr
%{_sbindir}/vipw
%{_mandir}/cs/man1/expiry.1.gz
%{_mandir}/cs/man1/gpasswd.1.gz
%{_mandir}/cs/man5/passwd.5.gz
%{_mandir}/cs/man8/groupadd.8.gz
%{_mandir}/cs/man8/groupdel.8.gz
%{_mandir}/cs/man8/groupmod.8.gz
%{_mandir}/cs/man8/grpck.8.gz
%{_mandir}/cs/man8/vipw.8.gz
%{_mandir}/de/man1/chfn.1.gz
%{_mandir}/de/man1/chsh.1.gz
%{_mandir}/de/man1/newgrp.1.gz
%{_mandir}/de/man1/passwd.1.gz
%{_mandir}/de/man5/passwd.5.gz
%{_mandir}/de/man8/vigr.8.gz
%{_mandir}/de/man8/vipw.8.gz
%{_mandir}/es/man1/newgrp.1.gz
%{_mandir}/es/man1/passwd.1.gz
%{_mandir}/es/man5/passwd.5.gz
%{_mandir}/es/man8/vigr.8.gz
%{_mandir}/es/man8/vipw.8.gz
%{_mandir}/fi/man1/chfn.1.gz
%{_mandir}/fi/man1/chsh.1.gz
%{_mandir}/fi/man1/passwd.1.gz
%{_mandir}/fr/man1/chage.1.gz
%{_mandir}/fr/man1/chfn.1.gz
%{_mandir}/fr/man1/chsh.1.gz
%{_mandir}/fr/man1/expiry.1.gz
%{_mandir}/fr/man1/gpasswd.1.gz
%{_mandir}/fr/man1/newgrp.1.gz
%{_mandir}/fr/man1/passwd.1.gz
%{_mandir}/fr/man1/sg.1.gz
%{_mandir}/fr/man5/passwd.5.gz
%{_mandir}/fr/man8/chpasswd.8.gz
%{_mandir}/fr/man8/groupadd.8.gz
%{_mandir}/fr/man8/groupdel.8.gz
%{_mandir}/fr/man8/groupmod.8.gz
%{_mandir}/fr/man8/grpck.8.gz
%{_mandir}/fr/man8/grpconv.8.gz
%{_mandir}/fr/man8/grpunconv.8.gz
%{_mandir}/fr/man8/logoutd.8.gz
%{_mandir}/fr/man8/newusers.8.gz
%{_mandir}/fr/man8/pwck.8.gz
%{_mandir}/fr/man8/pwconv.8.gz
%{_mandir}/fr/man8/pwunconv.8.gz
%{_mandir}/fr/man8/useradd.8.gz
%{_mandir}/fr/man8/userdel.8.gz
%{_mandir}/fr/man8/usermod.8.gz
%{_mandir}/fr/man8/vigr.8.gz
%{_mandir}/fr/man8/vipw.8.gz
%{_mandir}/hu/man1/chsh.1.gz
%{_mandir}/hu/man1/gpasswd.1.gz
%{_mandir}/hu/man1/newgrp.1.gz
%{_mandir}/hu/man1/passwd.1.gz
%{_mandir}/hu/man1/sg.1.gz
%{_mandir}/hu/man5/passwd.5.gz
%{_mandir}/id/man1/chsh.1.gz
%{_mandir}/id/man8/useradd.8.gz
%{_mandir}/it/man1/chage.1.gz
%{_mandir}/it/man1/chfn.1.gz
%{_mandir}/it/man1/chsh.1.gz
%{_mandir}/it/man1/expiry.1.gz
%{_mandir}/it/man1/gpasswd.1.gz
%{_mandir}/it/man1/newgrp.1.gz
%{_mandir}/it/man1/passwd.1.gz
%{_mandir}/it/man1/sg.1.gz
%{_mandir}/it/man5/passwd.5.gz
%{_mandir}/it/man8/chpasswd.8.gz
%{_mandir}/it/man8/groupadd.8.gz
%{_mandir}/it/man8/groupdel.8.gz
%{_mandir}/it/man8/groupmod.8.gz
%{_mandir}/it/man8/grpck.8.gz
%{_mandir}/it/man8/grpconv.8.gz
%{_mandir}/it/man8/grpunconv.8.gz
%{_mandir}/it/man8/newusers.8.gz
%{_mandir}/it/man8/pwck.8.gz
%{_mandir}/it/man8/pwconv.8.gz
%{_mandir}/it/man8/pwunconv.8.gz
%{_mandir}/it/man8/useradd.8.gz
%{_mandir}/it/man8/userdel.8.gz
%{_mandir}/it/man8/usermod.8.gz
%{_mandir}/it/man8/vigr.8.gz
%{_mandir}/it/man8/vipw.8.gz
%{_mandir}/ja/man1/chage.1.gz
%{_mandir}/ja/man1/chfn.1.gz
%{_mandir}/ja/man1/chsh.1.gz
%{_mandir}/ja/man1/expiry.1.gz
%{_mandir}/ja/man1/gpasswd.1.gz
%{_mandir}/ja/man1/newgrp.1.gz
%{_mandir}/ja/man1/passwd.1.gz
%{_mandir}/ja/man1/sg.1.gz
%{_mandir}/ja/man5/passwd.5.gz
%{_mandir}/ja/man8/chpasswd.8.gz
%{_mandir}/ja/man8/groupadd.8.gz
%{_mandir}/ja/man8/groupdel.8.gz
%{_mandir}/ja/man8/groupmod.8.gz
%{_mandir}/ja/man8/grpck.8.gz
%{_mandir}/ja/man8/grpconv.8.gz
%{_mandir}/ja/man8/grpunconv.8.gz
%{_mandir}/ja/man8/logoutd.8.gz
%{_mandir}/ja/man8/newusers.8.gz
%{_mandir}/ja/man8/pwck.8.gz
%{_mandir}/ja/man8/pwconv.8.gz
%{_mandir}/ja/man8/pwunconv.8.gz
%{_mandir}/ja/man8/useradd.8.gz
%{_mandir}/ja/man8/userdel.8.gz
%{_mandir}/ja/man8/usermod.8.gz
%{_mandir}/ja/man8/vigr.8.gz
%{_mandir}/ja/man8/vipw.8.gz
%{_mandir}/ko/man1/chfn.1.gz
%{_mandir}/ko/man1/chsh.1.gz
%{_mandir}/ko/man5/passwd.5.gz
%{_mandir}/ko/man8/vigr.8.gz
%{_mandir}/ko/man8/vipw.8.gz
%{_mandir}/man1/chage.1.gz
%{_mandir}/man1/chfn.1.gz
%{_mandir}/man1/chsh.1.gz
%{_mandir}/man1/expiry.1.gz
%{_mandir}/man1/gpasswd.1.gz
%{_mandir}/man1/newgrp.1.gz
%{_mandir}/man1/passwd.1.gz
%{_mandir}/man1/sg.1.gz
%{_mandir}/man5/passwd.5.gz
%{_mandir}/man8/chgpasswd.8.gz
%{_mandir}/man8/chpasswd.8.gz
%{_mandir}/man8/groupadd.8.gz
%{_mandir}/man8/groupdel.8.gz
%{_mandir}/man8/groupmems.8.gz
%{_mandir}/man8/groupmod.8.gz
%{_mandir}/man8/grpck.8.gz
%{_mandir}/man8/grpconv.8.gz
%{_mandir}/man8/grpunconv.8.gz
%{_mandir}/man8/logoutd.8.gz
%{_mandir}/man8/newusers.8.gz
%{_mandir}/man8/pwck.8.gz
%{_mandir}/man8/pwconv.8.gz
%{_mandir}/man8/pwunconv.8.gz
%{_mandir}/man8/useradd.8.gz
%{_mandir}/man8/userdel.8.gz
%{_mandir}/man8/usermod.8.gz
%{_mandir}/man8/vigr.8.gz
%{_mandir}/man8/vipw.8.gz
%{_mandir}/pl/man1/chage.1.gz
%{_mandir}/pl/man1/chfn.1.gz
%{_mandir}/pl/man1/chsh.1.gz
%{_mandir}/pl/man1/expiry.1.gz
%{_mandir}/pl/man1/gpasswd.1.gz
%{_mandir}/pl/man1/newgrp.1.gz
%{_mandir}/pl/man1/passwd.1.gz
%{_mandir}/pl/man1/sg.1.gz
%{_mandir}/pl/man5/passwd.5.gz
%{_mandir}/pl/man8/chpasswd.8.gz
%{_mandir}/pl/man8/groupadd.8.gz
%{_mandir}/pl/man8/groupdel.8.gz
%{_mandir}/pl/man8/groupmod.8.gz
%{_mandir}/pl/man8/grpck.8.gz
%{_mandir}/pl/man8/grpconv.8.gz
%{_mandir}/pl/man8/grpunconv.8.gz
%{_mandir}/pl/man8/logoutd.8.gz
%{_mandir}/pl/man8/newusers.8.gz
%{_mandir}/pl/man8/pwck.8.gz
%{_mandir}/pl/man8/pwconv.8.gz
%{_mandir}/pl/man8/pwunconv.8.gz
%{_mandir}/pl/man8/useradd.8.gz
%{_mandir}/pl/man8/userdel.8.gz
%{_mandir}/pl/man8/usermod.8.gz
%{_mandir}/pl/man8/vigr.8.gz
%{_mandir}/pl/man8/vipw.8.gz
%{_mandir}/pt_BR/man1/gpasswd.1.gz
%{_mandir}/pt_BR/man5/passwd.5.gz
%{_mandir}/pt_BR/man8/groupadd.8.gz
%{_mandir}/pt_BR/man8/groupdel.8.gz
%{_mandir}/pt_BR/man8/groupmod.8.gz
%{_mandir}/ru/man1/chage.1.gz
%{_mandir}/ru/man1/chfn.1.gz
%{_mandir}/ru/man1/chsh.1.gz
%{_mandir}/ru/man1/expiry.1.gz
%{_mandir}/ru/man1/gpasswd.1.gz
%{_mandir}/ru/man1/newgrp.1.gz
%{_mandir}/ru/man1/passwd.1.gz
%{_mandir}/ru/man1/sg.1.gz
%{_mandir}/ru/man5/passwd.5.gz
%{_mandir}/ru/man8/chgpasswd.8.gz
%{_mandir}/ru/man8/chpasswd.8.gz
%{_mandir}/ru/man8/groupadd.8.gz
%{_mandir}/ru/man8/groupdel.8.gz
%{_mandir}/ru/man8/groupmems.8.gz
%{_mandir}/ru/man8/groupmod.8.gz
%{_mandir}/ru/man8/grpck.8.gz
%{_mandir}/ru/man8/grpconv.8.gz
%{_mandir}/ru/man8/grpunconv.8.gz
%{_mandir}/ru/man8/logoutd.8.gz
%{_mandir}/ru/man8/newusers.8.gz
%{_mandir}/ru/man8/pwck.8.gz
%{_mandir}/ru/man8/pwconv.8.gz
%{_mandir}/ru/man8/pwunconv.8.gz
%{_mandir}/ru/man8/useradd.8.gz
%{_mandir}/ru/man8/userdel.8.gz
%{_mandir}/ru/man8/usermod.8.gz
%{_mandir}/ru/man8/vigr.8.gz
%{_mandir}/ru/man8/vipw.8.gz
%{_mandir}/sv/man1/chage.1.gz
%{_mandir}/sv/man1/chfn.1.gz
%{_mandir}/sv/man1/chsh.1.gz
%{_mandir}/sv/man1/expiry.1.gz
%{_mandir}/sv/man1/gpasswd.1.gz
%{_mandir}/sv/man1/newgrp.1.gz
%{_mandir}/sv/man1/passwd.1.gz
%{_mandir}/sv/man1/sg.1.gz
%{_mandir}/sv/man5/passwd.5.gz
%{_mandir}/sv/man8/chgpasswd.8.gz
%{_mandir}/sv/man8/chpasswd.8.gz
%{_mandir}/sv/man8/groupadd.8.gz
%{_mandir}/sv/man8/groupdel.8.gz
%{_mandir}/sv/man8/groupmems.8.gz
%{_mandir}/sv/man8/groupmod.8.gz
%{_mandir}/sv/man8/grpck.8.gz
%{_mandir}/sv/man8/grpconv.8.gz
%{_mandir}/sv/man8/grpunconv.8.gz
%{_mandir}/sv/man8/logoutd.8.gz
%{_mandir}/sv/man8/newusers.8.gz
%{_mandir}/sv/man8/pwck.8.gz
%{_mandir}/sv/man8/pwconv.8.gz
%{_mandir}/sv/man8/pwunconv.8.gz
%{_mandir}/sv/man8/useradd.8.gz
%{_mandir}/sv/man8/userdel.8.gz
%{_mandir}/sv/man8/usermod.8.gz
%{_mandir}/sv/man8/vigr.8.gz
%{_mandir}/sv/man8/vipw.8.gz
%{_mandir}/tr/man1/chage.1.gz
%{_mandir}/tr/man1/chfn.1.gz
%{_mandir}/tr/man1/passwd.1.gz
%{_mandir}/tr/man5/passwd.5.gz
%{_mandir}/tr/man8/groupadd.8.gz
%{_mandir}/tr/man8/groupdel.8.gz
%{_mandir}/tr/man8/groupmod.8.gz
%{_mandir}/tr/man8/useradd.8.gz
%{_mandir}/tr/man8/userdel.8.gz
%{_mandir}/tr/man8/usermod.8.gz
%{_mandir}/zh_CN/man1/chfn.1.gz
%{_mandir}/zh_CN/man1/chsh.1.gz
%{_mandir}/zh_CN/man1/newgrp.1.gz
%{_mandir}/zh_CN/man5/passwd.5.gz
%{_mandir}/zh_CN/man8/chpasswd.8.gz
%{_mandir}/zh_CN/man8/groupadd.8.gz
%{_mandir}/zh_CN/man8/groupdel.8.gz
%{_mandir}/zh_CN/man8/groupmod.8.gz
%{_mandir}/zh_CN/man8/useradd.8.gz
%{_mandir}/zh_CN/man8/userdel.8.gz
%{_mandir}/zh_CN/man8/usermod.8.gz
%{_mandir}/zh_TW/man1/chfn.1.gz
%{_mandir}/zh_TW/man1/chsh.1.gz
%{_mandir}/zh_TW/man1/newgrp.1.gz
%{_mandir}/zh_TW/man5/passwd.5.gz
%{_mandir}/zh_TW/man8/chpasswd.8.gz
%{_mandir}/zh_TW/man8/groupadd.8.gz
%{_mandir}/zh_TW/man8/groupdel.8.gz
%{_mandir}/zh_TW/man8/groupmod.8.gz
%{_mandir}/zh_TW/man8/useradd.8.gz
%{_mandir}/zh_TW/man8/userdel.8.gz
%{_mandir}/zh_TW/man8/usermod.8.gz
