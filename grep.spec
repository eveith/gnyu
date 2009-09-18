Name: grep
Version: 2.5.1a
Release: 1ev
Summary: Searches for matches of a userspecified pattern in a given input stream
URL: http://www.gnu.org/software/grep
Group: System Environment/Base
License: GPL
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: gcc-core, make >= 3.79.1, pcre
Requires: /sbin/install-info
Patch0: grep-2.5.1-fgrep.patch
Patch1: grep-2.5.1-bracket.patch
Patch2: grep-2.5-i18n.patch
Patch3: grep-2.5.1-oi.patch
Patch4: grep-2.5.1-manpage.patch
Patch5: grep-2.5.1-color.patch
Patch6: grep-2.5.1-icolor.patch
Patch10: grep-2.5.1-egf-speedup.patch
Patch11: grep-2.5.1-dfa-optional.patch
Patch12: grep-2.5.1-tests.patch
Patch13: grep-2.5.1-w.patch
Patch14: grep-P.patch

%description
GNU grep is based on a fast lazy-state deterministic matcher (about
twice as fast as stock Unix egrep) hybridized with a Boyer-Moore-Gosper
search for a fixed string that eliminates impossible text from being
considered by the full regexp matcher without necessarily having to
look at every character.  The result is typically many times faster
than Unix grep or egrep.  (Regular expressions containing backreferencing
will run more slowly, however.)


%prep
%setup -q
%patch0 -p1 -b .fgrep
%patch1 -p1 -b .bracket
%patch2 -p1 -b .i18n
%patch3 -p1 -b .oi
%patch4 -p1 -b .manpage
%patch5 -p1 -b .color
%patch6 -p1 -b .icolor
%patch10 -p1 -b .egf-speedup
%patch11 -p1 -b .dfa-optional
%patch12 -p1 -b .tests
%patch13 -p1 -b .w
%patch14 -p1 -b .P
chmod a+x tests/fmbtest.sh


%build
%configure
make CFLAGS="$RPM_OPT_FLAGS -static"
make check


%install
%makeinstall LDFLAGS="-s"
rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir
%find_lang grep

# Move grep to /bin where its needed at boottime
mkdir ${RPM_BUILD_ROOT}/bin
mv ${RPM_BUILD_ROOT}/%{_bindir}/*grep* ${RPM_BUILD_ROOT}/bin
if [ "$RPM_BUILD_ROOT" != "/" ]
then
	rm -rf "${RPM_BUILD_ROOT}/%{_bindir}"
fi


%post
/sbin/install-info %{_infodir}/grep.info.gz %{_infodir}/dir
/sbin/ldconfig

%preun
/sbin/install-info --delete %{_infodir}/grep.info.gz %{_infodir}/dir
/sbin/ldconfig


%clean
rm -rf ${RPM_BUILD_ROOT}


%files -f grep.lang
%defattr(-, root, root)
%doc ABOUT* AUTHORS COPYING ChangeLog* README* NEWS THANKS TODO
/bin/egrep
/bin/fgrep
/bin/grep
%{_infodir}/grep.info.gz
%{_mandir}/man1/egrep.1*
%{_mandir}/man1/fgrep.1*
%{_mandir}/man1/grep.1*
