Name: libogg
Version: 1.1.3
Release: 1ev
Summary: The Ogg bitstream library
URL: http://www.xiph.org/
Group: System Environment/Libraries
License: BSD
Vendor: GNyU-Linux
Source: http://www.vorbis.com/files/1.0.1/unix/%{name}-%{version}.tar.gz
BuildRequires: make >= 3.79.1, gcc, pkg-config
Requires: pkg-config

%description
Libogg is a library for manipulating ogg bitstreams.  It handles
both making ogg bitstreams and getting packets from ogg bitstreams.


%prep
%setup -q


%build
%configure \
	--enable-static
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR="${RPM_BUILD_ROOT}"
rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc AUTHORS CHANGES COPYING README
%doc doc/index.html
%doc doc/framing.html
%doc doc/oggstream.html
%doc doc/white-ogg.png
%doc doc/white-xifish.png
%doc doc/stream.png
%doc doc/libogg/*
%doc %{_datadir}/doc/%{name}-%{version}
%{_libdir}/libogg.*
%{_includedir}/ogg/
%{_libdir}/pkgconfig/ogg.pc
%{_datadir}/aclocal/ogg.m4
