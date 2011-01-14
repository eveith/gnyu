Name: gst-plugins-bad
Version: 0.10.14
Release: 1ev
Summary: A set of gstreamer plugins with possibly bad code quality
URL: http://gstreamer.freedesktop.org/modules/gst-plugins-bad.html
Group: System Environment/Libraries
License: GPL-2, LGPL-2
Vendor: GNyU-Linux
Source: http://gstreamer.freedesktop.org/src/%{name}/%{name}-%{version}.tar.bz2
BuildRequires: pkg-config >= 0.9.0, make, gcc, perl, gettext >= 0.17
BuildRequires: gstreamer >= 0.10.24, glib2 >= 2.16, liboil >= 0.3.8
BuildRequires: libX11, gtk2, libglade, alsa-lib >= 0.9.1, bzip2
BuildRequires: faad2, libmpeg2, neon >= 0.26.0, neon < 0.28.99
BuildRequires: libsdl, libsndfile >= 1.0.16, libtheora, xvidcore

%description
"That an accusation?" -- No perfectly groomed moustache or any amount of fine
clothing is going to cover up the truth - these plug-ins are Bad with a
capital B. They look fine on the outside, and might even appear to get the job
done, but at the end of the day they're a black sheep. Without a golden-haired
angel to watch over them, they'll probably land in an unmarked grave at the
final showdown.


%prep
	%setup -q


%build
	%configure
	%{__make} %{?_smp_mflags}


%install
	%{__make} install DESTDIR='%{buildroot}'
	%find_lang gst-plugins-bad-0.10


	[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
		&& %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
	%{__ldconfig}


%postun
	%{__ldconfig}


%files -f gst-plugins-bad-0.10.lang
	%defattr(-, root, root)
	%doc ABOUT-NLS AUTHORS ChangeLog COPYING* NEWS README RELEASE
	%{_bindir}/gst-camera
	%{_bindir}/gst-camera-perf
	%{_includedir}/gstreamer-0.10/gst/interfaces/photography*.h
	%{_includedir}/gstreamer-0.10/gst/video/gstbasevideo*.h
	%{_libdir}/gstreamer-0.10/*.*
	%{_libdir}/libgstbasevideo-0.10.*
	%{_libdir}/libgstphotography-0.10.*
	%{_libdir}/libgstsignalprocessor.*
	%dir %{_datadir}/gstreamer-0.10/camera-apps
	%{_datadir}/gstreamer-0.10/camera-apps/gst-camera.glade
