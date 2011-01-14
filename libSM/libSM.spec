Name: libSM
Version: 1.1.0
Release: 3ev
Summary: X Session Management Library
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
BuildRequires: make, gcc, pkg-config >= 0.9.0
BuildRequires: libICE, xorg-xproto, xtrans, uuid1

%description
This library manages X sessions.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc COPYING README AUTHORS
%{_includedir}/X11/SM/
%{_libdir}/libSM*.*
%{_libdir}/pkgconfig/sm.pc
