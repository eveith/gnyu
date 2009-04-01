Name: lcms
Version: 1.15
Release: 1ev
Summary: A little colour management system
URL: http://www.littlecms.com/
Group: System Environment/Libraries
License: LGPL
Vendor: MSP Slackware
Source: http://www.littlecms.com/lcms-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root
%define pyver %(echo $(python -c "import sys; print sys.version[0:3]"))
BuildRequires: libtiff, libpng, libjpeg, make >= 3.79.1, gcc-core
BuildRequires: python >= %pyver, zlib
Provides: libtool(%{_libdir}/liblcms.la)

%description
Little cms intends to be a small-footprint, speed optimized color management
engine in open source form.


%prep
%setup -q


%build
%configure \
	--with-python
make %{_smp_mflags}

%install
[ "$RPM_BUILD_ROOT" != '/' ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"
rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != '/' ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README* 
%{_bindir}/icc2ps
%{_bindir}/icclink
%{_bindir}/icctrans
%{_bindir}/jpegicc
%{_bindir}/tiffdiff
%{_bindir}/tifficc
%{_bindir}/wtpt
%{_includedir}/icc34.h
%{_includedir}/lcms.h
%{_libdir}/liblcms.*
%{_libdir}/pkgconfig/lcms.pc
%{_mandir}/man1/*.1*
