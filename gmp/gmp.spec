Name: gmp
Version: 4.3.2
Release: 3.0
Summary: A very fast bignum library (GNU Multiple Precision Arithmetic Library)
URL: http://gmplib.org/
Group: System Environment/Libraries
License: LGPL-3
Source: ftp://ftp.gnu.org/gnu/gmp/gmp-%{version}.tar.bz2
BuildRequires: grep, gawk, sed, m4, bison, flex, make, gcc, gcc-g++
BuildRequires: eglibc-devel, libstdc++-devel, kernel-headers
Requires: libgmp.3 = %{version}-%{release}, libgmpxx.4 = %{version}-%{release}

%description
GMP is a free library for arbitrary precision arithmetic, operating on signed integers, 
rational numbers, and floating point numbers. There is no practical limit to the 
precision except the ones implied by the available memory in the machine GMP runs on.
GMP has a rich set of functions, and the functions have a regular interface. 
The main target applications for GMP are cryptography applications and research, 
Internet security applications, algebra systems, computational algebra research, etc.


%package -n libgmp.3
Summary: Multiple precision arithmetic library for C
Group: System Environment/Libraries

%description -n libgmp.3
GMP is a free library for arbitrary precision arithmetic, operating on signed
integers, rational numbers, and floating point numbers. This is the pure C
library providing these functions.


%package -n libgmpxx.4
Summary: Multiple precision arithmetic library for C++
Group: System Environment/Libraries

%description -n libgmpxx.4
GMP is a free library for arbitrary precision arithmetic, operating on signed
integers, rational numbers, and floating point numbers. This is the C++
library providing these functions.


%package devel
Summary: Development headers for the GMP library
Group: Development/Libraries

%description devel
GMP is a free library for arbitrary precision arithmetic, operating on signed
integers, rational numbers, and floating point numbers. This packages offers
documentation on the API and development headers for creating applications
which use GMP.


%prep
%setup -q


%build
CFLAGS=${CFLAGS:-%{optflags}}
CXXFLAGS=${CXXFLAGS:-%{optflags}}
CC=${CC:-%{_target_platform}-gcc}
CXX=${CXX:-%{_target_platform}-g++}
export CC CXX CFLAGS CXXFLAGS
 
./configure \
    --build='%{_target_platform}' \
    --prefix='%{_prefix}' \
    --exec-prefix='%{_exec_prefix}' \
    --bindir='%{_bindir}' \
    --sbindir='%{_sbindir}' \
    --sysconfdir='%{_sysconfdir}' \
    --datadir='%{_datadir}' \
    --includedir='%{_includedir}' \
    --libdir='/%{_lib}' \
    --libexecdir='%{_libexecdir}' \
    --sharedstatedir='%{_sharedstatedir}' \
    --localstatedir='%{_localstatedir}' \
    --mandir='%{_mandir}' \
    --infodir='%{_infodir}' \
    --enable-fat \
    --enable-cxx
%{__make} %{?_smp_mflags}


%check
%{__make} check


%install
%{__make} install DESTDIR='%{buildroot}'

[[ -e '%{buildroot}%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}%{_infodir}/dir'


%post -n libgmp.3 -p %{__ldconfig}
%postun -n libgmp.3 -p %{__ldconfig}
%post -n libgmpxx.4 -p %{__ldconfig}
%postun -n libgmpxx.4 -p %{__ldconfig}


%files
%defattr(-, root, root)
%doc README COPYING* AUTHORS NEWS


%files devel
%defattr(-, root, root)
%doc README COPYING* AUTHORS NEWS
%{_includedir}/gmp.h
%{_includedir}/gmpxx.h
/%{_lib}/libgmp*.a
/%{_lib}/libgmp*.la
%doc %{_infodir}/gmp.info*


%files -n libgmp.3
%defattr(-, root, root)
%doc README COPYING* AUTHORS NEWS
/%{_lib}/libgmp.so
/%{_lib}/libgmp.so.3*


%files -n libgmpxx.4
%defattr(-, root, root)
%doc README COPYING* AUTHORS NEWS
/%{_lib}/libgmpxx.so
/%{_lib}/libgmpxx.so.4*
