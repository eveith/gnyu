Name: nss-ldapd
Version: 0.6.2
Release: 1ev
Summary: A NSS module for name lookups using LDAP
URL: http://ch.tudelft.nl/~arthur/nss-ldapd/
Group: System Environment/Libraries
License: LGPL-2.1
Vendor: GNyU-Linux
Source0: http://ch.tudelft.nl/~arthur/nss-ldapd/nss-ldapd-%{version}.tar.gz
Source1: %{name}-nslcd.i
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: coreutils,grep, sed, make >= 3.79.1, gcc
BuildRequires: cyrus-sasl, openldap-libs

%description
nss-ldapd is a (glibc) NSS module for doing name lookups to an LDAP server.
This module allows retrieval of information about Unix accounts, groups,
hosts, and other information from an LDAP directory. It is a fork from the
nss_ldap module to do some architectural changes. This implementation splits
the functionality into an NSS part and a local daemon to do the lookups. This
works around a number of problems in the original implementation.


%prep
%setup -q


%build
%configure \
	--libdir=/%{_lib} \
	--sbindir=/sbin \
	--with-ldap-conf-file=%{_sysconfdir}/nss-ldapd.conf \
	--with-ldap-secret-file=%{_sysconfdir}/nss-ldapd.secret \
	--with-nslcd-pidfile=%{_localstatedir}/run/nslcd.pid \
	--with-nslcd-socket=%{_localstatedir}/run/nslcd.sock
%{__make} %{?_smp_mflags}
	

%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'

pushd '%{buildroot}'

touch etc/nss-ldapd.secret

%{__mkdir_p} ./%{_localstatedir}/run
touch ./%{_localstatedir}/run/nslcd.{pid,sock}

%{__mkdir_p} etc/initng/daemon
%{__cat} < '%{SOURCE1}' |\
	%{__sed} -e 's,@localstatedir@,%{_localstatedir},g' \
	> etc/initng/daemon/nslcd.i

# cd sbin
# %{__ln_s} '%{_target_platform}-nslcd' nslcd
# cd ..
# cd usr/man/man5
# %{__ln_s} '%{_target_platform}-nss-ldapd.conf.5.gz' nss-ldapd.conf.5.gz
# cd ../man8
# %{__ln_s} '%{_target_platform}-nslcd.8.gz' nslcd.8.gz

popd


%preun
if [[ "${1}" -eq 0 ]]
then
	ngc -d daemon/nlscd 
	ng-update del daemon/nlscd default
fi > /dev/null 2>&1
exit 0

%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING HACKING NEWS README TODO
%{_sysconfdir}/initng/daemon/nslcd.i
%config(noreplace) %{_sysconfdir}/nss-ldapd.conf
%attr(0600, root, root) %config(noreplace) %ghost %{_sysconfdir}/nss-ldapd.secret
/%{_lib}/libnss_ldap*.*
/sbin/*nslcd
%{_mandir}/man5/*nss-ldapd.conf.5.gz
%{_mandir}/man8/*nslcd.8.gz
%ghost %{_localstatedir}/run/nslcd.*
