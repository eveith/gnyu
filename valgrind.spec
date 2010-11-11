Name: valgrind
Version: 3.6.0
Release: 2.0ev
Summary: A framework for building dynamic analysis tools
URL: http://www.valgrind.org
Group: Development/Tools
License: GPL-2
Vendor: GNyU-Linux
Source: http://valgrind.org/downloads/valgrind-%{version}.tar.bz2
BuildRequires: grep, sed, make, gcc >= 3.0, gcc-g++ >= 3.0, pkg-config
BuildRequires: perl, diffutils
BuildRequires: boost, qt4 >= 4.3, gdb, glibc >= 2.2
BuildConflicts: glibc > 2.12
Conflicts: glibc > 2.12

%description
Valgrind is an award-winning instrumentation framework for building
dynamic analysis tools. There are Valgrind tools that can automatically
detect many memory management and threading bugs, and profile your
programs in detail. You can also use Valgrind to build new tools.

The Valgrind distribution currently includes six production-quality
tools: a memory error detector, two thread error detectors, a cache and
branch-prediction profiler, a call-graph generating cache profiler, and
a heap profiler. It also includes two experimental tools:  a
heap/stack/global array overrun detector, and a SimPoint basic block vector
generator.


%package doc
Summary: Additional documentation for Valgrind
Group: Documentation
License: FDL-1.2

%description doc
Additional documentation for Valgrind, including the full user's manual.


%package devel
Summary: Development headers for Valgrind
Group: Development/Libraries
Requires: pkg-config, valgrind = %{version}-%{release}

%description devel
Contains header files and pkg-config information needed to develop
applications with the valgrind framework.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}
%{__make} check


%install
%{__make} install DESTDIR='%{buildroot}'


%post
%{__ldconfig}


%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc AUTHORS FAQ.txt README* COPYING NEWS
%dir %{_libdir}/valgrind
%{_libdir}/valgrind/*
%{_bindir}/callgrind_annotate
%{_bindir}/callgrind_control
%{_bindir}/cg_annotate
%{_bindir}/cg_diff
%{_bindir}/cg_merge
%{_bindir}/ms_print
%{_bindir}/no_op_client_for_valgrind
%{_bindir}/valgrind
%{_bindir}/valgrind-listener
%doc %{_mandir}/man1/callgrind_annotate.1*
%doc %{_mandir}/man1/callgrind_control.1*
%doc %{_mandir}/man1/cg_annotate.1*
%doc %{_mandir}/man1/ms_print.1*
%doc %{_mandir}/man1/valgrind.1*


%files doc
%defattr(-, root, root)
%doc COPYING.DOCS
%dir %{_datadir}/doc/valgrind
%doc %{_datadir}/doc/valgrind/valgrind_manual.*
%dir %{_datadir}/doc/valgrind/html
%dir %{_datadir}/doc/valgrind/html/images
%doc %{_datadir}/doc/valgrind/html/*.html
%{_datadir}/doc/valgrind/html/*.css
%{_datadir}/doc/valgrind/html/images/*.*


%files devel
%defattr(-, root, root)
%dir %{_includedir}/valgrind
%dir %{_includedir}/valgrind/vki
%{_includedir}/valgrind/*.h
%{_includedir}/valgrind/vki/*.h
%{_libdir}/pkgconfig/valgrind.pc
