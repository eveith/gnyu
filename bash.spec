Name: bash
Version: 3.2
Release: 2ev
Summary: The Bourne Again SHell
URL: http://www.gnu.org/software/bash
Group: System Environment/Shells
License: GPL
Vendor: GNyU-Linux
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
Patch034: bash32-034
Patch035: bash32-035
Patch036: bash32-036
Patch037: bash32-037
Patch038: bash32-038
Patch039: bash32-039
Patch040: bash32-040
Patch041: bash32-041
Patch042: bash32-042
Patch043: bash32-043
Patch044: bash32-044
Patch045: bash32-045
Patch046: bash32-046
Patch047: bash32-047
Patch048: bash32-048
Patch100: bash-requires.patch
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc, libtermcap

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
%patch001
%patch002
%patch003
%patch004
%patch005
%patch006
%patch007
%patch008
%patch009
%patch010
%patch011
%patch012
%patch013
%patch014
%patch015
%patch016
%patch017 -p0
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
%patch034
%patch035
%patch036
%patch037
%patch038
%patch039
%patch040
%patch041
%patch042
%patch043
%patch044
%patch045
%patch046
%patch047
%patch048
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
	--enable-mem-scramble
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%find_lang bash
%{__rm} -f '%{buildroot}/%{_infodir}/dir'

pushd %{buildroot}/bin
%{__ln_s} bash sh
popd



%post
%{__ldconfig}
update-info-dir > /dev/null 2>&1 ||:

%postun
%{__ldconfig}
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
%doc %{_infodir}/bash.info*
%doc %{_mandir}/man1/bash.1*
%doc %{_mandir}/man1/bashbug.1*
