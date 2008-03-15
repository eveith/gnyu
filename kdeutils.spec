Name: kdeutils
Version: 3.5.6
Release: 1ev
Summary: Several helpful utilities for KDE
URL: http://www.kde.org/
Group: User Interface/Desktops
License: GPL, LGPL, BSD
Vendor: MSP Slackware
Source: http://download.kde.org/stable/%{version}/src/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-g++, qt3, kdelibs, kdebase, fontconfig, freetype
BuildRequires: zlib, libxml2 >= 2.4.8, libxslt >= 1.0.7, libstdc++, libart
BuildRequires: libICE, libX11, libSM, libXrender, libXrandr, libXext, expat

%description
* ark: manager for compressed files and archives
* kcalc: scientific calculator
* kcharselect: select special characters from any fonts and put them into
               the clipboard
* charselectapplet: dito, but as a Kicker applet
* kdepasswd: like 'passwd', a graphical password changer
* kdessh: front end to ssh
* kdf: like 'df', a graphical free disk space viewer
* kedit: a simple text editor, without formatting like bold, italics etc
* kfloppy: format a floppy disks with this app
* khexedit: binary file editor
* kjots: manages several "books" with a subject and notes
* klaptopdaemon: battery and power management, including KControl plugins
* kregexpeditor: graphical regular expression editor
* ktimer: execute programs after some time


%prep
%setup -q


%build
%configure \
	--enable-pch \
	--enable-final \
	--disable-debug \
	--disable-warnings \
	--without-xmms
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
%doc AUTHORS COPYING* README
%doc %{_datadir}/doc/HTML/en/*
%{_bindir}/ark
%{_bindir}/irkick
%{_bindir}/kcalc
%{_bindir}/kcharselect
%{_bindir}/kdessh
%{_bindir}/kdf
%{_bindir}/kedit
%{_bindir}/kfloppy
%{_bindir}/kgpg
%{_bindir}/khexedit
%{_bindir}/kjots
%{_bindir}/klaptop_acpi_helper
%{_bindir}/klaptop_check
%{_bindir}/kregexpeditor
%{_bindir}/ktimer
%{_bindir}/kwalletmanager
%{_bindir}/kwikdisk
%{_bindir}/superkaramba
%{_includedir}/*.h
%{_includedir}/ksim/
%{_libdir}/kde3/*.la
%{_libdir}/kde3/*.so
%{_libdir}/*.la
%{_libdir}/*.so*
%{_datadir}/applications/kde/*.desktop
%{_datadir}/applnk/Utilities/superkaramba.desktop
%{_datadir}/apps/ark/
%{_datadir}/apps/irkick/
%{_datadir}/apps/kcalc/
%{_datadir}/apps/kconf_update/*.upd
%{_datadir}/apps/kcharselect/
%{_datadir}/apps/kedit/
%{_datadir}/apps/kdf/
%{_datadir}/apps/kgpg/
%{_datadir}/apps/khexedit/
%{_datadir}/apps/khexedit2part/
%{_datadir}/apps/kicker/*/*.desktop
%{_datadir}/apps/kjots/
%{_datadir}/apps/klaptopdaemon/
%{_datadir}/apps/konqueror/servicemenus/*.desktop
%{_datadir}/apps/kregexpeditor/
%{_datadir}/apps/ksim/
%{_datadir}/apps/kwalletmanager/
%{_datadir}/apps/profiles/*.*
%{_datadir}/apps/remotes/
%{_datadir}/apps/superkaramba/
%{_datadir}/autostart/*.desktop
%{_datadir}/config.kcfg/*.kcfg
%{_datadir}/config/ksim_panelextensionrc
%{_datadir}/icons/*/*/*/*.png
%{_datadir}/icons/hicolor/scalable/*/*.svg*
%{_datadir}/icons/crystalsvg/scalable/*/*.svg*
%{_datadir}/mimelnk/application/x-superkaramba.desktop
%{_datadir}/services/*.desktop
%{_datadir}/services/kmilo/
%{_datadir}/services/kded/*.desktop
%{_datadir}/servicetypes/kmilo/
