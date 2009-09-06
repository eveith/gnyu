Name: gnokii
Version: 0.6.14
Release: 1ev
Summary: An application to communicate with various (Nokia) mobile phones
URL: http://www.gnokii.org/
Group: Applications/Communications
License: GPL
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: http://www.gnokii.org/download/gnokii/gnokii-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc-core, libusb, gettext, gtk2
Requires: libusb
Provides: libtool(%{_libdir}/libgnokii.la)

%description
gnokii allows you to communicate with the phone over the serial cable
connection, usb connection (support depends mostly on the operatins system
level support), infrared connection and bluetooth connection.
gnokii provides many functionality of different areas for user to manipulate
mobile phone.

%package gtk2
Summary: A X/GTK2-based frontend to gnokii
Group: Applications/Communications
Requires: gtk2

%description gtk2
gnokii-x11 is a frontend to gnokii for X11.


%prep
%setup -q


%build
%configure \
	--enable-security


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"

rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir
%find_lang gnokii


%post

%postun


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files -f gnokii.lang
%defattr(-, root, root)
%doc ABOUT-NLS COPYING COPYRIGHT ChangeLog MAINTAINERS TODO VERSION
%doc Docs/
%{_bindir}/gnokii
%{_bindir}/todologo
%{_bindir}/sendsms
%{_bindir}/ppm2nokia
%{_bindir}/waitcall
%{_sbindir}/gnokiid
%{_sbindir}/mgnokiidev
%{_libdir}/libgnokii*.*
%{_libdir}/pkgconfig/gnokii.pc
%{_includedir}/gnokii/
%{_includedir}/gnokii.h
%{_datadir}/doc/gnokii/

%files gtk2
%{_datadir}/xgnokii/
%{_libdir}/pkgconfig/xgnokii.pc
%{_datadir}/applications/xgnokii.desktop
%{_bindir}/xgnokii
