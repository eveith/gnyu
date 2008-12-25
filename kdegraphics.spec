Name: kdegraphics
Version: 3.5.10
Release: 2ev
Summary: A collection of graphic-oriented programs for the KDE suite
URL: http://www.kde.org/
Group: User Interface/Desktops
License: GPL-2, LGPL, BSD
Vendor: GNyU-Linux
Source: http://download.kde.org/stable/%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires: make, gcc-g++, qt3, kdelibs, kdebase, fontconfig, freetype
BuildRequires: zlib, libxml2 >= 2.4.8, libxslt >= 1.0.7, libstdc++, libart
BuildRequires: libICE, libX11, libSM, libXrender, libXrandr, libXext, expat
BuildRequires: openexr, libXft, libXt, libXcursor, libXau, libpng, libtiff
BuildRequires: libusb, libieee1284, libXmu

%description
* kamera
    Digital camera io_slave for Konqueror. Together gPhoto this allows you
    to access your camera's picture with the URL kamera:/
* kcoloredit
    Contains two programs: a color value editor and also a color picker.
* kdvi
    Program (and embeddable KPart) to display *.DVI files from TeX.
* kfax
    A program to display raw and tiffed fax images (g3, g3-2d, g4).
* kfaxview
    An embeddable KPart to display tiffed fax images.
* kfile-plugins
    Provide meta information for graphic files.
* kghostview
    Program (and embeddable KPart) to display *.pdf and *.ps
* kiconedit
    An icon editor.
* kmrml
    Connects to a MRML server and find similar images
* kooka
    A raster image scan program, based on SANE and libkscan.
* kolourpaint
    An easy-to-use paint program designed for everyday tasks like drawing
    simple diagrams/logos/icons and editing screenshots.
* kpovmodeler
    Program to enter scenes for the 3D rendering engine PovRay.
* kruler
    A ruler in inch, centimeter and pixel to check distances on the screen.
* ksnapshot
    Make snapshots of the screen contents.
* kuickshow
    Fast and comfortable imageviewer.
* kview
    Picture viewer, provided as standalone program and embeddable KPart.
* kviewshell
    Generic framework for viewer applications.
* libkscan
    Library to access scanners used by kooka (and koffice), needs SANE to be
    used


%prep
%setup -q


%build
%configure \
	--disable-debug \
	--disable-warnings
%{__make} %{?_smp_mflags}


%install
%{__make_install} DESTDIR='%{buildroot}'


%files
%defattr(-, root, root)
%doc AUTHORS COPYING* README
%doc %{_datadir}/doc/HTML/en/*
%{_bindir}/kcolorchooser
%{_bindir}/kcoloredit
%{_bindir}/kdvi
%{_bindir}/kfax
%{_bindir}/kfaxview
%{_bindir}/kghostview
%{_bindir}/kiconedit
%{_bindir}/kolourpaint
%{_bindir}/kooka
%{_bindir}/kpdf
%{_bindir}/kpovmodeler
%{_bindir}/kruler
%{_bindir}/ksnapshot
%{_bindir}/kuickshow
%{_bindir}/kview
%{_bindir}/kviewshell
%{_bindir}/mrmlsearch
%{_bindir}/printnodetest
%{_bindir}/svgdisplay
%{_bindir}/xf86gammacfg
%{_includedir}/*.h
%{_includedir}/dom/*.h
%{_includedir}/ksvg/
%{_includedir}/kviewshell/
%{_includedir}/libtext2path-0.1/
%{_libdir}/kde3/*.la
%{_libdir}/kde3/*.so
%{_libdir}/*.la
%{_libdir}/*.so*
%{_datadir}/applications/kde/*.desktop
%{_datadir}/applnk/Graphics/kruler.desktop
%{_datadir}/apps/djvumultipage.rc
%{_datadir}/apps/kcoloredit/
%{_datadir}/apps/kfax/
%{_datadir}/apps/kgamma/
%{_datadir}/apps/kghostview/
%{_datadir}/apps/kconf_update/kghostview.upd
%{_datadir}/apps/kconf_update/update-to-xt-names.pl
%{_datadir}/apps/kiconedit/
%{_datadir}/apps/konqueror/servicemenus/mrml-servicemenu.desktop
%{_datadir}/apps/kolourpaint/
%{_datadir}/apps/kpdf/
%{_datadir}/apps/kpdfpart/
%{_datadir}/apps/kpovmodeler/
%{_datadir}/apps/kruler/
%{_datadir}/apps/ksvg/
%{_datadir}/apps/kuickshow/
%{_datadir}/apps/kview/
%{_datadir}/apps/kviewviewer/
%{_datadir}/apps/photobook/
%{_datadir}/apps/kviewerpart/
%{_datadir}/apps/kviewshell/
%{_datadir}/apps/kfaxview/
%{_datadir}/apps/kdvi/
%{_datadir}/apps/kooka/
%{_datadir}/config.kcfg/*.kcfg
%{_datadir}/config/kookarc
%{_datadir}/icons/*/*/*/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svgz
%{_datadir}/mimelnk/text/mrml.desktop
%{_datadir}/services/*.desktop
%{_datadir}/services/kconfiguredialog/*.desktop
%{_datadir}/services/kded/daemonwatcher.desktop
%{_datadir}/services/mrml.protocol
%{_datadir}/servicetypes/*.desktop
