Name: libattr
Version: 2.4.43
Release: 2ev
Summary: Extended file system attributes userspace library
URL: http://oss.sgi.com/projects/xfs/
Group: System Environment/Libraries
License: LGPL
Vendor: GNyU-Linux
Source: ftp://oss.sgi.com/projects/xfs/cmd_tars/attr_%{version}-1.tar.gz
BuildRequires: make >= 3.79.1, gcc, libtool

%description
Extended attributes implement the ability for a user to attach name:value
pairs to objects within the XFS filesystem.
They  could  be used to store meta-information about the file.  For
example "character-set=kanji" could tell a document browser to use the Kanji
character set when displaying that document and "thumbnail=..." could provide a
reduced resolution overview of a high resolution graphic image.


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
	%{__rm_rf} '%{buildroot}/%{_datadir}/doc'


%post
	%{__ldconfig}


%postun
	%{__ldconfig}


%files -f attr.lang
	%defattr(-, root, root)
	%doc README VERSION doc 
	/bin/attr
	/bin/getfattr
	/bin/setfattr
	%{_includedir}/attr/
	/%{_lib}/libattr.*
	%{_libexecdir}/libattr.*
	%doc %{_mandir}/man1/attr.1.gz
	%doc %{_mandir}/man1/getfattr.1.gz
	%doc %{_mandir}/man1/setfattr.1.gz
	%doc %{_mandir}/man2/fgetxattr.2.gz
	%doc %{_mandir}/man2/flistxattr.2.gz
	%doc %{_mandir}/man2/fremovexattr.2.gz
	%doc %{_mandir}/man2/fsetxattr.2.gz
	%doc %{_mandir}/man2/getxattr.2.gz
	%doc %{_mandir}/man2/lgetxattr.2.gz
	%doc %{_mandir}/man2/listxattr.2.gz
	%doc %{_mandir}/man2/llistxattr.2.gz
	%doc %{_mandir}/man2/lremovexattr.2.gz
	%doc %{_mandir}/man2/lsetxattr.2.gz
	%doc %{_mandir}/man2/removexattr.2.gz
	%doc %{_mandir}/man2/setxattr.2.gz
	%doc %{_mandir}/man3/attr_get.3.gz
	%doc %{_mandir}/man3/attr_getf.3.gz
	%doc %{_mandir}/man3/attr_list.3.gz
	%doc %{_mandir}/man3/attr_listf.3.gz
	%doc %{_mandir}/man3/attr_multi.3.gz
	%doc %{_mandir}/man3/attr_multif.3.gz
	%doc %{_mandir}/man3/attr_remove.3.gz
	%doc %{_mandir}/man3/attr_removef.3.gz
	%doc %{_mandir}/man3/attr_set.3.gz
	%doc %{_mandir}/man3/attr_setf.3.gz
	%doc %{_mandir}/man5/attr.5.gz
