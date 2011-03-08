Name: mpc
Version: 0.9
Release: 1.0
Summary: A C library for the arithmetic of complex numbers
URL: http://www.multiprecision.org
Group: System Environment/Libraries
License: LGPL-2.1+
Source: http://www.multiprecision.org/mpc/download/mpc-%{version}.tar.gz
BuildRequires: gawk, grep, sed, make, gcc, binutils
BuildRequires: eglibc-devel, kernel-headers
BuildRequires: gmp-devel >= 4.3.2, mpfr-devel >= 2.4.2
Requires: libmpc2 = %{version}-%{release}

%description
Mpc is a C library for the arithmetic of complex numbers with arbitrarily high
precision and correct rounding of the result. It is built upon and follows the
same principles as Mpfr.


%package -n libmpc2
Summary: A C library for the arithmetic of complex numbers
Group: System Environment/Libraries

%description -n libmpc2
Mpc is a C library for the arithmetic of complex numbers with arbitrarily high
precision and correct rounding of the result. It is built upon and follows the
same principles as Mpfr.


%package devel
Summary: Arithmetic of complex numbers development package
Group: Development/Libraries
Requires: mpc = %{version}-%{release}

%description devel
Mpc is a C library for the arithmetic of complex numbers with arbitrarily high
precision and correct rounding of the result. It is built upon and follows the
same principles as Mpfr.
You will need this package when compiling programs that use MPC or if you want
to develop MPC-based programs yourself.


%prep
%setup -q


%build
export EGREP='/bin/grep -E'
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%check
%{__make} check


%post -n libmpc2 -p %{__ldconfig}
%postun -n libmpc2 -p %{__ldconfig}


%files
%defattr(-, root, root)
%doc AUTHORS COPYING.LIB ChangeLog NEWS README TODO
%{_libdir}/libmpc.so


%files -n libmpc2
%defattr(-, root, root)
%doc AUTHORS COPYING.LIB ChangeLog NEWS README TODO
%{_libdir}/libmpc.so.2*


%files devel
%defattr(-, root, root)
%doc AUTHORS COPYING.LIB ChangeLog NEWS README TODO
%doc %{_infodir}/mpc.info*
%{_includedir}/mpc.h
%{_libdir}/libmpc.la
%{_libdir}/libmpc.a
