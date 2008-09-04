Name: xorg-proto
Version: 7.3
Release: 4ev
Summary: Xorg protocol headers
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Buildroot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch
Requires: xorg-applewmproto >= 1.0.3, xorg-bigreqsproto >= 1.0.2
Requires: xorg-compositeproto >= 0.4, xorg-damageproto >= 1.1.0
Requires: xorg-dmxproto >= 2.2.2, xorg-evieext >= 1.0.2, xorg-fixesproto >= 4.0
Requires: xorg-fontcacheproto >= 0.1.2, xorg-fontsproto >= 2.0.2
Requires: xorg-glproto >= 1.4.8, xorg-inputproto >= 1.4.2.1
Requires: xorg-kbproto >= 1.0.3, xorg-printproto >= 1.0.3
Requires: xorg-randrproto >= 1.2.1, xorg-recordproto >= 1.13.2
Requires: xorg-renderproto >= 0.9.3, xorg-resourceproto >= 1.0.2
Requires: xorg-scrnsaverproto >= 1.1.0, xorg-trapproto >= 3.4.3
Requires: xorg-videoproto >= 2.2.2, xorg-windowswmproto >= 1.0.3
Requires: xorg-windowswmproto >= 1.0.3, xorg-xcmiscproto >= 1.1.2
Requires: xorg-xextproto >= 7.0.2, xorg-xf86bigfontproto >= 1.1.2
Requires: xorg-xf86dgaproto >= 2.0.3, xorg-xf86driproto >= 2.0.3
Requires: xorg-xf86miscproto >= 0.9.2, xorg-xf86rushproto >= 1.1.2
Requires: xorg-xf86vidmodeproto >= 2.2.2, xorg-xineramaproto >= 1.1.2
Requires: xorg-xproto >= 7.0.10, xorg-xproxymanagementprotocol >= 1.0.2
Provides: x11-proto = %{version}-%{release}

%description
The Xorg protocol headers provide the header files required to build the
system, and to allow other applications to build against the installed X
Window system.
This package is a meta-package, wrapping up all header packages into one neat
dependency chain. It also provides the needed directory architecture.


%prep
exit 0


%build
exit 0

%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__mkdir_p} '%{buildroot}/%{_includedir}/GL'
%{__mkdir_p} '%{buildroot}/%{_includedir}/GL/internal'
%{__mkdir_p} '%{buildroot}/%{_includedir}/X11'
%{__mkdir_p} '%{buildroot}/%{_includedir}/X11/extensions'
%{__mkdir_p} '%{buildroot}/%{_includedir}/X11/PM'
%{__mkdir_p} '%{buildroot}/%{_includedir}/X11/dri'
%{__mkdir_p} '%{buildroot}/%{_includedir}/X11/fonts'


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%dir %{_includedir}/GL
%dir %{_includedir}/GL/internal
%dir %{_includedir}/X11
%dir %{_includedir}/X11/extensions
%dir %{_includedir}/X11/PM
%dir %{_includedir}/X11/dri
%dir %{_includedir}/X11/fonts
