Name: apr-util
Version: 1.2.12
Release: 1ev
Summary: APR-util provides a number of helpful abstractions on top of APR.
URL: http://apr.apache.org/
Group: System Environment/Libraries
License: Apache 2.0
Vendor: GNyU-Linux
Source: http://www.apache.org/dist/apr/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc, apr, db >= 4.5, sqlite >= 3.0
BuildRequires: openldap-libs, %{_prefix}/bin/apr-1-config, expat, pkg-config

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
	--with-apr=%{_prefix} \
	--includedir=%{_includedir}/apr \
	--with-ldap \
	--with-dbm=db45 \
	--with-berkeley-db \
	--with-sqlite3
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
%doc CHANGES LICENSE NOTICE
%{_includedir}/apr/*
%{_libdir}/pkgconfig/apr-util-1.pc
%{_libdir}/libaprutil*.*
%{_libdir}/aprutil.exp
%{_bindir}/apu-1-config
