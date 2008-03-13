Name: kdebase
Version: 3.5.8
Release: 1ev
Summary: Base package of the K Desktop Environment (KDE)
URL: http://www.kde.org/
Group: User Interface/Desktops
License: GPL, LGPL, BSD
Vendor: MSP Slackware
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
BuildRequires: openldap-libs, %{_datadir}/usb.ids, dbus-qt3
BuildRequires: automake-110, kdelibs = %{version}
Provides: libtool(%{_libdir}/kde3/kded_favicons.la)
Provides: libtool(%{_libdir}/kde3/konq_sound.la)
Provides: libtool(%{_libdir}/kde3/kate.la)
Provides: libtool(%{_libdir}/kde3/kwrite.la)
Provides: libtool(%{_libdir}/kde3/kcminit.la)
Provides: libtool(%{_libdir}/kde3/kcminit_startup.la)
Provides: libtool(%{_libdir}/kde3/kcm_useraccount.la)
Provides: libtool(%{_libdir}/kde3/kcm_printmgr.la)
Provides: libtool(%{_libdir}/kde3/kjobviewer.la)
Provides: libtool(%{_libdir}/kde3/kprinter.la)
Provides: libtool(%{_libdir}/kde3/kio_print.la)
Provides: libtool(%{_libdir}/kde3/libkdeprint_part.la)
Provides: libtool(%{_libdir}/kde3/kgreet_classic.la)
Provides: libtool(%{_libdir}/kde3/kgreet_winbind.la)
Provides: libtool(%{_libdir}/kde3/libkfindpart.la)
Provides: libtool(%{_libdir}/kde3/khelpcenter.la)
Provides: libtool(%{_libdir}/kde3/kcm_khotkeys.la)
Provides: libtool(%{_libdir}/kde3/kcm_khotkeys_init.la)
Provides: libtool(%{_libdir}/kde3/kded_khotkeys.la)
Provides: libtool(%{_libdir}/kde3/khotkeys.la)
Provides: libtool(%{_libdir}/kde3/khotkeys_arts.la)
Provides: libtool(%{_libdir}/kde3/kio_about.la)
Provides: libtool(%{_libdir}/kde3/kcm_cgi.la)
Provides: libtool(%{_libdir}/kde3/kio_cgi.la)
Provides: libtool(%{_libdir}/kde3/kio_floppy.la)
Provides: libtool(%{_libdir}/kde3/kio_filter.la)
Provides: libtool(%{_libdir}/kde3/kio_fish.la)
Provides: libtool(%{_libdir}/kde3/kio_info.la)
Provides: libtool(%{_libdir}/kde3/kio_mac.la)
Provides: libtool(%{_libdir}/kde3/kio_man.la)
Provides: libtool(%{_libdir}/kde3/libkmanpart.la)
Provides: libtool(%{_libdir}/kde3/kio_nfs.la)
Provides: libtool(%{_libdir}/kde3/kio_nntp.la)
Provides: libtool(%{_libdir}/kde3/kio_pop3.la)
Provides: libtool(%{_libdir}/kde3/kio_smtp.la)
Provides: libtool(%{_libdir}/kde3/kio_sftp.la)
Provides: libtool(%{_libdir}/kde3/kio_tar.la)
Provides: libtool(%{_libdir}/kde3/kio_finger.la)
Provides: libtool(%{_libdir}/kde3/kio_thumbnail.la)
Provides: libtool(%{_libdir}/kde3/imagethumbnail.la)
Provides: libtool(%{_libdir}/kde3/textthumbnail.la)
Provides: libtool(%{_libdir}/kde3/htmlthumbnail.la)
Provides: libtool(%{_libdir}/kde3/djvuthumbnail.la)
Provides: libtool(%{_libdir}/kde3/cursorthumbnail.la)
Provides: libtool(%{_libdir}/kde3/kio_ldap.la)
Provides: libtool(%{_libdir}/kde3/kio_smb.la)
Provides: libtool(%{_libdir}/kde3/kio_settings.la)
Provides: libtool(%{_libdir}/kde3/kio_trash.la)
Provides: libtool(%{_libdir}/kde3/kfile_trash.la)
Provides: libtool(%{_libdir}/kde3/kio_media.la)
Provides: libtool(%{_libdir}/kde3/kded_mediamanager.la)
Provides: libtool(%{_libdir}/kde3/kded_medianotifier.la)
Provides: libtool(%{_libdir}/kde3/kfile_media.la)
Provides: libtool(%{_libdir}/kde3/kcm_media.la)
Provides: libtool(%{_libdir}/kde3/kio_remote.la)
Provides: libtool(%{_libdir}/kde3/kded_remotedirnotify.la)
Provides: libtool(%{_libdir}/kde3/kio_home.la)
Provides: libtool(%{_libdir}/kde3/kded_homedirnotify.la)
Provides: libtool(%{_libdir}/kde3/kio_system.la)
Provides: libtool(%{_libdir}/kde3/kded_systemdirnotify.la)
Provides: libtool(%{_libdir}/kde3/klipper_panelapplet.la)
Provides: libtool(%{_libdir}/kde3/klipper.la)
Provides: libtool(%{_libdir}/kde3/kmenuedit.la)
Provides: libtool(%{_libdir}/kde3/kcontroledit.la)
Provides: libtool(%{_libdir}/kde3/libkonsolepart.la)
Provides: libtool(%{_libdir}/kde3/kded_kwrited.la)
Provides: libtool(%{_libdir}/kde3/konsole.la)
Provides: libtool(%{_libdir}/kde3/ksplashdefault.la)
Provides: libtool(%{_libdir}/kde3/ksplashstandard.la)
Provides: libtool(%{_libdir}/kde3/ksplashredmond.la)
Provides: libtool(%{_libdir}/kde3/kcm_ksplashthemes.la)
Provides: libtool(%{_libdir}/kde3/sysguard_panelapplet.la)
Provides: libtool(%{_libdir}/kde3/kwin.la)
Provides: libtool(%{_libdir}/kde3/kcm_kwinoptions.la)
Provides: libtool(%{_libdir}/kde3/kcm_kwindecoration.la)
Provides: libtool(%{_libdir}/kde3/kcm_kwinrules.la)
Provides: libtool(%{_libdir}/kde3/kwin_rules_dialog.la)
Provides: libtool(%{_libdir}/kde3/kwin_plastik_config.la)
Provides: libtool(%{_libdir}/kde3/kwin3_plastik.la)
Provides: libtool(%{_libdir}/kde3/kwin3_b2.la)
Provides: libtool(%{_libdir}/kde3/kwin_b2_config.la)
Provides: libtool(%{_libdir}/kde3/kwin3_default.la)
Provides: libtool(%{_libdir}/kde3/kwin_default_config.la)
Provides: libtool(%{_libdir}/kde3/kwin3_keramik.la)
Provides: libtool(%{_libdir}/kde3/kwin_keramik_config.la)
Provides: libtool(%{_libdir}/kde3/kwin3_laptop.la)
Provides: libtool(%{_libdir}/kde3/kwin_modernsys_config.la)
Provides: libtool(%{_libdir}/kde3/kwin3_modernsys.la)
Provides: libtool(%{_libdir}/kde3/kwin3_quartz.la)
Provides: libtool(%{_libdir}/kde3/kwin_quartz_config.la)
Provides: libtool(%{_libdir}/kde3/kwin3_redmond.la)
Provides: libtool(%{_libdir}/kde3/kwin3_web.la)
Provides: libtool(%{_libdir}/kde3/kcm_keyboard.la)
Provides: libtool(%{_libdir}/kde3/kxkb.la)
Provides: libtool(%{_libdir}/kde3/libnsplugin.la)
Provides: libtool(%{_libdir}/kde3/kcm_nsplugins.la)
Provides: libtool(%{_libdir}/kde3/konqueror.la)
Provides: libtool(%{_libdir}/kde3/kfmclient.la)
Provides: libtool(%{_libdir}/kde3/konq_iconview.la)
Provides: libtool(%{_libdir}/kde3/konq_listview.la)
Provides: libtool(%{_libdir}/kde3/keditbookmarks.la)
Provides: libtool(%{_libdir}/kde3/konq_shellcmdplugin.la)
Provides: libtool(%{_libdir}/kde3/konq_aboutpage.la)
Provides: libtool(%{_libdir}/kde3/konq_sidebar.la)
Provides: libtool(%{_libdir}/kde3/konqsidebar_tree.la)
Provides: libtool(%{_libdir}/kde3/konq_sidebartree_dirtree.la)
Provides: libtool(%{_libdir}/kde3/konq_sidebartree_history.la)
Provides: libtool(%{_libdir}/kde3/kcm_history.la)
Provides: libtool(%{_libdir}/kde3/konq_sidebartree_bookmarks.la)
Provides: libtool(%{_libdir}/kde3/konqsidebar_web.la)
Provides: libtool(%{_libdir}/kde3/kded_konqy_preloader.la)
Provides: libtool(%{_libdir}/kde3/konq_remoteencoding.la)
Provides: libtool(%{_libdir}/kde3/libkhtmlkttsdplugin.la)
Provides: libtool(%{_libdir}/kde3/ksmserver.la)
Provides: libtool(%{_libdir}/kde3/kicker.la)
Provides: libtool(%{_libdir}/kde3/dockbar_panelextension.la)
Provides: libtool(%{_libdir}/kde3/taskbar_panelextension.la)
Provides: libtool(%{_libdir}/kde3/kasbar_panelextension.la)
Provides: libtool(%{_libdir}/kde3/sidebar_panelextension.la)
Provides: libtool(%{_libdir}/kde3/clock_panelapplet.la)
Provides: libtool(%{_libdir}/kde3/systemtray_panelapplet.la)
Provides: libtool(%{_libdir}/kde3/minipager_panelapplet.la)
Provides: libtool(%{_libdir}/kde3/taskbar_panelapplet.la)
Provides: libtool(%{_libdir}/kde3/run_panelapplet.la)
Provides: libtool(%{_libdir}/kde3/launcher_panelapplet.la)
Provides: libtool(%{_libdir}/kde3/naughty_panelapplet.la)
Provides: libtool(%{_libdir}/kde3/lockout_panelapplet.la)
Provides: libtool(%{_libdir}/kde3/menu_panelapplet.la)
Provides: libtool(%{_libdir}/kde3/media_panelapplet.la)
Provides: libtool(%{_libdir}/kde3/trash_panelapplet.la)
Provides: libtool(%{_libdir}/kde3/kickermenu_find.la)
Provides: libtool(%{_libdir}/kde3/kickermenu_kdeprint.la)
Provides: libtool(%{_libdir}/kde3/kickermenu_prefmenu.la)
Provides: libtool(%{_libdir}/kde3/kickermenu_recentdocs.la)
Provides: libtool(%{_libdir}/kde3/kickermenu_konsole.la)
Provides: libtool(%{_libdir}/kde3/kickermenu_konqueror.la)
Provides: libtool(%{_libdir}/kde3/kickermenu_remotemenu.la)
Provides: libtool(%{_libdir}/kde3/kickermenu_systemmenu.la)
Provides: libtool(%{_libdir}/kde3/kickermenu_kate.la)
Provides: libtool(%{_libdir}/kde3/appletproxy.la)
Provides: libtool(%{_libdir}/kde3/extensionproxy.la)
Provides: libtool(%{_libdir}/kde3/kcm_bell.la)
Provides: libtool(%{_libdir}/kde3/kcm_background.la)
Provides: libtool(%{_libdir}/kde3/kcm_kdnssd.la)
Provides: libtool(%{_libdir}/kde3/kcm_filetypes.la)
Provides: libtool(%{_libdir}/kde3/kcm_samba.la)
Provides: libtool(%{_libdir}/kde3/kcm_input.la)
Provides: libtool(%{_libdir}/kde3/kcm_info.la)
Provides: libtool(%{_libdir}/kde3/kcm_ioslaveinfo.la)
Provides: libtool(%{_libdir}/kde3/kcm_kdm.la)
Provides: libtool(%{_libdir}/kde3/kcm_kicker.la)
Provides: libtool(%{_libdir}/kde3/kcm_locale.la)
Provides: libtool(%{_libdir}/kde3/kcm_launch.la)
Provides: libtool(%{_libdir}/kde3/kcm_keys.la)
Provides: libtool(%{_libdir}/kde3/kcm_kio.la)
Provides: libtool(%{_libdir}/kde3/kcm_konq.la)
Provides: libtool(%{_libdir}/kde3/kstyle_keramik_config.la)
Provides: libtool(%{_libdir}/kde3/kcm_style.la)
Provides: libtool(%{_libdir}/kde3/kcm_kded.la)
Provides: libtool(%{_libdir}/kde3/kcm_konqhtml.la)
Provides: libtool(%{_libdir}/kde3/libkuriikwsfilter.la)
Provides: libtool(%{_libdir}/kde3/libkurisearchfilter.la)
Provides: libtool(%{_libdir}/kde3/libkshorturifilter.la)
Provides: libtool(%{_libdir}/kde3/liblocaldomainurifilter.la)
Provides: libtool(%{_libdir}/kde3/kcm_kurifilt.la)
Provides: libtool(%{_libdir}/kde3/kcm_arts.la)
Provides: libtool(%{_libdir}/kde3/kcontrol.la)
Provides: libtool(%{_libdir}/kde3/kcm_knotify.la)
Provides: libtool(%{_libdir}/kde3/kcm_clock.la)
Provides: libtool(%{_libdir}/kde3/kcm_access.la)
Provides: libtool(%{_libdir}/kde3/kaccess.la)
Provides: libtool(%{_libdir}/kde3/kcm_colors.la)
Provides: libtool(%{_libdir}/kde3/kcm_energy.la)
Provides: libtool(%{_libdir}/kde3/kcm_fonts.la)
Provides: libtool(%{_libdir}/kde3/kcm_css.la)
Provides: libtool(%{_libdir}/kde3/kcm_icons.la)
Provides: libtool(%{_libdir}/kde3/kcm_screensaver.la)
Provides: libtool(%{_libdir}/kde3/kcm_taskbar.la)
Provides: libtool(%{_libdir}/kde3/kcm_crypto.la)
Provides: libtool(%{_libdir}/kde3/kcm_privacy.la)
Provides: libtool(%{_libdir}/kde3/kcm_smserver.la)
Provides: libtool(%{_libdir}/kde3/kcm_konsole.la)
Provides: libtool(%{_libdir}/kde3/kcm_spellchecking.la)
Provides: libtool(%{_libdir}/kde3/kcm_usb.la)
Provides: libtool(%{_libdir}/kde3/kcm_nic.la)
Provides: libtool(%{_libdir}/kde3/fontthumbnail.la)
Provides: libtool(%{_libdir}/kde3/libkfontviewpart.la)
Provides: libtool(%{_libdir}/kde3/kcm_fontinst.la)
Provides: libtool(%{_libdir}/kde3/kfile_font.la)
Provides: libtool(%{_libdir}/kde3/kio_fonts.la)
Provides: libtool(%{_libdir}/kde3/kcm_randr.la)
Provides: libtool(%{_libdir}/kde3/kcm_componentchooser.la)
Provides: libtool(%{_libdir}/kde3/kcm_performance.la)
Provides: libtool(%{_libdir}/kde3/kcm_xinerama.la)
Provides: libtool(%{_libdir}/kde3/kcm_display.la)
Provides: libtool(%{_libdir}/kde3/kcm_kthememanager.la)
Provides: libtool(%{_libdir}/kde3/kcm_joystick.la)
Provides: libtool(%{_libdir}/kde3/kdesktop.la)
Provides: libtool(%{_libdir}/libkonq.la)
Provides: libtool(%{_libdir}/libkateutils.la)
Provides: libtool(%{_libdir}/libkateinterfaces.la)
Provides: libtool(%{_libdir}/libkdeinit_kate.la)
Provides: libtool(%{_libdir}/libkdeinit_kwrite.la)
Provides: libtool(%{_libdir}/libkdeinit_kcminit.la)
Provides: libtool(%{_libdir}/libkdeinit_kcminit_startup.la)
Provides: libtool(%{_libdir}/libkdeinit_kjobviewer.la)
Provides: libtool(%{_libdir}/libkdeinit_kprinter.la)
Provides: libtool(%{_libdir}/libkdeinit_khelpcenter.la)
Provides: libtool(%{_libdir}/libkhotkeys_shared.la)
Provides: libtool(%{_libdir}/libkdeinit_khotkeys.la)
Provides: libtool(%{_libdir}/libkdeinit_klipper.la)
Provides: libtool(%{_libdir}/libkdeinit_kmenuedit.la)
Provides: libtool(%{_libdir}/libkdeinit_kcontroledit.la)
Provides: libtool(%{_libdir}/libkdeinit_konsole.la)
Provides: libtool(%{_libdir}/libksplashthemes.la)
Provides: libtool(%{_libdir}/libksgrd.la)
Provides: libtool(%{_libdir}/libkdecorations.la)
Provides: libtool(%{_libdir}/libkdeinit_kwin.la)
Provides: libtool(%{_libdir}/libkdeinit_kwin_rules_dialog.la)
Provides: libtool(%{_libdir}/libkdeinit_kxkb.la)
Provides: libtool(%{_libdir}/libkdeinit_konqueror.la)
Provides: libtool(%{_libdir}/libkdeinit_kfmclient.la)
Provides: libtool(%{_libdir}/libkdeinit_keditbookmarks.la)
Provides: libtool(%{_libdir}/libkonqsidebarplugin.la)
Provides: libtool(%{_libdir}/libkdeinit_ksmserver.la)
Provides: libtool(%{_libdir}/libkickermain.la)
Provides: libtool(%{_libdir}/libtaskmanager.la)
Provides: libtool(%{_libdir}/libtaskbar.la)
Provides: libtool(%{_libdir}/libkdeinit_kicker.la)
Provides: libtool(%{_libdir}/libkasbar.la)
Provides: libtool(%{_libdir}/libkdeinit_appletproxy.la)
Provides: libtool(%{_libdir}/libkdeinit_extensionproxy.la)
Provides: libtool(%{_libdir}/libkdeinit_kcontrol.la)
Provides: libtool(%{_libdir}/libkdeinit_kaccess.la)
Provides: libtool(%{_libdir}/libkfontinst.la)
Provides: libtool(%{_libdir}/libkdeinit_kdesktop.la)

%description
kdebase is the second mandatory package (besides kdelibs) for the K Desktop
Environment. Here we have various applications and infrastructure files and
libraries.


%prep
%setup -q
%patch -P 0 -p1


%build
%configure \
	--enable-pch \
	--enable-final \
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
%{__make} %{_smp_mflags}


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
	| sed -e 's,@kdm@,%{_bindir}/kdm,g' \
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
rm -f files.list ||:


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
/etc/xdg/menus/*
/etc/xdg/menus/applications-merged/
%{_libdir}/*
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
%dir %{_datadir}/locale/l10n
%{_datadir}/locale/*
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
%dir %{_datadir}/config/kdm
%{_datadir}/config/*
