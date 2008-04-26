Name: mesalib
Version: 7.0.3
Release: 1ev
Summary: 3-D graphics library which uses the OpenGL API
URL: http://mesa3d.sf.net/
Group: System Environment/Libraries
License: MIT, LGPL
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: http://downloads.sourceforge.net/mesa3d/MesaLib-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: gcc, gcc-g++, sed, make >= 3.79.1

%description
Mesa is a 3-D graphics library which uses the OpenGL API (Application
Programming Interface). Mesa cannot be called an implementation of OpenGL
since the author did not obtain an OpenGL license from SGI. Furthermore, Mesa
cannot claim OpenGL conformance since the conformance tests are only available
to OpenGL licensees. Despite these technical/legal terms, you may find Mesa to
be a valid alternative to OpenGL. Most applications written for OpenGL can use
Mesa instead without changing the source code.


%prep
%setup -q -n Mesa-%{version}
%{__sed} -i "s,\(OPT_FLAGS\s*=\s*\).*,\1${RPM_OPT_FLAGS}," configs/linux


%build
%ifarch %ix86
%{__make} %{?_smp_mflags} linux-x86
%endif
%ifarch x86_64
%{__make} %{?_smp_mflags} linux-x86-64
%endif


%install
%{__mkdir_p} '%{buildroot}/%{_prefix}'
%{__make_install} INSTALL_DIR='%{_prefix}' DESTDIR='%{buildroot}'
%{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-, root, root)
%doc docs/
%{_includedir}/GL/
%{_libdir}/libGL.*
%{_libdir}/libGLU.*
%{_libdir}/libGLw.*
%{_libdir}/libOSMesa.*
%{_libdir}/pkgconfig/gl.pc
%{_libdir}/pkgconfig/glu.pc
%{_libdir}/pkgconfig/glw.pc
