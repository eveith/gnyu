Name: gimp
Version: 2.2.13
Release: 1ev
Summary: The GNU Image Manipulation Program
URL: http://www.gimp.org/
Group: Applications/Productivity
License: GPL
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: ftp://ftp.gimp.org/pub/gimp/v2.2/gimp-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc-core, perl >= 5.8, python >= 2.2.0
BuildRequires: librsvg >= 2.2, libwmf >= 0.2.8, libjpeg >= 6b, libpng >= 1.2.5
BuildRequires: libtiff >= 3.5.7, libmng >= 1.0.5, libexif >= 0.5.12
BuildRequires: gtk2 >= 2.4.4, glib2 >= 2.4.5, pango >= 1.4.0, libart >= 2.0
BuildRequires: atk >= 1.6.1, freetype >= 2.1.7, fontconfig >= 2.2.2
Requires: make >= 3.79.1, gcc-core, perl >= 5.8, python >= 2.2.0
Requires: librsvg >= 2.2, libwmf >= 0.2.8, libjpeg >= 6b, libpng >= 1.2.5
Requires: libtiff >= 3.5.7, libmng >= 1.0.5, libexif >= 0.5.12
Requires: gtk2 >= 2.4.4, glib2 >= 2.4.5, pango >= 1.4.0, libart >= 2.0
Requires: atk >= 1.6.1, freetype >= 2.1.7, fontconfig >= 2.2.2
Provides: libtool(%{_libdir}/gimp/2.0/modules/libcolorsel_cmyk.la)
Provides: libtool(%{_libdir}/gimp/2.0/modules/libcolorsel_triangle.la)
Provides: libtool(%{_libdir}/gimp/2.0/modules/libcolorsel_water.la)
Provides: libtool(%{_libdir}/gimp/2.0/modules/libcdisplay_colorblind.la)
Provides: libtool(%{_libdir}/gimp/2.0/modules/libcdisplay_gamma.la)
Provides: libtool(%{_libdir}/gimp/2.0/modules/libcdisplay_highcontrast.la)
Provides: libtool(%{_libdir}/gimp/2.0/modules/libcdisplay_proof.la)
Provides: libtool(%{_libdir}/gimp/2.0/modules/libcontroller_midi.la)
Provides: libtool(%{_libdir}/gimp/2.0/modules/libcontroller_linux_input.la)
Provides: libtool(%{_libdir}/gimp/2.0/python/gimpmodule.la)
Provides: libtool(%{_libdir}/gimp/2.0/python/gimpprocbrowsermodule.la)
Provides: libtool(%{_libdir}/libgimpbase-2.0.la)
Provides: libtool(%{_libdir}/libgimpcolor-2.0.la)
Provides: libtool(%{_libdir}/libgimpmath-2.0.la)
Provides: libtool(%{_libdir}/libgimpmodule-2.0.la)
Provides: libtool(%{_libdir}/libgimpthumb-2.0.la)
Provides: libtool(%{_libdir}/libgimpwidgets-2.0.la)
Provides: libtool(%{_libdir}/libgimp-2.0.la)
Provides: libtool(%{_libdir}/libgimpui-2.0.la)

%description
GIMP is an acronym for GNU Image Manipulation Program. It is a freely
distributed program for such tasks as photo retouching, image composition and
image authoring.


%prep
%setup -q


%build
%configure \
	--disable-debug --disable-warnings \
	--enable-mmx --enable-sse \
	--disable-gimpprinttest --disable-print \
	--enable-python
make


%install
make install DESTDIR="$RPM_BUILD_ROOT"
rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir

find "${RPM_BUILD_ROOT}" -name "*.mo" -print | \
	sed "s,${RPM_BUILD_ROOT},," >> gimp.lang

# Correct env path in python scripts

ENV=$(which env)
find "${RPM_BUILD_ROOT}" -name "*.py" \
	-exec sed -i "s,^#!.*python,#!${ENV} python," {} \;


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
rm -rf ${RPM_BUILD_ROOT}
rm -vf gimp.lang


%files -f gimp.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog* HACKING LICENSE NEWS* README*
%doc %{_datadir}/gtk-doc/html/libgimpbase/
%doc %{_datadir}/gtk-doc/html/libgimpcolor/
%doc %{_datadir}/gtk-doc/html/libgimpmath/
%doc %{_datadir}/gtk-doc/html/libgimpmodule/
%doc %{_datadir}/gtk-doc/html/libgimpthumb/
%doc %{_datadir}/gtk-doc/html/libgimpwidgets/
%doc %{_datadir}/gtk-doc/html/libgimp/
%{_datadir}/aclocal/gimp-2.0.m4
%{_datadir}/gimp/
%{_mandir}/man1/gimp-2.2.1*
%{_mandir}/man1/gimp-remote-2.2.1*
%{_mandir}/man1/gimptool-2.0.1*
%{_mandir}/man1/gimp.1*
%{_mandir}/man1/gimp-remote.1*
%{_mandir}/man5/gimprc-2.2.5*
%{_mandir}/man5/gimprc.5*
%{_bindir}/gimp-remote-2.2
%{_bindir}/gimp-remote
%{_bindir}/gimp-2.2
%{_bindir}/gimp
%{_bindir}/gimptool-2.0
%{_libdir}/gimp/
%{_libdir}/libgimp*.*
%{_libdir}/pkgconfig/gimp-2.0.pc
%{_libdir}/pkgconfig/gimpthumb-2.0.pc
%{_libdir}/pkgconfig/gimpui-2.0.pc
%{_includedir}/gimp-2.0/
%dir /etc/gimp
%dir /etc/gimp/2.0
%config /etc/gimp/2.0/*rc
