Name: graphviz
Version: 2.26.3
Release: 2.0ev
Summary: Graph drawing utilities with web and graphical interfaces
URL: http://www.graphviz.org/
Group: Development/Tools
License: CPL-1.0
Source: http://www.graphviz.org/pub/graphviz/stable/SOURCES/graphviz-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, grep, sed, pkg-config >= 0.20, flex, bison
BuildRequires: gcc, gcc-g++
BuildRequires: cairo >= 1.1.10, expat >= 2.0, libX11, zlib
BuildRequires: ghostscript >= 8.52, freetype >= 2.0, fontconfig, gtk2 >= 2.7.0
BuildRequires: libpng, libjpeg, librsvg

%description
graphviz is a set of graph drawing tools and libraries. It supports
hierarchical and mass-spring drawings; although the tools are scalable, their
emphasis is on making very good drawings of reasonably-sized graphs. Package
components include batch layout filters and interactive editors for X11, Java,
and a TCL/tk extension. The batch filters can be configured as a web
visualization service (using GIF and click-maps). Typical applications include
display of finite state machines, software diagrams, database schemas, and
communication networks.


%package devel
Summary: Graphviz development headers
Group: Development/Libraries
Requires: pkg-config

%description devel
This package contains include files and pkg-config information intended for
compiling applications that will ultimately link with Graphviz.


%prep
%setup -q


%build
%configure \
	--disable-sharp \
	--disable-guile \
	--disable-java \
	--disable-lua \
	--disable-php \
	--disable-r \
	--disable-tcl
%{__make} %{?_smp_mflag}


%install
%{__make} install DESTDIR='%{buildroot}'


%post
%{__ldconfig}


%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/diffimg
%{_bindir}/gml2gv
%{_bindir}/gv2gxl
%{_bindir}/gvgen
%{_bindir}/gxl2gv
%{_bindir}/mm2gv
%{_bindir}/osage
%{_bindir}/sfdp
%{_bindir}/vimdot
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
%{_libdir}/libcdt.so*
%{_libdir}/libgraph.so*
%{_libdir}/libcgraph.so*
%{_libdir}/libpathplan.so*
%{_libdir}/libxdot.so*
%{_libdir}/libgvc.so*
%{_libdir}/libgvpr.so*
%dir %{_libdir}/graphviz
%{_libdir}/graphviz/libgvplugin_core.so*
%{_libdir}/graphviz/libgvplugin_gd.so*
%{_libdir}/graphviz/libgvplugin_gdk_pixbuf.so*
%{_libdir}/graphviz/libgvplugin_gs.so*
%{_libdir}/graphviz/libgvplugin_gtk.so*
%{_libdir}/graphviz/libgvplugin_pango.so*
%{_libdir}/graphviz/libgvplugin_rsvg.so*
%{_libdir}/graphviz/libgvplugin_xlib.so*
%{_libdir}/graphviz/libgvplugin_dot_layout.so*
%{_libdir}/graphviz/libgvplugin_neato_layout.so*
%doc %{_mandir}/man1/dot.1*
%doc %{_mandir}/man1/osage.1*
%doc %{_mandir}/man1/neato.1*
%doc %{_mandir}/man1/twopi.1*
%doc %{_mandir}/man1/fdp.1*
%doc %{_mandir}/man1/circo.1*
%doc %{_mandir}/man1/sfdp.1*
%doc %{_mandir}/man1/gc.1*
%doc %{_mandir}/man1/gvcolor.1*
%doc %{_mandir}/man1/gxl2gv.1*
%doc %{_mandir}/man1/acyclic.1*
%doc %{_mandir}/man1/nop.1*
%doc %{_mandir}/man1/ccomps.1*
%doc %{_mandir}/man1/sccmap.1*
%doc %{_mandir}/man1/tred.1*
%doc %{_mandir}/man1/unflatten.1*
%doc %{_mandir}/man1/gvpack.1*
%doc %{_mandir}/man1/dijkstra.1*
%doc %{_mandir}/man1/bcomps.1*
%doc %{_mandir}/man1/mm2gv.1*
%doc %{_mandir}/man1/gvgen.1*
%doc %{_mandir}/man1/gml2gv.1*
%doc %{_mandir}/man1/gv2gxl.1*
%doc %{_mandir}/man1/gvpr.1*
%doc %{_mandir}/man1/lefty.1*
%doc %{_mandir}/man1/lneato.1*
%doc %{_mandir}/man1/dotty.1*
%doc %{_mandir}/man1/smyrna.1*
%doc %{_mandir}/man1/prune.1*
%doc %{_mandir}/man7/graphviz.7*
%dir %{_datadir}/graphviz
%doc %{_datadir}/graphviz/doc
%{_datadir}/graphviz/graphs
%{_datadir}/graphviz/lefty


%files devel
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%doc %{_mandir}/man3/cdt.3*
%doc %{_mandir}/man3/graph.3*
%doc %{_mandir}/man3/cgraph.3*
%doc %{_mandir}/man3/pathplan.3*
%doc %{_mandir}/man3/xdot.3*
%doc %{_mandir}/man3/gvc.3*
%dir %{_includedir}/graphviz
%{_includedir}/graphviz/*.h
%{_includedir}/graphviz/gv.i
%{_includedir}/graphviz/gv.cpp
%{_libdir}/libcdt.la
%{_libdir}/libgraph.la
%{_libdir}/libcgraph.la
%{_libdir}/libpathplan.la
%{_libdir}/libxdot.la
%{_libdir}/libgvc.la
%{_libdir}/libgvpr.la
%{_libdir}/graphviz/libgvplugin_core.la
%{_libdir}/graphviz/libgvplugin_gd.la
%{_libdir}/graphviz/libgvplugin_gdk_pixbuf.la
%{_libdir}/graphviz/libgvplugin_gs.la
%{_libdir}/graphviz/libgvplugin_gtk.la
%{_libdir}/graphviz/libgvplugin_pango.la
%{_libdir}/graphviz/libgvplugin_rsvg.la
%{_libdir}/graphviz/libgvplugin_xlib.la
%{_libdir}/graphviz/libgvplugin_dot_layout.la
%{_libdir}/graphviz/libgvplugin_neato_layout.la
%{_libdir}/pkgconfig/libcdt.pc
%{_libdir}/pkgconfig/libcgraph.pc
%{_libdir}/pkgconfig/libgraph.pc
%{_libdir}/pkgconfig/libgvc.pc
%{_libdir}/pkgconfig/libgvpr.pc
%{_libdir}/pkgconfig/libpathplan.pc
%{_libdir}/pkgconfig/libxdot.pc
