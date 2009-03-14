Name: libXext
Version: 1.0.5
Release: 1ev
Summary: Miscellaneous X Extension Library
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
BuildRequires: make, gcc, pkg-config >= 0.9.0
BuildRequires: xorg-xproto >= 7.0.13, xorg-xextproto >= 7.0.5
BuildRequires: libX11 >= 1.1.99.1, libXau

%description
This library carries several extensions for X, like DPMS and XShm.


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
%{_libdir}/libXext*.*
%{_libdir}/pkgconfig/xext.pc
%doc %{_mandir}/man3/*.3*
