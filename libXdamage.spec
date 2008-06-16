Name: libXdamage
Version: 1.1.1
Release: 2ev
Summary: Allows to compute which parts of a X11 window must be redrawn
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: MSP Slackware
Source: http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: coreutils, grep, sed, make, gcc, pkg-config
BuildRequires: x11-proto, libX11, libXfixes

%description
This library allows to compute when a certain widget on a screen is afected by
another, e.g. the mouse cursor hovering over a button, or a windows
overleaping another. This allows transparency and shadows to be drawn
correctly in real-time.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc COPYING README AUTHORS
%{_libdir}/libXdamage*.*
%{_libdir}/pkgconfig/xdamage.pc
%{_includedir}/X11/extensions/Xdamage.h
