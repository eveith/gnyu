Name: pwdutils
Version: 3.1.3
Release: 1ev
Summary: Utilities to manage/change user passwd information.
URL: http://www.thkukuk.de/pam/pwdutils/
Group: System Environment/Base
License: GPL
Vendor: MSP Slackware
Source: ftp://ftp.kernel.org/pub/linux/utils/net/NIS/%{name}-%{version}.tar.bz2
Source1: pwdutils-pam-chage
Source3: pwdutils-pam-chpasswd
Source4: pwdutils-pam-groupadd
Source5: pwdutils-pam-groupdel
Source7: pwdutils-pam-groupmod
Source10: pwdutils-pam-passwd
Source12: pwdutils-pam-useradd
Source13: pwdutils-pam-usermod
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc-core, openssl, openldap-libs, libpam
Requires: libpam, openldap-libs
Conflicts: shadow-utils
Provides: libtool(%{_libdir}/pwdutils/liblog_syslog.la)

%description
pwdutils is a collection of utilities to manage the passwd and shadow user
information. The difference to the shadow suite is that these utilities can
also modify the information stored in NIS, NIS+, or LDAP. PAM is used for user
authentication and changing the pasword. It contains passwd, chage, chfn,
chsh, chpasswd, expiry, gpasswd, grpck, groupadd, groupdel, groupmod,
grpunconv, newgrp, pwck, pwconv, pwunconv, useradd, userdel, usermod, vipw,
and a daemon for changing the password on a remote machine over a secure SSL
connection. The daemon also uses PAM, so it can change passwords no matter
where they are stored.
The pwdutils rely on the openldap libraries, which brings alot of dependencies
and additional libraries to install. If you wish to keep your system clean and
tidy, and have no need accessing LDAP databases for user management pourposes,
you should use shadow-utils instead.


%prep
%setup -q


%build
%configure \
	--disable-selinux \
	--enable-ldap
make


%install
[[ "$RPM_BUILD_ROOT" != "/" ]] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"

rm -vf "$RPM_BUILD_ROOT"/"%{_infodir}"/dir

%find_lang pwdutils

# Install default pam files

mkdir -p "$RPM_BUILD_ROOT"/etc/pam.d
for source in %{SOURCE1} %{SOURCE3} %{SOURCE4} %{SOURCE5} \
        %{SOURCE7} %{SOURCE10} %{SOURCE12} %{SOURCE13}
do
	newname=${source#$RPM_SOURCE_DIR/}
    cp $source ${RPM_BUILD_ROOT}/etc/pam.d/${newname#pwdutils-pam-}
done

pushd "$RPM_BUILD_ROOT"

# Remove unneccessary startup file
rm -fr etc/init.d

# This is provided by the shadow package (which provides login and su!)
rm -f etc/login.defs

popd


%post
/sbin/ldconfig
chown root:root /etc/shadow
chmod 400 /etc/shadow

%postun
/sbin/ldconfig


%clean
[[ "$RPM_BUILD_ROOT" != "/" ]] && rm -rf "$RPM_BUILD_ROOT"


%files -f pwdutils.lang
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS COPYING ChangeLog* README THANKS TODO 
%dir /etc/default
%config(noreplace) /etc/default/passwd
%config(noreplace) /etc/default/useradd
%config(noreplace) /etc/pam.d/usermod
%config(noreplace) /etc/pam.d/chage
%config(noreplace) /etc/pam.d/chfn
%config(noreplace) /etc/pam.d/chsh
%config(noreplace) /etc/pam.d/chpasswd
%config(noreplace) /etc/pam.d/passwd
%config(noreplace) /etc/pam.d/rpasswd
%config(noreplace) /etc/pam.d/shadow
%config(noreplace) /etc/pam.d/useradd
%config(noreplace) /etc/pam.d/groupadd
%config(noreplace) /etc/pam.d/groupdel
%config(noreplace) /etc/pam.d/groupmod
%dir /etc/pwdutils
%config(noreplace) /etc/pwdutils/logging
%config(noreplace) /etc/rpasswd.conf
%attr(4711, root, root) %{_bindir}/chage
%attr(4711, root, root) %{_bindir}/chfn
%attr(4711, root, root) %{_bindir}/chsh
%attr(4711, root, root) %{_bindir}/expiry
%attr(4711, root, root) %{_bindir}/passwd
%{_bindir}/gpasswd
%{_bindir}/newgrp
%{_bindir}/rpasswd
%{_bindir}/sg
%{_libdir}/pwdutils/
%{_mandir}/*/*
%{_sbindir}/chpasswd
%{_sbindir}/groupadd
%config(noreplace) %{_sbindir}/groupadd.local
%{_sbindir}/groupdel
%{_sbindir}/groupmod
%{_sbindir}/grpck
%{_sbindir}/grpconv
%{_sbindir}/grpunconv
%{_sbindir}/pwck
%{_sbindir}/pwconv
%{_sbindir}/pwunconv
%{_sbindir}/rpasswdd
%{_sbindir}/useradd
%config(noreplace) %{_sbindir}/useradd.local
%{_sbindir}/userdel
%config(noreplace) %{_sbindir}/userdel-post.local
%config(noreplace) %{_sbindir}/userdel-pre.local
%{_sbindir}/usermod
%{_sbindir}/vigr
%{_sbindir}/vipw
