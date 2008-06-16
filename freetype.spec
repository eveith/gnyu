Name: freetype
Version: 2.3.5
Release: 1ev
Summary: An open-source font renderer
URL: http://www.freetype.org/
Group: System Environment/Libraries
License: GPL
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: http://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz
Patch0: freetype-2.1.10-enable-ft2-bci.patch
Patch1: freetype-2.2.1-memcpy-fix.patch
Patch2: freetype-2.3.0-enable-spr.patch
Patch3: freetype-multilib.patch
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc-core, zlib

%description
FreeType 2 is a software font engine that is designed to be small, efficient,
highly customizable, and portable while capable of producing high-quality
output (glyph images). It can be used in graphics libraries, display servers,
font conversion tools, text image generation tools, and many other products as
well.


%prep
%setup -q
# %patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1


%build
%configure
%__make %{_smp_mflags}


%install
[ "$RPM_BUILD_ROOT" != '/' ] && %__rm -rf "$RPM_BUILD_ROOT"
%__make_install DESTDIR="$RPM_BUILD_ROOT"


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != '/' ] && %__rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc ChangeLog* README* docs/*
%{_bindir}/freetype-config
%{_includedir}/freetype2/
%{_includedir}/ft2build.h
%{_libdir}/libfreetype.*
%{_libdir}/pkgconfig/freetype2.pc
%{_datadir}/aclocal/freetype2.m4
