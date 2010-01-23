Name: bash
Version: 4.1
Release: 5.0ev
Summary: The Bourne Again SHell
URL: http://www.gnu.org/software/bash
Group: System Environment/Shells
License: GPL-3
Vendor: GNyU-Linux
Source: http://ftp.gnu.org/gnu/bash/%{name}-%{version}.tar.gz
Patch001: %{name}-%{version}-001.diff
Patch002: %{name}-%{version}-002.diff
Patch100: bash-requires.patch
BuildRequires: make >= 3.79.1, bison, gettext, gcc
BuildRequires: readline >= 5.0, ncurses

%description
This is the Bourne Again Shell.  Bash is the GNU Project's Bourne
Again SHell, a complete implementation of the POSIX.2 shell spec,
but also with interactive command line editing, job control on
architectures that support it, csh-like features such as history
substitution and brace expansion, and a slew of other features.
For more information on the features of Bash that are new to this
type of shell, see the file `doc/bashref.texi'.  There is also a
large Unix-style man page.  The man page is the definitive description
of the shell's features.


%prep
%setup -q
%patch001 -p0 
%patch002
#%patch -P 100 -p1

%build
%configure \
	--bindir=/bin \
	--sbindir=/sbin \
	--libdir=/%{_lib} \
	--enable-alias \
	--enable-arith-for-command \
	--enable-array-variables \
	--enable-bang-history \
	--enable-brace-expansion \
	--enable-command-timing \
	--enable-cond-command \
	--enable-cond-regexp \
	--enable-debugger \
	--enable-directory-stack \
	--enable-dparen-arithmetic \
	--enable-extended-glob \
	--enable-help-builtin \
	--enable-history \
	--enable-job-control \
	--enable-multibyte \
	--enable-net-redirections \
	--enable-process-substitution \
	--enable-progcomp \
	--enable-prompt-string-decoding \
	--enable-readline \
	--enable-restricted \
	--enable-select \
	--enable-mem-scramble \
	--with-curses
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%find_lang bash
%{__rm} -f '%{buildroot}/%{_infodir}/dir'

pushd %{buildroot}/bin
%{__ln_s} bash sh
popd

%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/bash_completion.d'



%post
%{__ldconfig}
update-info-dir > /dev/null 2>&1 ||:


%postun
%{__ldconfig}
update-info-dir 2>/dev/null 2>&1 ||:


%files -f bash.lang
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS CHANGES COMPAT COPYING CWRU INSTALL MANIFEST* NEWS
%doc NOTES POSIX RBASH README* Y2K 
%dir %{_sysconfdir}/bash_completion.d
/bin/sh
%attr(0711, root, root) /bin/bash
%attr(0711, root, root) /bin/bashbug
%doc %{_infodir}/bash.info*
%doc %{_mandir}/man1/bash.1*
%doc %{_mandir}/man1/bashbug.1*
