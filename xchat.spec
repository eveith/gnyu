Name: xchat
Version: 2.8.4
Release: 2ev
Summary: An IRC client ontop of the GTK+2 framework
URL: http://www.xchat.org/
Group: Applications/Communications
License: GPL-2
Vendor: GNyU-Linux
Source: http://www.xchat.org/files/source/2.8/xchat-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
Requires: glib2, dbus, gtk2, openssl
BuildRequires: gcc, gcc-g++, make >= 3.79.1, glib2, gtk2, dbus, openssl
BuildRequires: perl, python, startup-notification, atk, pango, zlib, libnotify
BuildRequires: libICE, libSM, libX11, libXau, libXdmcp, libXext, libXrender

%description
Xchat is a GTK2-based IRC client for X.


%prep
%setup -q


%build
%configure \
	--enable-ipv6 \
	--enable-openssl \
	--enable-perl \
	--enable-python \
	--disable-tcl \
	--enable-shm \
	--disable-textfe
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%find_lang xchat


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files -f xchat.lang
%defattr(-, root, root)
%doc AUTHORS COPYING README ChangeLog HACKING
%{_bindir}/xchat
%{_libdir}/xchat/
%{_datadir}/applications/xchat.desktop
%{_datadir}/pixmaps/xchat.png
%{_datadir}/dbus-1/services/org.xchat.service.service
