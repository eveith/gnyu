Name: pixman
Version: 0.15.8
Release: 2ev
Summary: A library to privde low-level pixel manipulation features
URL: http://www.x.org/
Group: System Environment/Libraries
License: MIT
Vendor: GNyU-Linux
Source: http://ftp.x.org/pub/individual/lib/pixman-%{version}.tar.bz2
BuildRequires: make, gcc, pkg-config >= 0.9.0

%description
pixman is a library that provides low-level pixel manipulation
features such as image compositing and trapezoid rasterization.


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
	%doc AUTHORS COPYING ChangeLog README NEWS TODO
	%{_includedir}/pixman-1/
	%{_libdir}/libpixman-1.*
	%{_libdir}/pkgconfig/pixman-1.pc
