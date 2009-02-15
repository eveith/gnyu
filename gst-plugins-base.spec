Name: gst-plugins-base
Version: 0.10.22
Release: 2ev
Summary: A collection of well-maintained plugins for GStreamer
URL: http://gstreamer.freedesktop.org/
Group: System Environment/Libraries
License: GPL, LGPL
Vendor: MSP Slackware
Source: http://gstreamer.freedesktop.org/src/%{name}/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, pkg-config >= 0.9.0, gettext, perl
BuildRequires: gstreamer >= 0.10.11.2, liboil >= 0.3.14
BuildRequires: libX11, libXv, libXext, libICE, libSM, libXau, libXdmcp
BuildRequires: alsa-lib >= 0.9.1, cdparanoia, libogg >= 1.0, libtheora, libvorbis
BuildRequires: pango, glib2, zlib, libxml2
Requires: gstreamer, cdparanoia

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
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR="${RPM_BUILD_ROOT}"
%find_lang gst-plugins-base-0.10


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files -f gst-plugins-base-0.10.lang
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS COPYING* NEWS README RELEASE
%doc %{_datadir}/gtk-doc/html/gst-plugins-base-libs-0.10
%doc %{_datadir}/gtk-doc/html/gst-plugins-base-plugins-0.10
%{_bindir}/gst-visualise-0.10
%dir %{_includedir}/gstreamer-0.10/gst/app
%dir %{_includedir}/gstreamer-0.10/gst/audio
%dir %{_includedir}/gstreamer-0.10/gst/cdda
%dir %{_includedir}/gstreamer-0.10/gst/fft
%dir %{_includedir}/gstreamer-0.10/gst/floatcast
%dir %{_includedir}/gstreamer-0.10/gst/interfaces
%dir %{_includedir}/gstreamer-0.10/gst/netbuffer
%dir %{_includedir}/gstreamer-0.10/gst/pbutils
%dir %{_includedir}/gstreamer-0.10/gst/riff
%dir %{_includedir}/gstreamer-0.10/gst/rtp
%dir %{_includedir}/gstreamer-0.10/gst/rtsp
%dir %{_includedir}/gstreamer-0.10/gst/sdp
%dir %{_includedir}/gstreamer-0.10/gst/tag
%dir %{_includedir}/gstreamer-0.10/gst/video
%{_includedir}/gstreamer-0.10/gst/*/*.h
%{_libdir}/libgst*.*
%{_libdir}/gstreamer-0.10/*.*
%{_libdir}/pkgconfig/gstreamer-plugins-base-0.10.pc
%{_libdir}/pkgconfig/gstreamer-app-0.10.pc  
%{_libdir}/pkgconfig/gstreamer-audio-0.10.pc
%{_libdir}/pkgconfig/gstreamer-cdda-0.10.pc 
%{_libdir}/pkgconfig/gstreamer-fft-0.10.pc  
%{_libdir}/pkgconfig/gstreamer-floatcast-0.10.pc
%{_libdir}/pkgconfig/gstreamer-interfaces-0.10.pc
%{_libdir}/pkgconfig/gstreamer-netbuffer-0.10.pc 
%{_libdir}/pkgconfig/gstreamer-pbutils-0.10.pc   
%{_libdir}/pkgconfig/gstreamer-riff-0.10.pc      
%{_libdir}/pkgconfig/gstreamer-rtp-0.10.pc       
%{_libdir}/pkgconfig/gstreamer-rtsp-0.10.pc      
%{_libdir}/pkgconfig/gstreamer-sdp-0.10.pc       
%{_libdir}/pkgconfig/gstreamer-tag-0.10.pc       
%{_libdir}/pkgconfig/gstreamer-video-0.10.pc
%doc %{_mandir}/man1/gst-visualise-0.10.1*
