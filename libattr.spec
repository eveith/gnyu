Name: libattr
Version: 2.4.39
Release: 1ev
Summary: Extended file system attributes userspace library
URL: http://oss.sgi.com/projects/xfs/
Group: System Environment/Libraries
License: LGPL
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: ftp://oss.sgi.com/projects/xfs/cmd_tars/attr_%{version}-1.tar.gz
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: autoconf, make >= 3.79.1, gcc-core, libtool
Provides: libtool(%{_libdir}/libattr.la) libtool(%{_libexecdir}/libattr.la)

%description
Extended attributes implement the ability for a user to attach name:value
pairs to objects within the XFS filesystem.
They  could  be used to store meta-information about the file.  For
example "character-set=kanji" could tell a document browser to use the Kanji
character set when displaying that document and "thumbnail=..." could provide a
reduced resolution overview of a high resolution graphic image.


%prep
%setup -q -n attr-%{version}


%build
%configure
make CC="%{_target_platform}-gcc" %{_smp_mflags}

%install
[ "$RPM_BUILD_ROOT" != '/' ] && rm -rf "${RPM_BUILD_ROOT}"
make DIST_ROOT="$RPM_BUILD_ROOT" install install-lib install-dev
%find_lang attr


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != '/' ] && rm -rf "${RPM_BUILD_ROOT}"


%files -f attr.lang
%defattr(-, root, root)
%doc README VERSION doc 
%doc %{_datadir}/doc/attr
%{_bindir}/attr
%{_bindir}/getfattr
%{_bindir}/setfattr
%{_includedir}/attr/
%{_libdir}/libattr.*
%{_libexecdir}/libattr.*
%{_mandir}/man1/attr.1.gz
%{_mandir}/man1/getfattr.1.gz
%{_mandir}/man1/setfattr.1.gz
%{_mandir}/man2/fgetxattr.2.gz
%{_mandir}/man2/flistxattr.2.gz
%{_mandir}/man2/fremovexattr.2.gz
%{_mandir}/man2/fsetxattr.2.gz
%{_mandir}/man2/getxattr.2.gz
%{_mandir}/man2/lgetxattr.2.gz
%{_mandir}/man2/listxattr.2.gz
%{_mandir}/man2/llistxattr.2.gz
%{_mandir}/man2/lremovexattr.2.gz
%{_mandir}/man2/lsetxattr.2.gz
%{_mandir}/man2/removexattr.2.gz
%{_mandir}/man2/setxattr.2.gz
%{_mandir}/man3/attr_get.3.gz
%{_mandir}/man3/attr_getf.3.gz
%{_mandir}/man3/attr_list.3.gz
%{_mandir}/man3/attr_listf.3.gz
%{_mandir}/man3/attr_multi.3.gz
%{_mandir}/man3/attr_multif.3.gz
%{_mandir}/man3/attr_remove.3.gz
%{_mandir}/man3/attr_removef.3.gz
%{_mandir}/man3/attr_set.3.gz
%{_mandir}/man3/attr_setf.3.gz
%{_mandir}/man5/attr.5.gz
