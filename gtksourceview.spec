Name: gtksourceview
Version: 2.2.1
Release: 1ev
Summary: A widget extension to GTK+2
URL: http://gtksourceview.sourceforge.net/
Group: System Environment/Libraries
License: GPL-2, LGPL-2.1
Vendor: GNyU-Linux
Source: http://ftp.gnome.org/pub/gnome/sources/%{name}/2.2/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: coreutils, grep, sed, make, gcc, pkg-config
BuildRequires: gtk2, gettext, pcre

%description
GtkSourceView is a text widget that extends the standard gtk+ 2.x text widget.
It improves the gtk+ text widget by implementing syntax highlighting and other
features typical of a source editor.


%prep
%setup -q


%build
%configure \
	--with-system-pcre
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%{find_lang} gtksourceview-2.0

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files -f gtksourceview-2.0.lang
%defattr(-, root, root)
%doc README AUTHORS COPYING* HACKING MAINTAINERS NEWS
%doc %{_datadir}/gtk-doc/html/gtksourceview-2.0
%{_includedir}/gtksourceview-2.0/
%{_libdir}/libgtksourceview-2.0.*
%{_libdir}/pkgconfig/gtksourceview-2.0.pc
%{_datadir}/gtksourceview-2.0/
