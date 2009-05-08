Name: libacl
Version: 2.2.45
Release: 1ev
Summary: Access control lists userspace library
URL: http://oss.sgi.com/projects/xfs/
Group: System Environment/Libraries
License: LGPL
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: ftp://oss.sgi.com/projects/xfs/cmd_tars/acl_%{version}-1.tar.gz
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: libattr, autoconf, make >= 3.79.1, gcc-core, libtool
Requires: libattr
Provides: libtool(%{_libdir}/libacl.la) libtool(%{_libexecdir}/libacl.la)

%description
A library and tools to read, create and modify ACL file attributes.


%prep
%setup -q -n acl-%{version}


%build
%configure
make CC="%{_target_platform}-gcc" %{_smp_mflags}


%install
[ "$RPM_BUILD_ROOT" != '/' ] && rm -rf "${RPM_BUILD_ROOT}"
make DIST_ROOT="$RPM_BUILD_ROOT" install install-lib install-dev
%find_lang acl

%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != '/' ] && rm -rf "${RPM_BUILD_ROOT}"


%files -f acl.lang
%defattr(-, root, root)
%doc doc/ README VERSION
%doc %{_datadir}/doc/acl
%{_bindir}/chacl
%{_bindir}/getfacl
%{_bindir}/setfacl
%{_includedir}/acl/
%{_includedir}/sys/acl.h
%{_libdir}/libacl.*
%{_libexecdir}/libacl.*
%{_mandir}/man1/chacl.1.gz
%{_mandir}/man1/getfacl.1.gz
%{_mandir}/man1/setfacl.1.gz
%{_mandir}/man3/acl_add_perm.3.gz
%{_mandir}/man3/acl_calc_mask.3.gz
%{_mandir}/man3/acl_check.3.gz
%{_mandir}/man3/acl_clear_perms.3.gz
%{_mandir}/man3/acl_cmp.3.gz
%{_mandir}/man3/acl_copy_entry.3.gz
%{_mandir}/man3/acl_copy_ext.3.gz
%{_mandir}/man3/acl_copy_int.3.gz
%{_mandir}/man3/acl_create_entry.3.gz
%{_mandir}/man3/acl_delete_def_file.3.gz
%{_mandir}/man3/acl_delete_entry.3.gz
%{_mandir}/man3/acl_delete_perm.3.gz
%{_mandir}/man3/acl_dup.3.gz
%{_mandir}/man3/acl_entries.3.gz
%{_mandir}/man3/acl_equiv_mode.3.gz
%{_mandir}/man3/acl_error.3.gz
%{_mandir}/man3/acl_extended_fd.3.gz
%{_mandir}/man3/acl_extended_file.3.gz
%{_mandir}/man3/acl_free.3.gz
%{_mandir}/man3/acl_from_mode.3.gz
%{_mandir}/man3/acl_from_text.3.gz
%{_mandir}/man3/acl_get_entry.3.gz
%{_mandir}/man3/acl_get_fd.3.gz
%{_mandir}/man3/acl_get_file.3.gz
%{_mandir}/man3/acl_get_perm.3.gz
%{_mandir}/man3/acl_get_permset.3.gz
%{_mandir}/man3/acl_get_qualifier.3.gz
%{_mandir}/man3/acl_get_tag_type.3.gz
%{_mandir}/man3/acl_init.3.gz
%{_mandir}/man3/acl_set_fd.3.gz
%{_mandir}/man3/acl_set_file.3.gz
%{_mandir}/man3/acl_set_permset.3.gz
%{_mandir}/man3/acl_set_qualifier.3.gz
%{_mandir}/man3/acl_set_tag_type.3.gz
%{_mandir}/man3/acl_size.3.gz
%{_mandir}/man3/acl_to_any_text.3.gz
%{_mandir}/man3/acl_to_text.3.gz
%{_mandir}/man3/acl_valid.3.gz
%{_mandir}/man5/acl.5.gz
