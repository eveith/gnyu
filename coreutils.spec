Name: coreutils
Version: 7.3
Release: 2ev
Summary: Core utilities that ought to exist on every GNU/Linux system
URL: http://www.gnu.org/software/coreutils
Group: System Environment/Base
License: GPL-3
Vendor: GNyU-Linux
Source0: http://ftp.gnu.org/pub/gnu/coreutils/%{name}-%{version}.tar.gz
Patch0: coreutils-5.97-i18n-1.patch
Patch1: coreutils-5.97-uname-1.patch
Patch2: coreutils-5.97-uname-2.patch
BuildRequires: make, gcc, gettext, gmp
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
	# %patch -p1 -P 0
	%patch -p1 -P 1
	%patch -p1 -P 2


%build
	%configure
	%{__make} %{?_smp_mflags}


%install
	%{__make} install DESTDIR='%{buildroot}'
	%{__rm} -f %{buildroot}/%{_infodir}/dir

	# Move binaries as (partly) proposed by the FHS, but keep some in 
	# %{_bindir}.

	%{__mkdir_p} %{buildroot}/bin

	# (These binaries MUST be in /bin:)
	for file in cat chgrp chmod chown cp date dd df echo false \
			kill ln ls mkdir mknod mv pwd rm rmdir stty sync true uname \
			test '['
	do
		%{__mv} "%{buildroot}/%{_bindir}/${file}" '%{buildroot}/bin'
		%{__ln_s} "/bin/${file}" '%{buildroot}/%{_bindir}'
	done

	# These must be moved, too, but some of them may reside in /usr/bin in future
	# versions, keep an eye on this list!

	for file in basename chroot cksum comm csplit cut dir dircolors dirname \
			expand expr fmt fold groups head hostid id install \
			link logname mkfifo nice nl nohup od paste \
			ptx readlink seq shred sleep sort split stat tail touch tr \
			tsort unexpand uniq unlink uptime users vdir wc who whoami yes
	do
		%{__mv} "%{buildroot}/%{_bindir}/${file}" '%{buildroot}/bin'
		%{__ln_s} "/bin/${file}" '%{buildroot}/%{_bindir}'
	done

	# FIXME: env should only be in /usr/bin, we must update some old packages.
	%{__cp} %{buildroot}/%{_bindir}/env %{buildroot}/bin

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


%post
	update-info-dir
	%{__ldconfig}


%preun
	update-info-dir
	%{__ldconfig}



%files -f coreutils.lang
	%defattr(-, root, root)
	%doc ABOUT-NLS AUTHORS COPYING ChangeLog README* THANKS* TODO
	/bin/*
	%{_bindir}/*
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
