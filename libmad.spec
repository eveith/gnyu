Name: libmad
Version: 0.15.1b
Release: 3ev
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

# Create pkgconfig file
%{__mkdir_p} '%{buildroot}/%{_libdir}/pkgconfig'
%{__cat} > '%{buildroot}/%{_libdir}/pkgconfig/mad.pc' << __EOF__
prefix=%{_prefix}
exec_prefix=%{_exec_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: mad
Description: MPEG audio decoder
Requires:
Version: 0.15.1b
Libs: -L%{_libdir} -lmad
Cflags: -I%{_includedir}
__EOF__


%post
%{__ldconfig}


%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc CHANGES COPYRIGHT COPYING CREDITS README TODO VERSION
%{_libdir}/libmad*.*
%{_libdir}/pkgconfig/mad.pc
%{_includedir}/mad.h
