Name: kdeutils4
Version: 4.3.2
Release: 3.0ev
Summary: A compilation of various utilities for KDE 4
URL: http://www.kde.org/
Group: User Interface/Desktop
License: GPL-2, LGPL-2.1, FDL-1.2
Vendor: GNyU-Linux
Source: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdeutils-%{version}.tar.bz2
BuildRequires: cmake >= 2.6.2, make, flex, bison, gcc-g++, perl, gettext
BuildRequires: libX11, libSM, libICE, libXrender, libXt, libxkbfile
BuildRequires: qt4 >= 4.5.0, automoc4 >= 0.9.88
BuildRequires: kdelibs4 = %{version}, kdelibs4-experimental = %{version}
BuildRequires: kdebase4 = %{version}, kdebindings4 = %{version}
BuildRequires: qimageblitz, gmp, zlib, libzip, libarchive
BuildRequires: python, python-PyQt4, python-PyKDE4, pycups

%description
The package contains various utilties for the KDE 4 desktop:
   - ark, an archiving tool,
   - various Cmake modules,
   - kcalc, a scientific calculator,
   - kdessh, a KDE frontend to SSH,
   - kcharselect, a special character selector,
   - kdf, a frontend to df (a disk space viewer),
   - kfloppy to format floppy disks,
   - kgpg, a graphical GnuPG frontend,
   - kwallet, the KDE wallet management tool (a password safe),
   - okteta, a binary/hex file viewer,
   - the printer applet for the system tray,
   - superkaramba for even more desktop applets, and
   - sweeper, a utility that clean unwanted traces the user may leave.


%prep
	%setup -q -n 'kdeutils-%{version}'


%build
	%{cmake} \
		-DQT_QMAKE_EXECUTABLE:FILEPATH='%{_libdir}/qt4/bin/qmake' \
		.
	%{__make} %{?_smp_mflags}


%install
	%{__make} install DESTDIR='%{buildroot}'


%post
	%{__ldconfig}


%postun
	%{__ldconfig}


%files
	%defattr(-, root, root)
	%doc README COPYING* AUTHORS
	%doc %{_datadir}/doc/HTML/en/*
	%config %{_sysconfdir}/kde4/superkaramba.knsrc
	%{_bindir}/ark
	%{_bindir}/irkick
	%{_bindir}/kcalc
	%{_bindir}/kcharselect
	%{_bindir}/kdessh
	%{_bindir}/kdf
	%{_bindir}/kfloppy
	%{_bindir}/kgpg
	%{_bindir}/ktimer
	%{_bindir}/kwalletmanager
	%{_bindir}/kwikdisk
	%{_bindir}/okteta
	%{_bindir}/superkaramba
	%{_bindir}/sweeper
	%{_libdir}/kde4/*.so
	%{_libdir}/libkdeinit4_irkick.so
	%{_libdir}/libkdeinit4_kcalc.so
	%{_libdir}/libkdelirc_shared.so*
	%{_libdir}/libkerfuffle.so*
	%{_libdir}/liboktetacore.so*
	%{_libdir}/liboktetagui.so*
	%{_libdir}/libsuperkaramba.so*
	%doc %{_mandir}/man1/ark.1*
	%{_datadir}/applications/kde4/*.desktop
	%dir %{_datadir}/apps/ark
	%{_datadir}/apps/ark/ark*.rc
	%dir %{_datadir}/apps/irkick
	%{_datadir}/apps/irkick/irkick.notifyrc
	%dir %{_datadir}/apps/kcalc
	%{_datadir}/apps/kcalc/kcalcui.rc
	%{_datadir}/apps/kcalc/scienceconstants.xml
	%dir %{_datadir}/apps/kcharselect
	%{_datadir}/apps/kcharselect/kcharselectui.rc
	%dir %{_datadir}/apps/kconf_update
	%{_datadir}/apps/kconf_update/kcalcrc.upd
	%{_datadir}/apps/kconf_update/kcharselect.upd
	%dir %{_datadir}/apps/kdf
	%{_datadir}/apps/kdf/kdfui.rc
	%dir %{_datadir}/apps/kgpg
	%{_datadir}/apps/kgpg/keysmanager.rc
	%{_datadir}/apps/kgpg/kgpg.rc
	%dir %{_datadir}/apps/kgpg/icons
	%dir %{_datadir}/apps/kgpg/icons/oxygen
	%{_datadir}/apps/kgpg/icons/oxygen/*
	%dir %{_datadir}/apps/kgpg/pics
	%{_datadir}/apps/kgpg/pics/kgpg_anim.gif
	%{_datadir}/apps/kgpg/tips
	%dir %{_datadir}/apps/kwalletmanager
	%dir %{_datadir}/apps/kwalletmanager/icons
	%dir %{_datadir}/apps/kwalletmanager/icons/oxygen
	%{_datadir}/apps/kwalletmanager/icons/oxygen/*
	%{_datadir}/apps/kwalletmanager/kwalleteditor.rc
	%{_datadir}/apps/kwalletmanager/kwalletmanager.rc
	%dir %{_datadir}/apps/okteta
	%{_datadir}/apps/okteta/oktetaui.rc
	%dir %{_datadir}/apps/oktetapart
	%{_datadir}/apps/oktetapart/oktetapartui.rc
	%dir %{_datadir}/apps/profiles
	%{_datadir}/apps/profiles/*.profile.xml
	%{_datadir}/apps/profiles/profile.dtd
	%dir %{_datadir}/apps/remotes
	%{_datadir}/apps/remotes/*.remote.xml
	%{_datadir}/apps/remotes/remote.dtd
	%dir %{_datadir}/apps/superkaramba
	%{_datadir}/apps/superkaramba/superkarambaui.rc
	%dir %{_datadir}/apps/sweeper
	%{_datadir}/apps/sweeper/sweeperui.rc
	%{_datadir}/autostart/kgpg.desktop
	%{_datadir}/autostart/irkick.desktop
	%{_datadir}/config.kcfg/*.kcfg
	%{_datadir}/dbus-1/interfaces/org.kde.*.xml
	%{_datadir}/icons/*/*/*/*.*
	%{_datadir}/kde4/services/ServiceMenus/*.desktop
	%{_datadir}/kde4/services/*.desktop
	%{_datadir}/kde4/servicetypes/*.desktop
