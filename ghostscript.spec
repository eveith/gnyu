Name: ghostscript
Version: 8.62
Release: 1ev
Summary: A postscript and PDF interpreter
URL: http://www.ghostscript.com/
Group: Applications/Publishing
License: GPL-2
Vendor: GNyU-Linux
Source: ftp://mirror.cs.wisc.edu/pub/mirrors/ghost/GPL/gs862/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, fontconfig, libpng, libjpeg, zlib, cups-libs
BuildRequires: coreutils, gawk, perl, libstdc++, pkg-config
BuildRequires: gtk2, libX11, libSM, libICE, libXext, libXt
Requires: gnu-gs-fonts
Obsoletes: espgs

%description
Ghostscript is a package of software that provides: 
· An interpreter for the PostScript (TM) language, with the ability to 
  convert PostScript language files to many raster formats, view them on 
  displays, and print them on printers that don't have PostScript language 
  capability built in; 
· An interpreter for Portable Document Format (PDF) files, with the same 
  abilities; 
· The ability to convert PostScript language files to PDF (with some 
  limitations) and vice versa; and 
· A set of C procedures (the Ghostscript library) that implement the graphics 
  and filtering (data compression / decompression / conversion) capabilities 
  that appear as primitive operations in the PostScript language and in PDF.

%package gtk2
Summary: A GTK-enabled PostScript(TM) interpreter and renderer
Group: Applications/Publishing
Requires: %{name} = %{version}

%description gtk2
A GTK-enabled version of Ghostscript, called 'gsx'.


%prep
%setup -q
sh autogen.sh
for f in man/de/*.1
do
	iconv -f iso-8859-1 -t utf-8 < "${f}" > "${f}_"
	%{__mv} "${f}_" "${f}"
done


%build
%configure \
	--enable-dynamic \
	--with-ijs \
	--without-jasper \
	--with-drivers=ALL \
	--with-gtk \
	--with-omni \
	--with-x \
    --with-cups
%{__make} %{?_smp_mflags}

%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} soinstall DESTDIR='%{buildroot}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc LICENSE doc/*.htm doc/README doc/COPYING doc/*.css
%{_bindir}/bdftops
%{_bindir}/dumphint
%{_bindir}/dvipdf
%{_bindir}/eps2eps
%{_bindir}/fixmswrd.pl
%{_bindir}/font2c
%{_bindir}/gs
%{_bindir}/gsc
%{_bindir}/gsbj
%{_bindir}/gsdj
%{_bindir}/gsdj500
%{_bindir}/gslj
%{_bindir}/gslp
%{_bindir}/gsnd
%{_bindir}/lprsetup.sh
%{_bindir}/pdf2dsc
%{_bindir}/pdf2ps
%{_bindir}/pdfopt
%{_bindir}/pf2afm
%{_bindir}/pfbtopfa
%{_bindir}/printafm
%{_bindir}/ps2ascii
%{_bindir}/ps2epsi
%{_bindir}/ps2pdf
%{_bindir}/ps2pdf12
%{_bindir}/ps2pdf13
%{_bindir}/ps2pdf14
%{_bindir}/ps2pdfwr
%{_bindir}/ps2ps
%{_bindir}/ps2ps2
%{_bindir}/pv.sh
%{_bindir}/unix-lpr.sh
%{_bindir}/wftopfa
%{_libdir}/libgs.so*
%{_includedir}/ghostscript/
%dir %{_libdir}/ghostscript
%dir %{_libdir}/ghostscript/%{version}
%dir %{_datadir}/ghostscript
%{_datadir}/ghostscript/%{version}/
%{_mandir}/man1/dvipdf.1*
%{_mandir}/man1/eps2eps.1*
%{_mandir}/man1/font2c.1*
%{_mandir}/man1/gs.1*
%{_mandir}/man1/gslp.1*
%{_mandir}/man1/gsnd.1*
%{_mandir}/man1/pdf2dsc.1*
%{_mandir}/man1/pdf2ps.1*
%{_mandir}/man1/pdfopt.1*
%{_mandir}/man1/pf2afm.1*
%{_mandir}/man1/pfbtopfa.1*
%{_mandir}/man1/printafm.1*
%{_mandir}/man1/ps2ascii.1*
%{_mandir}/man1/ps2epsi.1*
%{_mandir}/man1/ps2pdf.1*
%{_mandir}/man1/ps2pdf12.1*
%{_mandir}/man1/ps2pdf13.1*
%{_mandir}/man1/ps2pdfwr.1*
%{_mandir}/man1/ps2ps.1*
%{_mandir}/man1/wftopfa.1*
%{_mandir}/*/man1/dvipdf.1*
%{_mandir}/*/man1/eps2eps.1*
%{_mandir}/*/man1/font2c.1*
%{_mandir}/*/man1/gsnd.1*
%{_mandir}/*/man1/pdf2dsc.1*
%{_mandir}/*/man1/pdf2ps.1*
%{_mandir}/*/man1/pdfopt.1*
%{_mandir}/*/man1/printafm.1*
%{_mandir}/*/man1/ps2ascii.1*
%{_mandir}/*/man1/ps2pdf.1*
%{_mandir}/*/man1/ps2pdf12.1*
%{_mandir}/*/man1/ps2pdf13.1*
%{_mandir}/*/man1/ps2ps.1*
%{_mandir}/*/man1/wftopfa.1*
%{_sysconfdir}/cups/pstoraster.convs
%{_libdir}/cups/filter/pstopxl
%{_libdir}/cups/filter/pstoraster
%{_datadir}/cups/model/pxlcolor.ppd
%{_datadir}/cups/model/pxlmono.ppd

%files gtk2
%defattr(-, root, root)
%{_libdir}/ghostscript/%{version}/X11.so
%{_bindir}/gsx
