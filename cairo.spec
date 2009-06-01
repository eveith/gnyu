Name: cairo
Version: 1.8.6
Release: 2ev
Summary: A vector graphics library with cross-device output support
URL: http://www.cairographics.org/
Group: System Environment/Libraries
License: LGPL, MIT
Vendor: GNyU-Linux
Source: http://cairographics.org/releases/cairo-%{version}.tar.gz
BuildRequires: make, pkg-config >= 0.9.0, gcc
BuildRequires: zlib, libpng, librsvg >= 2.15.0, poppler >= 0.9.2
BuildRequires: libX11, libXrender >= 0.6, pixman >= 0.12.0
BuildRequires: freetype >= 2.1.9, fontconfig, ghostscript

%description
Cairo is a vector graphics library with cross-device output support. It
currently supports the X Window System and in-memory image buffers as output
targets. It is designed to produce identical output on all output media while
taking advantage of display hardware acceleration when available (eg. through
the X Render Extension). It provides a stateful user-level API with
capabilities similar to the PDF 1.4 imaging model and provides operations
including stroking and filling Bezier cubic splines, transforming and
compositing translucent images, and antialiased text rendering.


%prep
%setup -q


%build
	%configure 
	%{__make} %{?_smp_mflags}


%install
	%{__make} install DESTDIR="${RPM_BUILD_ROOT}"


%post
	%{__ldconfig}


%postun
	%{__ldconfig}


%files
	%defattr(-, root, root)
	%doc AUTHORS BIBLIOGRAPHY BUGS COPYING* ChangeLog* CODING_STYLE NEWS
	%doc PORTING_GUIDE README RELEASING HACKING
	%doc %{_datadir}/gtk-doc/html/%{name}/
	%{_libdir}/libcairo.*
	%{_libdir}/pkgconfig/cairo*.pc
	%{_includedir}/cairo/
