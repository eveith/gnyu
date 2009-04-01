Name: lcms
Version: 1.18
Release: 2ev
Summary: A little colour management system
URL: http://www.littlecms.com/
Group: System Environment/Libraries
License: BSD
Vendor: GNyU-Linux
Source: http://www.littlecms.com/lcms-%{version}.tar.gz
BuildRequires: gcc, make, pkg-config, libtiff, libpng, libjpeg, zlib
Requires: python >= %{python_version}

%description
Little cms intends to be a small-footprint, speed optimized color management
engine in open source form.


%prep
%setup -q


%build
%configure \
	--with-python
%{__make} %{?_smp_mflags}

%install
%{__make} install DESTDIR='%{buildroot}'


%post
%{__ldconfig}

%postun
%{__ldconfig}


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
%doc %{_mandir}/man1/*.1*
%{_libdir}/python?.?/site-packages/lcms.py
%{_libdir}/python?.?/site-packages/_lcms.*
