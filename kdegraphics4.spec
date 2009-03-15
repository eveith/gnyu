Name: kdegraphics4
Version: 4.2.1
Release: 2ev
Summary: A collection of graphic oriented applications for KDE 4.2
URL: http://www.kde.org/
Group: User Interface/Desktops
License: GPL-2, LGPL-2.1, FDL-1.2
Vendor: GNyU-Linux
Source: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdegraphics-%{version}.tar.bz2
BuildRequires: cmake >= 2.4.5, make, gcc-g++, qt4 >= 4.4.2, automoc4 >= 0.8.86
BuildRequires: perl, phonon >= 4.3.0, kdelibs4 = %{version}, strigi, qimageblitz
BuildRequires: sane-backends, lcms, libjpeg, libtiff, poppler-qt4, zlib, freetype
BuildRequires: libX11, libICE, libXxf86vm, exiv2, pkg-config
Obsoletes: kdegraphics < %{version}

%description
kdegraphics is a collection of graphic oriented applications:
* gwenview: An image viewer,
* kfile-plugins: provide meta information for graphic files,
* kolourpaint: an easy-to-use paint program designed for everyday tasks
  like drawing simple diagrams/logos/icons and editing screenshots,
* kruler: a ruler in inch, centimeter and pixel to check distances on the
  screen,
* ksnapshot: make snapshots of the screen contents,
* libkscan: a library to access scanners used by kooka (and koffice), and
* okular: A document viewer; support different kinds of documents.


%prep
%setup -q -n 'kdegraphics-%{version}'


%build
%{cmake} \
	-DQT_QMAKE_EXECUTABLE:FILEPATH='%{_libdir}/qt4/bin/qmake' \
	.
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'


%files
%defattr(-, root, root)
%doc COPYING* AUTHORS ChangeLog README
%doc %{_datadir}/doc/HTML/en/*
%config %{_sysconfdir}/kde4/okular.knsrc
%{_bindir}/gwenview
%{_bindir}/kbackgroundsnapshot              
%{_bindir}/kcolorchooser                    
%{_bindir}/kolourpaint                      
%{_bindir}/kruler                           
%{_bindir}/ksnapshot                        
%{_bindir}/okular                           
%{_bindir}/xf86gammacfg 
%{_includedir}/libkdcraw/
%{_includedir}/libkipi/
%{_includedir}/libksane/
%{_includedir}/okular/
%{_includedir}/libkexiv2/
%{_libdir}/kde4/*.so
%{_libdir}/libkexiv2.so*
%{_libdir}/libgwenviewlib.so*
%{_libdir}/libkdcraw.so*
%{_libdir}/libkipi.so*
%{_libdir}/libkolourpaint_lgpl.so*
%{_libdir}/libksane.so*
%{_libdir}/libokularcore.so*
%{_libdir}/strigi/strigita_dvi.so
%{_libdir}/pkgconfig/libkdcraw.pc
%{_libdir}/pkgconfig/libkipi.pc
%{_libdir}/pkgconfig/libksane.pc
%{_libdir}/pkgconfig/libkexiv2.pc
%{_datadir}/applications/kde4/*.desktop
%{_datadir}/apps/cmake/modules/*.cmake
%dir %{_datadir}/apps/gvpart
%{_datadir}/apps/gvpart/gvpart.rc
%dir %{_datadir}/apps/gwenview
%{_datadir}/apps/gwenview/gwenviewui.rc
%dir %{_datadir}/apps/gwenview/cursors
%{_datadir}/apps/gwenview/cursors/zoom.png
%dir %{_datadir}/apps/gwenview/fullscreenthemes
%dir %{_datadir}/apps/gwenview/fullscreenthemes/blackglass
%{_datadir}/apps/gwenview/fullscreenthemes/blackglass/*.*
%dir %{_datadir}/apps/kgamma
%dir %{_datadir}/apps/kgamma/pics
%{_datadir}/apps/kgamma/pics/*.png
%dir %{_datadir}/apps/kipi
%dir %{_datadir}/apps/kipi/data
%{_datadir}/apps/kipi/data/kipi-plugins_logo.png
%dir %{_datadir}/apps/kolourpaint
%{_datadir}/apps/kolourpaint/kolourpaintui.rc
%dir %{_datadir}/apps/kolourpaint/icons
%dir %{_datadir}/apps/kolourpaint/icons/hicolor
%dir %{_datadir}/apps/kolourpaint/icons/hicolor/48x48
%dir %{_datadir}/apps/kolourpaint/icons/hicolor/48x48/actions
%dir %{_datadir}/apps/kolourpaint/icons/hicolor/22x22
%dir %{_datadir}/apps/kolourpaint/icons/hicolor/22x22/actions
%dir %{_datadir}/apps/kolourpaint/icons/hicolor/16x16
%dir %{_datadir}/apps/kolourpaint/icons/hicolor/16x16/actions
%dir %{_datadir}/apps/kolourpaint/icons/hicolor/32x32
%dir %{_datadir}/apps/kolourpaint/icons/hicolor/32x32/actions
%dir %{_datadir}/apps/kolourpaint/icons/hicolor/scalable
%dir %{_datadir}/apps/kolourpaint/icons/hicolor/scalable/actions
%{_datadir}/apps/kolourpaint/icons/hicolor/*/*/*.*
%dir %{_datadir}/apps/kolourpaint/pics
%{_datadir}/apps/kolourpaint/pics/*.png
%dir %{_datadir}/apps/kruler
%{_datadir}/apps/kruler/kruler.notifyrc
%dir %{_datadir}/apps/kruler/pics
%{_datadir}/apps/kruler/pics/*.png
%dir %{_datadir}/apps/kruler/sounds
%{_datadir}/apps/kruler/sounds/move.wav
%dir %{_datadir}/apps/libkdcraw
%dir %{_datadir}/apps/libkdcraw/profiles
%{_datadir}/apps/libkdcraw/profiles/*.icm
%dir %{_datadir}/apps/okular
%{_datadir}/apps/okular/*.*
%dir %{_datadir}/apps/okular/pics
%{_datadir}/apps/okular/pics/*.*
%dir %{_datadir}/apps/svgpart
%{_datadir}/apps/svgpart/svgpart.rc
%{_datadir}/config.kcfg/okular.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.ksnapshot.xml
%{_datadir}/icons/*/*/*/*.*
%{_datadir}/kde4/services/*.desktop
%{_datadir}/kde4/services/ServiceMenus/slideshow.desktop
%{_datadir}/kde4/servicetypes/*.desktop
