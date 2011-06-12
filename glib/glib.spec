Name: glib
Version: 2.28.8
Release: 1.0
Summary: The low-level core library for projects such as GTK+ and Qt 4
URL: http://www.gtk.org
Group: Sytem Environment/Libraries
License: LGPL-2
Source: ftp://ftp.gtk.org/pub/glib/2.20/glib-%{version}.tar.bz2
BuildRequires: grep, sed, make >= 3.79.1, gcc
BuildRequires: gettext-tools, pkg-config >= 0.16
BuildRequires: eglibc-devel, kernel-headers
BuildRequires: attr-devel, zlib-devel, pcre-devel >= 8.11
BuildRequires: python >= 2.4, perl >= 5.002
BuildRequires(check): libxml2
Requires: libglib2.0 = %{version}-%{release}
Provides: glib2 = %{version}-%{release}
Obsoletes: glibc2 < %{version}-%{release}
Conflicts: glibc2 < %{version}-%{release}

%description
GLib is the low-level core library that forms the basis 
for projects such as GTK+ and GNOME. It provides data 
structure handling for C, portability wrappers, and interfaces 
for such runtime functionality as an event loop, threads, 
dynamic loading, and an object system.


%package devel
Summary: Development files for the GLib library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
GLib is a library containing many useful C routines for things such as trees,
hashes, lists, and strings. It is a useful general-purpose C library used by
projects such as GTK+, GIMP, and GNOME.
This package is needed to compile programs against libglib2.0, as only it
includes the header files and static libraries (optionally) needed for
compiling. 


%package -n libglib2.0
Summary: The GLib library of C routines
Group: System Environment/Libraries

%description -n libglib2.0
GLib is a library containing many useful C routines for things such as trees,
hashes, lists, and strings. It is a useful general-purpose C library used by
projects such as GTK+, GIMP, and GNOME.
This package contains the shared libraries. 


%package doc
Summary: Documentation files for the GLib library
Group: Documentation

%description doc
GLib is a library containing many useful C routines for things such as trees,
hashes, lists, and strings. It is a useful general-purpose C library used by
projects such as GTK+, GIMP, and GNOME.
This package contains the HTML documentation for the GLib library.


%prep
%setup -q


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
%{__make} install DESTDIR='%{buildroot}'
%{__rm} "%{buildroot}%{_infodir}/dir" ||:
%find_lang glib20

%{__mkdir_p} '%{buildroot}%{_localstatedir}/cache/gio-2.0' \
    '%{buildroot}%{_datadir}/applications'
%{__touch} '%{buildroot}%{_localstatedir}/cache/gio-2.0/defaults.list'
%{__ln_s} '%{_localstatedir}/cache/gio-2.0/defaults.list' \
    '%{buildroot}%{_datadir}/applications/defaults.list'
%{__touch} '%{buildroot}%{_libdir}/gio/modules/giomodule.cache'
%{__touch} '%{buildroot}%{_datadir}/glib-2.0/schemas/gschemas.compiled'


%check
%{__make} -k check ||:


%post -n libglib2.0 -p %{__ldconfig}
%postun -n libglib2.0 -p %{__ldconfig}


%files -f glib20.lang
%defattr(-, root, root)
%{_sysconfdir}/bash_completion.d/gdbus-bash-completion.sh
%{_sysconfdir}/bash_completion.d/gsettings-bash-completion.sh

%{_bindir}/gdbus
%{_bindir}/gio-querymodules*
%{_bindir}/glib-compile-schemas
%{_bindir}/gsettings

%doc %{_mandir}/man1/gdbus.1*
%doc %{_mandir}/man1/gio-querymodules.1*
%doc %{_mandir}/man1/glib-compile-schemas.1*
%doc %{_mandir}/man1/gsettings.1*


%files doc
%defattr(-, root, root)
%doc AUTHORS* COPYING* ChangeLog* NEWS* README*
%doc docs/*.txt docs/reference
#%doc %{_datadir}/gtk-doc/html/*


%files -n libglib2.0
%defattr(-, root, root)
%doc AUTHORS* COPYING* ChangeLog* NEWS* README*
%{_libdir}/libglib-2.0.so.0*
%{_libdir}/libgmodule-2.0.so.0*
%{_libdir}/libgobject-2.0.so.0*
%{_libdir}/libgthread-2.0.so.0*
%{_libdir}/libgio-2.0.so.0*

%dir %{_libdir}/gio
%dir %{_libdir}/gio/modules
%ghost %{_libdir}/gio/modules/giomodule.cache
%dir %{_datadir}/glib-2.0/
%dir %{_datadir}/glib-2.0/schemas/
%ghost %{_datadir}/glib-2.0/schemas/gschemas.compiled
%{_datadir}/applications/defaults.list
%dir %{_localstatedir}/cache/gio-2.0
%ghost %{_localstatedir}/cache/gio-2.0/defaults.list


%files devel
%defattr(-, root, root)
%doc AUTHORS* COPYING* ChangeLog* NEWS* README*
%{_bindir}/glib-genmarshal
%{_bindir}/glib-gettextize
%{_bindir}/glib-mkenums
%{_bindir}/gobject-query
%{_bindir}/gtester
%{_bindir}/gtester-report

%doc %{_mandir}/man1/glib-genmarshal.1*
%doc %{_mandir}/man1/glib-gettextize.1*
%doc %{_mandir}/man1/glib-mkenums.1*
%doc %{_mandir}/man1/gobject-query.1*
%doc %{_mandir}/man1/gtester.1*
%doc %{_mandir}/man1/gtester-report.1*
%dir %{_datadir}/glib-2.0/

%doc %{_datadir}/gtk-doc/html/gio
%doc %{_datadir}/gtk-doc/html/glib
%doc %{_datadir}/gtk-doc/html/gobject

%{_datadir}/glib-2.0/gdb/
%{_datadir}/glib-2.0/gettext/
%{_datadir}/glib-2.0/schemas/gschema.dtd

%{_includedir}/glib-2.0
%{_includedir}/gio-unix-2.0

%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/glib-2.0/include/

%{_libdir}/pkgconfig/glib-2.0.pc
%{_libdir}/pkgconfig/gmodule-2.0.pc
%{_libdir}/pkgconfig/gmodule-export-2.0.pc
%{_libdir}/pkgconfig/gmodule-no-export-2.0.pc
%{_libdir}/pkgconfig/gobject-2.0.pc
%{_libdir}/pkgconfig/gthread-2.0.pc
%{_libdir}/pkgconfig/gio-2.0.pc
%{_libdir}/pkgconfig/gio-unix-2.0.pc

%{_datadir}/aclocal/glib-2.0.m4
%{_datadir}/aclocal/glib-gettext.m4
%{_datadir}/aclocal/gsettings.m4

%{_datadir}/gdb/auto-load/%{_libdir}/*-gdb.py
