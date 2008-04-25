Name: x11-server
Version: 1.4.0.90
Release: 1ev
Summary: The X Server
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: MSP Slackware
Source: http://ftp.x.org/pub/individual/xserver/xorg-server-%{version}.tar.bz2
Patch: xorg-server-1.2.0-xcmisc-1.patch
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, pkg-config, x11-fonts, xkeyboard-config, zlib
BuildRequires: mesalib, libdrm, libICE, libSM, libX11, libXau, libXaw
BuildRequires: libXdmcp, libXext, libXfixes, libXrender, libXfont, libXi
BuildRequires: libXi, libXmu, libXpm, libxcb, libxkbfile, libXt, libXxf86misc

%description
The Xorg Server is the core of the X Window system.


%prep
%setup -q -n xorg-server-%{version}
# %patch0 -p1


%build
%configure \
	--with-module-dir=%{_libdir}/X11/modules \
	--with-dri-driver-path=%{_libdir}/X11/modules/dri \
	--with-xkb-output=/%{_var}/lib/xkb \
	--enable-install-setuid \
	--enable-xorgcfg \
	--enable-kdrive \
	--enable-xephyr
%{__make} %{_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
touch %{buildroot}/etc/X11/xorg.conf


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc COPYING
%dir /etc/X11
%ghost %config(noreplace) /etc/X11/xorg.conf
%dir /etc/X11/Xsession.d
/etc/X11/Xsession.d/92xprint-xpserverlist
%{_bindir}/X
%{_bindir}/Xdmx
%{_bindir}/Xnest
%{_bindir}/Xorg
%{_bindir}/Xprt
%{_bindir}/Xvfb
%{_bindir}/cvt
%{_bindir}/dmxaddinput
%{_bindir}/dmxaddscreen
%{_bindir}/dmxreconfig
%{_bindir}/dmxresize
%{_bindir}/dmxrminput
%{_bindir}/dmxrmscreen
%{_bindir}/dmxtodmx
%{_bindir}/dmxwininfo
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
%{_bindir}/vdltodmx
%{_bindir}/xdmx
%{_bindir}/xdmxconfig
%{_bindir}/xorgcfg
%{_bindir}/xorgconfig
%{_bindir}/Xati
%{_bindir}/Xchips
%{_bindir}/Xephyr
%{_bindir}/Xepson
%{_bindir}/Xfake
%{_bindir}/Xfbdev
%{_bindir}/Xi810
%{_bindir}/Xmach64
%{_bindir}/Xmga
%{_bindir}/Xneomagic
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
%{_libdir}/X11/xserver/
%{_libdir}/X11/Cards/
%{_libdir}/X11/Options/
%{_libdir}/X11/modules/
%{_libdir}/xserver/
%{_libdir}/pkgconfig/xorg-server.pc
%{_mandir}/man1/Xdmx.1*
%{_mandir}/man1/Xnest.1*
%{_mandir}/man1/Xorg.1*
%{_mandir}/man1/Xprt.1*
%{_mandir}/man1/Xserver.1*
%{_mandir}/man1/Xvfb.1*
%{_mandir}/man1/cvt.1*
%{_mandir}/man1/dmxtodmx.1*
%{_mandir}/man1/gtf.1*
%{_mandir}/man1/pcitweak.1*
%{_mandir}/man1/scanpci.1*
%{_mandir}/man1/vdltodmx.1*
%{_mandir}/man1/xdmxconfig.1*
%{_mandir}/man1/xorgcfg.1*
%{_mandir}/man1/xorgconfig.1*
%{_mandir}/man4/exa.4*
%{_mandir}/man4/fbdevhw.4*
%{_mandir}/man5/xorg.conf.5*
%{_datadir}/X11/app-defaults/XOrgCfg
%{_datadir}/aclocal/xorg-server.m4
%dir /%{_var}/lib/xkb
/%{_var}/lib/xkb/README.compiled
