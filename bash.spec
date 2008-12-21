Name: bash
Version: 3.2
Release: 1ev
Summary: The Bourne Again SHell
URL: http://www.gnu.org/software/bash
Group: System Environment/Shells
License: GPL
Vendor: MSP Slackware
Source: http://ftp.gnu.org/gnu/bash/%{name}-%{version}.tar.gz
Patch001: bash32-001
Patch002: bash32-002
Patch003: bash32-003
Patch004: bash32-004
Patch005: bash32-005
Patch006: bash32-006
Patch007: bash32-007
Patch008: bash32-008
Patch009: bash32-009
Patch010: bash32-010
Patch011: bash32-011
Patch012: bash32-012
Patch013: bash32-013
Patch014: bash32-014
Patch015: bash32-015
Patch016: bash32-016
Patch017: bash32-017
Patch018: bash32-018
Patch019: bash32-019
Patch020: bash32-020
Patch021: bash32-021
Patch022: bash32-022
Patch023: bash32-023
Patch024: bash32-024
Patch025: bash32-025
Patch026: bash32-026
Patch027: bash32-027
Patch028: bash32-028
Patch029: bash32-029
Patch030: bash32-030
Patch031: bash32-031
Patch032: bash32-032
Patch033: bash32-033
Patch100: bash-requires.patch
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc-core, libtermcap

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
%patch -P 001
%patch -P 002
%patch -P 003
%patch -P 004
%patch -P 005
%patch -P 006
%patch -P 007
%patch -P 008
%patch -P 009
%patch -P 010
%patch -P 011
%patch -P 012
%patch -P 013
%patch -P 014
%patch -P 015
%patch -P 016
%patch -P 017 
%patch018
%patch019
%patch020
%patch021
%patch022
%patch023
%patch024
%patch025
%patch026
%patch027
%patch028
%patch029
%patch030
%patch031
%patch032
%patch033
%patch -P 100 -p1

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
	--enable-mem-scramble
%{__make} %{_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%find_lang bash
%{__rm} -f %{buildroot}/%{_infodir}/dir

pushd %{buildroot}/bin
ln -sf bash sh
popd



%post
/sbin/ldconfig
update-info-dir > /dev/null 2>&1 ||:

%postun
/sbin/ldconfig
update-info-dir 2>/dev/null 2>&1 ||:


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files -f bash.lang
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS CHANGES COMPAT COPYING CWRU INSTALL MANIFEST* NEWS
%doc NOTES POSIX RBASH README* Y2K 
/bin/sh
/bin/bash
/bin/bashbug
%{_infodir}/bash.info.gz
%{_mandir}/man1/bash.1.gz
%{_mandir}/man1/bashbug.1.gz
