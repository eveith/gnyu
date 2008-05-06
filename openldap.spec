Name: openldap
Version: 2.3.39
Release: 2ev
Summary: LDAP suite of applications and development tools
URL: http://www.openldap.org/
Group: Applications/Communications
License: BSD
Vendor: GNyU-Linux
Source0: ftp://ftp.openldap.org/pub/OpenLDAP/%{name}-release/%{name}-%{version}.tgz
Source1: %{name}-slapd.i
Source2: %{name}-slurpd.i
Source3: %{name}-slapd.conf.d
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: coreutils, grep, sed, gettext, gcc, make >= 3.79.1
BuildRequires: openssl >= 0.9.7, db >= 4.2, heimdal-libs, cyrus-sasl >= 2.1.18
BuildRequires: pcre, openslp
%define _slapd_uid 507
%define _ldap_gid 54

%description
The OpenLDAP Project is a collaborative effort to provide a robust,
commercial-grade, fully featured, open source LDAP software suite. The project
is managed by a worldwide community of volunteers that use the Internet to
communicate, plan, and develop OpenLDAP Software and its related
documentation. OpenLDAP Software provides a complete LDAP implementation
including server, clients, C SDK, and associated tools.
This package provies client tools and utilities to access a LDAP directory.


%package libs
Summary: OpenLDAP libraries
Group: System Environment/Libraries

%description libs
The OpenLDAP Project is a collaborative effort to provide a robust,
commercial-grade, fully featured, open source LDAP software suite. The project
is managed by a worldwide community of volunteers that use the Internet to
communicate, plan, and develop OpenLDAP Software and its related
documentation. OpenLDAP Software provides a complete LDAP implementation
including server, clients, C SDK, and associated tools.
Every program that accesses OpenLDAP directories will need this package: It
contains libldap and liblber.


%package servers
Summary: OpenLDAP server software
Group: Applications/Databases

%description servers
The OpenLDAP Project is a collaborative effort to provide a robust,
commercial-grade, fully featured, open source LDAP software suite. The project
is managed by a worldwide community of volunteers that use the Internet to
communicate, plan, and develop OpenLDAP Software and its related
documentation. OpenLDAP Software provides a complete LDAP implementation
including server, clients, C SDK, and associated tools.
The 'servers package' contains the OpenLDAP server daemon (slapd), the
replication daemon (slurpd) along with tools a directory administrator will
need on the server machine.


%prep
%setup -q


%build
%configure \
	--enable-dynamic \
	--enable-syslog \
	--enable-proctitle \
	--enable-ipv6 \
	--enable-local \
	--enable-slapd \
	--enable-cleartext \
	--enable-crypt \
	--enable-bdb \
	--disable-ldbm \
	--enable-monitor \
	--enable-passwd \
	--enable-slurpd \
	--with-cyrus-sasl \
	--with-threads \
	--with-tls \
	--with-slp
%{__make} %{?_smp_mflags} depend CC='%{_target_platform}-gcc'
%{__make} %{?_smp_mflags} CC='%{_target_platform}-gcc'


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'

# Copy init files for slapd and slurpd
%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/initng'/{daemon,iconfig}
%{__cat} < '%{SOURCE1}' |\
	%{__sed} \
		-e 's,@slapd@,%{_libexecdir}/slapd,g' \
		-e 's,@localstatedir@,%{_localstatedir},g' \
	> '%{buildroot}/%{_sysconfdir}/initng/daemon/slapd.i'
%{__cat} < '%{SOURCE2}' |\
	%{__sed} \
		-e 's,@slurpd@,%{_libexecdir}/slurpd,g' \
		-e 's,@localstatedir@,%{_localstatedir},g' \
	> '%{buildroot}/%{_sysconfdir}/initng/daemon/slurpd.i'
%{__cat} < '%{SOURCE3}' > '%{buildroot}/%{_sysconfdir}/initng/iconfig/slapd'

# Create the PID dir and correct slapd.conf entries (it wont work otherwise).

%{__mkdir_p} '%{buildroot}/%{_localstatedir}/run/openldap'
%{__sed} -i 's,\(pidfile\s*\).*,\1%{_localstatedir}/run/openldap/slapd.pid,' \
	'%{buildroot}/%{_sysconfdir}/openldap'/slapd.conf*
%{__sed} -i 's,\(argsfile\s*\).*,\1%{_localstatedir}/run/openldap/slapd.args,' \
	'%{buildroot}/%{_sysconfdir}/openldap'/slapd.conf*


%post libs
/sbin/ldconfig

%postun libs
/sbin/ldconfig

%pre servers
{
	groupadd \
		-g '%{_ldap_gid}' \
		ldap
	useradd \
		-g '%{_ldap_gid}' \
	    -u '%{_slapd_uid}' \
		-c 'OpenLDAP daemon' \
		slapd
} > /dev/null 2>&1
exit 0

%preun servers
if [[ "${1}" -eq 0 ]]
then
	ngc -d daemon/slapd
    ngc -d daemon/slurpd
	ng-update del daemon/slapd default
    ng-update del daemon/slurpd default
fi > /dev/null 2>&1
exit 0

%postun servers
if [[ "${1}" -eq 0 ]]
then
    userdel slapd
    groupdel ldap
fi > /dev/null 2>&1
exit 0


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files libs
%defattr(-, root, root)
%{_includedir}/lber.h
%{_includedir}/lber_types.h
%{_includedir}/ldap.h
%{_includedir}/ldap_cdefs.h
%{_includedir}/ldap_schema.h
%{_includedir}/ldap_utf8.h
%{_includedir}/slapi-plugin.h
%{_includedir}/ldap_features.h
%{_libdir}/liblber*
%{_libdir}/libldap*.*
%{_mandir}/man3/ber_scanf.3*
%{_mandir}/man3/lber-decode.3*
%{_mandir}/man3/ber_get_next.3*
%{_mandir}/man3/ber_skip_tag.3*
%{_mandir}/man3/ber_peek_tag.3*
%{_mandir}/man3/ber_get_int.3*
%{_mandir}/man3/ber_get_stringa.3*
%{_mandir}/man3/ber_get_stringb.3*
%{_mandir}/man3/ber_get_null.3*
%{_mandir}/man3/ber_get_enum.3*
%{_mandir}/man3/ber_get_boolean.3*
%{_mandir}/man3/ber_get_bitstring.3*
%{_mandir}/man3/ber_first_element.3*
%{_mandir}/man3/ber_next_element.3*
%{_mandir}/man3/ber_flush.3*
%{_mandir}/man3/lber-encode.3*
%{_mandir}/man3/ber_alloc_t.3*
%{_mandir}/man3/ber_printf.3*
%{_mandir}/man3/ber_put_int.3*
%{_mandir}/man3/ber_put_ostring.3*
%{_mandir}/man3/ber_put_string.3*
%{_mandir}/man3/ber_put_null.3*
%{_mandir}/man3/ber_put_enum.3*
%{_mandir}/man3/ber_start_set.3*
%{_mandir}/man3/ber_put_seq.3*
%{_mandir}/man3/ber_put_set.3*
%{_mandir}/man3/ber_bvdup.3*
%{_mandir}/man3/lber-memory.3*
%{_mandir}/man3/lber-types.3*
%{_mandir}/man3/ber_bvarray_add.3*
%{_mandir}/man3/ber_bvarray_free.3*
%{_mandir}/man3/ber_bvecadd.3*
%{_mandir}/man3/ber_bvecfree.3*
%{_mandir}/man3/ber_bvfree.3*
%{_mandir}/man3/ber_bvstr.3*
%{_mandir}/man3/ber_bvstrdup.3*
%{_mandir}/man3/ber_dupbv.3*
%{_mandir}/man3/ber_free.3*
%{_mandir}/man3/ber_str2bv.3*
%{_mandir}/man3/ldap_add_s.3*
%{_mandir}/man3/ldap.3*
%{_mandir}/man3/ldap_abandon.3*
%{_mandir}/man3/ldap_abandon_ext.3*
%{_mandir}/man3/ldap_add.3*
%{_mandir}/man3/ldap_add_ext.3*
%{_mandir}/man3/ldap_add_ext_s.3*
%{_mandir}/man3/ld_errno.3*
%{_mandir}/man3/ldap_bind.3*
%{_mandir}/man3/ldap_bind_s.3*
%{_mandir}/man3/ldap_simple_bind.3*
%{_mandir}/man3/ldap_simple_bind_s.3*
%{_mandir}/man3/ldap_sasl_bind.3*
%{_mandir}/man3/ldap_sasl_bind_s.3*
%{_mandir}/man3/ldap_unbind.3*
%{_mandir}/man3/ldap_unbind_ext.3*
%{_mandir}/man3/ldap_unbind_s.3*
%{_mandir}/man3/ldap_unbind_ext_s.3*
%{_mandir}/man3/ldap_compare.3*
%{_mandir}/man3/ldap_compare_s.3*
%{_mandir}/man3/ldap_compare_ext.3*
%{_mandir}/man3/ldap_compare_ext_s.3*
%{_mandir}/man3/ldap_delete.3*
%{_mandir}/man3/ldap_delete_s.3*
%{_mandir}/man3/ldap_delete_ext.3*
%{_mandir}/man3/ldap_delete_ext_s.3*
%{_mandir}/man3/ldap_error.3*
%{_mandir}/man3/ldap_perror.3*
%{_mandir}/man3/ldap_result2error.3*
%{_mandir}/man3/ldap_errlist.3*
%{_mandir}/man3/ldap_err2string.3*
%{_mandir}/man3/ldap_init.3*
%{_mandir}/man3/ldap_first_attribute.3*
%{_mandir}/man3/ldap_next_attribute.3*
%{_mandir}/man3/ldap_first_entry.3*
%{_mandir}/man3/ldap_next_entry.3*
%{_mandir}/man3/ldap_count_entries.3*
%{_mandir}/man3/ldap_first_message.3*
%{_mandir}/man3/ldap_next_message.3*
%{_mandir}/man3/ldap_count_messages.3*
%{_mandir}/man3/ldap_first_reference.3*
%{_mandir}/man3/ldap_next_reference.3*
%{_mandir}/man3/ldap_count_references.3*
%{_mandir}/man3/ldap_get_dn.3*
%{_mandir}/man3/ldap_explode_dn.3*
%{_mandir}/man3/ldap_explode_rdn.3*
%{_mandir}/man3/ldap_dn2ufn.3*
%{_mandir}/man3/ldap_str2dn.3*
%{_mandir}/man3/ldap_dn2str.3*
%{_mandir}/man3/ldap_dn2dcedn.3*
%{_mandir}/man3/ldap_dcedn2dn.3*
%{_mandir}/man3/ldap_dn2ad_canonical.3*
%{_mandir}/man3/ldap_get_values.3*
%{_mandir}/man3/ldap_get_values_len.3*
%{_mandir}/man3/ldap_value_free.3*
%{_mandir}/man3/ldap_value_free_len.3*
%{_mandir}/man3/ldap_count_values.3*
%{_mandir}/man3/ldap_count_values_len.3*
%{_mandir}/man3/ldap_modify.3*
%{_mandir}/man3/ldap_modify_s.3*
%{_mandir}/man3/ldap_modify_ext.3*
%{_mandir}/man3/ldap_modify_ext_s.3*
%{_mandir}/man3/ldap_mods_free.3*
%{_mandir}/man3/ldap_modrdn.3*
%{_mandir}/man3/ldap_modrdn_s.3*
%{_mandir}/man3/ldap_modrdn2.3*
%{_mandir}/man3/ldap_modrdn2_s.3*
%{_mandir}/man3/ldap_open.3*
%{_mandir}/man3/ldap_msgid.3*
%{_mandir}/man3/ldap_parse_reference.3*
%{_mandir}/man3/ldap_parse_result.3*
%{_mandir}/man3/ldap_parse_sasl_bind_result.3*
%{_mandir}/man3/ldap_parse_extended_result.3*
%{_mandir}/man3/ldap_result.3*
%{_mandir}/man3/ldap_msgfree.3*
%{_mandir}/man3/ldap_msgtype.3*
%{_mandir}/man3/ldap_schema.3*
%{_mandir}/man3/ldap_str2syntax.3*
%{_mandir}/man3/ldap_syntax2str.3*
%{_mandir}/man3/ldap_syntax2name.3*
%{_mandir}/man3/ldap_syntax_free.3*
%{_mandir}/man3/ldap_str2matchingrule.3*
%{_mandir}/man3/ldap_matchingrule2str.3*
%{_mandir}/man3/ldap_matchingrule2name.3*
%{_mandir}/man3/ldap_matchingrule_free.3*
%{_mandir}/man3/ldap_str2attributetype.3*
%{_mandir}/man3/ldap_attributetype2str.3*
%{_mandir}/man3/ldap_attributetype2name.3*
%{_mandir}/man3/ldap_attributetype_free.3*
%{_mandir}/man3/ldap_str2objectclass.3*
%{_mandir}/man3/ldap_objectclass2str.3*
%{_mandir}/man3/ldap_objectclass2name.3*
%{_mandir}/man3/ldap_objectclass_free.3*
%{_mandir}/man3/ldap_scherr2str.3*
%{_mandir}/man3/ldap_search.3*
%{_mandir}/man3/ldap_search_s.3*
%{_mandir}/man3/ldap_search_st.3*
%{_mandir}/man3/ldap_search_ext.3*
%{_mandir}/man3/ldap_search_ext_s.3*
%{_mandir}/man3/ldap_sort.3*
%{_mandir}/man3/ldap_sort_entries.3*
%{_mandir}/man3/ldap_sort_values.3*
%{_mandir}/man3/ldap_sort_strcasecmp.3*
%{_mandir}/man3/ldap_url.3*
%{_mandir}/man3/ldap_is_ldap_url.3*
%{_mandir}/man3/ldap_url_parse.3*
%{_mandir}/man3/ldap_free_urldesc.3*
%{_mandir}/man5/ldap.conf.5*
%dir %{_sysconfdir}/openldap
%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/openldap/ldap.conf
%attr(0644, root, root) %{_sysconfdir}/openldap/ldap.conf.default

%files servers
%defattr(-, root, root)
%{_libexecdir}/slapd
%{_libexecdir}/slurpd
%{_sbindir}/slapadd
%{_sbindir}/slapcat
%{_sbindir}/slapdn
%{_sbindir}/slapindex
%{_sbindir}/slappasswd
%{_sbindir}/slaptest
%{_sbindir}/slapauth
%{_sbindir}/slapacl
%{_mandir}/man5/slapd-hdb.5*
%{_mandir}/man5/ldif.5*
%{_mandir}/man5/slapd-bdb.5*
%{_mandir}/man5/slapd-dnssrv.5*
%{_mandir}/man5/slapd-ldap.5*
%{_mandir}/man5/slapd-ldbm.5*
%{_mandir}/man5/slapd-ldif.5*
%{_mandir}/man5/slapd-meta.5*
%{_mandir}/man5/slapd-monitor.5*
%{_mandir}/man5/slapd-null.5*
%{_mandir}/man5/slapd-passwd.5*
%{_mandir}/man5/slapd-perl.5*
%{_mandir}/man5/slapd-relay.5*
%{_mandir}/man5/slapd-shell.5*
%{_mandir}/man5/slapd-sql.5*
%{_mandir}/man5/slapd-tcl.5*
%{_mandir}/man5/slapd.access.5*
%{_mandir}/man5/slapd.conf.5*
%{_mandir}/man5/slapd.plugin.5*
%{_mandir}/man5/slapd.replog.5*
%{_mandir}/man5/slapo-accesslog.5*
%{_mandir}/man5/slapo-auditlog.5*
%{_mandir}/man5/slapo-chain.5*
%{_mandir}/man5/slapo-dynlist.5*
%{_mandir}/man5/slapo-lastmod.5*
%{_mandir}/man5/slapo-pcache.5*
%{_mandir}/man5/slapo-ppolicy.5*
%{_mandir}/man5/slapo-refint.5*
%{_mandir}/man5/slapo-retcode.5*
%{_mandir}/man5/slapo-rwm.5*
%{_mandir}/man5/slapo-syncprov.5*
%{_mandir}/man5/slapo-translucent.5*
%{_mandir}/man5/slapo-unique.5*
%{_mandir}/man5/slapo-valsort.5*
%{_mandir}/man8/slapacl.8*
%{_mandir}/man8/slapadd.8*
%{_mandir}/man8/slapauth.8*
%{_mandir}/man8/slapcat.8*
%{_mandir}/man8/slapd.8*
%{_mandir}/man8/slapdn.8*
%{_mandir}/man8/slapindex.8*
%{_mandir}/man8/slappasswd.8*
%{_mandir}/man8/slaptest.8*
%{_mandir}/man8/slurpd.8*
%{_sysconfdir}/initng/daemon/*.i
%config(noreplace) %{_sysconfdir}/initng/iconfig/slapd
%attr(0755, root, root) %dir %{_sysconfdir}/openldap
%attr(0755, root, ldap) %dir %{_sysconfdir}/openldap/schema
%attr(0644, root, ldap) %{_sysconfdir}/openldap/schema/*
%attr(640, root, ldap) %{_sysconfdir}/openldap/slapd.conf.default
%attr(640, root, ldap) %config(noreplace) %{_sysconfdir}/openldap/slapd.conf
%attr(640, root, ldap) %{_sysconfdir}/openldap/DB_CONFIG.example
%attr(770, root, ldap) %dir %{_localstatedir}/openldap-data
%attr(770, root, ldap) %dir %{_localstatedir}/openldap-slurp
%attr(640, root, ldap) %{_localstatedir}/openldap-data/DB_CONFIG.example
%attr(770, root, ldap) %dir %{_localstatedir}/run/openldap

%files
%defattr(-, root, root)
%doc ANNOUNCEMENT CHANGES COPYRIGHT LICENSE README
%{_bindir}/ldapadd
%{_bindir}/ldapsearch
%{_bindir}/ldapmodify
%{_bindir}/ldapdelete
%{_bindir}/ldapmodrdn
%{_bindir}/ldappasswd
%{_bindir}/ldapwhoami
%{_bindir}/ldapcompare
%{_mandir}/man1/ldapadd.1*
%{_mandir}/man1/ldapcompare.1*
%{_mandir}/man1/ldapdelete.1*
%{_mandir}/man1/ldapmodify.1*
%{_mandir}/man1/ldapmodrdn.1*
%{_mandir}/man1/ldappasswd.1*
%{_mandir}/man1/ldapsearch.1*
%{_mandir}/man1/ldapwhoami.1*
