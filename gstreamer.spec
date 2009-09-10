Name: gstreamer
Version: 0.10.24
Release: 3ev
Summary: A multimedia playback and processing framework
URL: http://gstreamer.freedesktop.org/
Group: System Environment/Libraries
License: LGPL-2
Vendor: GNyU-Linux
Source: http://gstreamer.freedesktop.org/src/%{name}/%{name}-%{version}.tar.bz2
BuildRequires: pkg-config >= 0.9.0, make, gcc, gettext >= 0.17, perl
BuildRequires: glib2 >= 2.16, libxml2 >= 2.4.9

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
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR="${RPM_BUILD_ROOT}"
%find_lang gstreamer-0.10


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files -f gstreamer-0.10.lang
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS COPYING ChangeLog NEWS README RELEASE TODO
%doc %{_datadir}/gtk-doc/html/gstreamer-0.10
%doc %{_datadir}/gtk-doc/html/gstreamer-libs-0.10
%doc %{_datadir}/gtk-doc/html/gstreamer-plugins-0.10
%{_bindir}/gst-feedback
%{_bindir}/gst-feedback-0.10
%{_bindir}/gst-inspect
%{_bindir}/gst-inspect-0.10
%{_bindir}/gst-launch
%{_bindir}/gst-launch-0.10
%{_bindir}/gst-typefind
%{_bindir}/gst-typefind-0.10
%{_bindir}/gst-xmlinspect
%{_bindir}/gst-xmlinspect-0.10
%{_bindir}/gst-xmllaunch
%{_bindir}/gst-xmllaunch-0.10
%{_includedir}/gstreamer-0.10/
%{_libdir}/gstreamer-0.10/
%{_libdir}/libgst*-0.10*.*
%{_libdir}/pkgconfig/gstreamer-*0.10.pc
%doc %{_mandir}/man1/*.1*
%{_datadir}/aclocal/gst-element-check-0.10.m4
