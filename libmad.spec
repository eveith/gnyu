Name: libmad
Version: 0.15.1b
Release: 1ev
Summary: A high-quality MPEG audio decoder
URL: http://www.underbit.com/products/mad/
Group: System Environment/Libraries
License: GPL
Vendor: MSP Slackware
Source: ftp://ftp.mars.org/pub/mpeg/%{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core

%description
MAD is a high-quality MPEG audio decoder capable of 24-bit output. All
computations are performed with fixed-point integer arithmetic, making it
ideal for systems without a floating-point unit. The implementation is
entirely new, based on the ISO/IEC standards. 


%prep
%setup -q


%build
%configure \
	--enable-accuracy
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
%doc CHANGES COPYRIGHT COPYING CREDITS README TODO VERSION
%{_libdir}/libmad*.*
%{_includedir}/mad.h
