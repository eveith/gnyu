Name: gcc
Version: 4.2.3
Release: 2ev
Summary: The GNU Compiler Collection (Core Package)
License: GPL-3
Group: Development/Languages
Vendor: GNyU-Linux
Source0: ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{version}/gcc-%{version}.tar.bz2
URL: http://gcc.gnu.org/
BuildRequires: coreutils, grep, sed, gettext, gcc, make >= 3.79.1, binutils,
BuildRequires: bison
BuildRoot: %{_tmppath}/%{name}-root
Provides: gcc-core = %{version}
Obsoletes: gcc-core < %{version}-%{release}

%description
The GNU Compiler Collection includes front ends for C, C++, Objective-C,
Fortran, Java, and Ada, as well as libraries for these languages (libstdc++,
libgcj,...). The GCC is one of the most basic things a system will need if new
software is ever compiled on it.
This package contains "gcc", the GNU C Compiler. 


%package -n libgcc_s
Summary: Low-level runtime library
Group: System Environment/Libraries
Conflicts: gcc < %{version}-%{release}

%description -n libgcc_s
GCC provides a low-level runtime library, libgcc.a or libgcc_s.so.1 on some 
platforms. GCC generates calls to routines in this library automatically, 
whenever it needs to perform some operation that is too complicated to emit 
inline code for. 
Most of the routines in libgcc handle arithmetic operations that the target 
processor cannot perform directly. This includes integer multiply and divide 
on some machines, and all floating-point and fixed-point operations on other 
machines. libgcc also includes routines for exception handling, and a handful 
of miscellaneous operations.


%package g++
Summary: The GNU Compiler Collection (C++ Package)
Group: Development/Languages

%description -n gcc-g++
The GNU Compiler Collection includes front ends for C, C++, Objective-C,
Fortran, Java, and Ada, as well as libraries for these languages (libstdc++,
libgcj,...). The GCC is one of the most basic things a system will need if new
software is ever compiled on it.
This package comes with the C++ compiler.


%package -n libstdc++
Summary: Standard C++ implementations library
Group: System Environment/Libraryibstdc++

%description -n libstdc++
The C++ standard defines some methods and classes that ought to be always
available. The libstdc++ is the GNU implementation of these methods/classes.
It is used by every program that is written in C++ and dynamically linked.


%prep
# %setup -q -T -b0
# %setup -q -D -T -b1 -n "gcc-%{version}"
%setup -q
%{__rm} -rf %{_builddir}/%{name}-obj
%{__mkdir_p} %{_builddir}/%{name}-obj


%build
pushd %{_builddir}/%{name}-obj

# Run configure
#CFLAGS="$RPM_OPT_FLAGS"
#CXXFLAGS="$RPM_OPT_FLAGS"
#export CFLAGS CXXFLAGS
${RPM_BUILD_DIR}/gcc-%{version}/configure \
	--host=%{_host} \
	--build=%{_build} \
	--target=%{_target_platform} \
	--program-prefix=%{?_program_prefix} \
	--prefix=%{_prefix} \
	--exec-prefix=%{_exec_prefix} \
	--bindir=%{_bindir} \
	--sbindir=%{_sbindir} \
	--sysconfdir=%{_sysconfdir} \
	--datadir=%{_datadir} \
	--includedir=%{_includedir} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libexecdir} \
	--localstatedir=%{_localstatedir} \
	--sharedstatedir=%{_sharedstatedir} \
	--mandir=%{_mandir} \
	--infodir=%{_infodir} \
	--enable-threads=posix \
	--with-cpu=%{_target_cpu} \
	--enable-__cxa_atexit \
	--enable-nls \
	--with-system-zlib \
	--without-x \
	--enable-languages=c,c++
%{__make} %{?_smp_mflags}

popd


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'

pushd %{_builddir}/%{name}-obj
%{__make_install} DESTDIR='%{buildroot}'
popd

# Remove libiberty.a, this is shipped by GNU binutils.
%{__rm} -f "$RPM_BUILD_ROOT/%{_libdir}/libiberty.a"

%find_lang gcc
%find_lang libstdc++

pushd %{buildroot}/%{_bindir}
%{__ln_s} gcc cc
# %{__ln_s} %{_target_platform}-g++ g++
# %{__ln_s} %{_target_platform}-g++ c++
# %{__ln_s} %{_target_platform}-g++ %{_target_platform}-c++
popd

%{__rm} -f $RPM_BUILD_ROOT/%{_infodir}/dir


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__rm} -rf %{_builddir}/%{name}-obj


%post
/sbin/ldconfig
update-info-dir

%postun 
/sbin/ldconfig
update-info-dir

%post -n libstdc++
/sbin/ldconfig

%postun -n libstdc++
/sbin/ldconfig


%files -f gcc.lang
%defattr(-, root, root)
%doc ABOUT-NLS BUGS COPYING* ChangeLog* FAQ LAST_UPDATED MAINTAINERS NEWS
%doc README* *.html
%{_bindir}/*cc*
%{_bindir}/cpp
%{_bindir}/gcov
%{_infodir}/cpp.info*
%{_infodir}/cppinternals.info*
%{_infodir}/gcc.info*
%{_infodir}/gccinstall.info*
%{_infodir}/gccint.info*
%{_infodir}/libgomp.info*
%{_libdir}/gcc/
%{_libdir}/libgomp.*
%{_libdir}/libmudflap*.*
%{_libdir}/libssp*.*
%dir %{_libexecdir}/gcc
%dir %{_libexecdir}/gcc/%{_target_platform}
%dir %{_libexecdir}/gcc/%{_target_platform}/%{version}
%{_libexecdir}/gcc/%{_target_platform}/%{version}/cc1
%{_libexecdir}/gcc/%{_target_platform}/%{version}/collect2
%dir %{_libexecdir}/gcc/%{_target_platform}/%{version}/install-tools
%{_libexecdir}/gcc/%{_target_platform}/%{version}/install-tools/fixinc.sh
%{_libexecdir}/gcc/%{_target_platform}/%{version}/install-tools/fixincl
%{_libexecdir}/gcc/%{_target_platform}/%{version}/install-tools/mkheaders
%{_mandir}/man1/cpp.1*
%{_mandir}/man1/gcc.1*
%{_mandir}/man1/gcov.1*
%{_mandir}/man7/fsf-funding.7*
%{_mandir}/man7/gfdl.7*
%{_mandir}/man7/gpl.7*
%{_datadir}/locale/*/*/cpplib.mo

%files g++
%defattr(-, root, root)
%doc ABOUT-NLS BUGS COPYING* ChangeLog* FAQ LAST_UPDATED MAINTAINERS NEWS
%doc README* *.html
%{_bindir}/*?++
%{_libexecdir}/gcc/%{_target_platform}/%{version}/cc1plus
%{_mandir}/man1/g++.1*

%files -n libstdc++ -f libstdc++.lang
%defattr(-, root, root)
%{_includedir}/c++/
%{_libdir}/libstdc++*.*
%{_libdir}/libsupc++*.*

%files -n libgcc_s
%defattr(-, root, root)
%{_libdir}/libgcc_s*.*
