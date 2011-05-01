Name: acl
Version: 2.2.47
Release: 3.0
Summary: Access control lists userspace programs
URL: http://oss.sgi.com/projects/xfs
Group: System Environment/Base
License: LGPL-2.1
Source: ftp://oss.sgi.com/projects/xfs/cmd_tars/acl_%{version}-1.tar.gz
BuildRequires: make, libtool, gcc
BuildRequires: gettext-tools
BuildRequires: eglibc-devel, kernel-headers
BuildRequires: attr-devel

%description
A set of tools to read, create and modify ACL file attributes.


%package -n libacl1
Summary: Access control lists userspace library
Group: System Environment/Libraries

%description -n libacl1
A library to read, create and modify ACL file attributes.


%package devel
Summary: Development headers for libacl
Group: Development/Libraries
Requires: libacl1 = %{name}-%{version}

%description devel
ACL/libacl is a set of tools and a library for reading, creating and modifing
Access Control List file attributes. 
If you want to develop or compile applications that make direct use of ACLs,
you will need to have this package installed. It provides the neccessary
header files as well as the libacl API documentation in manpages format.



%prep
%setup -q


%build
%configure \
    --bindir=/bin \
    --libdir='/%{_lib}'

# No CC substitution, we'd confuse libtool.
%{__make} %{?_smp_mflags} CC='%{_target_platform}-gcc'


%install
%{__make} \
    install \
    install-lib \
    install-dev \
    DIST_ROOT='%{buildroot}'
%find_lang acl
%{__rm_rf} '%{buildroot}%{_datadir}/doc'


%post -n libacl1 -p %{__ldconfig}
%postun -n libacl1 -p %{__ldconfig}


%files -f acl.lang
%defattr(-, root, root)
%doc doc/ README VERSION
/bin/chacl
/bin/getfacl
/bin/setfacl
%doc %{_mandir}/man1/chacl.1*
%doc %{_mandir}/man1/getfacl.1*
%doc %{_mandir}/man1/setfacl.1*
%doc %{_mandir}/man5/acl.5*


%files -n libacl1
%defattr(-, root, root)
%doc doc/COPYING README VERSION
/%{_lib}/libacl.so.1*


%files devel
%defattr(-, root, root)
%doc doc/COPYING README VERSION
/%{_lib}/libacl.so
/%{_lib}/libacl.la
/%{_lib}/libacl.a
%dir %{_includedir}/acl
%{_includedir}/acl/*.h
%{_includedir}/sys/acl.h
%{_libexecdir}/libacl.so
%{_libexecdir}/libacl.la
%{_libexecdir}/libacl.a
%doc %{_mandir}/man3/acl_add_perm.3*
%doc %{_mandir}/man3/acl_calc_mask.3*
%doc %{_mandir}/man3/acl_check.3*
%doc %{_mandir}/man3/acl_clear_perms.3*
%doc %{_mandir}/man3/acl_cmp.3*
%doc %{_mandir}/man3/acl_copy_entry.3*
%doc %{_mandir}/man3/acl_copy_ext.3*
%doc %{_mandir}/man3/acl_copy_int.3*
%doc %{_mandir}/man3/acl_create_entry.3*
%doc %{_mandir}/man3/acl_delete_def_file.3*
%doc %{_mandir}/man3/acl_delete_entry.3*
%doc %{_mandir}/man3/acl_delete_perm.3*
%doc %{_mandir}/man3/acl_dup.3*
%doc %{_mandir}/man3/acl_entries.3*
%doc %{_mandir}/man3/acl_equiv_mode.3*
%doc %{_mandir}/man3/acl_error.3*
%doc %{_mandir}/man3/acl_extended_fd.3*
%doc %{_mandir}/man3/acl_extended_file.3*
%doc %{_mandir}/man3/acl_free.3*
%doc %{_mandir}/man3/acl_from_mode.3*
%doc %{_mandir}/man3/acl_from_text.3*
%doc %{_mandir}/man3/acl_get_entry.3*
%doc %{_mandir}/man3/acl_get_fd.3*
%doc %{_mandir}/man3/acl_get_file.3*
%doc %{_mandir}/man3/acl_get_perm.3*
%doc %{_mandir}/man3/acl_get_permset.3*
%doc %{_mandir}/man3/acl_get_qualifier.3*
%doc %{_mandir}/man3/acl_get_tag_type.3*
%doc %{_mandir}/man3/acl_init.3*
%doc %{_mandir}/man3/acl_set_fd.3*
%doc %{_mandir}/man3/acl_set_file.3*
%doc %{_mandir}/man3/acl_set_permset.3*
%doc %{_mandir}/man3/acl_set_qualifier.3*
%doc %{_mandir}/man3/acl_set_tag_type.3*
%doc %{_mandir}/man3/acl_size.3*
%doc %{_mandir}/man3/acl_to_any_text.3*
%doc %{_mandir}/man3/acl_to_text.3*
%doc %{_mandir}/man3/acl_valid.3*
