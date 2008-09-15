Name: xrdb
Version: 1.0.5
Release: 1ev
Summary: X.org X11 resource manager
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/archive/individual/app/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, xorg-proto, libX11, libXmu

%description
Xrdb is used to get or set the contents of the RESOURCE_MANAGER property
on the root window of screen 0, or the SCREEN_RESOURCES property
on the root window of any or all screens, or everything combined. You
would normally run this program from your X startup file.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING README NEWS
%{_bindir}/xrdb
%doc %{_mandir}/man1/xrdb.1*
