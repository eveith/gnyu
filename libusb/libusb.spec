Name: libusb-1_0
Version: 1.0.8
Release: 1.0
Summary: A library for accessing USB devices
URL: http://www.libusb.org
Group: System Environment/Libraries
License: LGPL-2.1
Source: http://sourceforge.net/projects/libusb/files/libusb-1.0/libusb-%{version}/libusb-%{version}.tar.bz2
BuildRequires: make, gcc
BuildRequires: eglibc-devel, linux-headers
Requires: libusb-1_0-0

%description
libusb is a library for USB device access from Linux userspace.


%package devel
Summary: Development files for libusb
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
libusb is a library for USB device access from Linux userspace.
This package contains the development headers needed to compile programs that
use libusb.


%package -n libusb-1_0-0
Summary: A library for accessing USB devices
Group: System Environment/Libraries

%description
libusb is a library for USB device access from Linux userspace.


%prep
%setup -q -n 'libusb-%{version}'


%build
%configure \
    --libdir='/%{_lib}'
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

%{__mkdir_p} '%{buildroot}%{_libdir}'
%{__mv} '%{buildroot}/%{_lib}/pkgconfig' '%{buildroot}%{_libdir}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%check
%{__make} check


%post -n libusb-1_0-0 -p %{__ldconfig}
%postun -n libusb-1_0-0 -p %{__ldconfig}


%files
%defattr(-, root, root)
%doc README AUTHORS COPYING NEWS THANKS


%files -n libusb-1_0-0
%defattr(-, root, root)
%doc README AUTHORS COPYING NEWS THANKS
/%{_lib}/libusb-1.0.so.0*


%files devel
%defattr(-, root, root)
%doc README AUTHORS COPYING NEWS THANKS PORTING TODO
/%{_lib}/libusb-1.0.so
/%{_lib}/libusb-1.0.la
/%{_lib}/libusb-1.0.a

%{_libdir}/pkgconfig/libusb-1.0.pc

%dir %{_includedir}/libusb-1.0
%{_includedir}/libusb-1.0/libusb.h
