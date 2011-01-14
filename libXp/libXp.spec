Name: libXp
Version: 1.0.0
Release: 2ev
Summary: X client printing interface
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, xorg-proto, pkg-config
BuildRequires: libX11, libXau, libXext

%description
Allows X applications to print via X server interfaces rather directly to a
spooler.


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
%{_libdir}/libXp*.*
%{_libdir}/pkgconfig/xp.pc
%doc %{_mandir}/man3/*Xp*.3*
