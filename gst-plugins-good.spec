Name: gst-plugins-good
Version: 0.10.13
Release: 1ev
Summary: Plugins for GStreamer with good, clean code
URL: http://gstramer.freedesktop.org/
Group: System Environment/Libraries
License: LGPL-2.1
Vendor: GNyU-Linux
Source: http://gstreamer.freedesktop.org/src/%{name}/%{name}-%{version}.tar.bz2
BuildRequires: make, gcc, gettext, pkg-config >= 0.9.0, gstreamer >= 0.10.11.2
BuildRequires: python >= 2.1, glib2, liboil >= 0.3.8, gtk2, cairo, hal
BuildRequires: libpng, libjpeg, speex, zlib, bzip2
BuildRequires: libX11, libICE, libSM, libXfixes, libXdamage, libXext
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
	--disable-gconftool \
	--disable-oss \
	--disable-esd \
	--disable-gconf
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
