Name: xorg-glproto
%define src_name %(echo %{name} | %{__sed} 's,^xorg-,,')
Version: 1.4.9
Release: 2ev
Summary: Protocol information and development headers for X11 OpenGL extension
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/releases/individual/proto/%{src_name}-%{version}.tar.bz2
BuildRequires: make, pkg-config >= 0.9.0
Requires: xorg-fslayout
BuildArch: noarch

%description
This package provides development headers describing the wire protocol for 
OpenGL-related extensions, used to enable the rendering of applications using 
OpenGL.


%prep
%setup -q -n '%{src_name}-%{version}'


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

# Make sure %doc files are there, even if they're empty.
touch README COPYING ChangeLog TODO AUTHORS NEWS


%files
%defattr(-, root, root)
%doc README COPYING ChangeLog TODO AUTHORS NEWS
%{_includedir}/GL/glxint.h
%{_includedir}/GL/glxmd.h
%{_includedir}/GL/glxproto.h
%{_includedir}/GL/glxtokens.h
%{_includedir}/GL/internal/glcore.h
%{_libdir}/pkgconfig/%{src_name}.pc
