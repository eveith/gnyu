Name: gnokii
Version: 0.6.27
Release: 2ev
Summary: An application to communicate with various (Nokia) mobile phones
URL: http://www.gnokii.org/
Group: Applications/Communications
License: GPL
Vendor: GNyU-Linux
Source: http://www.gnokii.org/download/gnokii/gnokii-%{version}.tar.bz2
BuildRequires: pkgconfig >= 0.9.0, make, gcc, gettext
BuildRequires: libX11, libXpm, libusb, bluez, glib2, gtk2

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
%{__make} install DESTDIR="${RPM_BUILD_ROOT}"
%find_lang gnokii


%post
%{__ldconfig}


%postun
%{__ldconfig}


%files -f gnokii.lang
%defattr(-, root, root)
%doc AUTHORS COPYING COPYRIGHT ChangeLog MAINTAINERS TODO
%doc Docs/
%{_bindir}/gnokii
%{_bindir}/sendsms
%{_bindir}/gnokiid
%{_bindir}/smsd
%{_sbindir}/mgnokiidev
%dir %{_libdir}/smsd
%{_libdir}/smsd/libsmsd_*.*
%{_libdir}/libgnokii*.*
%{_libdir}/pkgconfig/gnokii.pc
%{_includedir}/gnokii/
%{_includedir}/gnokii.h
%dir %{_datadir}/doc/gnokii/
%doc %{_datadir}/doc/gnokii/*
%doc %{_mandir}/man1/gnokii.1*
%doc %{_mandir}/man1/sendsms.1*
%doc %{_mandir}/man8/gnokiid.8*
%doc %{_mandir}/man8/mgnokiidev.8*
%doc %{_mandir}/man8/smsd.8*

%files gtk2
%defattr(-, root, root)
%doc COPYING COPYRIGHT ChangeLog MAINTAINERS TODO AUTHORS
%doc Docs/
%{_datadir}/xgnokii/
%{_libdir}/pkgconfig/xgnokii.pc
%{_datadir}/applications/xgnokii.desktop
%{_bindir}/xgnokii
%doc %{_mandir}/man1/xgnokii.1x*
