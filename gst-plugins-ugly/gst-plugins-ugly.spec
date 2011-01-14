Name: gst-plugins-ugly
Version: 0.10.12
Release: 3ev
Summary: Plugins for some proprietary video/audio file formats
URL: http://gstreamer.freedesktop.org/modules/gst-plugins-ugly.html
Group: System Environment/Libraries
License: LGPL-2.1
Vendor: GNyU-Linux
Source: http://gstreamer.freedesktop.org/src/%{name}/%{name}-%{version}.tar.bz2
BuildRequires: pkg-config >= 0.9.0, make, gcc, gettext >= 0.17
BuildRequires: gstreamer >= 0.10.23, glib2 >= 2.12, liboil >= 0.3.8
BuildRequires: lame, libid3tag >= 0.15, libmad >= 0.15, libmpeg2 >= 0.4
BuildRequires: x264, libdvdnav >= 0.1.7, liba52

%description
"When you have to shoot, shoot. Don't talk." 
There are times when the world needs a color between black and white. Quality
code to match the good's, but two-timing, backstabbing and ready to sell your
freedom down the river. These plug-ins might have a patent noose around their
neck, or a lock-up license, or any other problem that makes you think twice
about shipping them. 
We don't call them ugly because we like them less. Does a mother love her son
less because he's not as pretty as the other ones ? No - she commends him on
his great personality. These plug-ins are the life of the party. And we'll
still step in and set them straight if you report any unacceptable behaviour -
because there are two kinds of people in the world, my friend: those with a
rope around their neck and the people who do the cutting. 
This module contains a set of plug-ins that have good quality and correct
functionality, but distributing them might pose problems. The license on
either the plug-ins or the supporting libraries might not be how we'd like.
The code might be widely known to present patent problems. Distributors should
check if they want/can ship these plug-ins.


%prep
	%setup -q


%build
	%configure \
		--disable-dvdread \
		--enable-dvdnav
	%{__make} %{?_smp_mflags}


%install
	%{__make} install DESTDIR='%{buildroot}'
	%find_lang gst-plugins-ugly-0.10

	[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
		&& %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
	%{__ldconfig}


%postun
	%{__ldconfig}


%files -f gst-plugins-ugly-0.10.lang
	%defattr(-, root, root)
	%doc NEWS README RELEASE AUTHORS COPYING ABOUT-NLS
	%{_libdir}/gstreamer-0.10/*.*
	%{_datadir}/gstreamer-0.10/presets/GstX264Enc.prs
