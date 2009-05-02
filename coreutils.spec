Name: coreutils
Version: 6.9
Release: 1ev
Summary: Core utilities that ought to exist on every GNU/Linux system
URL: http://www.gnu.org/software/coreutils
Group: System Environment/Base
License: GPL
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source0: http://ftp.gnu.org/pub/gnu/coreutils/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: gcc-core, make >= 3.79.1
Requires: /sbin/install-info
Patch0: coreutils-5.97-i18n-1.patch
Patch1: coreutils-5.97-uname-1.patch
Patch2: coreutils-5.97-uname-2.patch

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
  ginstall groups head hostid hostname id join kill link ln logname ls
  md5sum mkdir mkfifo mknod mv nice nl nohup od paste pathchk pinky pr
  printenv printf ptx pwd readlink rm rmdir seq sha1sum shred sleep sort
  split stat stty sum sync tac tail tee test touch tr true tsort tty
  uname unexpand uniq unlink uptime users vdir wc who whoami yes


%prep
%setup -q
# %patch -p1 -P 0
%patch -p1 -P 1
%patch -p1 -P 2


%build
%configure
make


%install
[[ "$RPM_BUILD_ROOT" != "/" ]] && rm -rf "$RPM_BUILD_ROOT"
%{__make_install} DESTDIR='%{buildroot}'
%{__rm} -f %{buildroot}/%{_infodir}/dir

# Move binaries as (partly) proposed by the FHS, but keep some in 
# %{_bindir}.

%{__mkdir_p} %{buildroot}/bin
#mv ${RPM_BUILD_ROOT}/%{_bindir}/* "${RPM_BUILD_ROOT}/bin"
#mv "${RPM_BUILD_ROOT}/bin/env" "${RPM_BUILD_ROOT}/%{_bindir}"

# (These binaries MUST be in /bin:)
for file in cat chgrp chmod chown cp date dd df echo false hostname \
		kill ln ls mkdir mknod mv pwd rm rmdir stty sync true uname \
		test '['
do
	%{__mv} %{buildroot}/%{_bindir}/$file %{buildroot}/bin
done

# These must be moved, too, but some of them may reside in /usr/bin in future
# versions, keep an eye on this list!

for file in basename chroot cksum comm csplit cut dir dircolors dirname \
		expand expr fmt fold groups head hostid id install \
		link logname mkfifo nice nl nohup od paste \
		ptx readlink seq shred sleep sort split stat tail touch tr \
		tsort unexpand uniq unlink uptime users vdir wc who whoami yes
do
	%{__mv} %{buildroot}/%{_bindir}/$file %{buildroot}/bin
done

# FIXME: env should only be in /usr/bin, we must update some old packages.
%{__cp} %{buildroot}/%{_bindir}/env %{buildroot}/bin

# "su" is provided by another package, because this version is not
# PAM-enabled. So delete it for now. Likewise, the "groups" script comes with
# the "shadow" package. 
# And /bin/hostname is provided by net-tools.

find "$RPM_BUILD_ROOT" \
	\( -name 'su*' -or -name 'groups*' -or -name 'hostname*' \) \
	-exec rm -vf {} \;
%find_lang coreutils


%post
update-info-dir
/sbin/ldconfig

%preun
update-info-dir
/sbin/ldconfig


%clean
[[ "$RPM_BUILD_ROOT" != "/" ]] && %{__rm} -rf '%{buildroot}'
exit 0


%files -f coreutils.lang
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS COPYING ChangeLog README* THANKS* TODO
/bin/*
%{_bindir}/*
%{_mandir}/*/*
%{_infodir}/coreutils.info*
%{_datadir}/locale/*/LC_TIME/coreutils.mo
