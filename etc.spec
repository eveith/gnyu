Name: etc
Version: 2.1
Release: 2.1ev
Summary: Basic system configuration files
Group: System Environment/Base
License: OSL-3.0, GPL-3
Vendor: GNyU-Linux
Source0: http://sethwklein.net/iana-etc-2.30.tar.bz2
Source1: %{name}-profile.sh
Source2: %{name}-DIR_COLORS
Source3: %{name}-hosts
Source4: %{name}-passwd
Source5: %{name}-group
BuildRequires: gawk >= 3.1.0, make >= 3.79.1
BuildArch: noarch

%description
The etc package populates your /etc directory with some very basic files that
are needed by the system to funtion correctly. Although they are configuration
files, they aren't changed, though.


%prep
%setup -qca0


%build
pushd iana-etc*
%{__make}
popd


%install
# IANA /etc files
pushd iana-etc*
%{__make_install} DESTDIR="${RPM_BUILD_ROOT}"
popd

%{__mkdir_p} '%{buildroot}/etc'/cron.{hourly,daily,weekly}
%{__install} -m0644 '%{SOURCE1}' '%{buildroot}/etc/profile'
%{__cp} '%{SOURCE2}' '%{buildroot}/etc/DIR_COLORS'
%{__cp} '%{SOURCE3}' '%{buildroot}/etc/hosts'
echo gnyu.localdomain > '%{buildroot}/etc/HOSTNAME'
echo 'GNyU-Linux %{version}' > '%{buildroot}/etc/GNyU-version'
%{__cp} '%{SOURCE4}' '%{buildroot}/etc/passwd'
%{__cp} '%{SOURCE5}' '%{buildroot}/etc/group'
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
done < '%{SOURCE4}'
while read name passwd gid member_list
do
	echo "${name}:${passwd}:root:${member_list}" >> '%{buildroot}/etc/gshadow'
done < '%{SOURCE5}'
IFS=$old_ifs


%files
%defattr(-, root, root)
%config(noreplace) %attr(0644, root, root) /etc/HOSTNAME
%config(noreplace) %attr(0644, root, root) /etc/hosts
%config %attr(0644, root, root) /etc/protocols
%config %attr(0644, root, root) /etc/services
%dir %attr(0755, root, root) /etc/cron.*
%attr(0644, root, root) /etc/DIR_COLORS
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
