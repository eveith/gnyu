Name: kdebase
Version: 3.5.9
Release: 2ev
Summary: Base package of the K Desktop Environment (KDE)
URL: http://www.kde.org/
Group: User Interface/Desktops
License: GPL-2, LGPL-2, BSD
Vendor: GNyU-Linux
Source: http://download.kde.org/stable/%{version}/src/%{name}-%{version}.tar.bz2
Source1: %{name}-kdm.pamd
Source2: %{name}-kdm.i
Patch0: kdebase-3.5.5-dbus.patch
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc-g++, qt3 >= 3.3.2, fontconfig, ghostscript
BuildRequires: zlib, libxml2 >= 2.4.8, libxslt >= 1.0.7, cups >= 1.1.9, perl
BuildRequires: samba-libs, hal >= 0.4.0, dbus >= 0.2, cyrus-sasl, libstdc++
BuildRequires: openssl >= 0.9.6, libpam, mesalib, libtiff, libpng, libjpeg
BuildRequires: libmng, freetype >= 2.0.0, libogg, libvorbis, libusb, sudo, sed
BuildRequires: openldap-libs, %{_datadir}/usb.ids, dbus-qt3, coreutils
BuildRequires: automake-110, kdelibs = %{version}

%description
kdebase is the second mandatory package (besides kdelibs) for the K Desktop
Environment. Here we have various applications and infrastructure files and
libraries.


%prep
%setup -q
%patch -P 0 -p1


%build
%configure \
	--disable-debug \
	--disable-warnings \
	--without-shadow --disable-shadow \
	--with-pam=yes \
	--with-kdm-pam=kdm \
	--with-kcp-pam=kcheckpass \
	--with-kss-pam=kscreensaver \
	--with-java=%{_libdir}/java \
	--with-libusb \
	--with-usbids=%{_datadir}/usb.ids \
	--with-sudo-kdesu-backend \
	--with-hal \
	--with-samba \
	--with-cdparanoia \
	--disable-rpath 
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}' RUN_KAPPFINDER=no

pushd '%{buildroot}'

# Install pam files
%{__mkdir_p} etc/pam.d
%{__cp} %{SOURCE1} etc/pam.d/kdm
%{__cp} %{SOURCE1} etc/pam.d/kcheckpass
%{__cp} %{SOURCE1} etc/pam.d/kscreensaver

# The InitNG service file for kdm
%{__mkdir_p} etc/initng/daemon
%{__cat} < %{SOURCE2} \
	| %{__sed} -e 's,@kdm@,%{_bindir}/kdm,g' \
	> etc/initng/daemon/kdm.i

popd

# Add stuff to a global filelist, this saves us a lot of time. :-)
# The directories in /usr/share are either provided by aRts, kdelibs or
# the fhs package. If not, add them to our list.

#find "${RPM_BUILD_ROOT}/%{_datadir}" -not -type d -print \
#	| sed "s,^$RPM_BUILD_ROOT,," >> files.list

#for dir in $(find "${RPM_BUILD_ROOT}/%{_datadir}" -type d -print)
#do
#	dir=$(echo "$dir" | sed "s,^$RPM_BUILD_ROOT,,")
#	if [ $(rpm -q --whatprovides "$dir" | grep 'kdelibs|fhs|arts' | wc -l) -eq 0 \
#			-a "$?" -eq 0 ]
#	then
#		dir=$(echo "$dir" | sed 's,/\?%{_datadir},%%{_datadir},')
#		echo "%dir $dir" >> files.list
#	fi
#done


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__rm} -f files.list ||:


%files
%defattr(-, root, root)
%doc AUTHORS COPYING* README
%doc %{_datadir}/doc/HTML/en/kdeprint/
%doc %{_datadir}/doc/HTML/en/kdebugdialog/
%doc %{_datadir}/doc/HTML/en/kappfinder/
%doc %{_datadir}/doc/HTML/en/kate/
%doc %{_datadir}/doc/HTML/en/kmenuedit/
%doc %{_datadir}/doc/HTML/en/konqueror/
%doc %{_datadir}/doc/HTML/en/knetattach/
%doc %{_datadir}/doc/HTML/en/khelpcenter/
%doc %{_datadir}/doc/HTML/en/kfind/
%doc %{_datadir}/doc/HTML/en/kcontrol/
%doc %{_datadir}/doc/HTML/en/kdcop/
%doc %{_datadir}/doc/HTML/en/ksplashml/
%doc %{_datadir}/doc/HTML/en/kxkb/
%doc %{_datadir}/doc/HTML/en/kwrite/
%doc %{_datadir}/doc/HTML/en/klipper/
%doc %{_datadir}/doc/HTML/en/kinfocenter/
%doc %{_datadir}/doc/HTML/en/kicker/
%doc %{_datadir}/doc/HTML/en/kpager/
%doc %{_datadir}/doc/HTML/en/konsole/
%doc %{_datadir}/doc/HTML/en/kdm/
%doc %{_datadir}/doc/HTML/en/kdesu/
%doc %{_datadir}/doc/HTML/en/kompmgr/
%doc %{_datadir}/doc/HTML/en/ksysguard/
%doc %{_datadir}/doc/HTML/en/kioslave/
%doc %{_datadir}/doc/kdm/
%config(noreplace) /etc/pam.d/k*
/etc/initng/daemon/kdm.i
/etc/ksysguarddrc
/etc/xdg/menus/*.menu
/etc/xdg/menus/applications-merged/
%{_libdir}/*.*
%{_libdir}/kde3/*.*
%{_libdir}/kconf_update_bin/
%{_includedir}/*.h
%{_includedir}/kate/*.h
%{_includedir}/kate/utils/
%{_includedir}/ksgrd/
%{_includedir}/ksplash/
%{_includedir}/kwin/
%{_bindir}/*
%{_datadir}/autostart/*
%{_datadir}/apps/konqueror/
%{_datadir}/apps/kconf_update/
%{_datadir}/apps/kbookmark/
%{_datadir}/apps/drkonqi/
%{_datadir}/apps/kappfinder/
%{_datadir}/apps/kate/
%{_datadir}/apps/kwrite/
%{_datadir}/apps/kdcop/
%{_datadir}/apps/kdm/
%{_datadir}/apps/kjobviewer/
%{_datadir}/apps/kdeprintfax/
%{_datadir}/apps/kdeprint/
%{_datadir}/apps/kfindpart/
%{_datadir}/apps/khelpcenter/
%{_datadir}/apps/khotkeys/
%{_datadir}/apps/kio_info/
%{_datadir}/apps/kio_man/
%{_datadir}/apps/kio_finger/
%{_datadir}/apps/remoteview/
%{_datadir}/apps/systemview/
%{_datadir}/apps/kicker/
%{_datadir}/apps/kmenuedit/
%{_datadir}/apps/kcontroledit/
%{_datadir}/apps/konsole/
%{_datadir}/apps/kpersonalizer/
%{_datadir}/apps/ksplash/
%{_datadir}/apps/ksysguard/
%{_datadir}/apps/kdewizard/
%{_datadir}/apps/kwin/
%{_datadir}/apps/plugin/
%{_datadir}/apps/konqiconview/
%{_datadir}/apps/konqlistview/
%{_datadir}/apps/keditbookmarks/
%{_datadir}/apps/konqsidebartng/
%{_datadir}/apps/kdeprint_part/
%{_datadir}/apps/khtml/
%{_datadir}/apps/ksmserver/
%{_datadir}/apps/clockapplet/
%{_datadir}/apps/naughtyapplet/
%{_datadir}/apps/kcontrol/
%{_datadir}/apps/kthememanager/
%{_datadir}/apps/kdisplay/
%{_datadir}/apps/kcminput/
%{_datadir}/apps/kcmlocale/
%{_datadir}/apps/kcmkeys/
%{_datadir}/apps/kinfocenter/
%{_datadir}/apps/kaccess/
%{_datadir}/apps/kcmcss/
%{_datadir}/apps/kfontview/
%{_datadir}/apps/kcm_componentchooser/
%{_datadir}/apps/kdesktop/
%{_datadir}/applications/*
%{_datadir}/applnk/
%{_datadir}/services/
%{_datadir}/wallpapers/
%{_datadir}/fonts/
%{_datadir}/templates/
%{_datadir}/locale/l10n/
%{_datadir}/locale/en_US/*.desktop
%{_datadir}/desktop-directories/
%{_datadir}/icons/crystalsvg/
%{_datadir}/icons/hicolor/*/*/*
%dir %{_datadir}/mimelnk/media
%dir %{_datadir}/mimelnk/fonts
%dir %{_datadir}/mimelnk/print
%{_datadir}/mimelnk/*/*
%{_datadir}/sounds/
%{_datadir}/servicetypes/*
%{_datadir}/config.kcfg/
%{_datadir}/config/kdm/
%{_datadir}/config/*rc
%{_datadir}/config/kdesktop_custom_menu?
%{_datadir}/config/kxkb_groups
