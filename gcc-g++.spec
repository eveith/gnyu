Name: gcc-g++
Version: 4.2.1
Release: 4ev
Summary: The GNU Compiler Collection (C++ Package)
License: GPL
Group: Development/Languages
Source0: ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{version}/gcc-core-%{version}.tar.bz2
Source1: ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{version}/gcc-g++-%{version}.tar.bz2
URL: http://gcc.gnu.org/
BuildRequires: gcc-core, make >= 3.79.1, binutils
BuildRoot: %{_tmppath}/%{name}-root

%description
The GNU Compiler Collection includes front ends for C, C++, Objective-C,
Fortran, Java, and Ada, as well as libraries for these languages (libstdc++,
libgcj,...). The GCC is one of the most basic things a system will need if new
software is ever compiled on it.

This package comes with the C++ compiler.


%package -n libstdc++
Summary: Standard C++ implementations library
Group: System Environment/Library
Provides: libtool(%{_libdir}/libstdc++.la)
Provides: libtool(%{_libdir}/libsupc++.la)

%description -n libstdc++
The C++ standard defines some methods and classes that ought to be always
available. The libstdc++ is the GNU implementation of these methods/classes.
It is used by every program that is written in C++ and dynamically linked.


%prep
%setup -q -T -b0 -n "gcc-%{version}"
%setup -q -D -T -b1 -n "gcc-%{version}"
mkdir -p "$RPM_BUILD_DIR"/"%{name}-obj"


%build
pushd "$RPM_BUILD_DIR"/"%{name}-obj"

# Run configure
"$RPM_BUILD_DIR"/"gcc-%{version}"/configure \
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
	--without-x 
make %{_smp_mflags}

popd


%install
[[ "$RPM_BUILD_ROOT" != "/" ]] && rm -rf "$RPM_BUILD_ROOT"

pushd "$RPM_BUILD_DIR"/"%{name}-obj"

make -C %{_target_platform}/libstdc++-v3 install DESTDIR="$RPM_BUILD_ROOT"

mkdir -p "$RPM_BUILD_ROOT"/"%{_bindir}"
cp -v gcc/g++ "$RPM_BUILD_ROOT"/%{_bindir}/%{_target_platform}-g++ 

pushd "$RPM_BUILD_ROOT"/"%{_bindir}"

ln -sf %{_target_platform}-g++ g++
ln -sf %{_target_platform}-g++ c++
ln -sf %{_target_platform}-g++ %{_target_platform}-c++

popd

mkdir -p "$RPM_BUILD_ROOT"/%{_libexecdir}/gcc/%{_target_platform}/%{version}
cp -v gcc/cc1plus \
	"$RPM_BUILD_ROOT"/"%{_libexecdir}"/gcc/"%{_target_platform}"/"%{version}"

popd

%find_lang libstdc++

rm -f "$RPM_BUILD_ROOT"/"%{_infodir}"/dir


%clean
[[ "$RPM_BUILD_ROOT" != "/" ]] && rm -rf "$RPM_BUILD_ROOT"
rm -rf "$RPM_BUILD_DIR"/"%{name}-obj"


%post -n libstdc++
/sbin/ldconfig

%postun -n libstdc++
/sbin/ldconfig


%files
%defattr(-, root, root)
%doc ABOUT-NLS BUGS COPYING* ChangeLog* FAQ LAST_UPDATED MAINTAINERS NEWS
%doc README* *.html
%{_bindir}/*?++
%{_libexecdir}/gcc/%{_target_platform}/%{version}/cc1plus

%files -n libstdc++ -f libstdc++.lang
%{_includedir}/c++/
%{_libdir}/libstdc++*.*
%{_libdir}/libsupc++*.*
