Name: x11-proto
Version: 7.2
Release: 1ev
Summary: Xorg protocol headers
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: MSP Slackware
Source0: applewmproto-1.0.3.tar.bz2
Source1: bigreqsproto-1.0.2.tar.bz2
Source2: compositeproto-0.3.1.tar.bz2
Source3: damageproto-1.0.3.tar.bz2
Source4: dmxproto-2.2.2.tar.bz2
Source5: evieext-1.0.2.tar.bz2
Source6: fixesproto-4.0.tar.bz2
Source7: fontcacheproto-0.1.2.tar.bz2
Source8: fontsproto-2.0.2.tar.bz2
Source9: glproto-1.4.8.tar.bz2
Source10: inputproto-1.3.2.tar.bz2
Source11: kbproto-1.0.3.tar.bz2
Source12: printproto-1.0.3.tar.bz2
Source13: randrproto-1.1.2.tar.bz2
Source14: recordproto-1.13.2.tar.bz2
Source15: renderproto-0.9.2.tar.bz2
Source16: resourceproto-1.0.2.tar.bz2
Source17: scrnsaverproto-1.1.0.tar.bz2
Source18: trapproto-3.4.3.tar.bz2
Source19: videoproto-2.2.2.tar.bz2
Source20: windowswmproto-1.0.3.tar.bz2
Source21: xcmiscproto-1.1.2.tar.bz2
Source22: xextproto-7.0.2.tar.bz2
Source23: xf86bigfontproto-1.1.2.tar.bz2
Source24: xf86dgaproto-2.0.2.tar.bz2
Source25: xf86driproto-2.0.3.tar.bz2
Source26: xf86miscproto-0.9.2.tar.bz2
Source27: xf86rushproto-1.1.2.tar.bz2
Source28: xf86vidmodeproto-2.2.2.tar.bz2
Source29: xineramaproto-1.1.2.tar.bz2
Source30: xproto-7.0.10.tar.bz2
Source31: xproxymanagementprotocol-1.0.2.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, gcc-g++, sed, gettext

%description
The Xorg protocol headers provide the header files required to build the
system, and to allow other applications to build against the installed X
Window system.


%prep
%setup -q -c -a0 -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 
%setup -q -c -D -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25 -a26
%setup -q -c -D -a27 -a28 -a29 -a30 -a31


%build
for dirname in $(ls -1)
do
	pushd "$dirname"
	%configure
	make %{_smp_mflags}
	popd
done


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
for dirname in $(ls -1)
do
	pushd "$dirname"
	make install DESTDIR="$RPM_BUILD_ROOT"
	cp COPYING ../COPYING-${dirname%%-*}
	popd
done


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc COPYING*
%dir %{_includedir}/GL
%{_includedir}/GL/*.h
%dir %{_includedir}/GL/internal
%{_includedir}/GL/internal/*.h
%dir %{_includedir}/X11
%{_includedir}/X11/*.h
%dir %{_includedir}/X11/extensions
%{_includedir}/X11/extensions/*.h
%dir %{_includedir}/X11/PM
%{_includedir}/X11/PM/*.h
%dir %{_includedir}/X11/dri
%{_includedir}/X11/dri/*.h
%dir %{_includedir}/X11/fonts
%{_includedir}/X11/fonts/*.h
%{_libdir}/pkgconfig/*.pc
