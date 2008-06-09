Name: libpam
Version: 0.99.9.0
Release: 1ev
Summary: Linux Pluggable Authentication Modules
URL: http://www.kernel.org/pub/linux/libs/pam
Group: System Environment/Base
License: GPL
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source0: ftp://ftp.kernel.org/pub/linux/libs/pam/pre/library/Linux-PAM-%{version}.tar.bz2
Patch0: libpam-0.99.6.2-unix-username.patch
Source1: libpam-system-auth
Source2: libpam-other
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc-core, sed, db, gettext, flex, bison
Provides: libtool(%{_libdir}/libpam.la)

%description
PAM is a flexible mechanism for authenticating users.
Since the beginnings of UNIX, authenticating a user has been accomplished
via the user entering a password and the system checking if the entered
password corresponds to the encrypted official password that is stored in 
/etc/passwd.
That was in the beginning. Since then, a number of new ways of
authenticating users have become popular. The problem is that each time a
new authentication scheme is developed, it requires all the necessary 
programs (login, ftpd, etc...) to be rewritten to support it.
PAM provides a way to develop programs that are independent of
authentication scheme. These programs need "authentication modules" to be
attatched to them at run-time in order to work. Which authentication
module is to be attatched is dependent upon the local system setup and is 
at the discretion of the local system administrator.


%prep
%setup -q -n Linux-PAM-%{version}
[ "%{version}" = "0.99.6.2" ] && %patch0 -p1


%build
%configure \
    --libdir=/%{_lib} \
	--includedir=%{_includedir}/security \
	--enable-docdir=%{_docdir}/%{name} \
	--docdir=%{_docdir}/%{name} \
	--enable-securedir=/%{_lib}/security \
	--disable-selinux \
	--disable-audit \
	--disable-prelude \
	--disable-rpath

%{__make} %{?_smp_mflags}
%{__make} check
# make xtests


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%{__rm} -f %{buildroot}/%{_infodir}/dir
%find_lang Linux-PAM

%{__mkdir_p} %{buildroot}/etc/pam.d

# Install default system auth/account/session/password files
%{__cat} < %{SOURCE1} > %{buildroot}/etc/pam.d/system-auth

# Create a non-weak "other" configuration that at least allows to log in
%{__cat} < %{SOURCE2} > %{buildroot}/etc/pam.d/other

%{__mv} %{buildroot}/%{_docdir}/%{name} \
	${RPM_BUILD_DIR}/Linux-PAM-%{version}/Documentation


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files -f Linux-PAM.lang
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS README CHANGELOG ChangeLog Copyright NEWS
%doc Documentation/
%config(noreplace) /etc/environment
%dir /etc/pam.d
%config(noreplace) /etc/pam.d/system-*
%config(noreplace) /etc/pam.d/other
%dir /etc/security
%config(noreplace) /etc/security/access.conf
%config(noreplace) /etc/security/group.conf
%config(noreplace) /etc/security/limits.conf
%config(noreplace) /etc/security/pam_env.conf
%config(noreplace) /etc/security/time.conf
%config(noreplace) /etc/security/namespace.*
%{_includedir}/security/
/%{_lib}/libpam*.*
/%{_lib}/security/
%{_mandir}/*/*
%{_sbindir}/pam_tally
%attr(4755, root, root) %{_sbindir}/unix_chkpwd
