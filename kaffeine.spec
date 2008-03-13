Name: kaffeine
Version: 0.8.5
Release: 1ev
Summary:  full featured media player for KDE
URL: http://kaffeine.sf.net/
Group: Applications/Multimedia
License: GPL
Vendor: MSP Slackware
Source: http://prdownloads.sourceforge.net/kaffeine/kaffeine-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, gcc-g++, qt3 >= 3.3, xine-lib >= 1.1.1
BuildRequires: kdelibs >= 3.2, kdebase >= 3.2, lame, libogg, libvorbis, perl
BuildRequires: cdparanoia, autoconf, gettext, gstreamer
Requires: qt3, xine-lib >= 1.1.1, kdelibs >= 3.2, kdebase >= 3.2

%description
Kaffeine is a simple and easy to use media player based on the xine-lib and
full integrated in KDE3. It supports drag and drop and provides an editable
playlist, a Konqueror plugin, a Mozilla plugin, and much more.


%prep
%setup -q


%build
export CFLAGS="$RPM_OPT_FLAGS -I%{_includedir}/cdda"
export CXXFLAGS="$RPM_OPT_FLAGS -I%{_includedir}/cdda"
%configure \
	--disable-warnings \
	--disable-debug \
	--enable-final \
	--without-dvb \
	--without-gstreamer \
	--with-oggvorbis \
	--with-lame
make %{_smp_mflags}


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"
%find_lang kaffeine


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files -f kaffeine.lang
%defattr(-, root, root)
%doc README AUTHORS COPYING TODO ChangeLog VERSION
%doc %{_datadir}/doc/HTML/en/kaffeine
%{_bindir}/kaffeine
%{_includedir}/kaffeine
%{_libdir}/kde3/libkaffeine*.*
%{_libdir}/kde3/lib*part*.*
%{_libdir}/libkaffeine*.*
%{_datadir}/applications/kde/kaffeine.desktop
%{_datadir}/apps/kaffeine/
%{_datadir}/apps/konqueror/servicemenus/*.desktop
%{_datadir}/apps/profiles/kaffeine.profile.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/mimelnk/application/*.desktop
%{_datadir}/services/*.desktop
%{_datadir}/servicetypes/kaffeineaudioencoder.desktop
