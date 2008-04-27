Name: x11-server
Version: 1.3.0.0
Release: 3ev
Summary: The X Server
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://ftp.x.org/pub/individual/xserver/xorg-server-%{version}.tar.bz2
Patch0: %{name}-1.3.0.0-fix-xkb-openoffice-hangs.patch
Patch1: %{name}-1.3.0.0-fix-dual-head-screen-resolutions.patch
Patch2: %{name}-1.3.0.0-fix-randr-resizing.patch
Patch3: %{name}-1.3.0.0-fix-xephyr-amd64-segfault.patch
Patch4: %{name}-1.3.0.0-ramdac.patch
Patch5: %{name}-use-composite-for-unequal-depths.patch
Patch6: %{name}-1.2.0-fix-amd-cpu-detection.patch
Patch7: %{name}-1.2.0-properly-free-device-devprivates-memory-leak-fix.patch
Patch8: %{name}-1.2.0-typo-fix.patch
Patch9: %{name}-1.2.0-zero-out-client-devprivates-on-allocation.patch
Patch10: %{name}-1.3.0.0-use-proc-instead-of-sys.patch
Patch11: %{name}-avoid-crash-on-minimized-xv-window.patch
Patch12: %{name}-xorg-server-sam225bw-quirks.patch
Patch13: %{name}-1.3-alpha-build-fix.patch
Patch14: %{name}-1.3.0.0-xephyr_crash_at_exit.patch
Patch15: %{name}-xorg-x11-server-1.0.1-fpic-libxf86config.patch
Patch16: %{name}-1.4-0001-Fix-for-CVE-2007-5760-XFree86-Misc-extension-out-o.patch
Patch17: %{name}-1.4-0002-Fix-for-CVE-2007-6428-TOG-cup-extension-memory-cor.patch
Patch18: %{name}-1.3-0003-Fix-for-CVE-2007-6427-Xinput-extension-memory-corr.patch
Patch19: %{name}-1.4-0004-Fix-for-CVE-2007-6429-MIT-SHM-and-EVI-extensions-i.patch
Patch20: %{name}-1.4-0005-Fix-for-CVE-2008-0006-PCF-Font-parser-buffer-overf.patch
Patch21: %{name}-1.3-0006-Fix-for-CVE-2007-5958-File-existence-disclosure.patch
Patch22: %{name}-1.4-0007-CVE-2007-6429-Don-t-spuriously-reject-8bpp-shm-pix.patch
Patch23: %{name}-1.4-0008-CVE-2007-6429-Always-test-for-size-offset-wrapping.patch
Patch24: %{name}-1.4-0009-Don-t-break-grab-and-focus-state-for-a-window-when-r.patch
Patch25: %{name}-xorg-server-1.4.0.90-automake-1.10.1-fixup.patch
Patch26: xorg-server-1.2.0-xcmisc-1.patch
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: coreutils, sed, grep, make, gcc, pkg-config, zlib, mesalib
BuildRequires: x11-fonts, xkeyboard-config, libdrm, libICE, libSM, libX11
BuildRequires: libXau, libXaw, libXdmcp, libXext, libXfixes, libXrender
BuildRequires: libXfont, libXi, libXmu, libXpm, libxcb, libxkbfile, libXt
BuildRequires: libXxf86misc, libpciaccess >= 0.8.0, flex, bison, dbus, hal
BuildRequires: freetype >= 2.0.0, ncurses

%description
The Xorg Server is the core of the X Window system.


%prep
%setup -q -n xorg-server-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p0
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p0
%{__aclocal}
%{__automake} --add-missing
%{__autoconf}


%build
%configure \
	--with-os-vendor='GNyU Linux' \
	--with-module-dir=%{_libdir}/X11/modules \
	--with-dri-driver-path=%{_libdir}/X11/modules/dri \
	--with-xkb-output=%{_localstatedir}/lib/xkb \
	--disable-xprint \
	--disable-dmx \
	--enable-install-setuid \
	--enable-xorgcfg \
	--enable-kdrive \
	--enable-xephyr
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'

%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/X11/Xsession.d'
touch '%{buildroot}/%{_sysconfdir}/X11/xorg.conf'


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc COPYING
%dir %{_sysconfdir}/X11
%ghost %config(noreplace) %{_sysconfdir}/X11/xorg.conf
%dir %{_sysconfdir}/X11/Xsession.d
%{_bindir}/X
%{_bindir}/Xfake
%{_bindir}/Xneomagic
%{_bindir}/Xnest
%attr(4755, root, root) %{_bindir}/Xorg
%{_bindir}/Xvfb
%{_bindir}/cvt
%{_bindir}/gtf
%{_bindir}/inb
%{_bindir}/inl
%{_bindir}/inw
%{_bindir}/ioport
%{_bindir}/outb
%{_bindir}/outl
%{_bindir}/outw
%{_bindir}/pcitweak
%{_bindir}/scanpci
%{_bindir}/xorgcfg
%{_bindir}/xorgconfig
%{_bindir}/Xati
%{_bindir}/Xchips
%{_bindir}/Xephyr
%{_bindir}/Xepson
%{_bindir}/Xfbdev
%{_bindir}/Xi810
%{_bindir}/Xmach64
%{_bindir}/Xmga
%{_bindir}/Xnvidia
%{_bindir}/Xpm2
%{_bindir}/Xr128
%{_bindir}/Xsdl
%{_bindir}/Xsmi
%{_bindir}/Xvesa
%{_bindir}/Xvia
%{_includedir}/xorg/
%{_includedir}/X11/pixmaps/
%{_includedir}/X11/bitmaps/
%{_libdir}/X11/Cards/
%{_libdir}/X11/Options/
%{_libdir}/X11/modules/
%{_libdir}/xserver/
%{_libdir}/pkgconfig/xorg-server.pc
%{_mandir}/man1/Xnest.1*
%{_mandir}/man1/Xorg.1*
%{_mandir}/man1/Xserver.1*
%{_mandir}/man1/Xvfb.1*
%{_mandir}/man1/cvt.1*
%{_mandir}/man1/gtf.1*
%{_mandir}/man1/pcitweak.1*
%{_mandir}/man1/scanpci.1*
%{_mandir}/man1/xorgcfg.1*
%{_mandir}/man1/xorgconfig.1*
%{_mandir}/man4/exa.4*
%{_mandir}/man4/fbdevhw.4*
%{_mandir}/man5/xorg.conf.5*
%{_datadir}/X11/app-defaults/XOrgCfg
%{_datadir}/aclocal/xorg-server.m4
%dir %{_localstatedir}/lib/xkb
%{_localstatedir}/lib/xkb/README.compiled
