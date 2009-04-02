Name: xterm
Version: 229
Release: 1ev
Summary: A terminal emulator for the X Window System
URL: http://invisible-island.net/xterm/
Group: User Interface/X
License: MIT
Vendor: MSP Slackware
Source: ftp://invisible-island.net/xterm/xterm.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, pkg-config, luit, freetype, libXaw, libXt, zlib
BuildRequires: libICE, libSM, libX11, libXext, libXft, libXmu, libXrender
BuildRequires: fontconfig, libtermcap

%description
The xterm program is the standard terminal emulator for the X Window System.
It provides DEC VT102/VT220 and Tektronix 4014 compatible terminals for
programs that can't use the window system directly. If the underlying
operating system supports terminal resizing capabilities (for example, the
SIGWINCH signal in systems derived from 4.3bsd), xterm will use the facilities
to notify programs running in the window whenever it is resized.


%prep
%setup -q


%build
%configure \
	--enable-toolbar \
	--enable-load-vt-fonts \
	--enable-logging \
	--enable-256-color \
	--enable-readline-mouse \
	--enable-luit
make %{_smp_mflags}


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc README*
%{_bindir}/xterm
%{_bindir}/uxterm
%{_bindir}/resize
%{_libdir}/X11/app-defaults/*XTerm*
%{_mandir}/man1/resize.1*
%{_mandir}/man1/xterm.1*
%{_datadir}/pixmaps/xterm*.xpm
