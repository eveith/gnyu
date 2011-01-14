Name: libXfont
Version: 1.3.2
Release: 2ev
Summary: X font library
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: MSP Slackware
Source: ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: coreutils, grep, sed, make, gcc, pkg-config
BuildRequires: x11-proto, freetype, zlib, libfontenc

%description
Beeing the connection between Freetype and X, this library is responsible for
display of well-drawn fonts.


%prep
%setup -q


%build
%configure
%{__make} %{_smp_mflags}


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
%doc COPYING AUTHORS
%{_libdir}/libXfont*.*
%{_libdir}/pkgconfig/xfont*.pc
%{_includedir}/X11/fonts/*.h
