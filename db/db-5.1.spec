Name: db
Version: 5.1.25
Release: 2.0
Summary: An embedded database for traditional and client/server applications
URL: http://www.oracle.com/database/berkeley-db/index.html
Group: Databases
License: BSD
Source: http://download.oracle.com/otn/berkeley-db/db-%{version}.tar.gz
BuildRequires: grep, sed, make gcc, gcc-g++
BuildRequires: gettext-tools
BuildRequires: libstdc++-devel
Requires: libdb5.1 = %{version}-%{release}


%description
Berkeley DB (libdb) is a programmatic toolkit that provides embedded database
support for both traditional and client/server applications.  It includes
b+tree, queue, extended linear hashing, fixed, and variable-length record
access methods, transactions, locking, logging, shared memory caching,
database recovery, and replication for highly available systems. DB supports
C, C++, Java, PHP, and Perl APIs, which can be installed from separate
packages. It is available for a wide variety of UNIX platforms as well as
Windows XP, Windows NT, and Windows '95 (MSVC 6 and 7).


%files
%defattr(-, root, root)
%doc README LICENSE


%package -n libdb5.1
Summary: Berkeley DB C library API
Group: Databases/Libraries


%description -n libdb5.1
Berkeley DB (libdb) is a programmatic toolkit that provides embedded database
support for both traditional and client/server applications.  It includes
b+tree, queue, extended linear hashing, fixed, and variable-length record
access methods, transactions, locking, logging, shared memory caching,
database recovery, and replication for highly available systems. DB supports
C, C++, Java, PHP, and Perl APIs, which can be installed from separate
packages. It is available for a wide variety of UNIX platforms as well as
Windows XP, Windows NT, and Windows '95 (MSVC 6 and 7).


%files -n libdb5.1
%defattr(-, root, root)
%doc README LICENSE
%{_libdir}/libdb-5*.so*
%{_libdir}/libdb_sql.so
%{_libdir}/libdb_sql-5*.so*


%post -n libdb5.1 -p %{__ldconfig}
%postun -n libdb5.1 -p %{__ldconfig}


%package devel
Summary: Development headers for Berekeley DB %{version}
Group: Databases/Development
Requires: db = %{version}-%{release}


%description devel
While the Berkeley DB libraries are strongly ABI-versioned and it is not
possible to use a newer minor number if a program has been compiled
against the older one without re-compiling it, the headers cannot be
installed in parallel.
This devel package contains all db headers for version %{version}. You
need to installed them if you want to link against this version of the db
libraries.


%files devel
%defattr(-, root, root)
%doc README LICENSE
%{_includedir}/db.h
%{_includedir}/db_185.h
%{_includedir}/db_cxx.h
%{_includedir}/dbsql.h
%{_includedir}/db51/*.h
%dir %{_includedir}/db51
%{_libdir}/libdb*.a
%{_libdir}/libdb*.la
%{_libdir}/libdb.so
%{_libdir}/libdb_cxx.so


%package -n libdb_cxx5.1
Summary: C++ API to Berkeley DB
Group: Databases/Libraries
Obsoletes: db-cxx < %{version}-%{release}
Conflicts: db-cxx < %{version}-%{release}


%description -n libdb_cxx5.1
While the "libdb" package only contains the C API, this package comes with 
C++ bindings for Berkeley DB. It is totally independend from the C 
API package.


%files -n libdb_cxx5.1
%defattr(-, root, root)
%doc README LICENSE
%{_libdir}/libdb_cxx-5*.so*


%post -n libdb_cxx5.1 -p %{__ldconfig}
%postun -n libdb_cxx5.1 -p %{__ldconfig}


%package utils
Summary: Command line utilities to manage berkeley databases
Group: Databases


%description utils
This package provides serveral helper utilities to manage Berkeley DB
databases, such as:
db_archive  db_checkpoint  db_deadlock  db_dump  db_hotbackup  db_load
db_printlog  db_recover  db_stat  db_upgrade  db_verify


%files utils
%defattr(-, root, root)
%doc README LICENSE
%{_bindir}/db_*
%{_bindir}/dbsql


%package docs
Summary: Complete documentation package for Berkeley DB
Group: Documentation


%description docs
Independently shipped from the APIs, this package provides the complete
developer's documentation, as well as upgrade guides and other howtos.


%files docs
%defattr(-, root, root)
%doc docs/*


%package sqlite3
Summary: A drop-in replacement for SQLite
Group: Databases


%description
Berkeley DB provides a drop-in replacement for the traditional SQLite 3. This
package contains the command-line frontend to SQLite 3 database files.


%files sqlite3
%defattr(-, root, root)
%doc README LICENSE
%{_bindir}/sqlite3


%package libsqlite3
Summary: SQLite3 shared library from Berkeley DB
Group: Databases/Libraries


%description libsqlite3
BerkeleyDB offers a drop-in replacement for SQLite 3. This package contains
the shared library libsqlite3.


%files libsqlite3
%defattr(-, root, root)
%doc README LICENSE
%{_libdir}/libsqlite3.so


%post libsqlite3 -p %{__ldconfig}
%postun libsqlite3 -p %{__ldconfig}


%package sqlite3-devel
Summary: Development files for Berkeley DB SQLite 3 replacement
Group: Databases/Development
Requires: db-sqlite3 = %{version}-%{release}


%description sqlite3-devel
BerkeleyDB offers a drop-in replacement for SQLite 3. This package contains
development files needed to compile applications using Berkeley DB's SQLite
replacement.


%files sqlite3-devel
%defattr(-, root, root)
%doc README LICENSE
%{_includedir}/sqlite3.h
%{_libdir}/libsqlite3.a
%{_libdir}/libsqlite3.la


%prep
%setup -q


%build
pushd build_unix
	
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS
FFLAGS="${FFLAGS:-%optflags}" ; export FFLAGS
../dist/configure \
	--host='%{_host}' \
	--build='%{_build}' \
	--target='%{_target_platform}' \
	--program-prefix='%{?_program_prefix}' \
	--prefix='%{_prefix}' \
	--exec-prefix='%{_exec_prefix}' \
	--bindir='%{_bindir}' \
	--sbindir='%{_sbindir}' \
	--sysconfdir='%{_sysconfdir}' \
	--datadir='%{_datadir}' \
	--includedir='%{_includedir}' \
	--libdir='%{_libdir}' \
	--libexecdir='%{_libexecdir}' \
	--localstatedir='%{_localstatedir}' \
	--sharedstatedir='%{_sharedstatedir}' \
	--mandir='%{_mandir}' \
	--infodir='%{_infodir}' \
	--enable-sql \
    --enable-sql_compat \
    --enable-sql_codegen \
	--enable-compat185 \
	--enable-cxx
%{__make} %{?_smp_mflags}
popd


%install
pushd build_unix
%{__make} install DESTDIR='%{buildroot}'

# We do at least need to have write access for the installation.
%{__chmod} 0755 '%{buildroot}%{_bindir}'/*

# Remove stupidly placed docs
%{__rm} -rf '%{buildroot}%{_prefix}/docs'

# Compatibility for different header path expectations
%{__mkdir_p} '%{buildroot}%{_includedir}/db51'
pushd '%{buildroot}%{_includedir}/db51'
for i in ../*.h; do
	%{__ln_s} "${i}" .
done
popd

popd
