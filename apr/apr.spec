Name: apr
Version: 1.2.12
Release: 1ev
Summary: Runtime portability libraries for Unix
URL: http://apr.apache.org/
Group: System Environment/Libraries
License: Apache 2.0
Vendor: GNyU-Linux
Source: http://www.apache.org/dist/apr/apr-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc, pkg-config, openssl

%description
The mission of the Apache Portable Runtime (APR) project is to create and
maintain software libraries that provide a predictable and consistent
interface to underlying platform- specific implementations. The primary goal
is to provide an API to which software developers may code and be assured of
predictable if not identical behaviour regardless of the platform on which
their software is built, relieving them of the need to code special-case
conditions to work around or take advantage of platform-specific deficiencies
or features.


%prep
%setup -q


%build
%configure \
	--enable-threads \
	--with-installbuilddir=%{_datadir}/apr \
	--includedir=%{_includedir}/apr
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%{__rm} -f %{buildroot}/%{_infodir}/dir


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc CHANGES LICENSE README* NOTICE
%{_libdir}/pkgconfig/apr-1.pc
%{_libdir}/libapr*.*
%{_libdir}/apr.exp
%{_bindir}/apr-1-config
%{_datadir}/apr/
%{_includedir}/apr/
