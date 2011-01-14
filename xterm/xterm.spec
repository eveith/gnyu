Name: xterm
Version: 243
Release: 2ev
Summary: A terminal emulator for the X Window System
URL: http://invisible-island.net/xterm/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: ftp://invisible-island.net/xterm/xterm.tar.gz
BuildRequires: make, gcc, pkg-config, luit, freetype
BuildRequires: libICE, libX11, libXt, libXaw, libSM
BuildRequires: fontconfig, ncurses, zlib

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
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR="${RPM_BUILD_ROOT}"


%files
%defattr(-, root, root)
%doc README*
%{_bindir}/xterm
%{_bindir}/uxterm
%{_bindir}/koi8rxterm
%{_bindir}/resize
%{_libdir}/X11/app-defaults/*XTerm*
%doc %{_mandir}/man1/resize.1*
%doc %{_mandir}/man1/*xterm.1*
%{_datadir}/pixmaps/xterm*.xpm
