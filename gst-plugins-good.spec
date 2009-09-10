Name: gst-plugins-good
Version: 0.10.16
Release: 2ev
Summary: Plugins for GStreamer with good, clean code
URL: http://gstramer.freedesktop.org/
Group: System Environment/Libraries
License: LGPL-2.1
Vendor: GNyU-Linux
Source: http://gstreamer.freedesktop.org/src/%{name}/%{name}-%{version}.tar.bz2
BuildRequires: pkg-config >= 0.9.0, make, gcc, gettext >= 0.17
BuildRequires: gstreamer >= 0.10.24
BuildRequires: glib2 >= 2.16, liboil >= 0.3.8, zlib, bzip2
BuildRequires: python >= 2.1, cairo >= 1.0.0, gtk2 >= 2.8.0
BuildRequires: libflac >= 1.1.4, speex >= 1.1.5, taglib >= 1.5
BuildRequires: hal >= 0.5.6, dbus >= 0.52
BuildRequires: libpng, libjpeg
BuildRequires: libX11, libXfixes, libXdamage, libXext, libXv
Requires: gstreamer

%description
 --- "Such ingratitude.  After all the times I've saved your life."
A collection of plug-ins you'd want to have right next to you on the
battlefield.  Shooting sharp and making no mistakes, these plug-ins have it
all: good looks, good code, and good licensing.  Documented and dressed up
in tests.  If you're looking for a role model to base your own plug-in on,
here it is.
If you find a plot hole or a badly lip-synced line of code in them,
let us know - it is a matter of honour for us to ensure Blondie doesn't look
like he's been walking 100 miles through the desert without water.



%prep
%setup -q


%build
%configure \
	--disable-examples \
	--disable-gconftool \
	--disable-oss \
	--disable-esd \
	--disable-gconf \
	--disable-gst_v4l2
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%find_lang gst-plugins-good-0.10

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files -f gst-plugins-good-0.10.lang
%defattr(-, root, root)
%doc COPYING ABOUT-NLS AUTHORS README RELEASE REQUIREMENTS
%{_libdir}/gstreamer-0.10/*.*
%dir %{_datadir}/gstreamer-0.10
%dir %{_datadir}/gstreamer-0.10/presets
%{_datadir}/gstreamer-0.10/presets/GstIirEqualizer*.prs
