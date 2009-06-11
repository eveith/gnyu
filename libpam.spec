Name: libpam
Version: 1.0.4
Release: 3ev
Summary: Linux Pluggable Authentication Modules
URL: http://www.kernel.org/pub/linux/libs/pam
Group: System Environment/Base
License: GPL
Vendor: GNyU-Linux
Source0: ftp://ftp.kernel.org/pub/linux/libs/pam/library/Linux-PAM-%{version}.tar.bz2
Patch0: %{name}-0.99.6.2-unix-username.patch
Patch1: %{name}-1.0.4-fix-tst-pam_mkargv-x86.patch
Source1: %{name}-system-auth
Source2: %{name}-other
BuildRequires: make >= 3.79.1, gcc, flex, bison, gettext, db-devel

%description
PAM is a flexible mechanism for authenticating users.  Since the beginnings of
UNIX, authenticating a user has been accomplished via the user entering a
password and the system checking if the entered password corresponds to the
encrypted official password that is stored in /etc/passwd.  That was in the
beginning. Since then, a number of new ways of authenticating users have
become popular. The problem is that each time a new authentication scheme is
developed, it requires all the necessary programs (login, ftpd, etc...) to be
rewritten to support it.  PAM provides a way to develop programs that are
independent of authentication scheme. These programs need "authentication
modules" to be attatched to them at run-time in order to work. Which
authentication module is to be attatched is dependent upon the local system
setup and is at the discretion of the local system administrator.


%prep
	%setup -q -n Linux-PAM-%{version}
	[[ '%{version}' = '0.99.6.2' ]] && %patch0 -p1
	[[ '%{version}' = '1.0.4' ]] && %patch1 -p1


%build
	%configure \
	    --libdir='/%{_lib}' \
		--includedir='%{_includedir}/security' \
		--enable-docdir='%{_docdir}/%{name}' \
		--docdir='%{_docdir}/%{name}' \
		--enable-securedir='/%{_lib}/security' \
		--enable-db=db \
		--disable-selinux \
		--disable-audit \
		--disable-prelude \
		--disable-rpath
	%{__make} %{?_smp_mflags}
	%{__make} check


%install
	%{__make} install DESTDIR='%{buildroot}'
	%{__rm} -f '%{buildroot}/%{_infodir}/dir'
	%find_lang Linux-PAM
	
	%{__mkdir_p} '%{buildroot}/etc/pam.d'
	
	# Install default system auth/account/session/password files
	%{__cat} < '%{SOURCE1}' > '%{buildroot}/etc/pam.d/system-auth'
	
	# Create a non-weak "other" configuration that at least allows to log in
	%{__cat} < '%{SOURCE2}' > '%{buildroot}/etc/pam.d/other'
	
	%{__mv} '%{buildroot}/%{_docdir}/%{name}' \
		"${RPM_BUILD_DIR}/Linux-PAM-%{version}/Documentation"


%post
	%{__ldconfig}


%postun
	%{__ldconfig}


%files -f Linux-PAM.lang
	%defattr(-, root, root)
	%doc ABOUT-NLS AUTHORS README CHANGELOG ChangeLog Copyright NEWS
	%doc Documentation/ doc/sag doc/mwg doc/adg
	%config(noreplace) %{_sysconfdir}/environment
	%dir %{_sysconfdir}/pam.d
	%config(noreplace) %{_sysconfdir}/pam.d/system-*
	%config(noreplace) %{_sysconfdir}/pam.d/other
	%dir %{_sysconfdir}/security
	%config(noreplace) %{_sysconfdir}/security/access.conf
	%config(noreplace) %{_sysconfdir}/security/group.conf
	%config(noreplace) %{_sysconfdir}/security/limits.conf
	%config(noreplace) %{_sysconfdir}/security/pam_env.conf
	%config(noreplace) %{_sysconfdir}/security/time.conf
	%config(noreplace) %{_sysconfdir}/security/namespace.*
	%{_includedir}/security/
	/%{_lib}/libpam*.*
	/%{_lib}/security/
	%{_mandir}/*/*
	%{_sbindir}/pam_tally
	%{_sbindir}/unix_update
	%attr(4711, root, root) %{_sbindir}/unix_chkpwd
