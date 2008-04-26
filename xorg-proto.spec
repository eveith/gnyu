Name: x11-proto
Version: 7.2
Release: 3ev
Summary: Xorg protocol headers
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: MSP Slackware
Source0: http://xorg.freedesktop.org/releases/individual/proto/applewmproto-1.0.3.tar.bz2
Source1: http://xorg.freedesktop.org/releases/individual/proto/bigreqsproto-1.0.2.tar.bz2
Source2: http://xorg.freedesktop.org/releases/individual/proto/compositeproto-0.4.tar.bz2
Source3: http://xorg.freedesktop.org/releases/individual/proto/damageproto-1.1.0.tar.bz2
Source4: http://xorg.freedesktop.org/releases/individual/proto/dmxproto-2.2.2.tar.bz2
Source5: http://xorg.freedesktop.org/releases/individual/proto/evieext-1.0.2.tar.bz2
Source6: http://xorg.freedesktop.org/releases/individual/proto/fixesproto-4.0.tar.bz2
Source7: http://xorg.freedesktop.org/releases/individual/proto/fontcacheproto-0.1.2.tar.bz2
Source8: http://xorg.freedesktop.org/releases/individual/proto/fontsproto-2.0.2.tar.bz2
Source9: http://xorg.freedesktop.org/releases/individual/proto/glproto-1.4.8.tar.bz2
Source10: http://xorg.freedesktop.org/releases/individual/proto/inputproto-1.4.3.tar.bz2
Source11: http://xorg.freedesktop.org/releases/individual/proto/kbproto-1.0.3.tar.bz2
Source12: http://xorg.freedesktop.org/releases/individual/proto/printproto-1.0.3.tar.bz2
Source13: http://xorg.freedesktop.org/releases/individual/proto/randrproto-1.2.1.tar.bz2
Source14: http://xorg.freedesktop.org/releases/individual/proto/recordproto-1.13.2.tar.bz2
Source15: http://xorg.freedesktop.org/releases/individual/proto/renderproto-0.9.2.tar.bz2
Source16: http://xorg.freedesktop.org/releases/individual/proto/resourceproto-1.0.2.tar.bz2
Source17: http://xorg.freedesktop.org/releases/individual/proto/scrnsaverproto-1.1.0.tar.bz2
Source18: http://xorg.freedesktop.org/releases/individual/proto/trapproto-3.4.3.tar.bz2
Source19: http://xorg.freedesktop.org/releases/individual/proto/videoproto-2.2.2.tar.bz2
Source20: http://xorg.freedesktop.org/releases/individual/proto/windowswmproto-1.0.3.tar.bz2
Source21: http://xorg.freedesktop.org/releases/individual/proto/xcmiscproto-1.1.2.tar.bz2
Source22: http://xorg.freedesktop.org/releases/individual/proto/xextproto-7.0.2.tar.bz2
Source23: http://xorg.freedesktop.org/releases/individual/proto/xf86bigfontproto-1.1.2.tar.bz2
Source24: http://xorg.freedesktop.org/releases/individual/proto/xf86dgaproto-2.0.2.tar.bz2
Source25: http://xorg.freedesktop.org/releases/individual/proto/xf86driproto-2.0.4.tar.bz2
Source26: http://xorg.freedesktop.org/releases/individual/proto/xf86miscproto-0.9.2.tar.bz2
Source27: http://xorg.freedesktop.org/releases/individual/proto/xf86rushproto-1.1.2.tar.bz2
Source28: http://xorg.freedesktop.org/releases/individual/proto/xf86vidmodeproto-2.2.2.tar.bz2
Source29: http://xorg.freedesktop.org/releases/individual/proto/xineramaproto-1.1.2.tar.bz2
Source30: http://xorg.freedesktop.org/releases/individual/proto/xproto-7.0.10.tar.bz2
Source31: http://xorg.freedesktop.org/releases/individual/proto/xproxymanagementprotocol-1.0.2.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, gcc-g++, sed, gettext, gawk
BuildArch: noarch

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
	pushd "${dirname}"
	%configure
	%{__make} %{?_smp_mflags}
	popd
done


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
for dirname in $(ls -1)
do
	pushd "${dirname}"
	%{__make_install} DESTDIR='%{buildroot}'
	%{__cp} COPYING "../COPYING-${dirname%%-*}"
	popd
done

%{__mv} '%{buildroot}/%{_datadir}/doc'/*/*.txt \
	"${RPM_BUILD_DIR}/%{name}-%{version}"
%{__rm} -rf '%{buildroot}/%{_datadir}'


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc COPYING* *.txt
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
