Name: libmad
Version: 0.15.1b
Release: 2ev
Summary: An high-quality MPEG audio decoder
URL: http://www.underbit.com/products/mad/
Group: System Environment/Libraries
License: GPL-2
Vendor: GNyU-Linux
Source: ftp://ftp.mars.org/pub/mpeg/%{name}-%{version}.tar.gz
BuildRequires: make, gcc

%description
MAD is a high-quality MPEG audio decoder capable of 24-bit output. All
computations are performed with fixed-point integer arithmetic, making it
ideal for systems without a floating-point unit. The implementation is
entirely new, based on the ISO/IEC standards. 


%prep
%setup -q


%build
%configure \
	--enable-accuracy \
	--enable-sso
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR="${RPM_BUILD_ROOT}"


%post
%{__ldconfig}


%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc CHANGES COPYRIGHT COPYING CREDITS README TODO VERSION
%{_libdir}/libmad*.*
%{_includedir}/mad.h
