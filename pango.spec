Name: pango
Version: 1.18.4
Release: 2ev
Summary: A framework for the layout and rendering of international text
URL: http://www.pango.org/
Group: System Environement/Libraries
License: LGPL
Vendor: GNyU-Linux
Source: http://ftp.gnome.org/pub/GNOME/sources/%{name}/1.16/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: coreutils, sed, grep, make >= 3.79.1, gcc, zlib
BuildRequires: libX11, libXau, libXdmcp, libXft, libXrender, libxcb
BuildRequires: glib2 >= 2.10.0, fontconfig, freetype >= 2.0.4, cairo

%description
The goal of the Pango project is to provide an Open Source framework for the
layout and rendering of internationalized text. It uses Unicode for all of its
encoding, and will eventually support output in all the world's major
languages.


%prep
%setup -q


%build
if [[ -r '%{_prefix}/X11R6/lib/pkgconfig/xft.pc' \
		&& ! -r '%{_libdir}/pkgconfig/xft.pc' ]]
then
	export PKG_CONFIG_PATH="${PKG_CONFIG_PATH}:%{_prefix}/X11R6/lib/pkgconfig"
fi
%configure
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%{__rm} -f '%{buildroot}/%{_infodir}/dir'
touch '%{buildroot}/%{_sysconfdir}/pango/pango.modules'


%post
/sbin/ldconfig
%{_bindir}/pango-querymodules > '%{_sysconfdir}/pango/pango.modules'

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


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
