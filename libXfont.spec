Name: libXfont
Version: 1.3.0
Release: 1ev
Summary: X font library
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: MSP Slackware
Source: ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, pkg-config
BuildRequires: x11-proto, freetype, zlib, libfontenc

%description
Beeing the connection between Freetype and X, this library is responsible for
display of well-drawn fonts.


%prep
%setup -q


%build
%configure
make %{_smp_mflags}


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc COPYING AUTHORS
%{_libdir}/libXfont*.*
%{_libdir}/pkgconfig/xfont*.pc
%{_includedir}/X11/fonts/*.h
