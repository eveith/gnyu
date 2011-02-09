Name: fslayout
Version: 1.3
Release: 7.0
Summary: The empty directory tree
Group: System Environment/Base
License: GPL-3
Source0: languages.txt
Source1: dirlist.txt
Source2: http://sethwklein.net/iana-etc-2.30.tar.bz2
Source3: profile.sh
Source4: hosts
Source5: passwd
Source6: group
BuildArch: noarch
Obsoletes: fhs < %{version}-%{release}
Conflicts: fhs < %{version}-%{release}
Provides: fhs = %{version}-%{release}
BuildRequires: grep, sed, make, gawk

%description
This creates the empty directory tree for the whole distribuion, according to
the File Hierarchy Standard. It should never be removed, updated or otherwise
changed.


%package -n etc
Version: 2.2
Release: 3.0
Summary: Basic system configuration files
Group: System Environment/Base
License: OSL-3.0, GPL-3
BuildArch: noarch

%description -n etc
The etc package populates your /etc directory with some very basic files that
are needed by the system to funtion correctly. Although they are configuration
files, they aren't changed, though.


%prep
%setup -qcTa2


%build
pushd iana-etc*
%{__make}
popd


%install
echo '' > dirlist
while read LANG
do
	%{__mkdir_p} \
		"${RPM_BUILD_ROOT}/usr/share/locale/${LANG}"/LC_{MESSAGES,TIME}
	%{__mkdir_p} \
		"${RPM_BUILD_ROOT}"/usr/{share/,}man/"${LANG}"/man{1,2,3,4,5,6,7,8,9}

	for i in /usr/{share/,}man/"${LANG}"{,/man{1,2,3,4,5,6,7,8,9}} \
		"/usr/share/locale/${LANG}"{,/LC_{MESSAGES,TIME}}
	do
		echo '%dir %attr(0755, root, root)' "$i" >> dirlist
	done
done < '%{SOURCE0}'

while read dir
do
	echo "$dir" >> dirlist
	echo $dir | grep '%dir' > /dev/null 2>&1 || continue
	dir=$(echo $dir | \
		sed -e 's,\(%[a-z]\+\(([^)]*)\)\?\)\+,,g' -e 's,^[ ]*,,')
	%{__mkdir_p} "%{buildroot}${dir}"
done < '%{SOURCE1}'

# IANA /etc files
pushd iana-etc*
%{__make_install} DESTDIR="${RPM_BUILD_ROOT}"
popd

%{__install} -m0644 '%{SOURCE1}' '%{buildroot}/etc/profile'
%{__cp} '%{SOURCE4}' '%{buildroot}/etc/hosts'
echo gnyu.localdomain > '%{buildroot}/etc/HOSTNAME'
echo 'GNyU-Linux %{version}' > '%{buildroot}/etc/GNyU-version'
%{__cp} '%{SOURCE5}' '%{buildroot}/etc/passwd'
%{__cp} '%{SOURCE6}' '%{buildroot}/etc/group'
%{__touch} \
	'%{buildroot}/etc/passwd-' \
	'%{buildroot}/etc/group-' \
	'%{buildroot}/etc/shadow-' \
	'%{buildroot}/etc/gshadow-'

# Create /etc/shadow and /etc/gshadow from sources
old_ifs=$IFS
IFS=:
while read name rest
do
	echo "${name}:!:::::::" >> '%{buildroot}/etc/shadow'
done < '%{SOURCE5}'
while read name passwd gid member_list
do
	echo "${name}:${passwd}:root:${member_list}" >> '%{buildroot}/etc/gshadow'
done < '%{SOURCE6}'
IFS=$old_ifs


%clean
%{__rm} dirlist


%files -f dirlist
%defattr(-, root, root)
%attr(0755, root, root) %dir /


%files -n etc
%defattr(-, root, root)
%config(noreplace) %attr(0644, root, root) /etc/HOSTNAME
%config(noreplace) %attr(0644, root, root) /etc/hosts
%config %attr(0644, root, root) /etc/protocols
%config %attr(0644, root, root) /etc/services
%attr(0644, root, root) /etc/GNyU-version
%attr(0755, root, root) /etc/profile
%config(noreplace) %attr(0644, root, root) /etc/group
%ghost %config %attr(0644, root, root) /etc/group-
%config(noreplace) %attr(0644, root, root) /etc/passwd
%ghost %config %attr(0644, root, root) /etc/passwd-
%config(noreplace) %attr(0400, root, root) /etc/shadow
%ghost %config %attr(0400, root, root) /etc/shadow-
%config(noreplace) %attr(0400, root, root) /etc/gshadow
%ghost %config %attr(0400, root, root) /etc/gshadow-
