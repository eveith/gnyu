Name: kdeartwork
Version: 3.5.6
Release: 1ev
Summary: Some additional artwork for KDE
URL: http://www.kde.org/
Group: User Interface/Desktops
License: GPL/LGPL
Vendor: MSP Slackware
Source: http://download.kde.org/stable/%{version}/src/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-g++, qt3 >= 3.3.2, fontconfig, perl, sed
BuildRequires: zlib >= 1.1, libxml2 >= 2.4.8, libxslt >= 1.0.7, libpng
BuildRequires: libjpeg, xscreensaver

%description
This package contains additional

* themes,
* screensaver,
* sounds,
* wallpapers,
* widget styles and
* window styles

for KDE. We placed them into this module so that kdebase won't be too bloated.


%prep
%setup -q


%build
%configure \
	--disable-debug \
	--disable-warnings \
	--enable-final \
	--with-xscreensaver
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
%doc COPYING* README %{name}.lsm
%{_bindir}/kxs*
%{_bindir}/*.kss
%{_libdir}/kde3/*.*
%{_libdir}/kde3/plugins/styles/*.*
%{_datadir}/applnk/System/ScreenSavers/*.desktop
%{_datadir}/apps/kwin/*.desktop
%{_datadir}/apps/kwin/icewm-themes/
%{_datadir}/apps/kwin/glow-themes/
%{_datadir}/apps/kscreensaver/
%{_datadir}/apps/kfiresaver/
%{_datadir}/apps/kworldclock/
%{_datadir}/apps/kstyle/themes/*.themerc
%{_datadir}/emoticons/Boxed
%{_datadir}/emoticons/GroupWise
%{_datadir}/emoticons/KMess
%{_datadir}/emoticons/KMess-Blue
%{_datadir}/emoticons/KMess-Cartoon
%{_datadir}/emoticons/KMess-Violet
%{_datadir}/emoticons/Plain
%{_datadir}/emoticons/RedOnes
%{_datadir}/emoticons/ccmathteam.com
%{_datadir}/emoticons/greggman.com
%{_datadir}/emoticons/phpBB
%{_datadir}/emoticons/tweakers.net
%{_datadir}/icons/Locolor/
%{_datadir}/icons/ikons/
%{_datadir}/icons/kdeclassic/
%{_datadir}/icons/kids/
%{_datadir}/icons/slick/
%{_datadir}/sounds/*.*
%{_datadir}/wallpapers/*.*
