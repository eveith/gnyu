Name: xorg-drivers
Version: 7.3
Release: 2ev
Summary: A collection of input and video drivers for the X Server
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Buildroot: %{_tmppath}/%{name}-buildroot
Requires: xf86-input-keyboard >= 1.2.2, xf86-input-mouse >= 1.2.2
Obsoletes: x11-drivers < %{version}-%{release}
Provides: x11-drivers = %{version}-%{release}

%description
This is the X.org X11 drivers metapackage. Installing this will, by the
solving of dependencies, install all X.org drivers that come with the standard
X11 distribution.
If you do not want to install all drivers available, have a look at the
individual xf86-{input,video}-* driver packages. It is recommended that you
install at least xf86-input-keyboard, xf86-input-mouse and xf86-video-vesa.


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
%defattr(-, root, root)
