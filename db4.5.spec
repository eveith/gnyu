Name: db45
Version: 4.5.20
Release: 2ev
Summary: An embedded database for traditional and client/server applications
URL: http://www.oracle.com/database/berkeley-db/index.html
Group: System Environment/Libraries
License: BSD
Vendor: GNyU-Linux
Source: http://download-east.oracle.com/berkeley-db/db-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: coreutils, grep, sed, gcc, gcc-g++, make >= 3.79.1, java-jdk
BuildRequires: gettext, libstdc++
Obsoletes: db < %{version}-%{release}
Provides: db = %{version}

%description
Berkeley DB (libdb) is a programmatic toolkit that provides embedded database
support for both traditional and client/server applications. It includes
b+tree, queue, extended linear hashing, fixed, and variable-length record
access methods, transactions, locking, logging, shared memory caching,
database recovery, and replication for highly available systems. DB supports
C, C++, Java, PHP, and Perl APIs. It is available for a wide variety of UNIX
platforms as well as Windows XP, Windows NT, and Windows '95 (MSVC 6 and 7).


%package cxx
Summary: C++ API to Berkeley DB
Group: System Environment/Libraries
Obsoletes: db-cxx < %{version}-%{release}
Provides: db-cxx = %{version}

%description cxx
While the "db" package only contains the C API, this package comes with C++
bindings for Berkeley DB. It is totally independend from the C API package.


%package java
Summary: Java API to Berkeley DB
Group: System Environment/Libraries
Obsoletes: db-java < %{version}-%{release}
Provides: db-java = %{version}-%{release}

%description java
While the "db" package only contains the C API, this package comes with Java
bindings for Berkeley DB. It is totally independend from the C API package. 


%package utils
Summary: Command line utilities to manage berkeley databases
Group: Applications/Databases
Requires: db45 = %{version}
Obsoletes: db-utils < %{version}-%{release}

%description utils
This package provides serveral helper utilities to manage Berkeley DB
databases, such as:
db_archive  db_checkpoint  db_deadlock  db_dump  db_hotbackup  db_load
db_printlog  db_recover  db_stat  db_upgrade  db_verify


%package docs
Summary: Complete documentation package for Berkeley DB
Group: Documentation
Obsoletes: db-docs < %{version}-%{release}

%description docs
Independently shipped from the APIs, this package provides the complete
developer's documentation


%prep
%setup -q -n db-%{version}


%build
pushd build_unix

CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS
FFLAGS="${FFLAGS:-%optflags}" ; export FFLAGS
../dist/configure --host=%{_host} \
	--build=%{_build} \
	--target=%{_target_platform} \
	--program-prefix=%{?_program_prefix} \
	--prefix=%{_prefix} \
	--exec-prefix=%{_exec_prefix} \
	--bindir=%{_bindir} \
	--sbindir=%{_sbindir} \
	--sysconfdir=/etc \
	--datadir=%{_datadir} \
	--includedir=%{_includedir} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libexecdir} \
	--localstatedir=%{_localstatedir} \
	--sharedstatedir=%{_sharedstatedir} \
	--mandir=%{_mandir} \
	--infodir=%{_infodir} \
	--enable-compat185 \
	--enable-cxx \
	--enable-java \
	--enable-pthread_api \
	--enable-posixmutexes \
	--enable-verify \
	--enable-statistics
%{__make} %{?_smp_mflags}
popd


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'

pushd build_unix
%{__make_install} DESTDIR='%{buildroot}'

# We do at least need to have write access for the installation.
%{__chmod} 0755 '%{buildroot}/%{_bindir}'/*

# Move stupidly placed docs
%{__rm} -rf '%{buildroot}/%{_prefix}/docs'

popd


%post
/sbin/ldconfig

%post cxx
/sbin/ldconfig

%post java
/sbin/ldconfig

%postun
/sbin/ldconfig

%postun cxx
/sbin/ldconfig

%postun java
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc README LICENSE
%{_includedir}/db.h
%{_includedir}/db_185.h
%{_libdir}/libdb.so
%{_libdir}/libdb.a
%{_libdir}/libdb-4*.*

%files cxx
%defattr(-, root, root)
%doc README LICENSE
%{_includedir}/db_cxx.h
%{_libdir}/libdb_cxx.so
%{_libdir}/libdb_cxx.a
%{_libdir}/libdb_cxx-4*.*

%files java
%defattr(-, root, root)
%doc README LICENSE
%{_libdir}/libdb_java.so
%{_libdir}/libdb_java-4*.*
%{_libdir}/db.jar

%files utils
%defattr(-, root, root)
%doc README LICENSE
%attr(0555, root, root) %{_bindir}/db_*

%files docs
%defattr(-, root, root)
%doc docs/
