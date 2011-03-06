Name: mpfr
Version: 3.0.0
Release: 2.0
Summary: A C library for multiple-precision floating-point computations
URL: http://www.mpfr.org
Group: System Environment/Libraries
License: GPL-2
Source: http://www.mpfr.org/mpfr-current/mpfr-%{version}.tar.bz2
Patch: http://mpfr.loria.fr/mpfr-%{version}/allpatches
BuildRequires(prep): patch
BuildRequires: grep, sed, make, gcc, binutils
BuildRequires: gmp-devel >= 4.2.3, kernel-headers
Requires: libmpfr4 = %{version}-%{release}

%description
The main goal of MPFR is to provide a library for multiple-precision
floating-point computation which is both efficient and has a well-defined
semantics. It copies the good ideas from the ANSI/IEEE-754 standard for
double-precision floating-point arithmetic (53-bit mantissa).


%package -n libmpfr4
Summary: A C library for multiple-precision floating-point computations
Group: System Environment/Libraries

%description -n libmpfr4
The main goal of MPFR is to provide a library for multiple-precision
floating-point computation which is both efficient and has a well-defined
semantics. It copies the good ideas from the ANSI/IEEE-754 standard for
double-precision floating-point arithmetic (53-bit mantissa).


%package devel
Summary: Development headers for multiple-precision floating-point programs
Group: Development/Libraries

%description devel
The main goal of MPFR is to provide a library for multiple-precision
floating-point computation which is both efficient and has a well-defined
semantics. It copies the good ideas from the ANSI/IEEE-754 standard for
double-precision floating-point arithmetic (53-bit mantissa).
If you want to develop or compile applications using MPFR for high-precision
floating-point operations, you will need to install this package.


%prep
%setup -q
%{__patch} -p1 -N -Z < %{PATCH0}


%build
%configure \
    --enable-thread-safe
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%{__rm_rf} '%{buildroot}%{_datadir}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%check
%{__make} check


%post
%{__ldconfig}
update-info-dir


%postun
%{__ldconfig}
update-info-dir


%files
%defattr(-, root, root)
%doc AUTHORS BUGS COPYING* README FAQ* NEWS VERSION TODO ChangeLog PATCHES
%{_libdir}/libmpfr.so


%files -n libmpfr4
%defattr(-, root, root)
%doc AUTHORS BUGS COPYING* README FAQ* NEWS VERSION TODO ChangeLog PATCHES
%{_libdir}/libmpfr.so.4*


%files devel
%defattr(-, root, root)
%doc AUTHORS BUGS COPYING* README FAQ* NEWS VERSION TODO ChangeLog PATCHES
%doc %{_infodir}/mpfr.info*
%{_includedir}/mpfr.h
%{_includedir}/mpf2mpfr.h
%{_libdir}/libmpfr.a
%{_libdir}/libmpfr.la
