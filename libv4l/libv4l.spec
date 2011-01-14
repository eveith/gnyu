Name: libv4l
Version: 0.5.9
Release: 1ev
Summary: A (thin) abstraction layer on top of Video4Linux
URL: http://freshmeat.net/projects/libv4l
Group: System Environment/Libraries
License: LGPL-2.1
Vendor: GNyU-Linux
Source: http://people.atrpms.net/~hdegoede/%{name}-%{version}.tar.gz
BuildRequires: make, gcc

%description
libv4l is a collection of libraries that adds a thin abstraction layer 
on top of video4linux2 (V4L2) devices. The purpose of this layer is to make 
it easy for application writers to support a wide variety of devices 
without having to write separate code for different devices in the same 
class. It consists of 3 different libraries. libv4lconvert offers functions 
to convert from any (known) pixel format to V4l2_PIX_FMT_BGR24 or 
V4l2_PIX_FMT_YUV420. libv4l1 offers the (deprecated) v4l1 API on top of v4l2 
devices, independent of the drivers for those devices supporting v4l1 
compatibility (which many v4l2 drivers do not). libv4l2 offers the v4l2 API on
top of v4l2 devices, while adding support for the application transparent 
libv4lconvert conversion where necessary.

%prep
%setup -q


%build
%{__make} %{?_smp_mflags} \
	CFLAGS="${CFLAGS:-%{optflags}}" \
	CC="${CC:-%{_target_platform}-gcc}"


%install
%{__make} install \
	PREFIX='%{_prefix}' \
	DESTDIR='%{buildroot}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc README* ChangeLog TODO COPYING.LIB
%{_includedir}/libv4l[12].h
%{_includedir}/libv4lconvert.h
%dir %{_libdir}/libv4l
%{_libdir}/libv4l/v4l1compat.so
%{_libdir}/libv4l/v4l2convert.so
%{_libdir}/libv4l[12].*
%{_libdir}/libv4lconvert.*
%{_libdir}/pkgconfig/libv4l[12].pc
%{_libdir}/pkgconfig/libv4lconvert.pc
