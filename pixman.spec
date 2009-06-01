Name: pixman
Version: 0.9.6
Release: 1ev
Summary: A library to privde low-level pixel manipulation features
URL: http://www.x.org/
Group: System Environment/Libraries
License: MIT
Vendor: MSP Slackware
Source: http://ftp.x.org/pub/individual/lib/pixman-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, pkg-config

%description
pixman is a library that provides low-level pixel manipulation
features such as image compositing and trapezoid rasterization.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
[[ -d '%{buildroot}' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ -d '%{buildroot}' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog README NEWS TODO
%{_includedir}/pixman-1/
%{_libdir}/libpixman-1.*
%{_libdir}/pkgconfig/pixman-1.pc
