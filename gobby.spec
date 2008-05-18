Name: gobby
Version: 0.4.6
Release: 1ev
Summary: A collaborative real-time editor
URL: http://gobby.0x539.de/
Group: Applications/Editors
License: GPL-2
Vendor: GNyU-Linux
Source: http://releases.0x539.de/gobby/gobby-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: coreutils, sed, grep, make, gcc-g++, gettext
BuildRequires: libsigc++ >= 2.0.2, gnutls >= 1.0.0, net6 >= 1.3.0, obby >= 0.4
BuildRequires: glib2 >= 2.6.0, gtk2 >= 2.6.0, glibmm >= 2.6.0, libxml++ >= 2.6
BuildRequires: gtkmm >= 2.6.0, gtksourceview >= 1.8, libgnomeprint, libstdc++

%description
Gobby is a free collaborative editor. This means that it
provides you with the possibility to edit files simultaneously
with other users over a network. It supports multiple
documents in one session and a multi-user chat. The platforms
on which you could use Gobby are so far Microsoft Windows,
Linux, Mac OS X and other Unix-like ones. Developed with the
Gtk+ toolkit it integrates nicely into the GNOME desktop
environment if you want it to.


%prep
%setup -q


%build
%configure \
	--without-gnome
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%find_lang gobby

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files -f gobby.lang
%defattr(-, root, root)
%doc AUTHORS COPYING NEWS README
%{_bindir}/gobby
%{_mandir}/man1/gobby.1*
%{_datadir}/pixmaps/gobby.png
%{_datadir}/pixmaps/gobby/
