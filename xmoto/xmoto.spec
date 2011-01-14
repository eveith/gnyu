Name: xmoto
Version: 0.4.2
Release: 1ev
Summary: An arcade game with extremly realistic physics
URL: http://xmoto.tuxfamily.org/
Group: Entertainment/Games
License: GPL-2
Vendor: GNyU-Linux
Source: http://download.tuxfamily.org/xmoto/xmoto/%{version}/xmoto-%{version}-src.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: coreutils, grep, sed, make, gcc, gcc-g++, libjpeg, libpng
BuildRequires: zlib, bzip2, curl, libsdlttf, libsdlmixer, libsdl, lua50
BuildRequires: sqlite, ode, mesalib, libstdc++, gettext

%description
X-Moto is an arcade/skill game, where the player drives a motobike through
different levels. X-Moto uses a very realistic physics, which, in combination
with the terrain, brings the difficulty to the game.


%prep
%setup -q


%build
export LDFLAGS="-ldl ${LDFLAGS}"
%configure
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%find_lang xmoto

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files -f xmoto.lang
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS COPYING ChangeLog README NEWS TODO
%{_bindir}/xmoto
%{_mandir}/man6/xmoto.6*
%{_datadir}/xmoto/
