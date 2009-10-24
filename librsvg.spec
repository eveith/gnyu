Name: librsvg
Version: 2.16.1
Release: 1ev
Summary: A SVG rendering library.
URL: http://librsvg.sourceforge.net/
Group: System Environment/Libraries
License: LGPL
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: http://ftp.gnome.org/pub/GNOME/sources/librsvg/2.16/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: gcc-core, make >= 3.79.1, libxml2, libart, libcroco, libgsf sed
Requires: libxml2, libart, libcroco, libgsf
Provides: libtool(%{_libdir}/gtk-2.0/2.10.0/engines/libsvg.la)
Provides: libtool(%{_libdir}/gtk-2.0/2.10.0/loaders/svg_loader.la)
Provides: libtool(%{_libdir}/librsvg-2.la)

%description
libRSVG is a very fast SVG rendering engine written in C. It currently support
most of the SVG 1.2 specification, except the animation part. libRSVG is used
in many projects for SVG rendering, most notably GNOME.


%prep
%setup -q


%build
%configure \
	--disable-gnome-vfs
make


%install
make install DESTDIR="$RPM_BUILD_ROOT"
rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir

# Insert correct env string

ENV=$(which env)
sed -i s,"^#!.*env python,#!${ENV} python," \
	${RPM_BUILD_ROOT}/%{_bindir}/rsvg


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-, root, root)
%doc AUTHORS COPYING* ChangeLog* MAINTAINERS NEWS README TODO 
%doc %{_datadir}/gtk-doc/html/rsvg
%{_bindir}/rsvg
%{_bindir}/rsvg-convert
%{_bindir}/rsvg-view
%{_includedir}/librsvg-2/
%{_libdir}/gtk-2.0/2.10.0/engines/libsvg.*
%{_libdir}/gtk-2.0/2.10.0/loaders/svg_loader.*
%{_libdir}/librsvg-2.*
%{_libdir}/pkgconfig/librsvg-2.0.pc
%{_mandir}/man1/rsvg.1.gz
%{_datadir}/pixmaps/svg-viewer.svg
