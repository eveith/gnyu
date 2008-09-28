Name: compiz
Version: 0.7.8
Release: 1ev
Summary: An OpenGL-based compositing- and window manager
URL: http://www.compiz.org/
Group: User Interface/Desktops
License: MIT, LGPL, GPL
Vendor: GNyU-Linux
Source: http://releases.compiz-fusion.org/0.6.0/compiz/compiz-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, gcc-g++, qt3, kdelibs, librsvg, libxslt, libpng, glib2
BuildRequires: gettext, dbus, pkg-config
Requires: kdebase

%description
Compiz is an OpenGL compositing manager that use GLX_EXT_texture_from_pixmap
for binding redirected top-level windows to texture objects. It has a flexible
plug-in system and it is designed to run well on most graphics hardware.


%prep
%setup -q


%build
%configure \
	--disable-gnome \
	--disable-gnome-keybindings \
	--disable-gconf \
	--disable-gtk \
	--disable-metacity
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean -f compiz.lang
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc AUTHORS COPYING* ChangeLog README NEWS TODO
%{_bindir}/compiz
%{_bindir}/kde-window-decorator
%{_includedir}/compiz/
%{_libdir}/compiz/
%{_libdir}/libdecoration.*
%{_libdir}/pkgconfig/compiz*.pc
%{_libdir}/pkgconfig/libdecoration.pc
%{_datadir}/compiz/
%{_datadir}/config.kcfg/compiz-*.kcfg
%{_datadir}/config/compizrc
%{_datadir}/locale/*/LC_MESSAGES/compiz.mo
