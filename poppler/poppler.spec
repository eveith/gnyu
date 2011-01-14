Name: poppler
Version: 0.12.0
Release: 2ev
Summary: A PDF rendering library
URL: http://poppler.freedesktop.org
Group: System Environment/Libraries
License: GPL-2
Vendor: GNyU-Linux
Source: http://poppler.freedesktop.org/poppler-%{version}.tar.gz
BuildRequires: make, gcc-g++, pkg-config >= 0.9.0
Buildrequires: zlib, libjpeg, libpng, freetype >= 2.0, fontconfig >= 2.0.0
BuildRequires: cairo >= 1.8.4, glib2 >= 2.6
BuildRequires: gtk2 >= 2.12, qt4 >= 4.3.0, lcms
BuildRequires: poppler-data
Requires: poppler-data

%description
Poppler is a PDF rendering library based on the xpdf-3.0 code base. It is
used by various other frontends, such as KDE's Okular document viewer.


%package qt4
Summary: Qt4 bindings for the poppler PDF rendering library
Group: System Environment/Libraries

%description qt4
Poppler is a PDF rendering library based on the xpdf-3.0 code base. It is
used by various other frontends, such as KDE's Okular document viewer.
This is the interface library between the poppler routines and Qt4.


%prep
%setup -q


%build
%configure \
	--enable-zlib \
	--disable-poppler-qt \
	--enable-poppler-qt4 \
	--disable-abiword-output
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'


%post
%{__ldconfig}


%postun
%{__ldconfig}


%post qt4
%{__ldconfig}


%postun qt4
%{__ldconfig}


%files
%defattr(-, root, root)
%doc COPYING AUTHORS NEWS README* TODO ChangeLog
%{_bindir}/pdffonts                         
%{_bindir}/pdfimages                        
%{_bindir}/pdfinfo                          
%{_bindir}/pdftohtml                        
%{_bindir}/pdftoppm                         
%{_bindir}/pdftops                          
%{_bindir}/pdftotext
%dir %{_includedir}/poppler
%{_includedir}/poppler/glib/
%{_libdir}/libpoppler.*
%{_libdir}/libpoppler-glib.*
%{_libdir}/pkgconfig/poppler-cairo.pc
%{_libdir}/pkgconfig/poppler-glib.pc
%{_libdir}/pkgconfig/poppler-splash.pc
%{_libdir}/pkgconfig/poppler.pc
%doc %{_mandir}/man1/pdffonts.1*
%doc %{_mandir}/man1/pdfimages.1*
%doc %{_mandir}/man1/pdfinfo.1*
%doc %{_mandir}/man1/pdftohtml.1*
%doc %{_mandir}/man1/pdftoppm.1*
%doc %{_mandir}/man1/pdftops.1*
%doc %{_mandir}/man1/pdftotext.1*
%dir %{_datadir}/gtk-doc/html/poppler
%doc %{_datadir}/gtk-doc/html/poppler/*


%files qt4
%defattr(-, root, root)
%doc COPYING AUTHORS NEWS README* TODO ChangeLog
%{_includedir}/poppler/qt4/
%{_libdir}/libpoppler-qt4.*
%{_libdir}/pkgconfig/poppler-qt4.pc
