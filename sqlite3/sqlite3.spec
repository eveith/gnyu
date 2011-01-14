Name: sqlite3
Version: 3.6.10
Release: 2ev
Summary: A self-contained, embeddable SQL database
URL: http://www.sqlite.org/
Group: Applications/Databases
License: Public Domain
Vendor: GNyU-Linux
Source: http://www.sqlite.org/sqlite-%{version}.tar.gz
BuildRequires: gcc, make >= 3.79.1, pkg-config, readline
Obsoletes: sqlite

%description
SQLite is a small, fast, embeddable SQL database engine that supports most of
SQL92, including transactions with atomic commit and rollback, subqueries,
compound queries, triggers, and views. A complete database is stored in a
single cross-platform disk file. The native C/C++ API is simple and easy to
use. Bindings for other languages are also available.


%prep
%setup -q -n 'sqlite-%{version}'


%build
export LDFLAGS=-ldl
%configure \
	--enable-threadsafe \
	--enable-cross-thread-connections \
	--enable-threads-override-locks \
	--disable-tcl \
	--enable-load-extension \
	--enable-tempstore=yes
%{__make} %{?_smp_mflags}
%{__make} doc


%install
%{__make} install DESTDIR='%{buildroot}'


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc README VERSION doc/
%{_bindir}/sqlite3
%{_includedir}/sqlite3.h
%{_includedir}/sqlite3ext.h
%{_libdir}/libsqlite3.*
%{_libdir}/pkgconfig/sqlite3.pc
