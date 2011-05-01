Name: cloog-parma
Version: 0.16.1
Release: 1.0
Summary: A code generator for scanning Z-polyhedra
URL: http://cloog.org
Group: System Environment/Libraries
License: GPL-2
Source: http://www.bastoul.net/cloog/pages/download/count.php3?url=./%{name}-%{version}.tar.gz
BuildRequires: sed, grep, gawk, pkg-config, make
BuildRequires: gcc
BuildRequires: gmp-devel >= 4.3.2, ppl-devel >= 0.11
Requires: libcloog-ppl1 = %{version}-%{release}

%description
CLooG is a free software and library to generate code for scanning
Z-polyhedra. That is, it finds a code (e.g. in C, FORTRAN...) that reaches
each integral point of one or more parameterized polyhedra. CLooG has been
originally written to solve the code generation problem for optimizing
compilers based on the polytope model. Nevertheless it is used now in various
area e.g. to build control automata for high-level synthesis or to find the
best polynomial approximation of a function. CLooG may help in any situation
where scanning polyhedra matters. While the user has full control on generated
code quality, CLooG is designed to avoid control overhead and to produce a
very effective code. 
CLooG stands for Chunky Loop Generator: it is a part of the Chunky project, a
research tool for data locality improvement. It is designed to be also the
back-end of automatic parallelizers like LooPo. Thus it is very 'compilable
code oriented' and provides powerful program transformation facilities.
Mainly, it allows the user to specify very general schedules, e.g. where
unimodularity or invertibility doesn't matter. 


%package devel
Summary: Development headers for CLooG
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}, pkg-config

%description devel
CLooG is a free software and library to generate code for scanning
Z-polyhedra. That is, it finds a code (e.g. in C, FORTRAN...) that reaches
each integral point of one or more parameterized polyhedra. CLooG has been
originally written to solve the code generation problem for optimizing
compilers based on the polytope model. Nevertheless it is used now in various
area e.g. to build control automata for high-level synthesis or to find the
best polynomial approximation of a function. CLooG may help in any situation
where scanning polyhedra matters. While the user has full control on generated
code quality, CLooG is designed to avoid control overhead and to produce a
very effective code. 
CLooG stands for Chunky Loop Generator: it is a part of the Chunky project, a
research tool for data locality improvement. It is designed to be also the
back-end of automatic parallelizers like LooPo. Thus it is very 'compilable
code oriented' and provides powerful program transformation facilities.
Mainly, it allows the user to specify very general schedules, e.g. where
unimodularity or invertibility doesn't matter. 
This is the development package, including header files and compiling/linking
information via a pkg-config file.


%package -n libcloog-ppl1
Summary: The Chunky Loop Generator (runtime library)
Group: System Environment/Libraries

%description -n libcloog-ppl1
CLooG is a free software and library to generate code for scanning
Z-polyhedra. This is the runtime library, needed for programs that make use of
CLooG.


%prep
%setup -q


%build
%configure \
    --with-ppl
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%check
%{__make} check


%post -n libcloog-ppl1 -p %{__ldconfig}
%postun -n libcloog-ppl1 -p %{__ldconfig}


%files
%defattr(-, root, root)
%{_bindir}/cloog
%{_libdir}/libcloog-ppl.so


%files -n libcloog-ppl1
%defattr(-, root, root)
%{_libdir}/libcloog-ppl.so.1
%{_libdir}/libcloog-ppl.so.1.0.1


%files devel
%defattr(-, root, root)
%dir %{_includedir}/cloog
%{_includedir}/cloog/block.h
%{_includedir}/cloog/clast.h
%{_includedir}/cloog/cloog.h
%{_includedir}/cloog/constraints.h
%{_includedir}/cloog/domain.h
%{_includedir}/cloog/input.h
%{_includedir}/cloog/int.h
%{_includedir}/cloog/loop.h
%{_includedir}/cloog/matrix.h
%dir %{_includedir}/cloog/matrix
%{_includedir}/cloog/matrix/constraintset.h
%{_includedir}/cloog/names.h
%{_includedir}/cloog/options.h
%dir %{_includedir}/cloog/ppl
%{_includedir}/cloog/ppl/backend.h
%{_includedir}/cloog/ppl/cloog.h
%{_includedir}/cloog/ppl/domain.h
%{_includedir}/cloog/pprint.h
%{_includedir}/cloog/program.h
%{_includedir}/cloog/state.h
%{_includedir}/cloog/statement.h
%{_includedir}/cloog/stride.h
%{_includedir}/cloog/union_domain.h
%{_includedir}/cloog/version.h
%{_libdir}/libcloog-ppl.a
%{_libdir}/libcloog-ppl.la
%{_libdir}/pkgconfig/cloog-ppl.pc
