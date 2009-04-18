Name: cyrus-sasl
Version: 2.1.22
Release: 2ev
Summary: A generic client/server library for SASL authentication
URL: http://asg.web.cmu.edu/sasl/
Group: System Environment/Libraries
License: BSD
Vendor: GNyU-Linux
Source: ftp://ftp.andrew.cmu.edu/pub/cyrus-mail/cyrus-sasl-%{version}.tar.gz
Source1: %{name}-saslauthd
Source2: %{name}-saslauthd.i
BuildRequires: gcc, make >= 3.79.1, openssl, db >= 4.5
BuildRequires: heimdal-libs, libpam

%description
The Cyrus SASL library is a generic library for easy integration of secure
network authentication to any client or server application. It supports
authentication via standard plaintext methods as well as CRAM-MD5 and
DIGEST-MD5 shared secret methods and KERBEROS_V4 and GSSAPI Kerberos methods.
The SASL protocol framework is used by SMTP, IMAP, ACAP, LDAP, and other
standard protocols.


%prep
%setup -q


%build
%configure \
	--with-dbpath=%{_sysconfdir}/sasldb2 \
	--with-pwcheck=%{_localstatedir}/run \
	--with-saslauthd=%{_localstatedir}/run \
	--with-authdaemond=%{_localstatedir}/run \
	--disable-java \
	--enable-checkapop \
	--enable-cram \
	--enable-digest \
	--enable-gssapi \
	--enable-gss_mutexes \
	--enable-plain \
	--enable-anon \
	--enable-login 
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'


# Create saslauthd startup file
%{__mkdir_p} %{buildroot}/%{_sysconfdir}/initng/{daemon,iconfig}
%{__cat} < %{SOURCE1} > %{buildroot}/etc/initng/iconfig/saslauthd
%{install_ifile '%{SOURCE2}' daemon/saslauthd.i}


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc README* AUTHORS COPYING ChangeLog NEWS
%config(noreplace) %attr(0660, root, root) /etc/initng/iconfig/saslauthd
%config(noreplace) %attr(0660, root, root) /etc/initng/daemon/saslauthd.i
%{_includedir}/sasl/
%{_libdir}/lib*sasl*.*
%{_libdir}/sasl2/
%{_mandir}/*/*
%{_sbindir}/pluginviewer
%{_sbindir}/saslauthd
%{_sbindir}/sasldblistusers2
%{_sbindir}/saslpasswd2
%{_sbindir}/testsaslauthd
%{_sbindir}/pwcheck
