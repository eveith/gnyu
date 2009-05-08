Name: libacl
Version: 2.2.47
Release: 2ev
Summary: Access control lists userspace library
URL: http://oss.sgi.com/projects/xfs/
Group: System Environment/Libraries
License: LGPL-2.1
Vendor: GNyU-Linux
Source: ftp://oss.sgi.com/projects/xfs/cmd_tars/acl_%{version}-1.tar.gz
BuildRequires: make, libtool, gcc, gettext, libattr

%description
A library and tools to read, create and modify ACL file attributes.


%prep
	%setup -q -n 'acl-%{version}'


%build
	%configure \
		--bindir=/bin \
		--libdir='/%{_lib}'

	# No CC substitution, we'd confuse libtool.
	%{__make} %{?_smp_mflags} CC='%{_target_platform}-gcc'


%install
	%{__make} \
		install \
		install \
		install-lib \
		install-dev \
		DIST_ROOT='%{buildroot}'
	%find_lang acl
	%{__rm_rf} '%{buildroot}/%{_datadir}/doc'


%post
	%{__ldconfig}


%postun
	%{__ldconfig}


%files -f acl.lang
	%defattr(-, root, root)
	%doc doc/ README VERSION
	/bin/chacl
	/bin/getfacl
	/bin/setfacl
	%{_includedir}/acl/
	%{_includedir}/sys/acl.h
	/%{_lib}/libacl.*
	%{_libexecdir}/libacl.*
	%doc %{_mandir}/man1/chacl.1.gz
	%doc %{_mandir}/man1/getfacl.1.gz
	%doc %{_mandir}/man1/setfacl.1.gz
	%doc %{_mandir}/man3/acl_add_perm.3.gz
	%doc %{_mandir}/man3/acl_calc_mask.3.gz
	%doc %{_mandir}/man3/acl_check.3.gz
	%doc %{_mandir}/man3/acl_clear_perms.3.gz
	%doc %{_mandir}/man3/acl_cmp.3.gz
	%doc %{_mandir}/man3/acl_copy_entry.3.gz
	%doc %{_mandir}/man3/acl_copy_ext.3.gz
	%doc %{_mandir}/man3/acl_copy_int.3.gz
	%doc %{_mandir}/man3/acl_create_entry.3.gz
	%doc %{_mandir}/man3/acl_delete_def_file.3.gz
	%doc %{_mandir}/man3/acl_delete_entry.3.gz
	%doc %{_mandir}/man3/acl_delete_perm.3.gz
	%doc %{_mandir}/man3/acl_dup.3.gz
	%doc %{_mandir}/man3/acl_entries.3.gz
	%doc %{_mandir}/man3/acl_equiv_mode.3.gz
	%doc %{_mandir}/man3/acl_error.3.gz
	%doc %{_mandir}/man3/acl_extended_fd.3.gz
	%doc %{_mandir}/man3/acl_extended_file.3.gz
	%doc %{_mandir}/man3/acl_free.3.gz
	%doc %{_mandir}/man3/acl_from_mode.3.gz
	%doc %{_mandir}/man3/acl_from_text.3.gz
	%doc %{_mandir}/man3/acl_get_entry.3.gz
	%doc %{_mandir}/man3/acl_get_fd.3.gz
	%doc %{_mandir}/man3/acl_get_file.3.gz
	%doc %{_mandir}/man3/acl_get_perm.3.gz
	%doc %{_mandir}/man3/acl_get_permset.3.gz
	%doc %{_mandir}/man3/acl_get_qualifier.3.gz
	%doc %{_mandir}/man3/acl_get_tag_type.3.gz
	%doc %{_mandir}/man3/acl_init.3.gz
	%doc %{_mandir}/man3/acl_set_fd.3.gz
	%doc %{_mandir}/man3/acl_set_file.3.gz
	%doc %{_mandir}/man3/acl_set_permset.3.gz
	%doc %{_mandir}/man3/acl_set_qualifier.3.gz
	%doc %{_mandir}/man3/acl_set_tag_type.3.gz
	%doc %{_mandir}/man3/acl_size.3.gz
	%doc %{_mandir}/man3/acl_to_any_text.3.gz
	%doc %{_mandir}/man3/acl_to_text.3.gz
	%doc %{_mandir}/man3/acl_valid.3.gz
	%doc %{_mandir}/man5/acl.5.gz
