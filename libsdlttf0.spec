Name: libsdlttf
Version: 2.0.9
Release: 1ev
Summary: A library that allows to use TrueType fonts in SDL applications
URL: http://www.libsdl.org/projects/SDL_ttf/
Group: System Environment/Libraries
License: LGPL
Vendor: MSP Slackware
Source: http://www.libsdl.org/projects/SDL_ttf/release/SDL_ttf-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, libsdl, freetype >= 2.0.0, zlib
BuildConflicts: freetype = 2.1.3
Conflicts: freetype = 2.1.3

%description
This is a sample library which allows you to use TrueType fonts in your SDL applications. It comes with an example program "showfont" which displays an example string for a given TrueType font file.


%prep
%setup -q -n SDL_ttf-%{version}


%build
%configure
make %{_smp_mflags}


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"

[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc CHANGES README COPYING
%{_includedir}/SDL/SDL_ttf.h
%{_libdir}/libSDL_ttf*.*
