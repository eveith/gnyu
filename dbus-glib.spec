Name: dbus-glib
Version: 0.82
Release: 2ev
Summary: Glib2 bindings for DBUS
URL: http://www.freedesktop.org/wiki/Software_2fdbus
Group: System Environment/Libraries
License: AFL-2.1
Vendor: GNyU-Linux
Source: http://dbus.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
BuildRequires: make, pkg-config, gcc
BuildRequires: dbus, glib2 >= 2.6, expat
BuildRequires: doxygen, gettext

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
%{__make} %{?_smp_mflags}
%{__make} check


%install
%{__make} install DESTDIR='%{buildroot}'


%post
%{__ldconfig}


%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc AUTHORS COPYING HACKING README NEWS ChangeLog
%doc %{_datadir}/gtk-doc/html/dbus-glib/
%doc %{_mandir}/man1/dbus-binding-tool.1*
%{_sysconfdir}/bash_completion.d/dbus-bash-completion.sh
%{_libdir}/libdbus-glib-1.*
%{_libdir}/pkgconfig/dbus-glib-1.pc
%{_libexecdir}/dbus-bash-completion-helper
%{_bindir}/dbus-binding-tool
%{_includedir}/dbus-1.0/dbus/dbus-gtype-specialized.h
%{_includedir}/dbus-1.0/dbus/dbus-glib.h
%{_includedir}/dbus-1.0/dbus/dbus-glib-lowlevel.h
%{_includedir}/dbus-1.0/dbus/dbus-glib-error-enum.h
%{_includedir}/dbus-1.0/dbus/dbus-glib-bindings.h
