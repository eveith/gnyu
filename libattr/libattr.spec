Name: attr
Version: 2.4.43
Release: 3.0
Summary: Extended file system attributes
URL: http://oss.sgi.com/projects/xfs/
Group: System Environment/Libraries
License: LGPL-2.1
Source: ftp://oss.sgi.com/projects/xfs/cmd_tars/attr_%{version}-1.tar.gz
BuildRequires: grep, sed, make >= 3.79.1, libtool, gcc
BuildRequires: gettext-tools
BuildRequires: eglibc-devel, kernel-headers

%description
Extended attributes implement the ability for a user to attach name:value
pairs to objects within the XFS filesystem.
They  could  be used to store meta-information about the file.  For
example "character-set=kanji" could tell a document browser to use the Kanji
character set when displaying that document and "thumbnail=..." could provide a
reduced resolution overview of a high resolution graphic image.


%package -n libattr1
Summary: Library for extended file system attributes access
Group: System Environment/Libraries

%description -n libattr1
Extended attributes implement the ability for a user to attach name:value
pairs to objects within the XFS filesystem.
They  could  be used to store meta-information about the file.  For
example "character-set=kanji" could tell a document browser to use the Kanji
character set when displaying that document and "thumbnail=..." could provide a
reduced resolution overview of a high resolution graphic image.


%package devel
Summary: Development headers for libattr
Group: Development/Libraries

%description devel
Extended attributes implement the ability for a user to attach name:value
pairs to objects within the XFS filesystem.
For developing or compiling programs that make use of this feature, you will
need to install this package.


%prep
%setup -q -n 'attr-%{version}'


%build
%configure \
    --libdir='/%{_lib}' \
    --bindir='/bin'

# No good CC handling here, because otherwise we confuse libtool...
%{__make} %{?_smp_mflags} \
    CC="%{_target_platform}-gcc"


%install
%{__make} \
    DIST_ROOT="$RPM_BUILD_ROOT" \
    install \
    install-lib \
    install-dev
%find_lang attr
%{__rm_rf} '%{buildroot}%{_datadir}/doc'


%post -n libattr1 -p %{__ldconfig}
%postun -n libattr1 -p %{__ldconfig}


%files -f attr.lang
%defattr(-, root, root)
%doc README VERSION doc 
/bin/attr
/bin/getfattr
/bin/setfattr
%doc %{_mandir}/man1/attr.1*
%doc %{_mandir}/man1/getfattr.1*
%doc %{_mandir}/man1/setfattr.1*
%doc %{_mandir}/man5/attr.5*


%files -n libattr1
%defattr(-, root, root)
%doc README VERSION doc/COPYING
/%{_lib}/libattr.so.1*


%files devel
%doc README VERSION doc
/%{_lib}/libattr.so
/%{_lib}/libattr.la
/%{_lib}/libattr.a
%dir %{_includedir}/attr
%{_includedir}/attr/*.h
%{_libexecdir}/libattr.so
%{_libexecdir}/libattr.la
%{_libexecdir}/libattr.a
%doc %{_mandir}/man2/fgetxattr.2*
%doc %{_mandir}/man2/flistxattr.2*
%doc %{_mandir}/man2/fremovexattr.2*
%doc %{_mandir}/man2/fsetxattr.2*
%doc %{_mandir}/man2/getxattr.2*
%doc %{_mandir}/man2/lgetxattr.2*
%doc %{_mandir}/man2/listxattr.2*
%doc %{_mandir}/man2/llistxattr.2*
%doc %{_mandir}/man2/lremovexattr.2*
%doc %{_mandir}/man2/lsetxattr.2*
%doc %{_mandir}/man2/removexattr.2*
%doc %{_mandir}/man2/setxattr.2*
%doc %{_mandir}/man3/attr_get.3*
%doc %{_mandir}/man3/attr_getf.3*
%doc %{_mandir}/man3/attr_list.3*
%doc %{_mandir}/man3/attr_listf.3*
%doc %{_mandir}/man3/attr_multi.3*
%doc %{_mandir}/man3/attr_multif.3*
%doc %{_mandir}/man3/attr_remove.3*
%doc %{_mandir}/man3/attr_removef.3*
%doc %{_mandir}/man3/attr_set.3*
%doc %{_mandir}/man3/attr_setf.3*
