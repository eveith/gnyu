Name: xtrans
Version: 1.2.1
Release: 4ev
Summary: A library of transport code shared amoung various X packages
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
BuildRequires: make, pkg-config
BuildArch: noarch

%description
xtrans is a library of code that is shared among various X packages to handle
network protocol transport in a modular fashion, allowing a single place to
add new transport types. It is used by the X server, libX11, libICE, the
X font server, and related components.
It is however, *NOT* a shared library, but code which each consumer includes
and builds it's own copy of with various #ifdef flags to make each copy slightly
different. To support this in the modular build system, this package simply
installs the C source files into $(prefix)/include/X11/Xtrans and installs a
pkg-config file and an autoconf m4 macro file with the flags needed to use it.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__make} install DESTDIR='%{buildroot}'


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc AUTHORS COPYING README NEWS ChangeLog
%{_includedir}/X11/Xtrans/
%{_libdir}/pkgconfig/xtrans.pc
%{_datadir}/aclocal/xtrans.m4
