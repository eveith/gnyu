Name: mesalib
Version: 7.2
Release: 3ev
Summary: 3-D graphics library which uses the OpenGL API
URL: http://mesa3d.sf.net/
Group: System Environment/Libraries
License: MIT, LGPL-2
Vendor: GNyU-Linux
Source: http://downloads.sourceforge.net/mesa3d/MesaLib-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: gcc, gcc-g++, make >= 3.79.1, pkg-config >= 0.9.0
BuildRequires: libstdc++, libdrm >= 2.3.1, expat
BuildRequires: libX11, libICE, libSM, libXdamage, libXext, libXfixes, libXt
BuildRequires: libXxf86vm, libxcb

%description
Mesa is a 3-D graphics library which uses the OpenGL API (Application
Programming Interface). Mesa cannot be called an implementation of OpenGL
since the author did not obtain an OpenGL license from SGI. Furthermore, Mesa
cannot claim OpenGL conformance since the conformance tests are only available
to OpenGL licensees. Despite these technical/legal terms, you may find Mesa to
be a valid alternative to OpenGL. Most applications written for OpenGL can use
Mesa instead without changing the source code.


%prep
%setup -q -n 'Mesa-%{version}'


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__mkdir_p} '%{buildroot}/%{_prefix}'
%{__make} install INSTALL_DIR='%{_prefix}' DESTDIR='%{buildroot}'


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc docs/*
%{_includedir}/GL/
%{_libdir}/dri/
%{_libdir}/libGL.*
%{_libdir}/libGLU.*
%{_libdir}/libGLw.*
%{_libdir}/pkgconfig/gl.pc
%{_libdir}/pkgconfig/glu.pc
%{_libdir}/pkgconfig/glw.pc
%{_libdir}/pkgconfig/dri.pc
