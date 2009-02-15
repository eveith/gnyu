Name: liboil
Version: 0.3.12
Release: 1ev
Summary: A library of simple functions that are optimized for various CPUs
URL: http://liboil.freedesktop.org/
Group: System Environment/Libraries
License: BSD
Vendor: MSP Slackware
Source: http://liboil.freedesktop.org/download/liboil-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core

%description
Liboil is a library of simple functions that are optimized for various CPUs.
These functions are generally loops implementing simple algorithms, such as
converting an array of N integers to floating-point numbers or multiplying and
summing an array of N numbers. Such functions are candidates for significant
optimization using various techniques, especially by using extended
instructions provided by modern CPUs (Altivec, MMX, SSE, etc.). 
Many multimedia applications and libraries already do similar things
internally. The goal of this project is to consolidate some of the code used
by various multimedia projects, and also make optimizations easier to use by a
broader range of applications.


%prep
%setup -q


%build
%configure \
	--disable-glib
make %{_smp_mflags}


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"


[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc AUTHORS BUG-REPORTING COPYING HACKING ChangeLog* NEWS README
%doc %{_datadir}/gtk-doc/html/liboil
%{_bindir}/oil-bugreport
%{_includedir}/liboil-0.3/
%{_libdir}/liboil-0.3.*
%{_libdir}/pkgconfig/liboil-0.3.pc
