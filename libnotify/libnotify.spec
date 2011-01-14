Name: libnotify
Version: 0.4.4
Release: 2ev
Summary: Desktop notification library
URL: http://www.galago-project.org/specs/notification/
Group: System Environment/Libraries
License: LGPL-2.1
Vendor: GNyU-Linux
Source: http://www.galago-project.org/files/releases/source/%{name}/%{name}-%{version}.tar.bz2
BuildRequires: pkg-config >= 0.9.0, make, gcc
BuildRequires: dbus >= 0.36, glib2 >= 2.6, gtk2 >= 2.6, dbus-glib >= 0.36

%description
libnotify is an implementation of the freedesktop.org desktop
notification specification.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
%{__ldconfig}


%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc NEWS README COPYING AUTHORS
%doc %{_datadir}/gtk-doc/html/libnotify
%{_bindir}/notify-send
%dir %{_includedir}/libnotify
%{_includedir}/libnotify/*.h
%{_libdir}/libnotify*.*
%{_libdir}/pkgconfig/libnotify.pc
