Summary: The empty directory tree
Name: fhs
Version: 1.0
Release: 4ev
Group: System Environment/Base
License: GPL
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source0: fhs-languages
Source1: fhs-DIR_COLORS
Source2: fhs-profile
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-root

%description
This creates the empty directory tree for the whole distribuion, according to
the File Hierarchy Standard. It should never be removed, updated or otherwise
changed.


%prep
rm -f filelist 2>/dev/null


%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"
mkdir -p "$RPM_BUILD_ROOT"

while read LANG
do
	mkdir -m0755 -p \
		"${RPM_BUILD_ROOT}"/usr/share/locale/"${LANG}"/LC_{MESSAGES,TIME}
	mkdir -m0755 -p \
		"${RPM_BUILD_ROOT}"/usr/man/"${LANG}"/man{1,2,3,4,5,6,7,8,9}
done < %{SOURCE0}


mkdir -m0755 -p ${RPM_BUILD_ROOT}/bin
mkdir -m0755 -p ${RPM_BUILD_ROOT}/boot
mkdir -m0755 -p ${RPM_BUILD_ROOT}/dev
mkdir -m0755 -p ${RPM_BUILD_ROOT}/etc
mkdir -m0755 -p ${RPM_BUILD_ROOT}/etc/profile.d
mkdir -m0755 -p ${RPM_BUILD_ROOT}/etc/conf.d
mkdir -m0755 -p ${RPM_BUILD_ROOT}/etc/opt
mkdir -m0755 -p ${RPM_BUILD_ROOT}/etc/sgml
mkdir -m0755 -p ${RPM_BUILD_ROOT}/etc/X11
mkdir -m0755 -p ${RPM_BUILD_ROOT}/etc/xml
mkdir -m0755 -p ${RPM_BUILD_ROOT}/lib
mkdir -m0755 -p ${RPM_BUILD_ROOT}/lib/modules
mkdir -m0755 -p ${RPM_BUILD_ROOT}/media
mkdir -m0755 -p ${RPM_BUILD_ROOT}/media/cdrom
mkdir -m0755 -p ${RPM_BUILD_ROOT}/media/cdwriter
mkdir -m0755 -p ${RPM_BUILD_ROOT}/media/dvdrom
mkdir -m0755 -p ${RPM_BUILD_ROOT}/media/dvdwriter
mkdir -m0755 -p ${RPM_BUILD_ROOT}/media/floppy
mkdir -m0755 -p ${RPM_BUILD_ROOT}/media/zip
mkdir -m0755 -p ${RPM_BUILD_ROOT}/mnt
mkdir -m0755 -p ${RPM_BUILD_ROOT}/opt
mkdir -m0755 -p ${RPM_BUILD_ROOT}/sbin
mkdir -m0755 -p ${RPM_BUILD_ROOT}/srv
mkdir -m1777 -p ${RPM_BUILD_ROOT}/tmp
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/bin
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/doc
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/etc
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/games
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/include
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/info
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/lib
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/libexec
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/local
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/local/bin
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/local/etc
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/local/games
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/local/include
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/local/lib
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/local/man
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/local/sbin 
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/local/share
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/local/src
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/man/man{1,2,3,4,5,6,7,8,9}
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/sbin
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/share
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/share/dict
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/share/doc
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/share/games
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/share/info
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/share/locale
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/share/man/man{1,2,3,4,5,6,7,8,9}
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/share/misc
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/share/nls
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/share/sgml
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/share/sgml/docbook
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/share/sgml/tei
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/share/sgml/html
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/share/sgml/mathml
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/share/terminfo
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/share/tmac
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/share/xml
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/share/xml/xhtml
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/share/xml/docbook
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/share/xml/mathml
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/share/zoneinfo
mkdir -m0755 -p ${RPM_BUILD_ROOT}/usr/src
mkdir -m0755 -p ${RPM_BUILD_ROOT}/var
mkdir -m0755 -p ${RPM_BUILD_ROOT}/var/cache
mkdir -m0755 -p ${RPM_BUILD_ROOT}/var/cache/fonts
mkdir -m0755 -p ${RPM_BUILD_ROOT}/var/cache/man
mkdir -m0755 -p ${RPM_BUILD_ROOT}/var/cache/man/cat1
mkdir -m0755 -p ${RPM_BUILD_ROOT}/var/cache/man/cat2
mkdir -m0755 -p ${RPM_BUILD_ROOT}/var/cache/man/cat3
mkdir -m0755 -p ${RPM_BUILD_ROOT}/var/cache/man/cat4
mkdir -m0755 -p ${RPM_BUILD_ROOT}/var/cache/man/cat5
mkdir -m0755 -p ${RPM_BUILD_ROOT}/var/cache/man/cat6
mkdir -m0755 -p ${RPM_BUILD_ROOT}/var/cache/man/cat7
mkdir -m0755 -p ${RPM_BUILD_ROOT}/var/cache/man/cat8
mkdir -m0755 -p ${RPM_BUILD_ROOT}/var/cache/www
mkdir -m0755 -p ${RPM_BUILD_ROOT}/var/lib
mkdir -m0755 -p ${RPM_BUILD_ROOT}/var/lib/misc
mkdir -m0755 -p ${RPM_BUILD_ROOT}/var/lib/hwclock
mkdir -m0755 -p ${RPM_BUILD_ROOT}/var/local
mkdir -m0755 -p ${RPM_BUILD_ROOT}/var/lock
mkdir -m0755 -p ${RPM_BUILD_ROOT}/var/log
mkdir -m0755 -p ${RPM_BUILD_ROOT}/var/opt
mkdir -m0755 -p ${RPM_BUILD_ROOT}/var/run
mkdir -m0755 -p ${RPM_BUILD_ROOT}/var/spool
mkdir -m0755 -p ${RPM_BUILD_ROOT}/var/spool/mail
mkdir -m0755 -p ${RPM_BUILD_ROOT}/var/tmp
mkdir -m0755 -p ${RPM_BUILD_ROOT}/var/spool
mkdir -m0755 -p ${RPM_BUILD_ROOT}/home
mkdir -m0700 -p ${RPM_BUILD_ROOT}/root

find "$RPM_BUILD_ROOT" -type d \
	-exec stat --format='attr(%a, root, root) dir %n' {}  \; >> filelist
sed -i -e "s,$RPM_BUILD_ROOT,," -e 's,^attr,%attr,' -e 's, dir, %dir,' filelist


# After the directory mess, let's finally install some of the more or less
# important files in /etc.


pushd "$RPM_BUILD_ROOT/etc"

touch HOSTNAME
echo "MSP Slackware (%{name}-%{version}-%{release})" > slackware-version

cat << EOF > hosts
#
# hosts
#    This file describes a number of hostname-to-address mappings for the 
#    TCP/IP subsystem.  It is mostly used at boot time, when no name servers
#    are running. On small systems, this file can be used instead of a DNS
#    server. 
#    Just add the names, addresses and any aliases to the file.
#    By the way, Arnt Gulbrandsen <agulbra@nvg.unit.no> says that 127.0.0.1
#    should NEVER be named with the name of the machine.  It causes problems
#    for some (stupid) programs, irc and reputedly talk. :^)
#
# Format is:
# IPADDRESS        FQDN            ALIASES

# For loopbacking.
127.0.0.1          localhost

EOF

# ls dir/file colorisation
cp %{SOURCE1} DIR_COLORS

# /etc/profile shell start script
cp %{SOURCE2} profile

popd


%clean
rm filelist
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%post
# Even tough they are marked as config files, there is no need to keep some
# sort of *.rpmnew safe file.
rm -fv /etc/{HOSTNAME,DIR_COLORS,hosts}.rpm* 2>/dev/null || :


%files -f filelist
%defattr(-, root, root)
%attr(0755, root, root) %dir /
%attr(0644, root, root) /etc/slackware-version
%attr(0755, root, root) /etc/profile
%attr(0644, root, root) %config(noreplace) /etc/HOSTNAME
%attr(0644, root, root) %config(noreplace) /etc/DIR_COLORS
%attr(0644, root, root) %config(noreplace) /etc/hosts
