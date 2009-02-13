Name: exiv2
Version: 0.18
Release: 1ev
Summary: A library and cli utility to manage image metadata
URL: http://www.exiv2.org
Group: System Environment/Libraries
License: GPL-2
Vendor: GNyU-Linux
Source: http://www.exiv2.org/exiv2-0.18.tar.gz
BuildRequires: make, gcc-g++, zlib, expat, gettext, libstdc++

%description
Exiv2 is a C++ library and a command line utility to manage image metadata. 
It provides fast and easy read and write access to the Exif, IPTC and XMP 
metadata of images in various formats.


%prep
%setup -q


%build
%configure \
	--disable-rpath
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%find_lang exiv2


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files -f exiv2.lang
%defattr(-, root, root)
%doc README COPYING
%{_bindir}/exiv2
%{_includedir}/exiv2/
%{_libdir}/libexiv2.*
%{_libdir}/pkgconfig/exiv2.pc
%doc %{_mandir}/man1/exiv2.1*
