Name: fslayout
Version: 1.2
Release: 6.0ev
Summary: The empty directory tree
Group: System Environment/Base
License: GPL-3
Vendor: GNyU-Linux
Source0: %{name}-languages.txt
Source3: %{name}-dirlist.txt
BuildArch: noarch
Obsoletes: fhs < %{version}-%{release}
Conflicts: fhs < %{version}-%{release}
Provides: fhs = %{version}-%{release}

%description
This creates the empty directory tree for the whole distribuion, according to
the File Hierarchy Standard. It should never be removed, updated or otherwise
changed.


%build
:


%install
while read LANG
do
	%{__mkdir_p} \
		"${RPM_BUILD_ROOT}/usr/share/locale/${LANG}"/LC_{MESSAGES,TIME}
	%{__mkdir_p} \
		"${RPM_BUILD_ROOT}"/usr/{share/,}man/"${LANG}"/man{1,2,3,4,5,6,7,8,9}
done < '%{SOURCE0}'

while read dir
do
	echo $dir | grep '%dir' > /dev/null 2>&1 || continue
	dir=$(echo $dir | \
		sed -e 's,\(%[a-z]\+\(([^)]*)\)\?\)\+,,g' -e 's,^[ ]*,,')
	%{__mkdir_p} "%{buildroot}${dir}"
done < '%{SOURCE3}'


%files -f %{SOURCE3}
%defattr(-, root, root)
%attr(0755, root, root) %dir /
