Name: db4.5
Version: 4.5.20
Release: 4ev
Summary: An embedded database for traditional and client/server applications
URL: http://www.oracle.com/database/berkeley-db/index.html
Group: System Environment/Libraries
License: BSD
Vendor: GNyU-Linux
Source: http://download.oracle.com/berkeley-db/db-%{version}.tar.gz
BuildRequires: gcc, gcc-g++, make >= 3.79.1, java-jdk, gettext, libstdc++
Obsoletes: db < %{version}-%{release}, db45
Provides: db = %{version}

%description
	Berkeley DB (libdb) is a programmatic toolkit that provides embedded
	database support for both traditional and client/server applications.
	It includes b+tree, queue, extended linear hashing, fixed, and 
	variable-length record access methods, transactions, locking, logging,
	shared memory caching, database recovery, and replication for highly 
	available systems. DB supports C, C++, Java, PHP, and Perl APIs, which
	can be installed from separate packages. It is available for a wide 
	variety of UNIX platforms as well as Windows XP, Windows NT, and 
	Windows '95 (MSVC 6 and 7).


%package -n db-devel
Summary: Development headers for Berekeley DB %{version}
Group: System Environment/Libraries
Provides: db4.5-devel = %{version}-%{release}

%description -n db-devel
	While the Berkeley DB libraries are strongly ABI-versioned and it is not
	possible to use a newer minor number if a program has been compiled
	against the older one without re-compiling it, the headers cannot be
	installed in parallel.
	This devel package contains all db headers for version %{version}. You
	need to installed them if you want to link against this version of the db
	libraries.


%package cxx
Summary: C++ API to Berkeley DB
Group: System Environment/Libraries
Obsoletes: db-cxx < %{version}-%{release}, db45-cxx
Provides: db-cxx = %{version}

%description cxx
	While the "db" package only contains the C API, this package comes with 
	C++ bindings for Berkeley DB. It is totally independend from the C 
	API package.


%package java
Summary: Java API to Berkeley DB
Group: System Environment/Libraries
Obsoletes: db-java < %{version}-%{release}, db45-java
Provides: db-java = %{version}-%{release}

%description java
	While the "db" package only contains the C API, this package comes with
	Java bindings for Berkeley DB. It is totally independend from the C API
	package. 


%package -n db-utils
Summary: Command line utilities to manage berkeley databases
Group: Applications/Databases
Requires: db4.5 = %{version}
Provides: db4.5-utils = %{version}-%{release}
Obsoletes: db-utils < %{version}-%{release}, db45-utils
Obsoletes: db4.5-utils

%description -n db-utils
	This package provides serveral helper utilities to manage Berkeley DB
	databases, such as:
	db_archive  db_checkpoint  db_deadlock  db_dump  db_hotbackup  db_load
	db_printlog  db_recover  db_stat  db_upgrade  db_verify


%package docs
Summary: Complete documentation package for Berkeley DB
Group: Documentation
Obsoletes: db-docs < %{version}-%{release}, db45-docs

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
		--sysconfdir='%{_sysconfdir}' \
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
	pushd build_unix
	%{__make} install DESTDIR='%{buildroot}'

	# We do at least need to have write access for the installation.
	%{__chmod} 0755 '%{buildroot}/%{_bindir}'/*

	# Move stupidly placed docs
	%{__rm} -rf '%{buildroot}/%{_prefix}/docs'

	popd


%post
	%{__ldconfig}


%post cxx
	%{__ldconfig}


%post java
	%{__ldconfig}


%postun
	%{__ldconfig}


%postun cxx
	%{__ldconfig}


%postun java
	%{__ldconfig}


%files
	%defattr(-, root, root)
	%doc README LICENSE
	%{_libdir}/libdb.so
	%{_libdir}/libdb.a
	%{_libdir}/libdb-4*.*

%files -n db-devel
	%defattr(-, root, root)
	%doc README LICENSE
	%{_includedir}/db.h
	%{_includedir}/db_185.h

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

%files -n db-utils
	%defattr(-, root, root)
	%doc README LICENSE
	%attr(0555, root, root) %{_bindir}/db_*

%files docs
	%defattr(-, root, root)
	%doc docs/
