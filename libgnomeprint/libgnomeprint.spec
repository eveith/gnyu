Name: libgnomeprint
Version: 2.18.4
Release: 1ev
Summary: GNOME printing library
URL: http://ftp.acc.umu.se/pub/GNOME/sources/libgnomeprint
Group: System Environment/Libraries
License: GPL-2, LGPL-2.1
Vendor: GNyU-Linux
Source: http://ftp.acc.umu.se/pub/GNOME/sources/libgnomeprint/2.18/libgnomeprint-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: coreutils, grep, sed, make, gcc, pkg-config, gettext, flex
BuildRequires: freetype >= 2.0.5, glib2, libxml2, zlib, libart, bison

%description
This is an implementation of the Gnome Printing Architecture, as
described in: http://www.levien.com/gnome/print-arch.html


%prep
%setup -q


%build
%configure \
	--disable-gtk-doc \
	--without-cups
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%{find_lang} libgnomeprint-2.2

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files -f libgnomeprint-2.2.lang
%defattr(-, root, root)
%doc AUTHORS BUGS ChangeLog* COPYING* MAINTAINERS NEWS README
%doc %{_datadir}/gtk-doc/html/libgnomeprint/
%{_includedir}/libgnomeprint-2.2/
%{_libdir}/libgnomeprint-2-2.*
%{_libdir}/libgnomeprint/
%{_libdir}/pkgconfig/libgnomeprint-2.2.pc
%{_datadir}/libgnomeprint/
