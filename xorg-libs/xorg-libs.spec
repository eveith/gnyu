Name: xorg-libs
Version: 7.3
Release: 1ev
Summary: The X.org X11 library distribution
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Buildroot: %{_tmppath}/%{name}-buildroot
Requires: libAppleWM >= 1.0.0, libFS >= 1.0.0, libICE >= 1.0.4, libSM >= 1.0.3
Requires: libWindowsWM >= 1.0.0, libX11 >= 1.1.3, libXScrnSaver >= 1.1.2
Requires: libXTrap >= 1.0.0, libXau >= 1.0.3, libXaw >= 1.0.4
Requires: libXcomposite >= 0.4.0, libXcursor >= 1.1.9, libXdamage >= 1.0.4
Requires: libXdmcp >= 1.0.2, libXevie >= 1.0.2, libXext >= 1.0.2
Requires: libXfixes >= 4.0.3, libXfont >= 1.3.1, libXfontcache >= 1.0.4
Requires: libXft >= 2.1.12, libXi >= 1.1.3, libXinerama >= 1.0.2
Requires: libXmu >= 1.0.3, libXp >= 1.0.0, libXpm >= 3.5.7
Requires: libXprintAppUtil >= 1.0.1, libXprintUtil >= 1.0.1, libXrandr >= 1.2.2
Requires: libXrender >= 0.9.4, libXres >= 1.0.3, libXt >= 1.0.4
Requires: libXtst >= 1.0.3, libXv >= 1.0.3, libXvMC >= 1.0.4
Requires: libXxf86dga >= 1.0.2, libXxf86misc >= 1.0.1, libXxf86vm >= 1.0.1
Requires: libdmx >= 1.0.2, libfontenc >= 1.0.4, liblbxutil >= 1.0.1
Requires: liboldX >= 1.0.1, libxkbfile >= 1.0.4, libxkbui >= 1.0.2
Requires: xtrans >= 1.0.4, libxcb >= 1.0

%description
This meta-package resolves dependencies for all libraries in the X.org X11
distribution. Install it if you want the complete set, regardeless of the
actual need.


%prep
exit 0


%build
exit 0


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
exit 0


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
