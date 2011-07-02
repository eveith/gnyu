Name: gobject-introspection
Version: 0.6.14
Release: 1.0
Summary: A library for describing APIs
URL: http://live.gnome.org/GObjectIntrospection
Group: System Environment/Libraries
License: LGPL-2.1
Source: http://ftp.gnome.org/pub/GNOME/sources/gobject-introspection/0.6/gobject-introspection-%{version}.tar.bz2
BuildRequires: grep, sed, make
BuildRequires: flex, bison, gcc
BuildRequires: pkg-config
BuildRequires: glib-devel >= 2.0, libffi-devel, python-devel, pcre-devel


%description
The goal of the project is to describe the APIs and collect them in
a uniform, machine readable format.


%files
%defattr(-,root,root)
%doc AUTHORS CONTRIBUTORS COPYING COPYING.GPL NEWS README TODO
#%{_bindir}/g-ir-annotation-tool
%{_bindir}/g-ir-compiler
%{_bindir}/g-ir-generate
%{_bindir}/g-ir-scanner

%doc %{_mandir}/man1/g-ir-compiler.1*
%doc %{_mandir}/man1/g-ir-generate.1*
%doc %{_mandir}/man1/g-ir-scanner.1*

%{_datadir}/aclocal/introspection.m4
%{_datadir}/gir-1.0/*.gir

%dir %{_libdir}/gobject-introspection
%{_libdir}/gobject-introspection/giscanner/

%dir %{_datadir}/gobject-introspection-1.0
%{_datadir}/gobject-introspection-1.0/Makefile.introspection
#%{_datadir}/gobject-introspection-1.0/tests/
#%{_datadir}/gobject-introspection-1.0/gdump.c


%package devel
Summary: GObject Introspection Development Files
Group: Development/Libraries
License: LGPL-2.1
Requires: %{name} = %{version}
Requires: libffi-devel
 

%description devel
The goal of the project is to describe the APIs and collect them in
a uniform, machine readable format.


%files devel
%defattr(-,root,root)
#%doc %{_datadir}/gtk-doc/html/gi/
%{_includedir}/gobject-introspection-1.0/

%{_libdir}/libgirepository-1.0.so
%{_libdir}/libgirepository-1.0.la
%{_libdir}/libgirepository-1.0.a

%{_libdir}/pkgconfig/gobject-introspection-1.0.pc
%{_libdir}/pkgconfig/gobject-introspection-no-export-1.0.pc


%package -n libgirepository-1_0-1
Summary: GObject Introspection Library
Group: Development/Libraries
License: LGPL-2.1

 
%description -n libgirepository-1_0-1
The goal of the project is to describe the APIs and collect them in
a uniform, machine readable format.


%files -n libgirepository-1_0-1
%defattr(-,root,root)
%doc COPYING.LGPL
%dir %{_datadir}/gir-1.0
%{_libdir}/libgirepository-1.0.so.*
%{_libdir}/girepository-1.0/


%post -n libgirepository-1_0-1 -p %{__ldconfig}
%postun -n libgirepository-1_0-1 -p %{__ldconfig}


%prep
%setup -q


%build
%configure \
    --disable-tests
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'
