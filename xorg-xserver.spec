Name: xorg-xserver
Version: 1.5.3
Release: 7ev
Summary: The X Server
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://ftp.x.org/pub/individual/xserver/xorg-server-%{version}.tar.bz2
BuildRequires: make, gcc, pkg-config >= 0.9.0, flex, bison
BuildRequires: zlib, openssl, perl
BuildRequires: dbus, hal, mesalib >= 7.1.0, libdrm >= 2.3.2
BuildRequires: xorg-glproto >= 1.4.9, xorg-xf86driproto >= 2.0.4
BuildRequires: xorg-xextproto, xorg-xineramaproto, xorg-fontcacheproto
BuildRequires: xorg-renderproto, xorg-randrproto >= 1.2, xorg-dri2proto >= 1.1
BuildRequires: xorg-xf86dgaproto, xorg-xf86miscproto, xorg-xf86vidmodeproto
BuildRequires: xorg-fixesproto >= 4.0, xorg-damageproto >= 1.1
BuildRequires: xorg-scrnsaverproto >= 1.1, xorg-bigreqsproto
BuildRequires: xorg-resourceproto, xorg-fontsproto, xorg-inputproto >= 1.4.4
BuildRequires: xorg-kbproto >= 1.0.3, xorg-videoproto
BuildRequires: xorg-compositeproto >= 0.4, xorg-evieext
BuildRequires: xorg-xcmiscproto, xorg-xproto >= 7.0.9
BuildRequires: libX11, libXi, libxkbfile, libXdmcp, libXfont, libXext, libXau
BuildRequires: libXrender, libxkbui >= 1.0.2, libXmu, libXt, libXpm
BuildRequires: libXxf86vm, libXxf86misc, libXres, xtrans, libfontenc
BuildRequires: x11-fonts
BuildRequires: libsdl >= 1.2, libpciaccess >= 0.8.0
BuildRequires: freetype >= 2.0.0, ncurses
Requires: xorg-fslayout >= 7.3
Provides: x11-server = %{version}-%{release}
Provides: xorg-server = %{version}-%{release}
Obsoletes: x11-server < %{version}

%description
The Xorg Server is the core of the X Window system.


%prep
%setup -q -n xorg-server-%{version}


%build
%configure \
	--enable-aiglx \
	--enable-dri \
	--enable-xorg \
	--with-vendor-name='%{_vendor}' \
	--with-os-vendor='GNyU Linux' \
	--with-xkb-output='%{_localstatedir}/lib/xkb' \
	--disable-xprint \
	--enable-install-setuid \
	--enable-xorgcfg \
	--enable-kdrive \
	--enable-xephyr
%{__make} %{?_smp_mflags}


%install
%{__make_install} DESTDIR='%{buildroot}'

%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/X11/Xsession.d'
touch '%{buildroot}/%{_sysconfdir}/X11/xorg.conf'


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc COPYING
%dir %{_sysconfdir}/X11
%ghost %config(noreplace) %{_sysconfdir}/X11/xorg.conf
%dir %{_sysconfdir}/X11/Xsession.d
%{_bindir}/X
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
#%{_bindir}/pcitweak
#%{_bindir}/scanpci
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
%{_libdir}/X11/Cards
%{_libdir}/X11/Options
%{_libdir}/xorg/modules/*.??
%{_libdir}/xorg/modules/extensions/*.??
%{_libdir}/xorg/modules/fonts/*.??
%{_libdir}/xorg/modules/linux/*.??
%{_libdir}/xorg/modules/multimedia/*.??
#%{_libdir}/xserver/
%{_libdir}/pkgconfig/xorg-server.pc
%doc %{_libdir}/xorg/protocol.txt
%doc %{_mandir}/man1/Xnest.1*
%doc %{_mandir}/man1/Xorg.1*
%doc %{_mandir}/man1/Xserver.1*
%doc %{_mandir}/man1/Xvfb.1*
%doc %{_mandir}/man1/cvt.1*
%doc %{_mandir}/man1/gtf.1*
#%doc %{_mandir}/man1/pcitweak.1*
#%doc %{_mandir}/man1/scanpci.1*
%doc %{_mandir}/man1/xorgcfg.1*
%doc %{_mandir}/man1/xorgconfig.1*
%doc %{_mandir}/man4/exa.4*
%doc %{_mandir}/man4/fbdevhw.4*
%doc %{_mandir}/man5/xorg.conf.5*
#%doc %{_mandir}/man5/SecurityPolicy.5*
%{_datadir}/X11/app-defaults/XOrgCfg
%{_datadir}/aclocal/xorg-server.m4
%dir %{_localstatedir}/lib/xkb
%{_localstatedir}/lib/xkb/README.compiled
