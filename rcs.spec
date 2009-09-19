Name: rcs
Version: 5.7
Release: 1ev
Summary: GNU Revision Control System
URL: http://www.cs.purdue.edu/homes/trinkle/RCS/
Group: Applications/Archiving
License: GPL-2
Vendor: MSP Slackware
Source: http://www.cs.purdue.edu/homes/trinkle/RCS/rcs-%{version}.tar.Z
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, diffutils
Requires: diffutils

%description
The Revision Control System (RCS) manages multiple revisions of files. 
RCS automates the storing, retrieval, logging, identification, and merging 
of revisions. RCS is useful for text that is revised frequently, for 
example programs, documentation, graphics, papers, and form letters.


%prep
%setup -q


%build
CFLAGS="$RPM_OPT_FLAGS"
CXXFLAGS="$RPM_OPT_FLAGS"
CPPFLAGS="$RPM_OPT_FLAGS"
export CFLAGS CXXFLAGS CPPFLAGS
./configure \
	--host='%{_host}' \
	--build='%{_build}' \
	--target='%{_target_platform}' \
	--prefix='%{_prefix}' \
	--with-diffutils
%{__make} %{_smp_mflags}


%install
[[ -d '%{buildroot}' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} prefix='%{buildroot}/%{_prefix}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%clean
[[ -d '%{buildroot}' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc ChangeLog COPYING CREDITS NEWS README REFS
%{_bindir}/ci
%{_bindir}/co
%{_bindir}/ident
%{_bindir}/merge
%{_bindir}/rcs*
%{_bindir}/rlog
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
