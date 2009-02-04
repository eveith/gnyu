Name: cmake
Version: 2.4.6
Release: 1ev
Summary: A cross-platform build system
URL: http://www.cmake.org/
Group: Development/Tools
License: BSD
Vendor: MSP Slackware
Source: http://www.cmake.org/files/v2.4/cmake-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, gcc-g++, curl, expat, zlib, xmlrpc-c
Requires: curl, expat, zlib, xmlrpc-c

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
# Strip prefix from dir variables since cmake's bootstrap skript's somehow
# strange here...
_DATADIR=$(echo %{_datadir} | sed 's,^%{_prefix},,')
_DOCDIR=$(echo %{_docdir} | sed 's,^%{_prefix},,')
_MANDIR=$(echo %{_mandir} | sed 's,^%{_prefix},,')

CC=%{_target_platform}-gcc CXX=%{_target_platform}-g++ \
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./bootstrap \
	--prefix=%{_prefix} \
	--datadir=/${_DATADIR}/cmake \
	--docdir=/${_DOCDIR}/cmake-%{version} \
	--mandir=/${_MANDIR} \
make


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"

[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc Docs/*.html Docs/*.txt Docs/*.vim
%{_mandir}/*/*
%{_bindir}/c*
%{_datadir}/cmake/
