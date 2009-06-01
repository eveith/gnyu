Name: cairo
Version: 1.4.12
Release: 1ev
Summary: A vector graphics library with cross-device output support
URL: http://www.cairographics.org/
Group: System Environment/Libraries
License: LGPL, MIT
Vendor: MSP Slackware
Source: http://cairographics.org/releases/cairo-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: freetype >= 2.1.4, zlib, make, gcc-core, libpng, pkg-config
BuildRequires: libX11, libXrender, fontconfig
Provides: libtool(%{_libdir}/libcairo.la)

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
if [ -d %{_prefix}/X11R6/lib/pkgconfig ]
then
	export PKG_CONFIG_PATH="${PKG_CONFIG_PATH}:%{_prefix}/X11R6/lib/pkgconfig"
fi
%configure 
%__make # %{_smp_mflags} does not work.


%install
[ "$RPM_BUILD_ROOT" != '/' ] && %__rm -rf "${RPM_BUILD_ROOT}"
%__make_install DESTDIR="$RPM_BUILD_ROOT"
%__rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != '/' ] && %__rm -rf "${RPM_BUILD_ROOT}"


%files
%defattr(-, root, root)
%doc AUTHORS BUGS COPYING* CODING_STYLE NEWS PORTING_GUIDE README RELEASING TODO
%doc ROADMAP 
%doc %{_datadir}/gtk-doc/html/%{name}/
%{_libdir}/libcairo.*
%{_libdir}/pkgconfig/cairo*.pc
%{_includedir}/cairo/
