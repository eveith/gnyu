Name: libXtst
Version: 1.0.3
Release: 2ev
Summary: X11 Testing -- Resource extension library
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, pkg-config, xorg-proto, libX11, libXext

%description
libXtst provides an X Window System client interface to the Record extension
to the X protocol. The Record extension allows X clients to synthesise input 
events, which is useful for automated testing.


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
%{_libdir}/libXtst.*
%{_libdir}/pkgconfig/xtst.pc
%doc %{_mandir}/man3/XTest*.3*
