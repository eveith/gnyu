Name: cmake
Version: 2.6.2
Release: 2ev
Summary: A cross-platform build system
URL: http://www.cmake.org/
Group: Development/Tools
License: BSD
Vendor: GNyU-Linux
Source: http://www.cmake.org/files/v2.6/cmake-%{version}.tar.gz
BuildRequires: make, gcc-g++, libstdc++, ncurses, openssl

%description
CMake is a cross-platform, open-source build system. It is used to control the
software compilation process using simple platform and compiler independent
configuration files. It generates native makefiles and workspaces that can be
used in the compiler environment of your choice. CMake is quite sophisticated:
it is possible to support complex environments requiring system configuration,
pre-processor generation, and code generation.


%prep
%setup -q


%build
# Strip prefix from dir variables since cmake's bootstrap skript's somewhat
# strange here...
_datadir=$(echo %{_datadir} | sed 's,^%{_prefix},,')
_docdir=$(echo %{_docdir} | sed 's,^%{_prefix},,')
_mandir=$(echo %{_mandir} | sed 's,^%{_prefix},,')

CC='%{_target_platform}-gcc' CXX='%{_target_platform}-g++' \
CFLAGS="${CFLAGS:-%{optflags}}" CXXFLAGS="${CXXFLAGS:-%{optflags}}" \
./bootstrap \
	--prefix='%{_prefix}' \
	--datadir="${_datadir}/cmake" \
	--docdir="${_docdir}/cmake-%{version}" \
	--mandir="${_mandir}" 
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'


%files
%defattr(-, root, root)
%doc Docs/*.html Docs/*.txt Docs/*.vim
%{_bindir}/ccmake
%{_bindir}/cmake
%{_bindir}/cpack
%{_bindir}/ctest
%doc %{_mandir}/man1/ccmake.1*
%doc %{_mandir}/man1/cmake.1*
%doc %{_mandir}/man1/cmakecommands.1*
%doc %{_mandir}/man1/cmakecompat.1*
%doc %{_mandir}/man1/cmakemodules.1*
%doc %{_mandir}/man1/cmakepolicies.1*
%doc %{_mandir}/man1/cmakeprops.1*
%doc %{_mandir}/man1/cmakevars.1*
%doc %{_mandir}/man1/cpack.1*
%doc %{_mandir}/man1/ctest.1*
%dir %{_datadir}/apps/cmake/modules
%dir %{_datadir}/cmake
%dir %{_datadir}/cmake/Modules
%dir %{_datadir}/cmake/Templates
%dir %{_datadir}/cmake/include
%{_datadir}/cmake/Modules/*
%{_datadir}/cmake/Templates/*
%{_datadir}/cmake/include/*
