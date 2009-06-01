Name: atk
Version: 1.12.4
Release: 1ev
Summary: An accessibility toolkit for GTK/GNOME
URL: http://ftp.gnome.org/pub/gnome/sources/atk/  
Group: System Environment/Librarires
License: LGPL
Vendor: MSP Slackware
Source: http://ftp.gnome.org/pub/gnome/sources/atk/1.12/atk-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: gcc-core, make >= 3.79.1, glib2 >= 2.0.0
Requires: glib2 >= 2.0.0
Provides: libtool(%{_libdir}/libatk-1.0.la)

%description
Accessibility is enabling people with disabilities to participate in
substantial life activities that include work and the use of services,
products, and information.


%prep
%setup -q


%build
%configure
make %{_smp_mflags}


%install
[ "$RPM_BUILD_ROOT" != '/' ] && rm -rf "${RPM_BUILD_ROOT}"
make install DESTDIR="$RPM_BUILD_ROOT"
rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir
%find_lang atk10


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != '/' ] && rm -rf "${RPM_BUILD_ROOT}"


%files -f atk10.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%doc %{_datadir}/gtk-doc/html/atk/
%{_includedir}/atk-1.0/
%{_libdir}/libatk-1.0.*
%{_libdir}/pkgconfig/atk.pc
