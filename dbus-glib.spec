Name: dbus-glib
Version: 0.74
Release: 1ev
Summary: Glib bindings for DBUS
URL: http://www.freedesktop.org/wiki/Software_2fdbus
Group: System Environment/Libraries
License: Academic Free License
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: http://dbus.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: dbus, make >= 3.79.1, gcc-core, glib2 >= 2.6, doxygen, expat

%description
A core concept of the D-BUS implementation is that "libdbus" is
intended to be a low-level API, similar to Xlib. Most programmers are
intended to use the bindings to GLib, Qt, Python, Mono, Java, or
whatever. These bindings have varying levels of completeness.


%prep
%setup -q


%build
%configure \
	--enable-doxygen-docs
%{__make} %{_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc AUTHORS COPYING HACKING README NEWS ChangeLog
%doc %{_datadir}/gtk-doc/html/dbus-glib/
%{_libdir}/libdbus-glib-1.*
%{_libdir}/pkgconfig/dbus-glib-1.pc
%{_bindir}/dbus-binding-tool
%{_includedir}/dbus-1.0/dbus/dbus-gtype-specialized.h
%{_includedir}/dbus-1.0/dbus/dbus-glib.h
%{_includedir}/dbus-1.0/dbus/dbus-glib-lowlevel.h
%{_includedir}/dbus-1.0/dbus/dbus-glib-error-enum.h
%{_includedir}/dbus-1.0/dbus/dbus-glib-bindings.h
