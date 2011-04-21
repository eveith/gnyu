Name: gcc
Version: 4.5.2
Release: 4.0
Summary: The GNU Compiler Collection (Core Package)
URL: http://gcc.gnu.org/
License: GPL-3
Group: Development/Languages
Source0: ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{version}/gcc-%{version}.tar.bz2
BuildRequires: sed, grep, gawk >= 3.1.5, make >= 3.80
BuildRequires: gcc >= 2.95, gcc-g++ >= 2.95, binutils >= 2.20.51
BuildRequires: texinfo, gettext-tools
Buildrequires: gmp-devel >= 4.3.2, mpfr-devel >= 2.4.2, mpc-devel >= 0.8.1
BuildRequires: ppl-devel >= 0.11, cloog-parma >= 0.16.1
BuildRequires: zlib-devel, libelf-devel
Requires: cpp = %{version}-%{release}
Conflicts: gcc-core
Obsoletes: gcc-core < %{version}-%{release}

%description
The GNU Compiler Collection includes front ends for C, C++, Objective-C,
Fortran, Java, and Ada, as well as libraries for these languages (libstdc++,
libgcj,...). The GCC is one of the most basic things a system will need if new
software is ever compiled on it.
This package contains "gcc", the GNU C Compiler. 


%package -n cpp
Summary: The C Preprocessor
Group: Development/Languages

%description -n cpp
Cpp is the GNU C-Compatible Compiler Preprocessor.
Cpp is a macro processor which is used automatically
by the C compiler to transform your program before actual
compilation. It is called a macro processor because it allows
you to define macros, abbreviations for longer
constructs.
The C preprocessor provides four separate functionalities: the
inclusion of header files (files of declarations that can be
substituted into your program); macro expansion (you can define macros,
and the C preprocessor will replace the macros with their definitions
throughout the program); conditional compilation (using special
preprocessing directives, you can include or exclude parts of the
program according to various conditions); and line control (if you use
a program to combine or rearrange source files into an intermediate
file which is then compiled, you can use line control to inform the
compiler about where each source line originated).
You should install this package if you are a C programmer and you use
macros.


%package -n libgcc_s1
Summary: Low-level runtime library
Group: System Environment/Libraries
Conflicts: gcc < %{version}-%{release}

%description -n libgcc_s1
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
Requires: cpp = %{version}-%{release}

%description -n gcc-g++
The GNU Compiler Collection includes front ends for C, C++, Objective-C,
Fortran, Java, and Ada, as well as libraries for these languages (libstdc++,
libgcj,...). The GCC is one of the most basic things a system will need if new
software is ever compiled on it.
This package comes with the C++ compiler.


%package -n libstdc++6
Summary: Standard C++ implementations library
Group: System Environment/Libraries
Provides: libstdc++ = %{version}-%{release}

%description -n libstdc++6
The C++ standard defines some methods and classes that ought to be always
available. The libstdc++ is the GNU implementation of these methods/classes.
It is used by every program that is written in C++ and dynamically linked.


%package -n libstdc++-devel
Summary: Standard C++ implementations library development headers
Group: Development/Libraries
Requires: libstdc++ = %{version}-%{release}

%description -n libstdc++6
The C++ standard defines some methods and classes that ought to be always
available. The libstdc++ is the GNU implementation of these methods/classes.
It is used by every program that is written in C++ and dynamically linked.
If you want to compile programs that make use of the standard C++ features
such as the STL, you will need to install this development package.


%package -n libgomp1
Summary: GCC OpenMP v3.0 shared support library
Group: System Environment/Libraries

%description -n libgomp1
This package contains GCC shared support library which is needed
for OpenMP v3.0 support.


%package -n libmudflap0
Summary: GCC mudflap shared support library
Group: System Environment/Libraries

%description -n libmudflap0
This package contains GCC shared support library which is needed
for mudflap support.


%prep
%setup -qTca0
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
    --enable-lto \
	--enable-__cxa_atexit \
	--enable-nls \
	--with-system-zlib \
	--enable-languages=c,c++
%{__make} %{?_smp_mflags}
popd


%install
pushd obj
%{__make} install DESTDIR='%{buildroot}'
popd

# Remove libiberty.a, this is shipped by GNU binutils.
%{__rm} '%{buildroot}/%{_libdir}/libiberty.a'

# We don't ship libssp
%{__rm} '%{buildroot}%{_libdir}'/libssp*.*

%find_lang gcc
%find_lang cpplib

# Create some helpful links

pushd '%{buildroot}%{_bindir}'
[[ -e 'cc' ]] || %{__ln_s} gcc cc
[[ -e 'g++' ]] || %{__ln_s} %{_target_platform}-g++ g++
[[ -e 'c++' ]] || %{__ln_s} %{_target_platform}-g++ c++
[[ -e '%{_target_platform}-c++' ]] || \
    %{__ln_s} %{_target_platform}-g++ %{_target_platform}-c++
popd

pushd '%{buildroot}'
%{__mkdir_p} lib/cpp
%{__ln_s} '%{_bindir}/cpp' lib/cpp
popd

%{__rm} '%{buildroot}/%{_infodir}/dir' ||:


%post
%{__ldconfig}
update-info-dir


%postun 
%{__ldconfig}
update-info-dir


%post -n cpp
update-info-dir


%postun -n cpp
update-info-dir


%post -n libgcc_s1 -p %{__ldconfig}
%postun -n libgcc_s1 -p %{__ldconfig}
%post -n libstdc++6 -p %{__ldconfig}
%postun -n libstdc++6 -p %{__ldconfig}


   /usr/share/gcc-4.5.2/python/libstdcxx/v6/__init__.py
   /usr/share/gcc-4.5.2/python/libstdcxx/v6/printers.py
%files -f gcc.lang
%defattr(-, root, root)
%doc gcc-%{version}/ABOUT-NLS gcc-%{version}/COPYING*
%doc gcc-%{version}/ChangeLog* gcc-%{version}/LAST_UPDATED
%doc gcc-%{version}/MAINTAINERS gcc-%{version}/NEWS
%doc gcc-%{version}/README* gcc-%{version}/*/*.html
%{_bindir}/cc
%{_bindir}/gcc
%{_bindir}/%{_target_platform}-gcc
%{_bindir}/%{_target_platform}-gcc-%{version}
%{_bindir}/gccbug
%{_bindir}/gcov
%{_libdir}/libgcc_s.so
%{_libdir}/libgomp.a
%{_libdir}/libgomp.la
%{_libdir}/libgomp.so
%{_libdir}/libgomp.spec
%{_libdir}/libmudflap.a
%{_libdir}/libmudflap.la
%{_libdir}/libmudflap.so
%{_libdir}/libmudflapth.a
%{_libdir}/libmudflapth.la
%{_libdir}/libmudflapth.so
%dir %{_libdir}/gcc
%dir %{_libdir}/gcc/%{_target_platform}
%dir %{_libdir}/gcc/%{_target_platform}/%{version}
%{_libdir}/gcc/%{_target_platform}/%{version}/crtbegin.o
%{_libdir}/gcc/%{_target_platform}/%{version}/crtbeginS.o
%{_libdir}/gcc/%{_target_platform}/%{version}/crtbeginT.o
%{_libdir}/gcc/%{_target_platform}/%{version}/crtend.o
%{_libdir}/gcc/%{_target_platform}/%{version}/crtendS.o
%{_libdir}/gcc/%{_target_platform}/%{version}/crtfastmath.o
%{_libdir}/gcc/%{_target_platform}/%{version}/crtprec32.o
%{_libdir}/gcc/%{_target_platform}/%{version}/crtprec64.o
%{_libdir}/gcc/%{_target_platform}/%{version}/crtprec80.o
%dir %{_libdir}/gcc/%{_target_platform}/%{version}/include-fixed
%{_libdir}/gcc/%{_target_platform}/%{version}/include-fixed/README
%{_libdir}/gcc/%{_target_platform}/%{version}/include-fixed/limits.h
%dir %{_libdir}/gcc/%{_target_platform}/%{version}/include-fixed/linux
%{_libdir}/gcc/%{_target_platform}/%{version}/include-fixed/linux/a.out.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include-fixed/syslimits.h
%dir %{_libexecdir}/gcc/%{_target_platform}/%{version}/install-tools
%{_libexecdir}/gcc/%{_target_platform}/%{version}/install-tools/fixinc.sh
%{_libexecdir}/gcc/%{_target_platform}/%{version}/install-tools/fixincl
%{_libexecdir}/gcc/%{_target_platform}/%{version}/install-tools/mkheaders
%{_libexecdir}/gcc/%{_target_platform}/%{version}/install-tools/mkinstalldirs
%dir %{_libdir}/gcc/%{_target_platform}/%{version}/install-tools
%{_libdir}/gcc/%{_target_platform}/%{version}/install-tools/fixinc_list
%{_libdir}/gcc/%{_target_platform}/%{version}/install-tools/gsyslimits.h
%dir %{_libdir}/gcc/%{_target_platform}/%{version}/install-tools/include
%{_libdir}/gcc/%{_target_platform}/%{version}/install-tools/include/README
%{_libdir}/gcc/%{_target_platform}/%{version}/install-tools/include/limits.h
%{_libdir}/gcc/%{_target_platform}/%{version}/install-tools/macro_list
%{_libdir}/gcc/%{_target_platform}/%{version}/install-tools/mkheaders.conf
%{_libdir}/gcc/%{_target_platform}/%{version}/libgcc.a
%{_libdir}/gcc/%{_target_platform}/%{version}/libgcc_eh.a
%{_libdir}/gcc/%{_target_platform}/%{version}/libgcov.a
%dir %{_libdir}/gcc/%{_target_platform}/%{version}/plugin
%dir %{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include
%dir %{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/ada
%dir %{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/ada/gcc-interface
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/ada/gcc-interface/ada-tree.def
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/alias.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/all-tree.def
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/ansidecl.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/auto-host.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/b-header-vars
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/basic-block.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/bitmap.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/builtins.def
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/bversion.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/c-common.def
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/c-common.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/c-pragma.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/c-pretty-print.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/cfghooks.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/cfgloop.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/cgraph.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/cif-code.def
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/config.h
%dir %{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/config
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/config/dbxelf.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/config/elfos.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/config/glibc-stdint.h
%dir %{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/config/i386
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/config/i386/att.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/config/i386/i386-protos.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/config/i386/i386.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/config/i386/linux.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/config/i386/unix.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/config/linux.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/config/svr4.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/config/vxworks-dummy.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/configargs.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/coretypes.h
%dir %{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/cp
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/cp/cp-tree.def
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/cp/cp-tree.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/cp/cxx-pretty-print.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/cp/name-lookup.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/cppdefault.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/cpplib.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/debug.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/defaults.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/diagnostic.def
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/diagnostic.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/double-int.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/emit-rtl.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/except.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/filenames.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/fixed-value.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/flags.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/function.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/gcc-plugin.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/genrtl.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/ggc.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/gimple.def
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/gimple.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/gsstruct.def
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/gtype-desc.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/hard-reg-set.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/hashtab.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/highlev-plugin-common.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/hwint.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/incpath.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/input.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/insn-constants.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/insn-flags.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/insn-modes.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/insn-notes.def
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/intl.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/ipa-prop.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/ipa-reference.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/ipa-utils.h
%dir %{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/java
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/java/java-tree.def
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/langhooks.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/libiberty.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/line-map.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/machmode.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/md5.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/mode-classes.def
%dir %{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/objc
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/objc/objc-tree.def
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/obstack.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/omp-builtins.def
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/options.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/opts.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/output.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/params.def
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/params.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/partition.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/plugin-version.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/plugin.def
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/plugin.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/pointer-set.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/predict.def
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/predict.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/prefix.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/pretty-print.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/real.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/reg-notes.def
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/rtl.def
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/rtl.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/safe-ctype.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/sbitmap.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/splay-tree.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/statistics.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/symtab.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/sync-builtins.def
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/system.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/target.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/timevar.def
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/timevar.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/tm-preds.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/tm.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/tm_p.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/toplev.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/tree-check.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/tree-dump.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/tree-flow-inline.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/tree-flow.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/tree-inline.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/tree-iterator.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/tree-pass.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/tree-ssa-alias.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/tree-ssa-operands.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/tree-ssa-sccvn.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/tree.def
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/tree.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/treestruct.def
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/varray.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/vec.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/vecprim.h
%{_libdir}/gcc/%{_target_platform}/%{version}/plugin/include/version.h
%dir %{_libdir}/gcc/%{_target_platform}/%{version}/include
%{_libdir}/gcc/%{_target_platform}/%{version}/include/abmintrin.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/ammintrin.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/avxintrin.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/bmmintrin.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/cpuid.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/cross-stdarg.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/emmintrin.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/float.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/fma4intrin.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/ia32intrin.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/immintrin.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/iso646.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/lwpintrin.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/mf-runtime.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/mm3dnow.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/mm_malloc.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/mmintrin.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/nmmintrin.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/omp.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/pmmintrin.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/popcntintrin.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/smmintrin.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/ssp
%{_libdir}/gcc/%{_target_platform}/%{version}/include/stdarg.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/stdbool.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/stddef.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/stdfix.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/stdint-gcc.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/stdint.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/tmmintrin.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/unwind.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/varargs.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/wmmintrin.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/x86intrin.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/xmmintrin.h
%{_libdir}/gcc/%{_target_platform}/%{version}/include/xopintrin.h
%dir %{_libexecdir}/gcc
%dir %{_libexecdir}/gcc/%{_target_platform}
%dir %{_libexecdir}/gcc/%{_target_platform}/%{version}
%{_libexecdir}/gcc/%{_target_platform}/%{version}/collect2
%{_libexecdir}/gcc/%{_target_platform}/%{version}/lto1
%{_libexecdir}/gcc/%{_target_platform}/%{version}/lto-wrapper
%doc %{_mandir}/man1/gcc.1*
%doc %{_mandir}/man1/gcov.1*
%doc %{_mandir}/man7/fsf-funding.7*
%doc %{_mandir}/man7/gfdl.7*
%doc %{_mandir}/man7/gpl.7*
%doc %{_infodir}/gcc.info*
%doc %{_infodir}/gccinstall.info*
%doc %{_infodir}/gccint.info*
%doc %{_infodir}/libgomp.info*


%files -n cpp -f cpplib.lang
%defattr(-, root, root)
%doc gcc-%{version}/ABOUT-NLS gcc-%{version}/COPYING*
%doc gcc-%{version}/ChangeLog* gcc-%{version}/LAST_UPDATED
%doc gcc-%{version}/MAINTAINERS gcc-%{version}/NEWS
%doc gcc-%{version}/README* gcc-%{version}/*/*.html
/lib/cpp
%{_bindir}/cpp
%doc %{_infodir}/cpp.info*
%doc %{_infodir}/cppinternals.info*
%doc %{_mandir}/man1/cpp.1*
%dir %{_prefix}/libexec/gcc
%dir %{_prefix}/libexec/gcc/%{_target_platform}
%dir %{_prefix}/libexec/gcc/%{_target_platform}/%{version}
%{_libexecdir}/gcc/%{_target_platform}/%{version}/cc1


%files g++
%defattr(-, root, root)
%doc gcc-%{version}/ABOUT-NLS gcc-%{version}/COPYING*
%doc gcc-%{version}/ChangeLog* gcc-%{version}/LAST_UPDATED
%doc gcc-%{version}/MAINTAINERS gcc-%{version}/NEWS
%doc gcc-%{version}/README* gcc-%{version}/*/*.html
%{_bindir}/c++
%{_bindir}/g++
%{_bindir}/%{_target_platform}-g++
%{_bindir}/%{_target_platform}-c++
%dir %{_libexecdir}/gcc
%dir %{_libexecdir}/gcc/%{_target_platform}
%dir %{_libexecdir}/gcc/%{_target_platform}/%{version}
%{_libexecdir}/gcc/%{_target_platform}/%{version}/cc1plus
%doc %{_mandir}/man1/g++.1*


%files -n libstdc++-devel
%defattr(-, root, root)
%dir %{_includedir}/c++
%{_includedir}/c++/*
%{_libdir}/libstdc++.a
%{_libdir}/libstdc++.la
%{_libdir}/libstdc++.so
%{_libdir}/libsupc++.a
%{_libdir}/libsupc++.la


%files -n libstdc++6
%defattr(-, root, root)
%{_libdir}/libstdc++.so.6*
%dir %{_datadir}/gcc-%{version}
%dir %{_datadir}/gcc-%{version}/python
%dir %{_datadir}/gcc-%{version}/python/libstdcxx
%dir %{_datadir}/gcc-%{version}/python/libstdcxx/v6
%{_datadir}/gcc-%{version}/python/libstdcxx/__init__.py
%{_datadir}/gcc-%{version}/python/libstdcxx/v6/__init__.py
%{_datadir}/gcc-%{version}/python/libstdcxx/v6/printers.py


%files -n libgomp1
%defattr(-, root, root)
%{_libdir}/libgomp.so.1*


%files -n libmudflap0
%defattr(-, root, root)
%{_libdir}/libmudflap.so.0*
%{_libdir}/libmudflapth.so.0*


%files -n libgcc_s1
%defattr(-, root, root)
%{_libdir}/libgcc_s.so.1
