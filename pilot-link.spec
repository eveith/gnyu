Name: pilot-link
Version: 0.12.2
Release: 1ev
Summary: A suite of tools to connect a Palm handheld with Linux
URL: http://www.pilot-link.org/
Group: Applications/Productivity
License: LGPL
Vendor: MSP Slackware
Source: http://downloads.pilot-link.org.nyud.net:8090/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, libusb, python, popt
Requires: popt, perl
Provides: libtool(%{_libdir}/libpisock.la), libtool(%{_libdir}/libpisync.la)
%define pyver %(echo $(python -c "import sys; print sys.version[0:3]"))

%description
The pilot-link suite of tools contains a robust library and a series of
conduits for moving information between your desktop or workstation and your
Palm handheld device, such as those made by Palm, Sony, Handspring, Handera,
and others. It also includes language bindings for languages such as Perl,
Python, and Java.


%package java
Summary: Java bindings for Pilot Link
Group: System Environment/Library
Requires: sun-jre, pilot-link

%description java
Java bindings for Pilot Link


%package perl
Summary: Perl bindings to Pilot Link
Group: System Environment/Libraries
Requires: perl, pilot-link

%description perl
Perl bindings to Pilot Link


%package python
Summary: Python bindings to Pilot Link
Group: System Environment/Libraries
Requires: python >= %pyver, pilot-link

%description python
Python bindings to Pilot Link


%prep
%setup -q


%build
%configure \
	--without-perl \
	--with-java=%{_libdir}/java \
	--with-python \
	--enable-conduits \
	--enable-threads \
	--enable-libusb \
	--disable-debug
make


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT" 

[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"

%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc AUTHORS COPYING* NEWS README
%{_bindir}/*
%{_includedir}/pi-*.h
%{_libdir}/*.*
%{_libdir}/pkgconfig/pilot-link.pc
%{_datadir}/pilot-link/
%{_datadir}/aclocal/pilot-link.m4
%{_mandir}/man1/*
%{_mandir}/man7/*

%files java
%defattr(-, root, root)
%doc bindings/Java/README* bindings/Java/TODO
%{_libdir}/java/jre/lib/libjpisock.so

%files python
%defattr(-, root, root)
%doc bindings/Python/README bindings/Python/TODO
%{_libdir}/python*/site-packages/*.py
