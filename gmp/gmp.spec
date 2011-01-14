Name: gmp
Version: 4.2.4
Release: 2ev
Summary: A very fast bignum library (GNU Multiple Precision Arithmetic Library)
URL: http://gmplib.org/
Group: System Environment/Libraries
License: LGPL-3
Vendor: GNyU-Linux
Source: ftp://ftp.gnu.org/gnu/gmp/gmp-%{version}.tar.bz2
BuildRequires: make, gcc, gcc-g++, libstdc++

%description
GMP is a free library for arbitrary precision arithmetic, operating on signed integers, 
rational numbers, and floating point numbers. There is no practical limit to the 
precision except the ones implied by the available memory in the machine GMP runs on.
GMP has a rich set of functions, and the functions have a regular interface. 
The main target applications for GMP are cryptography applications and research, 
Internet security applications, algebra systems, computational algebra research, etc.


%prep
	%setup -q


%build
	CFLAGS=${CFLAGS:-%{optflags}}
	CXXFLAGS=${CXXFLAGS:-%{optflags}}
	CC=${CC:-%{_target_platform}-gcc}
	CXX=${CXX:-%{_target_platform}-g++}
	export CC CXX CFLAGS CXXFLAGS

	./configure \
		--build='%{_target_platform}' \
		--prefix='%{_prefix}' \
		--exec-prefix='%{_exec_prefix}' \
		--bindir='%{_bindir}' \
		--sbindir='%{_sbindir}' \
		--sysconfdir='%{_sysconfdir}' \
		--datadir='%{_datadir}' \
		--includedir='%{_includedir}' \
		--libdir='/%{_lib}' \
		--libexecdir='%{_libexecdir}' \
		--sharedstatedir='%{_sharedstatedir}' \
		--localstatedir='%{_localstatedir}' \
		--mandir='%{_mandir}' \
		--infodir='%{_infodir}' \
		--enable-fat \
		--enable-cxx
	%{__make} %{?_smp_mflags}
	%{__make} check


%install
	%{__make} install DESTDIR='%{buildroot}'

	[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
		&& %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
	%{__ldconfig}


%postun
	%{__ldconfig}


%files
	%defattr(-, root, root)
	%doc README COPYING* AUTHORS NEWS
	%{_includedir}/gmp.h
	%{_includedir}/gmpxx.h
	%doc %{_infodir}/gmp.info*
	/%{_lib}/libgmp.*
	/%{_lib}/libgmpxx.*
