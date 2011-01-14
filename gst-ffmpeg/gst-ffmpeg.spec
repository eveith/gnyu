Name: gst-ffmpeg
Version: 0.10.8
Release: 2ev
Summary: FFMPEG plugin for gstreamer
URL: http://gstreamer.freedesktop.org/modules/gst-ffmpeg.html
Group: System Environment/Libraries
License: GPL-3
Vendor: GNyU-Linux
Source: http://gstreamer.freedesktop.org/src/%{name}/%{name}-%{version}.tar.bz2
BuildRequires: pkg-config >= 0.9.0, make, gcc
BuildRequires: gstreamer >= 0.10.22, liboil >= 0.3.6, zlib, bzip2

%description
GStreamer FFmpeg plug-in contains one plugin with a set of elements using the
FFmpeg library code. It contains most popular decoders as well as very fast
colorspace conversion elements.


%prep
	%setup -q


%build
	%configure
	%{__make} %{?_smp_mflags}


%install
	%{__make} install DESTDIR='%{buildroot}'
	[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
		&& %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
	%{__ldconfig}


%postun
	%{__ldconfig}


%files
	%defattr(-, root, root)
	%doc AUTHORS COPYING NEWS README TODO
	%{_libdir}/gstreamer-0.10/libgstffmpeg.*
	%{_libdir}/gstreamer-0.10/libgstffmpegscale.*
	%{_libdir}/gstreamer-0.10/libgstpostproc.*
