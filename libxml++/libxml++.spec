Name: libxml++
Version: 2.23.1
Release: 1ev
Summary: A C++ wrapper for the libxml XML parser library
URL: http://libxmlplusplus.sourceforge.net/
Group: System Environment/Libraries
License: LGPL-2
Vendor: GNyU-Linux
Source: http://ftp.gnome.org/pub/GNOME/sources/libxml++/2.23/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: coreutils, grep, sed, make, gcc, gcc-g++, libxml2, glibmm >= 2.4
BuildRequires: pkg-config

%description
This library provides a C++ interface to XML files.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%{__mv} '%{buildroot}/%{_datadir}/doc/%{name}-2.6' \
	"${RPM_BUILD_DIR}/%{name}-%{version}/Docs"

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING NEWS README Docs/docs/*
%{_includedir}/libxml++-2.6/
%{_libdir}/libxml++-2.6.*
%{_libdir}/libxml++-2.6/
%{_libdir}/pkgconfig/libxml++-2.6.pc
