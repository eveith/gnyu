Name: gtk2
Version: 2.10.14
Release: 2ev
Summary: The GIMP Toolkit
URL: http://www.gtk.org/
Group: System Environment/Libraries
License: LGPL-2
Vendor: GNyU-Linux
Source: ftp://ftp.gtk.org/pub/gtk/v2.10/gtk+-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc, glib2 >= 2.12, libpng, libtiff, libjpeg
BuildRequires: pango >= 1.13, cairo >= 1.2, atk >= 1.9, pkg-config

%description
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects ranging from
small one-off projects to complete application suites.


%prep
%setup -q -n gtk+-%{version}


%build
%configure \
	--enable-shm \
	--enable-xkb \
	--with-xinput \
	--disable-rebuilds
%{__make} %{?_smp_mflags} \
	GTK_PRINT_PREVIEW_COMMAND='kpdf'


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%find_lang gtk20
%find_lang gtk20-properties
%{__cat} gtk20-properties.lang >> gtk20.lang
%{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files -f gtk20.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog* README* HACKING NEWS*
%doc %{_datadir}/gtk-doc/html/gdk-pixbuf
%doc %{_datadir}/gtk-doc/html/gdk 
%doc %{_datadir}/gtk-doc/html/gtk
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/themes
%{_datadir}/gtk-2.0
%{_includedir}/gtk-2.0/
%{_includedir}/gtk-unix-print-2.0/
%{_libdir}/gtk-2.0/
%{_libdir}/libgdk-x11-2.0.*
%{_libdir}/libgdk_pixbuf-2.0.*
%{_libdir}/libgdk_pixbuf_xlib-2.0.*
%{_libdir}/libgtk-x11-2.0.*
%{_libdir}/pkgconfig/gdk-2.0.pc
%{_libdir}/pkgconfig/gdk-pixbuf-2.0.pc
%{_libdir}/pkgconfig/gdk-pixbuf-xlib-2.0.pc
%{_libdir}/pkgconfig/gdk-x11-2.0.pc
%{_libdir}/pkgconfig/gtk+-2.0.pc
%{_libdir}/pkgconfig/gtk+-unix-print-2.0.pc
%{_libdir}/pkgconfig/gtk+-x11-2.0.pc
%{_mandir}/man1/gdk-pixbuf-csource.1.gz
%{_mandir}/man1/gdk-pixbuf-query-loaders.1*
%{_mandir}/man1/gtk-query-immodules-2.0.1*
%{_mandir}/man1/gtk-update-icon-cache.1*
%{_datadir}/aclocal/gtk-2.0.m4
%{_bindir}/gdk-pixbuf-csource
%{_bindir}/gdk-pixbuf-query-loaders
%{_bindir}/gtk-demo
%{_bindir}/gtk-query-immodules-2.0
%{_bindir}/gtk-update-icon-cache
