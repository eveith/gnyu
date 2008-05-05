Name: gtkmm
Version: 2.12.3
Release: 1ev
Summary: The official C++ interface to GTK+
URL: http://www.gtkmm.org/
Group: System Environment/Libraries
License: LGPL
Vendor: GNyU-Linux
Source: http://ftp.gnome.org/pub/GNOME/sources/gtkmm/2.12/gtkmm-%version.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: coreutils, grep, sed, binutils, make, gcc-g++, pkg-config,
BuildRequires: libsigc++, gtk2, glibmm >= 2.14.1, atk >= 1.9.0, atk, perl, 
BuildRequires: pango >= 1.1.12, cairomm, libstdc++

%description
gtkmm is the official C++ interface for the popular GUI library GTK+. 
Highlights include typesafe callbacks, and a comprehensive set of widgets 
that are easily extensible via inheritance. 


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'

[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && %__rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc README* AUTHORS NEWS PORTING CHANGES demos examples
%doc docs/index.html docs/FAQ docs/images docs/tutorial docs/reference
%doc %{_datadir}/doc/%{name}-2.4
%doc %{_datadir}/devhelp
%{_bindir}/demo
%{_includedir}/atkmm-*/
%{_includedir}/gdkmm-*/
%{_includedir}/gtkmm-*/
%{_includedir}/pangomm-*/
%{_libdir}/gdkmm-*/
%{_libdir}/gtkmm-*/
%{_libdir}/libatkmm-*.so*
%{_libdir}/libatkmm-*.la
%{_libdir}/libgdkmm-*.so*
%{_libdir}/libgdkmm-*.la
%{_libdir}/libgtkmm-*.so*
%{_libdir}/libgtkmm-*.la
%{_libdir}/libpangomm-*.so*
%{_libdir}/libpangomm-*.la
%{_libdir}/pkgconfig/atkmm-*.pc
%{_libdir}/pkgconfig/gdkmm-*.pc
%{_libdir}/pkgconfig/gtkmm-*.pc
%{_libdir}/pkgconfig/pangomm-*.pc
