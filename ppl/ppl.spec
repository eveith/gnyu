Name: ppl
Version: 0.11.2
Release: 1.0
Summary: A library providing numerical abstractions
URL: http://www.cs.unipr.it/ppl/
Group: System Environment/Libraries
License: GPL-3+
Vendor: GNyU-Linux
Source: ftp://ftp.cs.unipr.it/pub/ppl/releases/0.11.2/ppl-0.11.2.tar.bz2
BuildRequires: sed, grep, make
BuildRequires: gcc, gcc-g++
BuildRequires: perl, m4 >= 1.4.11
BuildRequires: gmp-devel >= 4.1.3, kernel-headers
Requires: libppl9 = %{version}-%{release}
Requires: libppl_c4 = %{version}-%{release}
Requires: libpwl5 = %{version}-%{release}

%description
The Parma Polyhedra Library (PPL) provides numerical abstractions especially
targeted at applications in the field of analysis and verification of complex
systems. These abstractions include convex polyhedra, defined as the
intersection of a finite number of (open or closed) halfspaces, each described
by a linear inequality (strict or non-strict) with rational coefficients; some
special classes of polyhedra shapes that offer interesting
complexity/precision tradeoffs; and grids which represent regularly spaced
points that satisfy a set of linear congruence relations. The library also
supports finite powersets and products of (any kind of) polyhedra and grids, a
mixed integer linear programming problem solver using an exact-arithmetic
version of the simplex algorithm, a parametric integer programming solver, and
primitives for the termination analysis via the automatic synthesis of linear
ranking functions. 


%package -n libppl9
Summary: Parma Polyhedra Library (runtime library)
Group: System Environment/Libraries

%description -n libppl9
The Parma Polyhedra Library (PPL) is a C++ library for the manipulation of
(not necessarily closed) convex polyhedra and other numerical abstractions.
The applications of convex polyhedra include program analysis, optimized
compilation, integer and combinatorial optimization and statistical
data-editing. The Parma Polyhedra Library is user friendly (you write `x + 2*y
+ 5*z <= 7' when you mean it), fully dynamic (available virtual memory is the
only limitation to the dimension of anything), written in standard C++,
exception-safe, rather efficient and thoroughly documented. 


%package -n libppl_c4
Summary: Parma Polyhedra Library (C interface)
Group: System Environment/Libraries

%description -n libppl_c4
The Parma Polyhedra Library (PPL) is a C++ library for the manipulation of
(not necessarily closed) convex polyhedra and other numerical abstractions.
The applications of convex polyhedra include program analysis, optimized
compilation, integer and combinatorial optimization and statistical
data-editing. The Parma Polyhedra Library is user friendly (you write `x + 2*y
+ 5*z <= 7' when you mean it), fully dynamic (available virtual memory is the
only limitation to the dimension of anything), written in standard C++,
exception-safe, rather efficient and thoroughly documented.
This package provides the C interface. 


%package -n libpwl5
Summary: Parma Watchdog Library (Watchdog timers - runtime library)
Group: System Environment/Libraries

%description -n libpwl5
The Parma Watchdog Library (PWL) provides support for multiple, concurrent
watchdog timers on systems providing setitimer(2). The PWL is currently
distributed with the Parma Polyhedra Library (PPL), but is totally independent
from it. 


%package doc
Summary: Auxilliary documentation for the PPL
Group: Development/Documentation
Requires: %{name} = %{version}-%{release}

%description doc
The Parma Polyhedra Library (PPL) is a C++ library for the manipulation of
(not necessarily closed) convex polyhedra and other numerical abstractions.
The applications of convex polyhedra include program analysis, optimized
compilation, integer and combinatorial optimization and statistical
data-editing. The Parma Polyhedra Library is user friendly (you write `x + 2*y
+ 5*z <= 7' when you mean it), fully dynamic (available virtual memory is the
only limitation to the dimension of anything), written in standard C++,
exception-safe, rather efficient and thoroughly documented.
This package provides the documentation. 


%package devel
Summary: Development headers for ppl
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: autoconf

%description devel
The Parma Polyhedra Library (PPL) is a C++ library for the manipulation of
(not necessarily closed) convex polyhedra and other numerical abstractions.
The applications of convex polyhedra include program analysis, optimized
compilation, integer and combinatorial optimization and statistical
data-editing. The Parma Polyhedra Library is user friendly (you write `x + 2*y
+ 5*z <= 7' when you mean it), fully dynamic (available virtual memory is the
only limitation to the dimension of anything), written in standard C++,
exception-safe, rather efficient and thoroughly documented. 
This package provides the header files and static libraries for the 
C and C++ interfaces. 


%prep
%setup -q


%build
%configure \
    --enable-cxx
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%check
%{__#make} check


%post -n libppl9 -p %{__ldconfig}
%postun -n libppl9 -p %{__ldconfig}

%post -n libppl_c4 -p %{__ldconfig}
%postun -n libppl_c4 -p %{__ldconfig}

%post -n libpwl5 -p %{__ldconfig}
%postun -n libpwl5 -p %{__ldconfig}


%files
%defattr(-, root, root)
%doc BUGS CREDITS COPYING ChangeLog* README* NEWS STANDARDS TODO
%{_bindir}/ppl_lcdd
%{_bindir}/ppl_pips
%{_libdir}/libppl.so
%{_libdir}/libppl_c.so
%{_libdir}/libpwl.so
%doc %{_mandir}/man1/ppl_lcdd.1*
%doc %{_mandir}/man1/ppl_pips.1*


%files -n libpwl5
%defattr(-, root, root)
%doc BUGS CREDITS COPYING ChangeLog* README* NEWS STANDARDS TODO
%{_libdir}/libpwl.so.5*


%files -n libppl9
%defattr(-, root, root)
%doc BUGS CREDITS COPYING ChangeLog* README* NEWS STANDARDS TODO
%{_libdir}/libppl.so.9*


%files -n libppl_c4
%defattr(-, root, root)
%doc BUGS CREDITS COPYING ChangeLog* README* NEWS STANDARDS TODO
%{_libdir}/libppl_c.so.4*


%files devel
%defattr(-, root, root)
%doc BUGS CREDITS COPYING ChangeLog* README* NEWS STANDARDS TODO
%{_bindir}/ppl-config
%{_bindir}/ppl_lcdd
%{_bindir}/ppl_pips
%{_includedir}/ppl.hh
%{_includedir}/ppl_c.h
%{_includedir}/pwl.hh
%{_libdir}/libppl.a
%{_libdir}/libppl.la
%{_libdir}/libppl_c.a
%{_libdir}/libppl_c.la
%{_libdir}/libpwl.a
%{_libdir}/libpwl.la
%doc %{_mandir}/man1/ppl-config.1*
%doc %{_mandir}/man3/libppl.3*
%doc %{_mandir}/man3/libppl_c.3*
%{_datadir}/aclocal/ppl.m4
%{_datadir}/aclocal/ppl_c.m4


%files doc
%defattr(-, root, root)
%doc BUGS CREDITS COPYING ChangeLog* README* NEWS STANDARDS TODO
%dir %{_datadir}/doc/ppl
%doc %{_datadir}/doc/ppl/*
%dir %{_datadir}/doc/pwl
%doc %{_datadir}/doc/pwl/*
