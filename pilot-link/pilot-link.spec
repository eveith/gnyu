Name: pilot-link
Version: 0.12.5
Release: 2.0ev
Summary: A suite of tools to connect a Palm handheld with Linux
URL: http://www.pilot-link.org
Group: Applications/Productivity
License: LGPL-2
Vendor: GNyU-Linux
Source: http://downloads.pilot-link.org/%{name}-%{version}.tar.bz2
BuildRequires: sed, make, bison, libtool, gcc
BuildRequires: libpng, libusb, bluez, popt, readline
BuildRequires: python, perl >= 5.0
%define pyver %(echo $(python -c "import sys; print sys.version[0:3]"))

%description
The pilot-link suite of tools contains a robust library and a series of
conduits for moving information between your desktop or workstation and your
Palm handheld device, such as those made by Palm, Sony, Handspring, Handera,
and others. It also includes language bindings for languages such as Perl,
Python, and Java.


%package devel
Summary: Pilot-Link development headers
Group: Development/Libraries
Requires: pilot-link = %{version}-%{release}, pkg-config, automake

%description devel
Contains development headers, pkg-config file and m4 macros used when
developing extensions for pilot-link or applications that link against one of
pilot-link's libraries.


%package perl
Summary: Perl bindings to Pilot Link
Group: System Environment/Libraries
Requires: perl, pilot-link = %{version}-%{release}

%description perl
Perl bindings to Pilot Link


%package python
Summary: Python bindings to Pilot Link
Group: System Environment/Libraries
Requires: python >= %pyver, pilot-link = %{version}-%{release}

%description python
Python bindings to Pilot Link


%prep
%setup -q


%build
%configure \
	--with-perl \
	--without-java \
	--without-tcl \
	--with-python \
	--enable-conduits \
	--enable-threads \
	--enable-libusb \
	--disable-debug \
	--disable-static
%{__make} %{?_smp_mflags}
%{__make} check


%install
%{__make} install DESTDIR='%{buildroot}' 
%{__rm_rf} '%{buildroot}/%{perl_archlib}/perllocal.pod'


%post
%{__ldconfig}


%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc AUTHORS COPYING* NEWS README
%{_bindir}/pilot-*
%{_libdir}/libpisock.so*
%{_libdir}/libpisync.so*
%dir %{_datadir}/pilot-link
%dir %{_datadir}/pilot-link/pix
%dir %{_datadir}/pilot-link/prc
%dir %{_datadir}/pilot-link/udev
%{_datadir}/pilot-link/*/*.*


%files devel
%defattr(-, root, root)
%{_includedir}/pi-*.h
%{_libdir}/libpi*.la
%{_libdir}/pkgconfig/pilot-link.pc
%{_datadir}/aclocal/pilot-link.m4


%files python
%defattr(-, root, root)
%doc bindings/Python/README bindings/Python/TODO
%{python_sitelib}/pisock.py*
%{python_sitelib}/pisockextras.py*
%{python_sitelib}/_pisock.so
%{python_sitelib}/python_libpisock-0.12.5-py2.6.egg-info


%files perl
%defattr(-, root, root)
%doc bindings/Perl/README bindings/Perl/MANIFEST
%doc %{_mandir}/man3/PDA::Pilot.3pm
%dir %{perl_vendorarch}/PDA
%{perl_vendorarch}/PDA/Pilot.pm
%{perl_vendorarch}/PDA/dump.pl
%dir %{perl_vendorarch}/auto/PDA
%dir %{perl_vendorarch}/auto/PDA/Pilot
%{perl_vendorarch}/auto/PDA/Pilot/.packlist
%{perl_vendorarch}/auto/PDA/Pilot/Pilot.[bs][so]
%{perl_vendorarch}/auto/PDA/Pilot/autosplit.ix
