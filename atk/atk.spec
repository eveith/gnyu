Name: atk
Version: 1.26.0
Release: 2ev
Summary: An accessibility toolkit for GTK/GNOME
URL: http://ftp.gnome.org/pub/gnome/sources/atk/  
Group: System Environment/Librarires
License: LGPL-2.0
Vendor: GNyU-Linux
Source: http://ftp.gnome.org/pub/gnome/sources/atk/1.12/atk-%{version}.tar.bz2
BuildRequires: make, gcc, pkg-config >= 0.16, perl, gettext, glib2 >= 2.0.0

%description
Accessibility is enabling people with disabilities to participate in
substantial life activities that include work and the use of services,
products, and information.


%prep
	%setup -q


%build
	%configure
	make %{?_smp_mflags}


%install
	%{__make} install DESTDIR="${RPM_BUILD_ROOT}"
	%{__rm} -f ${RPM_BUILD_ROOT}/%{_infodir}/dir
	%find_lang atk10


%post
	%{__ldconfig}


%postun
	%{__ldconfig}


%files -f atk10.lang
	%defattr(-, root, root)
	%doc AUTHORS COPYING ChangeLog NEWS README
	%doc %{_datadir}/gtk-doc/html/atk/
	%{_includedir}/atk-1.0/
	%{_libdir}/libatk-1.0.*
	%{_libdir}/pkgconfig/atk.pc
