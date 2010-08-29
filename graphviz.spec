Name: graphviz
Version: 2.12
Release: 1ev
Summary: Graph drawing utilities with web and graphical interfaces
URL: http://www.graphviz.org/
Group: Development/Tools
License: CPL
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: http://www.graphviz.org/pub/graphviz/ARCHIVE/graphviz-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, cairo, expat, fontconfig, freetype, gettext
BuildRequires: glib2, libpng, pango, gcc-core, gcc-g++, libtool, m4, swig
BuildRequires: ghostscript
Requires: cairo, expat, fontconfig, freetype, gettext, glib2, libpng, pango
Requires: ghostscript
Provides: libtool(%{_libdir}/graphviz/libgvplugin_core.la)
Provides: libtool(%{_libdir}/graphviz/libgvplugin_gd.la)
Provides: libtool(%{_libdir}/graphviz/libgvplugin_neato_layout.la)
Provides: libtool(%{_libdir}/graphviz/libgvplugin_pango.la)
Provides: libtool(%{_libdir}/graphviz/libgvplugin_xlib.la)
Provides: libtool(%{_libdir}/libagraph.la) libtool(%{_libdir}/libcdt.la)
Provides: libtool(%{_libdir}/libexpr.la) libtool(%{_libdir}/libgraph.la)
Provides: libtool(%{_libdir}/libgvc.la) libtool(%{_libdir}/libgvc_builtins.la)
Provides: libtool(%{_libdir}/libpathplan.la)

%description
graphviz is a set of graph drawing tools and libraries. It supports
hierarchical and mass-spring drawings; although the tools are scalable, their
emphasis is on making very good drawings of reasonably-sized graphs. Package
components include batch layout filters and interactive editors for X11, Java,
and a TCL/tk extension. The batch filters can be configured as a web
visualization service (using GIF and click-maps). Typical applications include
display of finite state machines, software diagrams, database schemas, and
communication networks.


%prep
%setup -q


%build
%configure --with-mylibgd --without-gtk
make


%install
make install DESTDIR="$RPM_BUILD_ROOT"
[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
	&& rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README doc/
%{_bindir}/acyclic
%{_bindir}/bcomps
%{_bindir}/ccomps
%{_bindir}/circo
%{_bindir}/dijkstra
%{_bindir}/dot
%{_bindir}/dot2gxl
%{_bindir}/dotty
%{_bindir}/fdp
%{_bindir}/gc
%{_bindir}/gvcolor
%{_bindir}/gvpack
%{_bindir}/gvpr
%{_bindir}/gxl2dot
%{_bindir}/lefty
%{_bindir}/lneato
%{_bindir}/neato
%{_bindir}/nop
%{_bindir}/prune
%{_bindir}/sccmap
%{_bindir}/tred
%{_bindir}/twopi
%{_bindir}/unflatten
%{_includedir}/graphviz/
%{_libdir}/graphviz/
%{_libdir}/libagraph.*
%{_libdir}/libcdt.*
%{_libdir}/libexpr.*
%{_libdir}/libgraph.*
%{_libdir}/libgvc.*
%{_libdir}/libgvc_builtins.*
%{_libdir}/libpathplan.*
%{_libdir}/pkgconfig/libagraph.pc
%{_libdir}/pkgconfig/libcdt.pc
%{_libdir}/pkgconfig/libexpr.pc
%{_libdir}/pkgconfig/libgraph.pc
%{_libdir}/pkgconfig/libgvc.pc
%{_libdir}/pkgconfig/libgvc_builtins.pc
%{_libdir}/pkgconfig/libpathplan.pc
%{_mandir}/man1/acyclic.1.gz
%{_mandir}/man1/bcomps.1.gz
%{_mandir}/man1/ccomps.1.gz
%{_mandir}/man1/circo.1.gz
%{_mandir}/man1/dijkstra.1.gz
%{_mandir}/man1/dot.1.gz
%{_mandir}/man1/dot2gxl.1.gz
%{_mandir}/man1/dotty.1.gz
%{_mandir}/man1/fdp.1.gz
%{_mandir}/man1/gc.1.gz
%{_mandir}/man1/gvcolor.1.gz
%{_mandir}/man1/gvpack.1.gz
%{_mandir}/man1/gvpr.1.gz
%{_mandir}/man1/gxl2dot.1.gz
%{_mandir}/man1/lefty.1.gz
%{_mandir}/man1/lneato.1.gz
%{_mandir}/man1/neato.1.gz
%{_mandir}/man1/nop.1.gz
%{_mandir}/man1/prune.1.gz
%{_mandir}/man1/sccmap.1.gz
%{_mandir}/man1/tred.1.gz
%{_mandir}/man1/twopi.1.gz
%{_mandir}/man1/unflatten.1.gz
%{_mandir}/man3/agraph.3.gz
%{_mandir}/man3/cdt.3.gz
%{_mandir}/man3/expr.3.gz
%{_mandir}/man3/graph.3.gz
%{_mandir}/man3/gvc.3.gz
%{_mandir}/man3/pathplan.3.gz
%{_datadir}/graphviz/
