Name: libpciaccess
Version: 0.10
Release: 1ev
Summary: Generic PCI access library for X
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://ftp.x.org/pub/individual/lib/libpciaccess-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, pkg-config, grep, sed, coreutils

%description
Provides functionality for X to access the PCI bus and devices in a 
platform-independant way.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc README NEWS AUTHORS ChangeLog COPYING
%{_includedir}/pciaccess.h
%{_libdir}/libpciaccess.*
%{_libdir}/pkgconfig/pciaccess.pc
