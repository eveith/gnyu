Name: pango
Version: 1.16.5
Release: 1ev
Summary: A framework for the layout and rendering of international text
URL: http://www.pango.org/
Group: System Environement/Libraries
License: LGPL
Vendor: MSP Slackware
Source: http://ftp.gnome.org/pub/GNOME/sources/%{name}/1.16/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc-core, glib2 >= 2.10.0, fontconfig
BuildRequires: freetype >= 2.0.4, cairo
Requires: glib2 >= 2.10.0, fontconfig, freetype >= 2.0.4, cairo
Provides: libtool(%{_libdir}/libpango-1.0.la)
Provides: libtool(%{_libdir}/libpangox-1.0.la)
Provides: libtool(%{_libdir}/libpangoft2-1.0.la)
Provides: libtool(%{_libdir}/libpangoxft-1.0.la)
Provides: libtool(%{_libdir}/libpangocairo-1.0.la)
Provides: libtool(%{_libdir}/pango/1.5.0/modules/pango-arabic-fc.la)
Provides: libtool(%{_libdir}/pango/1.5.0/modules/pango-arabic-lang.la)
Provides: libtool(%{_libdir}/pango/1.5.0/modules/pango-basic-x.la)
Provides: libtool(%{_libdir}/pango/1.5.0/modules/pango-basic-fc.la)
Provides: libtool(%{_libdir}/pango/1.5.0/modules/pango-hangul-fc.la)
Provides: libtool(%{_libdir}/pango/1.5.0/modules/pango-hebrew-fc.la)
Provides: libtool(%{_libdir}/pango/1.5.0/modules/pango-indic-fc.la)
Provides: libtool(%{_libdir}/pango/1.5.0/modules/pango-indic-lang.la)
Provides: libtool(%{_libdir}/pango/1.5.0/modules/pango-khmer-fc.la)
Provides: libtool(%{_libdir}/pango/1.5.0/modules/pango-syriac-fc.la)
Provides: libtool(%{_libdir}/pango/1.5.0/modules/pango-thai-fc.la)
Provides: libtool(%{_libdir}/pango/1.5.0/modules/pango-tibetan-fc.la)

%description
The goal of the Pango project is to provide an Open Source framework for the
layout and rendering of internationalized text. It uses Unicode for all of its
encoding, and will eventually support output in all the world's major
languages.


%prep
%setup -q


%build
if [ -r "%{_prefix}/X11R6/lib/pkgconfig/xft.pc" -a \
		! -r "%{_libdir}/pkgconfig/xft.pc" ]
then
	export PKG_CONFIG_PATH="${PKG_CONFIG_PATH}:%{_prefix}/X11R6/lib/pkgconfig"
fi
%configure
make %{_smp_mflags}


%install
[ "$RPM_BUILD_ROOT" != '/' ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"
rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir
touch "${RPM_BUILD_ROOT}/%{_sysconfdir}/pango/pango.modules"


%post
/sbin/ldconfig
%{_bindir}/pango-querymodules > %{_sysconfdir}/pango/pango.modules

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != '/' ] && rm -rf "$RPM_BUILD_ROOT"


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
%{_mandir}/man1/pango-querymodules.1.gz
%dir %{_sysconfdir}/pango
%config %{_sysconfdir}/pango/pangox.aliases
%ghost %config %{_sysconfdir}/pango/pango.modules
