Name: autoconf
Version: 2.61
Release: 1ev
Summary: A package of M4 macros to produce scripts to automatically configure sourcecode
URL: http://www.gnu.org/software/autoconf/
Group: Development/Tools
License: GPL
Vendor: MSP Slackware
Source: http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: perl, m4, gawk, sed, make, grep
Requires: m4, perl
BuildArch: noarch

%description
Autoconf is an extensible package of m4 macros that produce shell scripts to
automatically configure software source code packages. These scripts can adapt
the package to many kinds of UNIX-like systems without manual user
intervention.


%prep
%setup -q


%build
%configure
make %{_smp_mflags}


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"


[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"
rm -f "${RPM_BUILD_ROOT}/%{_infodir}/standards.info*"


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%post
/sbin/install-info --infodir="%{_infodir}" "%{_infodir}/autoconf.info.gz"

%postun
/sbin/install-info --delete --infodir="%{_infodir}" \
	"%{_infodir}/autoconf.info.gz"


%files
%defattr(-, root, root)
%doc AUTHORS BUGS COPYING ChangeLog* NEWS README THANKS TODO
%{_bindir}/auto*
%{_bindir}/ifnames
%{_mandir}/man1/*.1*
%{_datadir}/autoconf/
%{_datadir}/emacs/site-lisp/auto*-mode.el*
%{_infodir}/autoconf.info.gz
