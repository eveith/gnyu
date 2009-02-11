Name: kde4-l10n-de
Version: 4.2.0
Release: 1ev
Summary: German translations for KDE 4
URL: http://www.kde.org/
Group: User Interface/Desktops
License: FDL-1.2
Vendor: GNyU-Linux
Source: ftp://ftp.kde.org/pub/kde/stable/4.2.0/src/kde-l10n/kde-l10n-de-%{version}.tar.bz2
BuildRequires: cmake >= 2.4.5, make, kdelibs4, kdebase4, qt4 >= 4.4.2
BuildRequires: automoc4 >= 0.8.86, libICE, libX11, gettext, phonon >= 4.3.0
BuildArch: noarch
Requires: kdelibs4, kdebase4, kdegames4, kdeedu4

%description
This package provides German translations for all programs that are part of
the original kde source.


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
%{_mandir}/de/man1/adddebug.1*
%{_mandir}/de/man1/ark.1*
%{_mandir}/de/man1/cheatmake.1*
%{_mandir}/de/man1/checkXML.1*
%{_mandir}/de/man1/create_cvsignore.1*
%{_mandir}/de/man1/create_makefile.1*
%{_mandir}/de/man1/create_makefiles.1*
%{_mandir}/de/man1/cvscheck.1*
%{_mandir}/de/man1/cvslastchange.1*
%{_mandir}/de/man1/cvslastlog.1*
%{_mandir}/de/man1/cvsrevertlast.1*
%{_mandir}/de/man1/cxxmetric.1*
%{_mandir}/de/man1/demangle.1*
%{_mandir}/de/man1/extend_dmalloc.1*
%{_mandir}/de/man1/extractrc.1*
%{_mandir}/de/man1/fixincludes.1*
%{_mandir}/de/man1/kalzium.1*
%{_mandir}/de/man1/kappfinder.1*
%{_mandir}/de/man1/kate.1*
%{_mandir}/de/man1/kbookmarkmerger.1*
%{_mandir}/de/man1/kbruch.1*
%{_mandir}/de/man1/kconfig_compiler.1*
%{_mandir}/de/man1/kde4-config.1*
%{_mandir}/de/man1/kdesu.1*
%{_mandir}/de/man1/kfind.1*
%{_mandir}/de/man1/kig.1*
%{_mandir}/de/man1/kjs.1*
%{_mandir}/de/man1/kjscmd.1*
%{_mandir}/de/man1/kmag.1*
%{_mandir}/de/man1/kmousetool.1*
%{_mandir}/de/man1/kmouth.1*
%{_mandir}/de/man1/kmplot.1*
%{_mandir}/de/man1/kross.1*
%{_mandir}/de/man1/ktouch.1*
%{_mandir}/de/man1/makekdewidgets.1*
%{_mandir}/de/man1/po2xml.1*
%{_mandir}/de/man1/preparetips.1*
%{_mandir}/de/man1/pruneemptydirs.1*
%{_mandir}/de/man1/qtdoc.1*
%{_mandir}/de/man1/reportview.1*
%{_mandir}/de/man1/split2po.1*
%{_mandir}/de/man1/swappo.1*
%{_mandir}/de/man1/transxx.1*
%{_mandir}/de/man1/xml2pot.1*
%{_mandir}/de/man1/zonetab2pot.py.1*
%{_mandir}/de/man6/amor.6*
%{_mandir}/de/man6/khangman.6*
%{_mandir}/de/man6/kpat.6*
%{_mandir}/de/man7/kdeoptions.7*
%{_mandir}/de/man7/qtoptions.7*
%{_mandir}/de/man8/kbuildsycoca4.8*
%{_mandir}/de/man8/kcookiejar4.8*
%{_mandir}/de/man8/kded4.8*
%{_mandir}/de/man8/kdeinit4.8*
%{_mandir}/de/man8/meinproc4.8*
%{_datadir}/apps/khangman/de.txt
%{_datadir}/apps/klettres/de/
%{_datadir}/apps/ktuberling/sounds/de.soundtheme
%{_datadir}/apps/ktuberling/sounds/de/
%{_datadir}/apps/kvtml/de/
%{_datadir}/apps/step/objinfo/l10n/de/
%{_datadir}/locale/de/*/*.mo
%{_datadir}/locale/de/LC_SCRIPTS/
%{_datadir}/locale/de/entry.desktop
