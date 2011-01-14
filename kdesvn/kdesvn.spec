Name: kdesvn
Version: 0.13.0
Release: 1ev
Summary: A SVN frontend that integrates with KDE's Konqueror
URL: http://kdesvn.alwins-world.de/
Group: Development/Tools
License: GPL
Vendor: MSP Slackware
Source: %{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: cmake, make, gcc-g++, qt3, subversion, kdelibs, kdebase, apr

%description
KDESvn is a frontend to the subversion vcs. In difference to most other tools
it uses the subversion C-Api direct via a c++ wrapper made by Rapid SVN and
doesn't parse the output of the subversion client. So it is a real client
itself instead of a frontend to the command line tool. The origin wrapper is
meanwhile ported to Qt-toolkit and may used in other projects wanting a pure
qt-wrapper. 
As the name says its highly integrated into the the K-Desktop environment and
uses all of the goodies it has. This means: it is not usable on windows as
long as kde isn't ported there.


%prep
%setup -q

# Correct manpath.
sed -i 's,share/man,%{_mandir},g' doc/man/CMakeLists.txt


%build
cmake \
	-DAPPLNK_INSTALL_DIR:PATH='%{_datadir}/applnk' \
	-DEXEC_INSTALL_PREFIX:PATH='%{_prefix}' \
	-DCMAKE_INSTALL_PREFIX:PATH='%{_prefix}' \
	-DMAN_INSTALL_DIR:PATH='%{_mandir}' \
	-DCMAKE_BUILD_TYPE:STRING='Release' \
	-DCMAKE_CXX_FLAGS_RELEASE:STRING="$RPM_OPT_FLAGS" \
	-DCMAKE_CXX_COMPILER:FILEPATH='%{_target_platform}-g++' \
	.
make %{_smp_mflags}


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"
%find_lang kdesvn

[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files -f kdesvn.lang
%defattr(-, root, root)
%doc README TODO GPL* COPYING* AUTHORS ChangeLog
%doc %{_datadir}/doc/HTML/*/kdesvn
%{_bindir}/kdesvn*
%{_includedir}/svnqt/
%{_libdir}/kde3/*.*
%{_libdir}/libsvnqt.*
%{_datadir}/applications/kde/kdesvn.desktop
%{_datadir}/apps/kdesvn/
%{_datadir}/apps/kdesvnpart/
%{_datadir}/apps/konqueror/servicemenus/kdesvn_subversion.desktop
%{_datadir}/config.kcfg/kdesvn_part.kcfg
%{_datadir}/icons/*/*/*/*.*
%{_mandir}/man1/kdesvn*.*
%{_datadir}/services/kded/kdesvnd.desktop
%{_datadir}/services/*.protocol
