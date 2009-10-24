Name: librsvg
Version: 2.16.1
Release: 2.0ev
Summary: Tools for rendering and converting SVG images
URL: http://librsvg.sourceforge.net/
Group: System Environment/Libraries
License: GPL-2
Vendor: GNyU-Linux
Source: http://ftp.gnome.org/pub/GNOME/sources/librsvg/2.16/%{name}-%{version}.tar.bz2
BuildRequires: pkg-config >= 0.9.0, make, gcc
BuildRequires: freetype >= 2.0.0, fontconfig >= 1.0.1, cairo >= 1.2.0
BuildRequires: glib2 >= 2.12.0, gtk2 >= 2.6.0
BuildRequires: libxml2 >= 2.4.7, libgsf >= 1.6.0, libcroco >= 0.6.1

%description
SVG, "scalable vector graphics", is an XML-based open source vector format. It
is commonly used for icons. The great advantage of SVG is that it can be
scaled to almost any picture size while the file size remains very small.
This package contains tools for viewing and converting SVG images.


%package -n librsvg2
Summary: A SVG rendering library
Group: System Environment/Libraries
License: LGPL-2

%description -n librsvg2
libRSVG is a very fast SVG rendering engine written in C. It currently support
most of the SVG 1.2 specification, except the animation part. libRSVG is used
in many projects for SVG rendering, most notably GNOME.



%prep
%setup -q


%build
%configure \
	--disable-gnome-vfs
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%{__rm_rf} ${RPM_BUILD_ROOT}/%{_infodir}/dir



%post -n librsvg2
%{__ldconfig}


%postun -n librsvg
%{__ldconfig}


%files
%defattr(-, root, root)
%doc AUTHORS COPYING* ChangeLog* MAINTAINERS NEWS README TODO 
%doc %{_datadir}/gtk-doc/html/rsvg
%{_bindir}/rsvg
%{_bindir}/rsvg-convert
%{_bindir}/rsvg-view
%doc %{_mandir}/man1/rsvg.1*
%{_datadir}/pixmaps/svg-viewer.svg


%files -n librsvg2
%defattr(-, root, root)
%doc AUTHORS COPYING* ChangeLog* MAINTAINERS NEWS README TODO 
%dir %{_includedir}/librsvg-2
%dir %{_includedir}/librsvg-2/librsvg
%{_includedir}/librsvg-2/librsvg/librsvg-enum-types.h
%{_includedir}/librsvg-2/librsvg/librsvg-features.h
%{_includedir}/librsvg-2/librsvg/rsvg-cairo.h
%{_includedir}/librsvg-2/librsvg/rsvg.h
%{_libdir}/librsvg-2.*
%{_libdir}/pkgconfig/librsvg-2.0.pc
%{_libdir}/gtk-2.0/2.10.0/engines/libsvg.*
%{_libdir}/gtk-2.0/2.10.0/loaders/svg_loader.*
