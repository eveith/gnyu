Name: grep
Version: 2.5.4
Release: 2ev
Summary: Searches for matches of a userspecified pattern in a given input stream
URL: http://www.gnu.org/software/grep
Group: System Environment/Base
License: GPL-3
Vendor: GNyU-Linux
Source: ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.bz2
BuildRequires: gcc, make >= 3.79.1, pcre, gettext
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


%build
%configure
%{__make} %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -static"
%{__make} check


%install
%{__make} install LDFLAGS="-s" DESTDIR='%{buildroot}'
%{__rm} ${RPM_BUILD_ROOT}/%{_infodir}/dir ||:
%find_lang grep

# Move grep to /bin where its needed at boottime
%{__mkdir_p} "${RPM_BUILD_ROOT}/bin"
%{__mv} "${RPM_BUILD_ROOT}/%{_bindir}"/*grep* "${RPM_BUILD_ROOT}/bin"
%{__rm_rf} "${RPM_BUILD_ROOT}/%{_bindir}"


%post
update-info-dir
%{__ldconfig}


%preun
update-info-dir
%{__ldconfig}


%files -f grep.lang
%defattr(-, root, root)
%doc ABOUT* AUTHORS COPYING ChangeLog* README* NEWS THANKS TODO
/bin/egrep
/bin/fgrep
/bin/grep
%doc %{_infodir}/grep.info*
%doc %{_mandir}/man1/egrep.1*
%doc %{_mandir}/man1/fgrep.1*
%doc %{_mandir}/man1/grep.1*
