Name: kde4-l10n-de
Version: 4.3.2
Release: 5.0ev
Summary: German translations for KDE 4
URL: http://www.kde.org
Group: User Interface/Desktops
License: FDL-1.2
Vendor: GNyU-Linux
Source: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/kde-l10n-de-%{version}.tar.bz2
BuildRequires: cmake >= 2.4.5, make, kdelibs4, kdebase4, qt4 >= 4.4.2
BuildRequires: automoc4 >= 0.8.86, libICE, libX11, gettext, phonon >= 4.3.0
BuildArch: noarch
Requires: kdelibs4, kdebase4

%description
This package provides German translations for all programs that are part of
the original kde source. Some subpackages also provide localized sounds or
wordlists for games and educational programs; you might want to install them,
too.


%package games
Summary: Localized files KDE's games (German)
Group: User Interface/Desktops
Requires: kdegames4

%description games
This is a supplemant to the kde4-l10n-de package. It contains speech files and
wordlists for KDE's games.


%package edu
Summary: Localized files for KDE's educational programs (German)
Group: User Interface/Desktops
Requires: kdeedu4

%description edu
This is a supplemant to the kde4-l10n-de package. It contains localizations
for KDE's educational programs.


%prep
%setup -q -n 'kde-l10n-de-%{version}'


%build
%{cmake} \
	-DQT_QMAKE_EXECUTABLE:FILEPATH='%{_libdir}/qt4/bin/qmake' \
	.
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'


%files
%defattr(-, root, root)
%doc %{_datadir}/doc/HTML/de/*
%doc %{_mandir}/de/man1/adddebug.1*
%doc %{_mandir}/de/man1/ark.1*
%doc %{_mandir}/de/man1/cheatmake.1*
%doc %{_mandir}/de/man1/checkXML.1*
%doc %{_mandir}/de/man1/create_cvsignore.1*
%doc %{_mandir}/de/man1/create_makefile.1*
%doc %{_mandir}/de/man1/create_makefiles.1*
%doc %{_mandir}/de/man1/cvscheck.1*
%doc %{_mandir}/de/man1/cvslastchange.1*
%doc %{_mandir}/de/man1/cvslastlog.1*
%doc %{_mandir}/de/man1/cvsrevertlast.1*
%doc %{_mandir}/de/man1/cxxmetric.1*
%doc %{_mandir}/de/man1/demangle.1*
%doc %{_mandir}/de/man1/extend_dmalloc.1*
%doc %{_mandir}/de/man1/extractrc.1*
%doc %{_mandir}/de/man1/fixincludes.1*
%doc %{_mandir}/de/man1/kabcclient.1*
%doc %{_mandir}/de/man1/kalzium.1*
%doc %{_mandir}/de/man1/kappfinder.1*
%doc %{_mandir}/de/man1/kate.1*
%doc %{_mandir}/de/man1/kbookmarkmerger.1*
%doc %{_mandir}/de/man1/kbruch.1*
%doc %{_mandir}/de/man1/kconfig_compiler.1*
%doc %{_mandir}/de/man1/kde4-config.1*
%doc %{_mandir}/de/man1/kdesu.1*
%doc %{_mandir}/de/man1/kfind.1*
%doc %{_mandir}/de/man1/kig.1*
%doc %{_mandir}/de/man1/kjs.1*
%doc %{_mandir}/de/man1/kjscmd.1*
%doc %{_mandir}/de/man1/kmag.1*
%doc %{_mandir}/de/man1/kmousetool.1*
%doc %{_mandir}/de/man1/kmouth.1*
%doc %{_mandir}/de/man1/kmplot.1*
%doc %{_mandir}/de/man1/kross.1*
%doc %{_mandir}/de/man1/ktouch.1*
%doc %{_mandir}/de/man1/makekdewidgets.1*
%doc %{_mandir}/de/man1/plasmaengineexplorer.1*
%doc %{_mandir}/de/man1/po2xml.1*
%doc %{_mandir}/de/man1/preparetips.1*
%doc %{_mandir}/de/man1/pruneemptydirs.1*
%doc %{_mandir}/de/man1/qtdoc.1*
%doc %{_mandir}/de/man1/reportview.1*
%doc %{_mandir}/de/man1/split2po.1*
%doc %{_mandir}/de/man1/swappo.1*
%doc %{_mandir}/de/man1/transxx.1*
%doc %{_mandir}/de/man1/xml2pot.1*
%doc %{_mandir}/de/man1/xsldbg.1*
%doc %{_mandir}/de/man1/zonetab2pot.py.1*
%doc %{_mandir}/de/man6/amor.6*
%doc %{_mandir}/de/man6/khangman.6*
%doc %{_mandir}/de/man6/kpat.6*
%doc %{_mandir}/de/man7/kdeoptions.7*
%doc %{_mandir}/de/man7/qtoptions.7*
%doc %{_mandir}/de/man8/kbuildsycoca4.8*
%doc %{_mandir}/de/man8/kcookiejar4.8*
%doc %{_mandir}/de/man8/kded4.8*
%doc %{_mandir}/de/man8/kdeinit4.8*
%doc %{_mandir}/de/man8/meinproc4.8*
%doc %{_mandir}/de/man8/nepomukserver.8*
%doc %{_mandir}/de/man8/nepomukservicestub.8*
%lang(de) %{_datadir}/locale/de/*/*.mo
%{_datadir}/locale/de/LC_SCRIPTS/
%{_datadir}/locale/de/entry.desktop


%files games
%defattr(-, root, root)
%lang(de) %{_datadir}/apps/khangman/de.txt
%{_datadir}/apps/ktuberling/sounds/de.soundtheme
%{_datadir}/apps/ktuberling/sounds/de/


%files edu
%defattr(-, root, root)
%{_datadir}/apps/klettres/de/
%{_datadir}/apps/kvtml/de/
%{_datadir}/apps/step/objinfo/l10n/de/
