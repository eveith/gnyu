Name: gcc
Version: 4.2.2
Release: 1ev
Summary: The GNU Compiler Collection (Core Package)
License: GPL-3
Group: Development/Languages
Source0: ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{version}/gcc-%{version}.tar.bz2
URL: http://gcc.gnu.org/
BuildRequires: gcc-core, make >= 3.79.1, binutils, bison, sed, gettext
BuildRoot: %{_tmppath}/%{name}-root
Provides: gcc-core = %{version}

%description
The GNU Compiler Collection includes front ends for C, C++, Objective-C,
Fortran, Java, and Ada, as well as libraries for these languages (libstdc++,
libgcj,...). The GCC is one of the most basic things a system will need if new
software is ever compiled on it.
This package contains "gcc", the GNU C Compiler. 


%package g++
Summary: The GNU Compiler Collection (C++ Package)

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
%setup -q -T -b0
# %setup -q -D -T -b1 -n "gcc-%{version}"
%{__mkdir_p} %{buildroot}/%{name}-obj


%build
pushd %{buildroot}/%{name}-obj

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
%{__make} %{_smp_mflags}

popd


%install
[[ "$RPM_BUILD_ROOT" != "/" ]] && rm -rf "$RPM_BUILD_ROOT"

pushd ${RPM_BUILD_DIR}/%{name}-obj
%{__make_install} DESTDIR='%{buildroot}'
popd

# Remove libiberty.a, this is shipped by GNU binutils.
%{__rm} -f "$RPM_BUILD_ROOT/%{_libdir}/libiberty.a"

%find_lang gcc
%find_lang libstdc++

pushd %{buildroot}/%{_bindir}
ln -sf gcc cc
ln -sf %{_target_platform}-g++ g++
ln -sf %{_target_platform}-g++ c++
ln -sf %{_target_platform}-g++ %{_target_platform}-c++
popd

%{__rm} -f $RPM_BUILD_ROOT/%{_infodir}/dir


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__rm} -rf ${RPM_BUILD_DIR}/%{name}-obj


%post
/sbin/ldconfig
update-info-dir

%postun 
/sbin/ldconfig
update-info-dir

%post g++
/sbin/ldconfig
update-info-dir

%postun g++
/sbin/ldconfig
update-info-dir

%files -f gcc.lang
%defattr(-, root, root)
%doc ABOUT-NLS BUGS COPYING* ChangeLog* FAQ LAST_UPDATED MAINTAINERS NEWS
%doc README* *.html
%{_bindir}/*cc*
%{_bindir}/cpp
%{_bindir}/gcov
%{_infodir}/*.info*
%{_libdir}/gcc/
%{_libdir}/libgcc_s*.*
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

%files -n libstdc++ -f libstdc++.lang
%{_includedir}/c++/
%{_libdir}/libstdc++*.*
%{_libdir}/libsupc++*.*
