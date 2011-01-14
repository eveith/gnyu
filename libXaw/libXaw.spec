Name: libXaw
Version: 1.0.4
Release: 2ev
Summary: The X Athena Widgets Library
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, pkg-config, xorg-proto, libXt
BuildRequires: libICE, libSM, libX11, libXau, libXext, libXmu, libXp, libXpm

%description
Xaw is a widget set based on the X Toolkit Intrinsics (Xt) Library.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR="$RPM_BUILD_ROOT"


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc COPYING README AUTHORS
%{_includedir}/X11/Xaw/
%{_libdir}/libXaw*.*
%{_libdir}/pkgconfig/xaw?.pc
%doc %{_mandir}/man3/Xaw.3*
%{_datadir}/aclocal/xaw.m4
