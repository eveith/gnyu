Name: xinit
Version: 1.1.0
Release: 1ev
Summary: Helper to start the X Window Server and the first X client
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/archive/individual/app/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-g++, xorg-proto, libX11
Requires: xmodmap, xrdb, twm, xterm, xclock

%description
The xinit program is used to start the X Window System server and a
first client program on systems that cannot start X directly from
/etc/init or in environments that use multiple window systems.



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
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/startx
%{_bindir}/xinit
%{_libdir}/X11/xinit/xinitrc
%doc %{_mandir}/man1/startx.1*
%doc %{_mandir}/man1/xinit.1*
