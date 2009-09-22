Name: man-pages
Version: 2.44
Release: 1ev
Summary: The Linux manpages collection
URL: http://www.win.tue.nl/~aeb/linux/man/
Group: Documentation
License: Freely distributable
Vendor: MSP Slackware
Source: ftp://ftp.win.tue.nl/pub/linux-local/manpages/%{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: coreutils
BuildArch: noarch

%description
The manpages package contains a large collection of man pages for Linux
covering programming APIs, file formats, protocols, etc. 


%prep
%setup -q


%build
exit 0


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
mkdir -p "$RPM_BUILD_ROOT"/%{_mandir}

cp -vr man0p man1p man3  man4 man6 man8 \
	man1 man2 man3p man5 man7 man9 \
	"$RPM_BUILD_ROOT"/%{_mandir}

# We need to remove some man pages which are already provided by
# other packages.

# We begin with coreutils - yes, the GNU manpages suck,
# then openssl, libattr and shadow.

for manpage in man/man1/base64.1 \
		man1/basename.1 \
		man1/cat.1 \
		man1/chgrp.1 \
		man1/chmod.1 \
		man1/chown.1 \
		man1/chroot.1 \
		man1/cksum.1 \
		man1/comm.1 \
		man1/cp.1 \
		man1/csplit.1 \
		man1/cut.1 \
		man1/date.1 \
		man1/dd.1 \
		man1/df.1 \
		man1/dir.1 \
		man1/dircolors.1 \
		man1/dirname.1 \
		man1/du.1 \
		man1/echo.1 \
		man1/env.1 \
		man1/expand.1 \
		man1/expr.1 \
		man1/factor.1 \
		man1/false.1 \
		man1/fmt.1 \
		man1/fold.1 \
		man1/groups.1 \
		man1/head.1 \
		man1/hostid.1 \
		man1/hostname.1 \
		man1/id.1 \
		man1/install.1 \
		man1/join.1 \
		man1/kill.1 \
		man1/link.1 \
		man1/ln.1 \
		man1/logname.1 \
		man1/ls.1 \
		man1/md5sum.1 \
		man1/mkdir.1 \
		man1/mkfifo.1 \
		man1/mknod.1 \
		man1/mv.1 \
		man1/nice.1 \
		man1/nl.1 \
		man1/nohup.1 \
		man1/od.1 \
		man1/paste.1 \
		man1/pathchk.1 \
		man1/pinky.1 \
		man1/pr.1 \
		man1/printenv.1 \
		man1/printf.1 \
		man1/ptx.1 \
		man1/pwd.1 \
		man1/readlink.1 \
		man1/rm.1 \
		man1/rmdir.1 \
		man1/seq.1 \
		man1/sha1sum.1 \
		man1/sha224sum.1 \
		man1/sha256sum.1 \
		man1/sha384sum.1 \
		man1/sha512sum.1 \
		man1/shred.1 \
		man1/shuf.1 \
		man1/sleep.1 \
		man1/sort.1 \
		man1/split.1 \
		man1/stat.1 \
		man1/stty.1 \
		man1/sum.1 \
		man1/sync.1 \
		man1/tac.1 \
		man1/tail.1 \
		man1/tee.1 \
		man1/test.1 \
		man1/touch.1 \
		man1/tr.1 \
		man1/true.1 \
		man1/tsort.1 \
		man1/tty.1 \
		man1/uname.1 \
		man1/unexpand.1 \
		man1/uniq.1 \
		man1/unlink.1 \
		man1/uptime.1 \
		man1/users.1 \
		man1/vdir.1 \
		man1/wc.1 \
		man1/who.1 \
		man1/whoami.1 \
		man1/yes.1 \
		man3/err.3 \
		man3/rand.3 \
		man2/setxattr.2 \
		man2/llistxattr.2 \
		man2/listxattr.2 \
		man2/fgetxattr.2 \
		man2/fsetxattr.2 \
		man2/fremovexattr.2 \
		man2/lgetxattr.2 \
		man2/lsetxattr.2 \
		man2/lremovexattr.2 \
		man2/getxattr.2 \
		man2/removexattr.2 \
		man2/flistxattr.2 \
		man3/getspnam.3
do
	rm -vf "$RPM_BUILD_ROOT"/%{_mandir}/"$manpage"
done

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc Changes* README HOWTOHELP MAINTAINING POSIX-COPYRIGHT TODO *.Announce 
%{_mandir}/*/*
%dir %{_mandir}/man0p
%dir %{_mandir}/man1p
%dir %{_mandir}/man3p
