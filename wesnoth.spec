Name: wesnoth
Version: 1.2.8
Release: 1ev
Summary: A turn-based fantasy strategy game: The Battle for Wesnoth
URL: http://www.wesnoth.org/
Group: Amusements/Games
License: GPL-2
Vendor: MSP Slackware
Source: http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, gcc-g++, gettext, freetype, libX11
BuildRequires: libsdl >= 1.2, libsdlnet, libsdlmixer, libsdlimage

%description
The Battle for Wesnoth is a free, turn-based strategy game with a
fantasy theme. Fight a desperate battle to reclaim the throne of
Wesnoth, or take hand in any number of other adventures…


%prep
%setup -q


%build
%configure \
	--enable-server \
	--enable-editor \
	--disable-gnome1 \
	--disable-gnome2 \
	--with-kde \
	--without-gnome \
	--with-x
make %{_smp_mflags}


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"

[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc README COPYING MANUAL* ABOUT-NLS
%{_bindir}/wesnoth*
%{_mandir}/*/man6/wesnoth*.6*
%{_mandir}/man6/wesnoth*.6*
%{_datadir}/wesnoth/
%{_datadir}/applnk/Games/TacticStrategy/wesnoth*.desktop
%{_datadir}/icons/wesnoth*.png
%dir %attr(0700, root, root) /%{_var}/run/wesnothd
