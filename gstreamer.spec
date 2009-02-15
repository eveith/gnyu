Name: gstreamer
Version: 0.10.14
Release: 1ev
Summary:  A multimedia playback and processing framework
URL: http://gstreamer.freedesktop.org/
Group: System Environment/Libraries
License: LGPL
Vendor: MSP Slackware
Source: http://gstreamer.freedesktop.org/src/%{name}/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core

%description
GStreamer is a library that allows the construction of graphs of
media-handling components, ranging from simple Ogg/Vorbis playback to complex
audio (mixing) and video (non-linear editing) processing. 
Applications can take advantage of advances in codec and filter technology
transparently. Developers can add new codecs and filters by writing a simple
plugin with a clean, generic interface. 


%prep
%setup -q


%build
%configure \
	--disable-gtk-doc
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
%doc ABOUT-NLS AUTHORS COPYING ChangeLog NEWS README RELEASE TODO
%doc %{_datadir}/gtk-doc/html/gstreamer-0.10
%doc %{_datadir}/gtk-doc/html/gstreamer-libs-0.10
%doc %{_datadir}/gtk-doc/html/gstreamer-plugins-0.10
%{_bindir}/gst-*
%{_includedir}/gstreamer-0.10/
%{_libdir}/gstreamer-0.10/
%{_libdir}/libgst*-0.10*.*
%{_libdir}/pkgconfig/gstreamer-*0.10.pc
%{_mandir}/man1/*.1*
%{_datadir}/locale/*/LC_MESSAGES/*.mo
%{_datadir}/aclocal/gst-element-check-0.10.m4
