Name: pam_ldap
Version: 184
Release: 2ev
Summary: A PAM module that allows authentication against a LDAP service
URL: http://www.padl.com/OSS/pam_ldap.html
Group: System Environment/Libraries
License: LGPL-2, GPL-2
Vendor: GNyU-Linux
Source: ftp://ftp.padl.com/pub/pam_ldap.tgz
BuildRequires: make, gcc, libpam, openldap-libs, cyrus-sasl

%description
The pam_ldap module provides the means for Solaris and Linux servers 
and workstations to authenticate against LDAP directories, and to change 
their passwords in the directory. 
Key Benefits 
 - Uses the Pluggable Authentication Module API defined in OSF DCE RFC 86.0. 
 - Can utilize transport layer security (such as SSL or TLS) to encrypt 
   transactions between the workstation and the LDAP server and provide 
   strongly authenticated sign-on 
 - Support for SASL interactive authentication for strong authentication 
   without the overhead of SSL/TLS 
 - Supports PADL NIS/LDAP Gateway locator for finding LDAP servers 
 - Supports Netscape and IETF password policies 
 - Supports host- and group-based logon authorization


%prep
	%setup -q


%build
	%configure \
		--libdir='/%{_lib}'
	%{__make} %{?_smp_mflags}


%install
	%{__fakeroot} %{__make} install DESTDIR='%{buildroot}'


%files
	%defattr(-, root, root)
	%doc AUTHORS ChangeLog COPYING* NEWS README
	%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/ldap.conf
	/%{_lib}/security/pam_ldap.so*
	%doc %{_mandir}/man5/pam_ldap.5*
