Name: glib2
Version: 2.20.0
Release: 4ev
Summary: The low-level core library for projects such as GTK+ and Qt 4
URL: http://www.gtk.org/
Group: Sytem Environment/Libraries
License: LGPL-2
Vendor: GNyU-Linux
Source: ftp://ftp.gtk.org/pub/glib/2.20/glib-%{version}.tar.bz2
BuildRequires: make >= 3.79.1, gcc, gettext, pkg-config, zlib
BuildRequires: pcre >= 7.2, python >= 2.4, perl
Requires: pkg-config

%description
GLib is the low-level core library that forms the basis 
for projects such as GTK+ and GNOME. It provides data 
structure handling for C, portability wrappers, and interfaces 
for such runtime functionality as an event loop, threads, 
dynamic loading, and an object system.


%prep
%setup -q -n 'glib-%{version}'


%build
%configure \
	--enable-debug=no \
	--enable-threads \
	--disable-selinux \
	--disable-fam \
	--enable-xattr \
	--enable-regex \
	--enable-man \
	--with-pcre=system
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR="${RPM_BUILD_ROOT}"
%{__rm} -vrf "${RPM_BUILD_ROOT}/%{_infodir}/dir" 
%find_lang glib20


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files -f glib20.lang
%defattr(-, root, root)
%doc AUTHORS* COPYING* ChangeLog* NEWS* README*
%doc docs/*.txt docs/reference/glib docs/reference/gobject
%doc %{_datadir}/gtk-doc/html/*
%{_bindir}/glib-genmarshal
%{_bindir}/glib-gettextize
%{_bindir}/glib-mkenums
%{_bindir}/gobject-query
%{_bindir}/gtester
%{_bindir}/gtester-report
%{_includedir}/glib-2.0/
%{_includedir}/gio-unix-2.0/
%{_libdir}/glib-2.0/
%{_libdir}/libglib-2.0.*
%{_libdir}/libgmodule-2.0.*
%{_libdir}/libgobject-2.0.*
%{_libdir}/libgthread-2.0.*
%{_libdir}/libgio-2.0.*
%{_libdir}/pkgconfig/glib-2.0.pc
%{_libdir}/pkgconfig/gmodule-2.0.pc
%{_libdir}/pkgconfig/gmodule-export-2.0.pc
%{_libdir}/pkgconfig/gmodule-no-export-2.0.pc
%{_libdir}/pkgconfig/gobject-2.0.pc
%{_libdir}/pkgconfig/gthread-2.0.pc
%{_libdir}/pkgconfig/gio-2.0.pc
%{_libdir}/pkgconfig/gio-unix-2.0.pc
%doc %{_mandir}/man1/glib-genmarshal.1*
%doc %{_mandir}/man1/glib-gettextize.1*
%doc %{_mandir}/man1/glib-mkenums.1*
%doc %{_mandir}/man1/gobject-query.1*
%doc %{_mandir}/man1/gtester.1*
%doc %{_mandir}/man1/gtester-report.1*
%{_datadir}/aclocal/glib-2.0.m4
%{_datadir}/aclocal/glib-gettext.m4
%{_datadir}/glib-2.0/
