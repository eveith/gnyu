Name: pango
Version: 1.24.2
Release: 3ev
Summary: A framework for the layout and rendering of international text
URL: http://www.pango.org/
Group: System Environement/Libraries
License: LGPL
Vendor: GNyU-Linux
Source: http://ftp.gnome.org/pub/GNOME/sources/%{name}/1.24/%{name}-%{version}.tar.bz2
BuildRequires: make, pkg-config >= 0.9.0, gcc, perl
BuildRequires: glib2 >= 2.17.3, cairo >= 1.7.6, zlib
BuildRequires: fontconfig >= 2.5.0, freetype >= 2.1.5
BuildRequires: libXft >= 2.0.0, libXrender

%description
The goal of the Pango project is to provide an Open Source framework for the
layout and rendering of internationalized text. It uses Unicode for all of its
encoding, and will eventually support output in all the world's major
languages.


%prep
	%setup -q


%build
	%configure
	%{__make} %{?_smp_mflags}


%install
	%{__make} install DESTDIR='%{buildroot}'
	%{__rm} -f '%{buildroot}/%{_infodir}/dir'
	%{__touch} '%{buildroot}/%{_sysconfdir}/pango/pango.modules'


%post
	%{__ldconfig}
	%{_bindir}/pango-querymodules > '%{_sysconfdir}/pango/pango.modules'


%postun
	%{__ldconfig}


%files
	%defattr(-, root, root)
	%doc AUTHORS COPYING ChangeLog* HACKING MAINTAINERS NEWS README* THANKS
	%doc %{_datadir}/gtk-doc/html/pango
	%{_libdir}/libpango-1.0.*
	%{_libdir}/libpangox-1.0.*
	%{_libdir}/libpangoft2-1.0.*
	%{_libdir}/libpangoxft-1.0.*
	%{_libdir}/libpangocairo-1.0.*
	%{_libdir}/pango/
	%{_libdir}/pkgconfig/pango.pc
	%{_libdir}/pkgconfig/pangocairo.pc
	%{_libdir}/pkgconfig/pangox.pc
	%{_libdir}/pkgconfig/pangoxft.pc
	%{_libdir}/pkgconfig/pangoft2.pc
	%{_bindir}/pango-querymodules
	%{_bindir}/pango-view
	%{_includedir}/pango-1.0/
	%doc %{_mandir}/man1/pango-querymodules.1*
	%doc %{_mandir}/man1/pango-view.1*
	%doc %{_mandir}/man1/preload.1*
	%dir %{_sysconfdir}/pango
	%config %{_sysconfdir}/pango/pangox.aliases
	%ghost %config %{_sysconfdir}/pango/pango.modules
