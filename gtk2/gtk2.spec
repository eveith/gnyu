Name: gtk2
Version: 2.16.2
Release: 6ev
Summary: The GIMP Toolkit
URL: http://www.gtk.org/
Group: System Environment/Libraries
License: LGPL-2.1
Vendor: GNyU-Linux
Source: ftp://ftp.gtk.org/pub/gtk/v2.12/gtk+-%{version}.tar.bz2
Patch: %{name}-clipboard-check-display.patch
BuildRequires: make >= 3.79.1, gcc, pkg-config >= 0.9.0, gettext
BuildRequires: glib2 >= 2.13.5, pango >= 1.20, atk >= 1.13.0, cairo >= 1.6
BuildRequires: libjpeg, libpng, libtiff >= 3.6.0
BuildRequires: cups
BuildRequires: libX11, libXrender, libXext, libXi, libXrandr, libXcursor,
BuildRequires: libXfixes, libXcomposite, libXdamage

%description
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects ranging from
small one-off projects to complete application suites.


%prep
	%setup -q -n 'gtk+-%{version}'


%build
%configure \
	--enable-shm \
	--enable-xkb \
	--disable-xinerama \
	--with-xinput \
	--enable-man \
	--without-libjasper
	%{__make} %{?_smp_mflags} \
		GTK_PRINT_PREVIEW_COMMAND='okular'


%install
	%{__make} install DESTDIR='%{buildroot}'
	%find_lang gtk20
	%find_lang gtk20-properties
	%{__cat} gtk20-properties.lang >> gtk20.lang
	%{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
	%{__ldconfig}


%postun
	%{__ldconfig}


%files -f gtk20.lang
	%defattr(-, root, root)
	%doc AUTHORS COPYING ChangeLog* README* HACKING NEWS*
	%doc %{_datadir}/gtk-doc/html/gail-libgail-util
	%doc %{_datadir}/gtk-doc/html/gdk-pixbuf
	%doc %{_datadir}/gtk-doc/html/gdk 
	%doc %{_datadir}/gtk-doc/html/gtk
	%dir %{_datadir}/gtk-doc
	%dir %{_datadir}/gtk-doc/html
	%dir %{_sysconfdir}/gtk-2.0
	%config %{_sysconfdir}/gtk-2.0/im-multipress.conf
	%{_datadir}/themes
	%{_datadir}/gtk-2.0
	%{_includedir}/gail-1.0/
	%{_includedir}/gtk-2.0/
	%{_includedir}/gtk-unix-print-2.0/
	%{_libdir}/gtk-2.0/
	%{_libdir}/libgailutil.*
	%{_libdir}/libgdk-x11-2.0.*
	%{_libdir}/libgdk_pixbuf-2.0.*
	%{_libdir}/libgdk_pixbuf_xlib-2.0.*
	%{_libdir}/libgtk-x11-2.0.*
	%{_libdir}/pkgconfig/gail.pc
	%{_libdir}/pkgconfig/gdk-2.0.pc
	%{_libdir}/pkgconfig/gdk-pixbuf-2.0.pc
	%{_libdir}/pkgconfig/gdk-pixbuf-xlib-2.0.pc
	%{_libdir}/pkgconfig/gdk-x11-2.0.pc
	%{_libdir}/pkgconfig/gtk+-2.0.pc
	%{_libdir}/pkgconfig/gtk+-unix-print-2.0.pc
	%{_libdir}/pkgconfig/gtk+-x11-2.0.pc
	%{_datadir}/aclocal/gtk-2.0.m4
	%{_bindir}/gdk-pixbuf-csource
	%{_bindir}/gdk-pixbuf-query-loaders
	%{_bindir}/gtk-demo
	%{_bindir}/gtk-query-immodules-2.0
	%{_bindir}/gtk-update-icon-cache
	%{_bindir}/gtk-builder-convert
