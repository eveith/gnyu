Name: bash
Version: 4.2
Release: 6.0
Summary: The Bourne Again SHell
URL: http://www.gnu.org/software/bash
Group: System Environment/Shells
License: GPL-3
Source: http://ftp.gnu.org/gnu/bash/%{name}-%{version}.tar.gz
BuildRequires: make >= 3.79.1, bison, gettext-tools, gcc
BuildRequires: texinfo
BuildRequires: kernel-headers
BuildRequires: readline-devel >= 5.0, ncurses-devel
Requires(post): info
Requires(postun): info

%description
This is the Bourne Again Shell.  Bash is the GNU Project's Bourne Again SHell,
a complete implementation of the POSIX.2 shell spec, but also with interactive
command line editing, job control on architectures that support it, csh-like
features such as history substitution and brace expansion, and a slew of other
features.  For more information on the features of Bash that are new to this
type of shell, see `info bash'.  There is also a large Unix-style man page.
The man page is the definitive description of the shell's features.


%prep
%setup -q


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
    --enable-casemod-attributes \
    --enable-casemod-expansions \
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
	--with-curses \
    --with-installed-readline
%{__make} %{?_smp_mflags}


%check
%{__make} tests


%install
%{__make} install DESTDIR='%{buildroot}'
%find_lang bash
%{__rm} -f '%{buildroot}%{_infodir}/dir'

pushd %{buildroot}/bin
%{__ln_s} bash sh
popd

%{__mkdir_p} '%{buildroot}%{_sysconfdir}/bash_completion.d'



%post
if [[ "$1" -eq 1 ]]; then
    install-info '%{_infodir}'/bash.info*
fi
exit 0


%postun
if [[ "$1" -eq 0 ]]; then
    install-info --delete '%{_infodir}'/bash.info*
fi
exit 0


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
