Name: imagemagick
Version: 6.5.5
Release: 1ev
Summary: A suite of tools to process, convert and edit bitmap images
URL: http://www.imagemagick.org
Group: Applications/Imaging
License: ImageMagick
Vendor: GNyU-Linux
Source: ftp://ftp.imagemagick.org/pub/ImageMagick/ImageMagick-%{version}-9.tar.bz2
BuildRequires: pkg-config >= 0.9.0, make, gcc, gcc-g++, perl, gettext
BuildRequireS: libstdc++, bzip2, zlib, libX11, libXext, libXt
BuildRequires: fontconfig >= 2.1.0, freetype, ghostscript
BuildRequires: libjpeg, libpng, lcms, openexr >= 1.0.6, librsvg >= 2.9.0
BuildRequires: libtiff, libwmf, libxml2

%description
ImageMagick® is a software suite to create, edit, and compose bitmap images.
It can read, convert and write images in a variety of formats (over 100)
including DPX, EXR, GIF, JPEG, JPEG-2000, PDF, PhotoCD, PNG, Postscript, SVG,
and TIFF. Use ImageMagick to translate, flip, mirror, rotate, scale, shear and
transform images, adjust image colors, apply various special effects, or draw
text, lines, polygons, ellipses and Bézier curves.

%prep
	%setup -q -n 'ImageMagick-%{version}-9'


%build
	%configure
	%{__make} %{?_smp_mflags}


%install
	%{__make} install DESTDIR='%{buildroot}'
	%{__rm} -f '%{buildroot}/%{perl_archlib}/perllocal.pod'

	[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
		&& %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
	%{__ldconfig}


%postun
	%{__ldconfig}


%files
	%defattr(-, root, root)
	%doc 
	%{_bindir}/Magick++-config
	%{_bindir}/Magick-config
	%{_bindir}/MagickCore-config
	%{_bindir}/MagickWand-config
	%{_bindir}/Wand-config
	%{_bindir}/animate
	%{_bindir}/compare
	%{_bindir}/composite
	%{_bindir}/conjure
	%{_bindir}/convert
	%{_bindir}/display
	%{_bindir}/identify
	%{_bindir}/import
	%{_bindir}/mogrify
	%{_bindir}/montage
	%{_bindir}/stream
	%dir %{_includedir}/ImageMagick
	%dir %{_includedir}/ImageMagick/Magick++
	%dir %{_includedir}/ImageMagick/magick
	%dir %{_includedir}/ImageMagick/wand
	%{_includedir}/ImageMagick/Magick++.h
	%{_includedir}/ImageMagick/*/*.h
	%doc %{_mandir}/man1/ImageMagick.1*
	%dir %{_libdir}/ImageMagick-6.?.?
	%dir %{_libdir}/ImageMagick-6.?.?/config
	%{_libdir}/ImageMagick-6.?.?/config/*.xml
	%dir %{_libdir}/ImageMagick-6.?.?/modules-Q16
	%dir %{_libdir}/ImageMagick-6.?.?/modules-Q16/coders
	%dir %{_libdir}/ImageMagick-6.?.?/modules-Q16/filters
	%{_libdir}/ImageMagick-6.?.?/modules-Q16/*/*.*
	%{_libdir}/libMagick++.*
	%{_libdir}/libMagickCore.*
	%{_libdir}/libMagickWand.*
	%{_libdir}/pkgconfig/ImageMagick++.pc
	%{_libdir}/pkgconfig/ImageMagick.pc
	%{_libdir}/pkgconfig/Magick++.pc
	%{_libdir}/pkgconfig/MagickCore.pc
	%{_libdir}/pkgconfig/MagickWand.pc
	%{_libdir}/pkgconfig/Wand.pc
	%dir %{perl_sitearch}/Image
	%{perl_sitearch}/Image/Magick.pm
	%dir %{perl_sitearch}/auto/Image
	%dir %{perl_sitearch}/auto/Image/Magick
	%{perl_sitearch}/auto/Image/Magick/.packlist
	%{perl_sitearch}/auto/Image/Magick/Magick.[bs][so]
	%{perl_sitearch}/auto/Image/Magick/autosplit.ix
	%doc %{_mandir}/man1/Magick++-config.1*
	%doc %{_mandir}/man1/Magick-config.1*
	%doc %{_mandir}/man1/MagickCore-config.1*
	%doc %{_mandir}/man1/MagickWand-config.1*
	%doc %{_mandir}/man1/Wand-config.1*
	%doc %{_mandir}/man1/animate.1*
	%doc %{_mandir}/man1/compare.1*
	%doc %{_mandir}/man1/composite.1*
	%doc %{_mandir}/man1/conjure.1*
	%doc %{_mandir}/man1/convert.1*
	%doc %{_mandir}/man1/display.1*
	%doc %{_mandir}/man1/identify.1*
	%doc %{_mandir}/man1/import.1*
	%doc %{_mandir}/man1/mogrify.1*
	%doc %{_mandir}/man1/montage.1*
	%doc %{_mandir}/man1/stream.1*
	%doc %{_mandir}/man3/Image::Magick.3pm
	%dir %{_datadir}/ImageMagick-%{version}
	%{_datadir}/ImageMagick-%{version}/ChangeLog
	%{_datadir}/ImageMagick-%{version}/LICENSE
	%{_datadir}/ImageMagick-%{version}/NEWS.txt
	%dir %{_datadir}/ImageMagick-%{version}/config
	%{_datadir}/ImageMagick-%{version}/config/*.*
	%dir %{_datadir}/doc/ImageMagick-%{version}
	%doc %{_datadir}/doc/ImageMagick-%{version}/*
