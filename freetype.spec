Name: freetype
Version: 2.3.6
Release: 2ev
Summary: An open-source font renderer
URL: http://www.freetype.org/
Group: System Environment/Libraries
License: GPL
Vendor: GNyU-Linux
Source: http://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.bz2
Patch0: freetype-2.1.10-enable-ft2-bci.patch
Patch1: freetype-2.2.1-memcpy-fix.patch
Patch2: freetype-2.3.0-enable-spr.patch
Patch3: freetype-multilib.patch
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: coreutils, grep, sed, make >= 3.79.1, gcc, zlib, pkg-config

%description
FreeType 2 is a software font engine that is designed to be small, efficient,
highly customizable, and portable while capable of producing high-quality
output (glyph images). It can be used in graphics libraries, display servers,
font conversion tools, text image generation tools, and many other products as
well.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc ChangeLog* README* docs/*
%{_bindir}/freetype-config
%{_includedir}/freetype2/
%{_includedir}/ft2build.h
%{_libdir}/libfreetype.*
%{_libdir}/pkgconfig/freetype2.pc
%{_datadir}/aclocal/freetype2.m4
