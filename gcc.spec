Name: gcc
Version: 4.3.4
Release: 3ev
Summary: The GNU Compiler Collection (Core Package)
URL: http://gcc.gnu.org/
License: GPL-3
Group: Development/Languages
Vendor: GNyU-Linux
Source0: ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{version}/gcc-%{version}.tar.bz2
BuildRequires: make >= 3.80, gcc, gawk >= 3.1.5, binutils, gettext
Buildrequires: gmp >= 4.2, mpfr >= 2.3.2
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
Requires: gcc = %{version}-%{release}

%description -n gcc-g++
The GNU Compiler Collection includes front ends for C, C++, Objective-C,
Fortran, Java, and Ada, as well as libraries for these languages (libstdc++,
libgcj,...). The GCC is one of the most basic things a system will need if new
software is ever compiled on it.
This package comes with the C++ compiler.


%package -n libstdc++6
Summary: Standard C++ implementations library
Group: System Environment/Libraryibstdc++
Provides: libstdc++ = %{version}-%{release}

%description -n libstdc++6
The C++ standard defines some methods and classes that ought to be always
available. The libstdc++ is the GNU implementation of these methods/classes.
It is used by every program that is written in C++ and dynamically linked.


%prep
%setup -q -c -a0
%{__mkdir_p} obj


%build
pushd obj

# Run configure
CC="${CC:-%{_target_platform}-gcc}"
CFLAGS="${CFLAGS:-%{optflags}}"
CXX="${CXX:-%{_target_platform}-g++}"
CXXFLAGS="${CFLAGS:-%{optflags}}"
export CC CFLAGS CXX CXXFLAGS
../gcc-%{version}/configure \
	--host='%{_host}' \
	--build='%{_build}' \
	--target='%{_target_platform}' \
	--program-prefix='%{?_program_prefix}' \
	--prefix='%{_prefix}' \
	--exec-prefix='%{_exec_prefix}' \
	--bindir='%{_bindir}' \
	--sbindir='%{_sbindir}' \
	--sysconfdir='%{_sysconfdir}' \
	--datadir='%{_datadir}' \
	--includedir='%{_includedir}' \
	--libdir='%{_libdir}' \
	--libexecdir='%{_libexecdir}' \
	--localstatedir='%{_localstatedir}' \
	--sharedstatedir='%{_sharedstatedir}' \
	--mandir='%{_mandir}' \
	--infodir='%{_infodir}' \
	--enable-threads \
	--with-cpu='%{_target_cpu}' \
	--enable-__cxa_atexit \
	--enable-nls \
	--with-system-zlib \
	--without-x \
	--enable-languages=c,c++
%{__make} %{?_smp_mflags}
popd


%install
pushd obj
%{__make} install DESTDIR='%{buildroot}'
popd

# Remove libiberty.a, this is shipped by GNU binutils.
%{__rm} '%{buildroot}/%{_libdir}/libiberty.a'

%find_lang gcc
%find_lang cpplib

pushd '%{buildroot}/%{_bindir}'
%{__ln_s} gcc cc
# %{__ln_s} %{_target_platform}-g++ g++
# %{__ln_s} %{_target_platform}-g++ c++
# %{__ln_s} %{_target_platform}-g++ %{_target_platform}-c++
popd

%{__rm} '%{buildroot}/%{_infodir}/dir' ||:


%post
%{__ldconfig}
update-info-dir


%postun 
%{__ldconfig}
update-info-dir


%post -n libstdc++6
%{__ldconfig}


%postun -n libstdc++6
%{__ldconfig}


%files -f gcc.lang
%defattr(-, root, root)
%doc gcc-%{version}/ABOUT-NLS gcc-%{version}/COPYING*
%doc gcc-%{version}/ChangeLog* gcc-%{version}/LAST_UPDATED
%doc gcc-%{version}/MAINTAINERS gcc-%{version}/NEWS
%doc gcc-%{version}/README* gcc-%{version}/*/*.html
%{_bindir}/*cc*
%{_bindir}/cpp
%{_bindir}/gcov
%doc %{_infodir}/cpp.info*
%doc %{_infodir}/cppinternals.info*
%doc %{_infodir}/gcc.info*
%doc %{_infodir}/gccinstall.info*
%doc %{_infodir}/gccint.info*
%doc %{_infodir}/libgomp.info*
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
%{_libexecdir}/gcc/%{_target_platform}/%{version}/install-tools/mkinstalldirs
%doc %{_mandir}/man1/cpp.1*
%doc %{_mandir}/man1/gcc.1*
%doc %{_mandir}/man1/gcov.1*
%doc %{_mandir}/man7/fsf-funding.7*
%doc %{_mandir}/man7/gfdl.7*
%doc %{_mandir}/man7/gpl.7*
%{_datadir}/locale/*/*/cpplib.mo


%files g++
%defattr(-, root, root)
%doc gcc-%{version}/ABOUT-NLS gcc-%{version}/COPYING*
%doc gcc-%{version}/ChangeLog* gcc-%{version}/LAST_UPDATED
%doc gcc-%{version}/MAINTAINERS gcc-%{version}/NEWS
%doc gcc-%{version}/README* gcc-%{version}/*/*.html
%{_bindir}/*?++
%{_libexecdir}/gcc/%{_target_platform}/%{version}/cc1plus
%doc %{_mandir}/man1/g++.1*


%files -n libstdc++6 -f cpplib.lang
%defattr(-, root, root)
%{_includedir}/c++/
%{_libdir}/libstdc++*.*
%{_libdir}/libsupc++*.*


%files -n libgcc_s
%defattr(-, root, root)
%{_libdir}/libgcc_s*.*
