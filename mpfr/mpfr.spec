Name: mpfr
Version: 2.4.1
Release: 1ev
Summary: A C library for multiple-precision floating-point computations
URL: http://www.mpfr.org
Group: System Environment/Libraries
License: GPL-2
Vendor: GNyU-Linux
Source: http://www.mpfr.org/mpfr-current/mpfr-%{version}.tar.lzma
BuildRequires: make, gcc, gmp >= 4.2.3

%description
The main goal of MPFR is to provide a library for multiple-precision
floating-point computation which is both efficient and has a well-defined
semantics. It copies the good ideas from the ANSI/IEEE-754 standard for
double-precision floating-point arithmetic (53-bit mantissa).


%prep
	%setup -q
	%{__wget} 'http://www.mpfr.org/mpfr-%{version}/patches'
	%{__patch} -p1 < patches


%build
	%configure \
		--enable-thread-safe
	%{__make} %{?_smp_mflags}
	%{__make} check


%install
	%{__make} install DESTDIR='%{buildroot}'

	[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
		&& %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
	%{__ldconfig}
	update-info-dir


%postun
	%{__ldconfig}
	update-info-dir


%files
	%defattr(-, root, root)
	%doc AUTHORS BUGS COPYING* README FAQ* NEWS VERSION TODO ChangeLog PATCHES
	%{_includedir}/mpfr.h
	%{_includedir}/mpf2mpfr.h
	%doc %{_infodir}/mpfr.info*
	%{_libdir}/libmpfr.*	
