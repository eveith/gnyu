Name: audacious
Version: 1.3.2
Release: 1ev
Summary: A media player for X/GTK+2 with WinAmp look and feel
URL: http://www.audacious-media-player.org/
Group: Applications/Multimedia
License: GPL
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: http://audacious-media-player.org/release/%{name}-%{version}.tgz
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc-core, gtk2 >= 2.6, libglade >= 2.3
BuildRequires: taglib >= 1.4, libogg >= 1.0, libvorbis >= 1.0
BuildRequires: libflac >= 1.1.2, alsa-lib, gettext, libmcs >= 0.1
Requires: gtk2 >= 2.6, libglade >= 2.3, taglib >= 1.4, libogg >= 1.0,
Requires: libvorbis >= 1.0, libflac >= 1.1.2, alsa-lib, audacious-plugins,
Requires: libmcs >= 0.1

%description
Audacious is a fork of the Beep Media Player (which was a fork of XMMS) that
resembles the original WinAmp 2.x look and feel. It is small and fast and
comes with many new features.


%prep
%setup -q


%build
%configure \
	--enable-ipv6 \
	--disable-gconf
make %{_smp_mflags}


%install
[ "$RPM_BUILD_ROOT" != '/' ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"

rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir

%find_lang audacious


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
rm -rf ${RPM_BUILD_ROOT}


%files -f audacious.lang
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS COPYING ChangeLog* FAQ* NEWS* README*
%{_bindir}/audacious
%{_bindir}/audtool
%{_includedir}/audacious/
%{_libdir}/libaudacious.*
%{_libdir}/audacious/
%{_libdir}/pkgconfig/audacious.pc
%{_mandir}/man1/audacious.1.gz
%{_mandir}/man1/audtool.1.gz
%{_datadir}/applications/audacious.desktop
%{_datadir}/audacious/
%{_datadir}/pixmaps/audacious.png
