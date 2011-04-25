Name: coreutils
Version: 8.9
Release: 5.0
Summary: Core utilities that ought to exist on every GNU/Linux system
URL: http://www.gnu.org/software/coreutils
Group: System Environment/Base
License: GPL-3
Source0: http://ftp.gnu.org/pub/gnu/coreutils/%{name}-%{version}.tar.gz
BuildRequires: grep, sed, make, gcc, gcc-g++
BuildRequires: gettext-tools >= 0.17
BuildRequires: eglibc-devel, kernel-headers
BuildRequires: gmp-devel, libattr, libacl, libcap2
BuildRequires(check): findutils
Obsoletes: mktemp
Provides: mktemp

%description
The GNU Core Utilities are the basic file, shell and text manipulation
utilities of the GNU operating system. These are the core utilities which are
expected to exist on every operating system. 
Previously these utilities were offered as three individual sets of GNU
utilities, fileutils, shellutils, and textutils. Those three have been
combined into a single set of utilities called the coreutils.
The programs that are installed with this package are:
  [ basename cat chgrp chmod chown chroot cksum comm cp csplit cut date dd
  df dir dircolors dirname du echo env expand expr factor false fmt fold
  ginstall groups head hostid id join kill link ln logname ls
  md5sum mkdir mkfifo mknod mv nice nl nohup od paste pathchk pinky pr
  printenv printf ptx pwd readlink rm rmdir seq sha1sum shred sleep sort
  split stat stty sum sync tac tail tee test touch tr true tsort tty
  uname unexpand uniq unlink users vdir wc who whoami yes


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%{__rm} %{buildroot}%{_infodir}/dir ||:

# Move binaries as (partly) proposed by the FHS, but keep some in 
# %{_bindir}.
%{__mkdir_p} %{buildroot}/bin

# (These binaries MUST be in /bin:)
for file in cat chgrp chmod chown cp date dd df echo false \
		kill ln ls mkdir mknod mv pwd rm rmdir stty sync true uname \
		test '['
do
	%{__mv} "%{buildroot}%{_bindir}/${file}" '%{buildroot}/bin'
	%{__ln_s} "/bin/${file}" '%{buildroot}%{_bindir}'
done

# These must be moved, too, but some of them may reside in /usr/bin in future
# versions, keep an eye on this list!

for file in basename chroot cksum comm csplit cut dir dircolors dirname \
		expand expr fmt fold groups head hostid id install \
		link logname mkfifo nice nl nohup od paste \
		ptx readlink seq shred sleep sort split stat tail touch tr \
		tsort unexpand uniq unlink uptime users vdir wc who whoami yes
do
	%{__mv} "%{buildroot}%{_bindir}/${file}" '%{buildroot}/bin'
	%{__ln_s} "/bin/${file}" '%{buildroot}%{_bindir}'
done

# "su" is provided by another package, because this version is not
# PAM-enabled. So delete it for now. Likewise, the "groups" script comes with
# the "shadow" package. 
# And /bin/hostname is provided by net-tools.
%{__find} '%{buildroot}' \
	\( -name 'su' -or -name 'su.1*' \
		-or -name 'groups' -or -name 'groups.1*' \
		-or -name 'hostname' -or -name 'hostname.1*' \
		-or -name 'uptime' -or -name 'uptime.1*' \) \
	-exec %{__rm} -vf '{}' \;
	
%find_lang coreutils


%check
%{__make} check


%post
update-info-dir
%{__ldconfig}


%preun
update-info-dir
%{__ldconfig}



%files -f coreutils.lang
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS COPYING ChangeLog README* THANKS* TODO
%dir %{_libdir}/coreutils
/bin/cat
/bin/chgrp
/bin/chmod
/bin/chown
/bin/cp
/bin/date
/bin/dd
/bin/df
/bin/echo
/bin/false
/bin/kill
/bin/ln
/bin/ls
/bin/mkdir
/bin/mknod
/bin/mv
/bin/pwd
/bin/rm
/bin/rmdir
/bin/stty
/bin/sync
/bin/true
/bin/uname
/bin/test
/bin/[
/bin/basename
/bin/chroot
/bin/cksum
/bin/comm
/bin/csplit
/bin/cut
/bin/dir
/bin/dircolors
/bin/dirname
/bin/expand
/bin/expr
/bin/fmt
/bin/fold
/bin/head
/bin/hostid
/bin/id
/bin/install
/bin/link
/bin/logname
/bin/mkfifo
/bin/nice
/bin/nl
/bin/nohup
/bin/od
/bin/paste
/bin/ptx
/bin/readlink
/bin/seq
/bin/shred
/bin/sleep
/bin/sort
/bin/split
/bin/stat
/bin/tail
/bin/touch
/bin/tr
/bin/tsort
/bin/unexpand
/bin/uniq
/bin/unlink
/bin/users
/bin/vdir
/bin/wc
/bin/who
/bin/whoami
/bin/yes
%{_bindir}/install
%{_bindir}/chroot
%{_bindir}/hostid
%{_bindir}/nice
%{_bindir}/who
%{_bindir}/users
%{_bindir}/pinky
%{_bindir}/stty
%{_bindir}/df
%{_bindir}/stdbuf
%{_bindir}/[
%{_bindir}/base64
%{_bindir}/basename
%{_bindir}/cat
%{_bindir}/chcon
%{_bindir}/chgrp
%{_bindir}/chmod
%{_bindir}/chown
%{_bindir}/cksum
%{_bindir}/comm
%{_bindir}/cp
%{_bindir}/csplit
%{_bindir}/cut
%{_bindir}/date
%{_bindir}/dd
%{_bindir}/dir
%{_bindir}/dircolors
%{_bindir}/dirname
%{_bindir}/du
%{_bindir}/echo
%{_bindir}/env
%{_bindir}/expand
%{_bindir}/expr
%{_bindir}/factor
%{_bindir}/false
%{_bindir}/fmt
%{_bindir}/fold
%{_bindir}/head
%{_bindir}/id
%{_bindir}/join
%{_bindir}/kill
%{_bindir}/link
%{_bindir}/ln
%{_bindir}/logname
%{_bindir}/ls
%{_bindir}/md5sum
%{_bindir}/mkdir
%{_bindir}/mkfifo
%{_bindir}/mknod
%{_bindir}/mktemp
%{_bindir}/mv
%{_bindir}/nl
%{_bindir}/nproc
%{_bindir}/nohup
%{_bindir}/od
%{_bindir}/paste
%{_bindir}/pathchk
%{_bindir}/pr
%{_bindir}/printenv
%{_bindir}/printf
%{_bindir}/ptx
%{_bindir}/pwd
%{_bindir}/readlink
%{_bindir}/rm
%{_bindir}/rmdir
%{_bindir}/runcon
%{_bindir}/seq
%{_bindir}/sha1sum
%{_bindir}/sha224sum
%{_bindir}/sha256sum
%{_bindir}/sha384sum
%{_bindir}/sha512sum
%{_bindir}/shred
%{_bindir}/shuf
%{_bindir}/sleep
%{_bindir}/sort
%{_bindir}/split
%{_bindir}/stat
%{_bindir}/sum
%{_bindir}/sync
%{_bindir}/tac
%{_bindir}/tail
%{_bindir}/tee
%{_bindir}/test
%{_bindir}/timeout
%{_bindir}/touch
%{_bindir}/tr
%{_bindir}/true
%{_bindir}/truncate
%{_bindir}/tsort
%{_bindir}/tty
%{_bindir}/uname
%{_bindir}/unexpand
%{_bindir}/uniq
%{_bindir}/unlink
%{_bindir}/vdir
%{_bindir}/wc
%{_bindir}/whoami
%{_bindir}/yes
%{_libdir}/coreutils/libstdbuf.so
%doc %{_mandir}/man1/base64.1*
%doc %{_mandir}/man1/basename.1*
%doc %{_mandir}/man1/cat.1*
%doc %{_mandir}/man1/chcon.1*
%doc %{_mandir}/man1/chgrp.1*
%doc %{_mandir}/man1/chmod.1*
%doc %{_mandir}/man1/chown.1*
%doc %{_mandir}/man1/chroot.1*
%doc %{_mandir}/man1/cksum.1*
%doc %{_mandir}/man1/comm.1*
%doc %{_mandir}/man1/cp.1*
%doc %{_mandir}/man1/csplit.1*
%doc %{_mandir}/man1/cut.1*
%doc %{_mandir}/man1/date.1*
%doc %{_mandir}/man1/dd.1*
%doc %{_mandir}/man1/df.1*
%doc %{_mandir}/man1/dir.1*
%doc %{_mandir}/man1/dircolors.1*
%doc %{_mandir}/man1/dirname.1*
%doc %{_mandir}/man1/du.1*
%doc %{_mandir}/man1/echo.1*
%doc %{_mandir}/man1/env.1*
%doc %{_mandir}/man1/expand.1*
%doc %{_mandir}/man1/expr.1*
%doc %{_mandir}/man1/factor.1*
%doc %{_mandir}/man1/false.1*
%doc %{_mandir}/man1/fmt.1*
%doc %{_mandir}/man1/fold.1*
%doc %{_mandir}/man1/head.1*
%doc %{_mandir}/man1/hostid.1*
%doc %{_mandir}/man1/id.1*
%doc %{_mandir}/man1/install.1*
%doc %{_mandir}/man1/join.1*
%doc %{_mandir}/man1/kill.1*
%doc %{_mandir}/man1/link.1*
%doc %{_mandir}/man1/ln.1*
%doc %{_mandir}/man1/logname.1*
%doc %{_mandir}/man1/ls.1*
%doc %{_mandir}/man1/md5sum.1*
%doc %{_mandir}/man1/mkdir.1*
%doc %{_mandir}/man1/mkfifo.1*
%doc %{_mandir}/man1/mknod.1*
%doc %{_mandir}/man1/mktemp.1*
%doc %{_mandir}/man1/mv.1*
%doc %{_mandir}/man1/nice.1*
%doc %{_mandir}/man1/nl.1*
%doc %{_mandir}/man1/nohup.1*
%doc %{_mandir}/man1/nproc.1*
%doc %{_mandir}/man1/od.1*
%doc %{_mandir}/man1/paste.1*
%doc %{_mandir}/man1/pathchk.1*
%doc %{_mandir}/man1/pinky.1*
%doc %{_mandir}/man1/pr.1*
%doc %{_mandir}/man1/printenv.1*
%doc %{_mandir}/man1/printf.1*
%doc %{_mandir}/man1/ptx.1*
%doc %{_mandir}/man1/pwd.1*
%doc %{_mandir}/man1/readlink.1*
%doc %{_mandir}/man1/rm.1*
%doc %{_mandir}/man1/rmdir.1*
%doc %{_mandir}/man1/runcon.1*
%doc %{_mandir}/man1/seq.1*
%doc %{_mandir}/man1/sha1sum.1*
%doc %{_mandir}/man1/sha224sum.1*
%doc %{_mandir}/man1/sha256sum.1*
%doc %{_mandir}/man1/sha384sum.1*
%doc %{_mandir}/man1/sha512sum.1*
%doc %{_mandir}/man1/shred.1*
%doc %{_mandir}/man1/shuf.1*
%doc %{_mandir}/man1/sleep.1*
%doc %{_mandir}/man1/sort.1*
%doc %{_mandir}/man1/split.1*
%doc %{_mandir}/man1/stat.1*
%doc %{_mandir}/man1/stdbuf.1*
%doc %{_mandir}/man1/stty.1*
%doc %{_mandir}/man1/sum.1*
%doc %{_mandir}/man1/sync.1*
%doc %{_mandir}/man1/tac.1*
%doc %{_mandir}/man1/tail.1*
%doc %{_mandir}/man1/tee.1*
%doc %{_mandir}/man1/test.1*
%doc %{_mandir}/man1/timeout.1*
%doc %{_mandir}/man1/touch.1*
%doc %{_mandir}/man1/tr.1*
%doc %{_mandir}/man1/true.1*
%doc %{_mandir}/man1/truncate.1*
%doc %{_mandir}/man1/tsort.1*
%doc %{_mandir}/man1/tty.1*
%doc %{_mandir}/man1/uname.1*
%doc %{_mandir}/man1/unexpand.1*
%doc %{_mandir}/man1/uniq.1*
%doc %{_mandir}/man1/unlink.1*
%doc %{_mandir}/man1/users.1*
%doc %{_mandir}/man1/vdir.1*
%doc %{_mandir}/man1/wc.1*
%doc %{_mandir}/man1/who.1*
%doc %{_mandir}/man1/whoami.1*
%doc %{_mandir}/man1/yes.1*
%doc %{_infodir}/coreutils.info*
