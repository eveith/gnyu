Name: wesnoth
Version: 1.6a
Release: 5ev
Summary: A turn-based fantasy strategy game: The Battle for Wesnoth
URL: http://www.wesnoth.org/
Group: Amusements/Games
License: GPL-2
Vendor: GNyU-Linux
Source: http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
BuildRequires(build,install): make, gettext
BuildRequires(build): cmake >= 2.4.1, gcc-g++, boost >= 1.33.0
BuildRequires(build): libsdl >= 1.2.7, libsdlimage >= 1.2, libsdlmixer >= 1.2
BuildRequires(build): libsdlnet, libsdlttf >= 2.0.8, zlib
BuildRequires(build): fontconfig >= 2.4.1, pango >= 1.14.8
Requires: %{name}-common = %{version}

%description
The Battle for Wesnoth is a free, turn-based strategy game with a
fantasy theme. Fight a desperate battle to reclaim the throne of
Wesnoth, or take hand in any number of other adventures...


%package common
Summary: Common data files for wesnoth, e. g. maps
Group: Amusements/Games
Obsoletes: %{name}-data

%description common
Contains various data files that are required for wesnoth to run: maps, music, 
campaigns, graphic files, and so on.


%package server
Summary: Dedicated server for Battle For Wesnoth
Group: Amusements/Games
Requires: %{name}-common = %{version}

%description server
The dedicated `wesnothd' server binary that is used to host a wesnoth server.


%prep
%setup -q

# Fix a bug: http://www.wesnoth.org/forum/viewtopic.php?f=4&p=292862
#%{__sed} -ie 's/hr //' po/wesnoth/LINGUAS


%build
%configure \
	--disable-strict-compilation \
	--enable-server \
	--enable-editor \
	--enable-editor \
	--disable-gnome1 \
	--disable-gnome2 \
	--with-kde \
	--without-gnome \
	--with-x
%{__make} %{?_smp_mflags}


%install
%{__make_install} DESTDIR="${RPM_BUILD_ROOT}"
%{__rm} -rf '%{buildroot}/%{_datadir}/doc'


%files
%defattr(-, root, root)
%doc README COPYING ABOUT-NLS doc/manual
%{_bindir}/wesnoth
#%{_bindir}/wesnoth_editor
%doc %{_mandir}/*/man6/wesnoth.6*
%doc %{_mandir}/man6/wesnoth.6*
#%doc %{_mandir}/*/man6/wesnoth_editor.6*
#%doc %{_mandir}/man6/wesnoth_editor.6*
%{_datadir}/applications/wesnoth.desktop
%{_datadir}/applications/wesnoth_editor.desktop
%{_datadir}/icons/wesnoth-icon.png
%{_datadir}/icons/wesnoth_editor-icon.png

%files common
%defattr(-, root, root)
%{_datadir}/wesnoth/

%files server
%defattr(-, root, root)
%{_bindir}/wesnothd
%doc %{_mandir}/*/man6/wesnothd.6*
%doc %{_mandir}/man6/wesnothd.6*
%dir %attr(1770, root, wheel) %{_localstatedir}/run/wesnothd
