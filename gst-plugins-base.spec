Name: gst-plugins-base
Version: 0.10.14
Release: 1ev
Summary: A collection of well-maintained plugins for GStreamer
URL: http://gstreamer.freedesktop.org/
Group: System Environment/Libraries
License: GPL, LGPL
Vendor: MSP Slackware
Source: http://gstreamer.freedesktop.org/src/%{name}/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, gstreamer, alsa-lib, libogg, libvorbis,
BuildRequires: libtheora, cdparanoia, gettext, liboil >= 0.3.8, pango
Requires: gstreamer, liboil >= 0.3.8

%description
A well-groomed and well-maintained collection of GStreamer plug-ins and
elements, spanning the range of possible types of elements one would want
to write for GStreamer.


%prep
%setup -q


%build
%configure \
	--disable-gnome_vfs \
	--disable-libvisual \
	--disable-examples
make %{_smp_mflags}


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"

[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS COPYING* NEWS README RELEASE
%doc %{_datadir}/gtk-doc/html/gst-plugins-base-libs-0.10
%{_bindir}/gst-visualise-0.10
%{_includedir}/gstreamer-0.10
%{_libdir}/libgst*.*
%{_libdir}/gstreamer-0.10/*.*
%{_libdir}/pkgconfig/gstreamer-plugins-base-0.10.pc
%{_mandir}/man1/gst-visualise-0.10.1*
%{_datadir}/locale/*/LC_MESSAGES/*.mo
