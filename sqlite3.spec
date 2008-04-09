Name: sqlite
Version: 3.5.7
Release: 1ev
Summary: A self-contained, embeddable SQL database
URL: http://www.sqlite.org/
Group: Applications/Databases
License: Public Domain
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: http://www.sqlite.org/sqlite-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: gcc, make >= 3.79.1, pkg-config, readline

%description
SQLite is a small, fast, embeddable SQL database engine that supports most of
SQL92, including transactions with atomic commit and rollback, subqueries,
compound queries, triggers, and views. A complete database is stored in a
single cross-platform disk file. The native C/C++ API is simple and easy to
use. Bindings for other languages are also available.


%prep
%setup -q


%build
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
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc README VERSION doc/
%{_bindir}/sqlite3
%{_includedir}/sqlite3.h
%{_includedir}/sqlite3ext.h
%{_libdir}/libsqlite3.*
%{_libdir}/pkgconfig/sqlite3.pc
