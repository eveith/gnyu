Name: libsdlttf0
Version: 2.0.9
Release: 1.1ev
Summary: A library that allows to use TrueType fonts in SDL applications
URL: http://www.libsdl.org/projects/SDL_ttf/
Group: System Environment/Libraries
License: LGPL-2.1
Vendor: GNyU-Linux
Source: http://www.libsdl.org/projects/SDL_ttf/release/SDL_ttf-%{version}.tar.gz
BuildRequires: make, gcc
BuildRequires: libsdl >= 1.2.4, freetype >= 2.0.0, mesalib
BuildConflicts: freetype = 2.1.3
Conflicts: freetype = 2.1.3
Provides: libsdlttf = %{version}

%description
This is a sample library which allows you to use TrueType fonts in your SDL
applications. It comes with an example program "showfont" which displays an
example string for a given TrueType font file.


%prep
%setup -q -n 'SDL_ttf-%{version}'


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR="${RPM_BUILD_ROOT}"


%post
%{__ldconfig}


%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc CHANGES README COPYING
%{_includedir}/SDL/SDL_ttf.h
%{_libdir}/libSDL_ttf*.*
