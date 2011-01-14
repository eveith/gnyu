Name: gimp
Version: 2.4.6
Release: 2ev
Summary: The GNU Image Manipulation Program
URL: http://www.gimp.org/
Group: Applications/Productivity
License: GPL
Vendor: GNyU-Linux
Source: ftp://ftp.gimp.org/pub/gimp/v2.4/gimp-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
BuildRequires(prep,build,install): coreutils, grep, sed
BuildRequires(build,install): make, gettext, pkg-config
BuildRequires(build): gcc
BuildRequires(build): gtk2 >= 2.10.3, pango >= 1.12.2, freetype >= 2.1.7
BuildRequires(build): fontconfig >= 2.2.0, libart >= 2.0, dbus-glib
BuildRequires(build): libpng, libjpeg, libtiff, libmng, libwmf, librsvg
BuildRequires(build): zlib, curl, alsa-lib

%description
GIMP is an acronym for GNU Image Manipulation Program. It is a freely
distributed program for such tasks as photo retouching, image composition and
image authoring.


%prep
%setup -q


%build
%configure \
	--disable-debug \
	--disable-warnings \
	--disable-python
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
find '%{buildroot}' -type f -name \*.mo -print | \
	%{__sed} 's,%{buildroot},,' >> gimp.lang

%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__rm} -f gimp.lang


%files -f gimp.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog* HACKING LICENSE NEWS* README*
%doc %{_datadir}/gtk-doc/html/libgimpbase/
%doc %{_datadir}/gtk-doc/html/libgimpcolor/
%doc %{_datadir}/gtk-doc/html/libgimpconfig/
%doc %{_datadir}/gtk-doc/html/libgimpmath/
%doc %{_datadir}/gtk-doc/html/libgimpmodule/
%doc %{_datadir}/gtk-doc/html/libgimpthumb/
%doc %{_datadir}/gtk-doc/html/libgimpwidgets/
%doc %{_datadir}/gtk-doc/html/libgimp/
%{_datadir}/aclocal/gimp-2.0.m4
%{_datadir}/applications/gimp.desktop
%{_datadir}/application-registry/gimp.applications
%{_datadir}/icons/hicolor/*/apps/gimp.*
%{_datadir}/gimp/
%{_datadir}/mime-info/gimp.keys
%doc %{_mandir}/man1/gimp.1*
%doc %{_mandir}/man1/gimp-2.4.1*
%doc %{_mandir}/man1/gimp-console.1*
%doc %{_mandir}/man1/gimp-console-2.4.1*
%doc %{_mandir}/man1/gimp-remote.1*
%doc %{_mandir}/man1/gimp-remote-2.4.1*
%doc %{_mandir}/man1/gimptool-2.0.1*
%doc %{_mandir}/man5/gimprc-2.4.5*
%doc %{_mandir}/man5/gimprc.5*
%{_bindir}/gimp
%{_bindir}/gimp-2.4
%{_bindir}/gimp-console
%{_bindir}/gimp-console-2.4
%{_bindir}/gimp-remote
%{_bindir}/gimp-remote-2.4
%{_bindir}/gimptool-2.0
%{_libdir}/gimp/
%{_libdir}/libgimp*.*
%{_libdir}/pkgconfig/gimp-2.0.pc
%{_libdir}/pkgconfig/gimpthumb-2.0.pc
%{_libdir}/pkgconfig/gimpui-2.0.pc
%{_includedir}/gimp-2.0/
%dir %{_sysconfdir}/gimp
%dir %{_sysconfdir}/gimp/2.0
%config %{_sysconfdir}/gimp/2.0/*rc
