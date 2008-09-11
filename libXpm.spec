Name: libXpm
Version: 3.5.7
Release: 2ev
Summary: Library for the X Pixmap image format
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, pkg-config, xorg-proto
BuildRequires: libICE, libSM, libX11, libXau, libXdmcp, libXext

%description
XPM is an image format like PNG or JPEG. It comes with X11 and is mainly used
for icons.


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
%{_bindir}/?xpm
%{_includedir}/X11/xpm.h
%{_libdir}/libXpm*.*
%{_libdir}/pkgconfig/xpm.pc
%doc %{_mandir}/man1/?xpm.1*
