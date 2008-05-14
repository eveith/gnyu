Name: mysql
Version: 5.0.51a
Release: 2ev
Summary: A fast SQL database system: Programs and shared libraries
URL: http://www.mysql.com/
Group: Applications/Databases
License: GPL-2 (with exceptions)
Vendor: GNyU-Linux
Source0: http://www.mysql.com/Downloads/MySQL-5.0/mysql-%{version}.tar.gz
Source1: %{name}-my.cnf
Source2: %{name}-mysqld.ii
Source3: %{name}-filter-requires.sh
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, gcc-g++, ncurses, openssl, zlib, ncurses, gawk
BuildRequires: libtool, autoconf, automake-110, perl, readline, procps
BuildRequires: perl(Socket), libstdc++
Requires: %{name}-libs = %{version}
%define _mysqld_uid 502
%define _mysqld_gid 52
%define __perl_requires %{SOURCE3}

%description
The MySQL(TM) software delivers a very fast, multi-threaded, multi-user,
and robust SQL (Structured Query Language) database server. MySQL Server
is intended for mission-critical, heavy-load production systems as well
as for embedding into mass-deployed software. MySQL is a trademark of
MySQL AB.
The MySQL web site (http://www.mysql.com/) provides the latest
news and information about the MySQL software. Also please see the
documentation and the manual for more information.
This package contains the standard MySQL client programs and generic MySQL
files.


%package libs
Summary: MySQL shared client libraries
Group: Applications/Databases

%description libs
The mysql-libs package provides the essential shared libraries for any
MySQL client program or interface. You will need to install this package
to use any other MySQL package or any clients that need to connect to a
MySQL server.


%package server
Summary: The MySQL server
Group: Applications/Databases
Requires: %{name}-libs = %{version}, %{name} = %{version}

%description server
MySQL is a multi-user, multi-threaded SQL database server. MySQL is a
client/server implementation consisting of a server daemon (mysqld)
and many different client programs and libraries. This package contains
the MySQL server and some accompanying files and directories.


%package test
Summary: Test suite for the MySQL server
Group: Applications/Databases
Requires: %{name}-libs = %{version}, %{name} = %{version}
Requires: %{name}-server = %{version}

%description test
MySQL is a multi-user, multi-threaded SQL database server. This
package contains the regression test suite distributed with
the MySQL sources.



%prep
%setup -q


%build
CFLAGS='%{optflags} -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE'
CFLAGS="${CFLAGS} -fno-strict-aliasing -fwrapv"
CXXFLAGS="${CFLAGS} -fno-rtti -fno-exceptions"
export CFLAGS CXXFLAGS

%configure \
	--with-charset=utf8 \
	--with-extra-charsets=all \
	--with-mysqld-user=mysqld \
	--with-mysqld-group=mysqld \
	--enable-assembler \
	--enable-thread-safe-client \
	--with-unix-socket-path=/var/lib/mysql/mysql.sock \
	--with-mysqld-user=mysqld \
	--with-archive-storage-engine \
	--with-innodb \
	--without-bench \
	--with-csv-storage-engine \
	--with-archive-storage-engine \
	--with-federated-storage-engine \
	--with-openssl \
	--with-readline \
	--enable-largefile \
	--without-debug \
	--enable-shared
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'

%{__mv} %{buildroot}/%{_prefix}/mysql-test %{buildroot}/%{_datadir}

%{__mkdir_p} %{buildroot}/%{_localstatedir}/{log,run/mysqld,lib/mysql}
touch %{buildroot}/%{_localstatedir}/log/mysqld.log

%{__mkdir_p} %{buildroot}/%{_sysconfdir}
%{__cat} < %{SOURCE1} | %{__sed} \
	-e 's|@localstatedir@|%{_localstatedir}|g' \
	> %{buildroot}/%{_sysconfdir}/my.cnf

%{__mkdir_p} %{buildroot}/etc/initng/daemon
%{__cat} < %{SOURCE2} | %{__sed} \
	-e 's|@localstatedir@|%{_localstatedir}|g' \
	-e 's|@my_print_defaults@|%{_bindir}/my_print_defaults|g' \
	-e 's|@touch@|/bin/touch|g' \
	-e 's|@kill@|/bin/kill|g' \
	-e 's|@rm@|%{__rm}|g' \
	-e 's|@chown@|%{__chown}|g' \
	-e 's|@chmod@|%{__chmod}|g' \
	-e 's|@mysql_install_db@|%{_bindir}/mysql_install_db|g' \
	-e 's|@mysqld_safe@|%{_bindir}/mysqld_safe|g' \
	> %{buildroot}/etc/initng/daemon/mysqld.i

%{__mkdir_p} %{buildroot}/etc/ld.so.conf.d
echo '%{_libdir}/mysql' > %{buildroot}/etc/ld.so.conf.d/%{name}-%{_arch}

%{__rm} -f \
	%{buildroot}/%{_bindir}/{comp_err,mysql_client_test} \
	%{buildroot}/%{_mandir}/man1/{comp_err,make_win_{bin,src}_dist}*.1* \
	%{buildroot}/%{_datadir}/mysql/binary-configure \
	%{buildroot}/%{_datadir}/mysql/mi_test_all* \
	%{buildroot}/%{_datadir}/mysql/mysql-log-rotate \
	%{buildroot}/%{_datadir}/mysql/mysql*.server \
	%{buildroot}/%{_datadir}/mysql/ndb-config-2-node.ini

[ -e "${RPM_BuiLD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%post libs
/sbin/ldconfig

%postun libs
/sbin/ldconfig

%pre server
if [[ $1 -eq 1 ]]
then
	groupadd -g %{_mysqld_gid} mysql
	useradd \
		-u %{_mysqld_uid} \
		-g %{_mysqld_gid} \
		-c 'MySQL database' \
		-d %{_localstatedir}/lib/mysql \
		-s /sbin/nologin \
		mysqld
fi > /dev/null 2>&1
exit 0

%post server
ngc -r daemon/mysqld > /dev/null 2>&1
exit 0

%preun server
if [[ $1 -eq 0 ]]
then
	ngc -d daemon/mysqld
	ng-update delete daemon/mysqld
fi > /dev/null 2>&1

%postun server
if [[ $1 -eq 0 ]]
then
	userdel mysqld
	groupdel mysql
fi > /dev/null 2>&1
exit 0


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc README COPYING EXCEPTIONS-CLIENT
%{_bindir}/msql2mysql
%{_bindir}/mysql
%{_bindir}/mysql_config
%{_bindir}/mysql_find_rows
%{_bindir}/mysql_tableinfo
%{_bindir}/mysql_waitpid
%{_bindir}/mysqlaccess
%{_bindir}/mysqladmin
%{_bindir}/mysqlbinlog
%{_bindir}/mysqlcheck
%{_bindir}/mysqldump
%{_bindir}/mysqlimport
%{_bindir}/mysqlshow
%{_bindir}/my_print_defaults
%{_infodir}/*.info*
%{_mandir}/man1/mysql.1*
%{_mandir}/man1/mysql_config.1*
%{_mandir}/man1/mysql_find_rows.1*
%{_mandir}/man1/mysql_tableinfo.1*
%{_mandir}/man1/mysql_waitpid.1*
%{_mandir}/man1/mysqlaccess.1*
%{_mandir}/man1/mysqladmin.1*
%{_mandir}/man1/mysqldump.1*
%{_mandir}/man1/mysqlshow.1*
%{_mandir}/man1/my_print_defaults.1*


%files libs
%defattr(-, root, root)
/etc/ld.so.conf.d/%{name}-%{_arch}
%config(noreplace) %{_sysconfdir}/my.cnf
%dir %{_libdir}/mysql
%{_libdir}/mysql/libmysqlclient*.so*
%{_libdir}/mysql/libmysqlclient*.la*
%{_libdir}/mysql/*.a
%dir %{_datadir}/mysql
%{_datadir}/mysql/english
%lang(cs) %{_datadir}/mysql/czech
%lang(da) %{_datadir}/mysql/danish
%lang(nl) %{_datadir}/mysql/dutch
%lang(et) %{_datadir}/mysql/estonian
%lang(fr) %{_datadir}/mysql/french
%lang(de) %{_datadir}/mysql/german
%lang(el) %{_datadir}/mysql/greek
%lang(hu) %{_datadir}/mysql/hungarian
%lang(it) %{_datadir}/mysql/italian
%lang(ja) %{_datadir}/mysql/japanese
%lang(ko) %{_datadir}/mysql/korean
%lang(no) %{_datadir}/mysql/norwegian
%lang(no) %{_datadir}/mysql/norwegian-ny
%lang(pl) %{_datadir}/mysql/polish
%lang(pt) %{_datadir}/mysql/portuguese
%lang(ro) %{_datadir}/mysql/romanian
%lang(ru) %{_datadir}/mysql/russian
%lang(sr) %{_datadir}/mysql/serbian
%lang(sk) %{_datadir}/mysql/slovak
%lang(es) %{_datadir}/mysql/spanish
%lang(sv) %{_datadir}/mysql/swedish
%lang(uk) %{_datadir}/mysql/ukrainian
%{_datadir}/mysql/charsets
%{_includedir}/mysql/


%files server
%defattr(-, root, root)
%doc support-files/*.cnf
/etc/initng/daemon/mysqld.i
%{_bindir}/myisamchk
%{_bindir}/myisam_ftdump
%{_bindir}/myisamlog
%{_bindir}/myisampack
%{_bindir}/mysql_convert_table_format
%{_bindir}/mysql_explain_log
%{_bindir}/mysql_fix_extensions
%{_bindir}/mysql_fix_privilege_tables
%{_bindir}/mysql_install_db
%{_bindir}/mysql_secure_installation
%{_bindir}/mysql_setpermission
%{_bindir}/mysql_tzinfo_to_sql
%{_bindir}/mysql_upgrade
%{_bindir}/mysql_upgrade_shell
%{_bindir}/mysql_zap
%{_bindir}/mysqlbug
%{_bindir}/mysqldumpslow
%{_bindir}/mysqld_multi
%{_bindir}/mysqld_safe
%{_bindir}/mysqlhotcopy
%{_bindir}/mysqltestmanager
%{_bindir}/mysqltestmanager-pwgen
%{_bindir}/mysqltestmanagerc
%{_bindir}/mysqltest
%{_bindir}/innochecksum
%{_bindir}/perror
%{_bindir}/replace
%{_bindir}/resolve_stack_dump
%{_bindir}/resolveip
%{_libexecdir}/mysqld
%{_libexecdir}/mysqlmanager
%{_mandir}/man1/msql2mysql.1*
%{_mandir}/man1/myisamchk.1*
%{_mandir}/man1/myisamlog.1*
%{_mandir}/man1/myisampack.1*
%{_mandir}/man1/mysql_convert_table_format.1*
%{_mandir}/man1/myisam_ftdump.1*
%{_mandir}/man1/mysql.server.1*
%{_mandir}/man1/mysql_explain_log.1*
%{_mandir}/man1/mysql_fix_extensions.1*
%{_mandir}/man1/mysql_fix_privilege_tables.1*
%{_mandir}/man1/mysql_install_db.1*
%{_mandir}/man1/mysql_secure_installation.1*
%{_mandir}/man1/mysql_upgrade.1*
%{_mandir}/man1/mysql_zap.1*
%{_mandir}/man1/mysqlbinlog.1*
%{_mandir}/man1/mysqlcheck.1*
%{_mandir}/man1/mysqld_multi.1*
%{_mandir}/man1/mysqld_safe.1*
%{_mandir}/man1/mysqlhotcopy.1*
%{_mandir}/man1/mysqlimport.1*
%{_mandir}/man1/mysqlman.1*
%{_mandir}/man1/mysql_setpermission.1*
%{_mandir}/man1/mysqltest.1*
%{_mandir}/man1/innochecksum.1*
%{_mandir}/man1/perror.1*
%{_mandir}/man1/replace.1*
%{_mandir}/man1/resolve_stack_dump.1*
%{_mandir}/man1/resolveip.1*
%{_mandir}/man1/safe_mysqld.1*
%{_mandir}/man1/mysql_tzinfo_to_sql.1*
%{_mandir}/man1/mysqlmanager-pwgen.1*
%{_mandir}/man1/mysqlmanagerc.1*
%{_mandir}/man8/mysqld.8*
%{_mandir}/man8/mysqlmanager.8*
%{_datadir}/mysql/errmsg.txt
%{_datadir}/mysql/fill_help_tables.sql
%{_datadir}/mysql/mysql_fix_privilege_tables.sql
%{_datadir}/mysql/mysql_system_tables.sql
%{_datadir}/mysql/mysql_system_tables_data.sql
%{_datadir}/mysql/mysql_test_data_timezone.sql
%{_datadir}/mysql/my-*.cnf
%attr(0755, mysqld, mysql) %dir %{_localstatedir}/run/mysqld
%attr(0755, mysqld, mysql) %dir %{_localstatedir}/lib/mysql
%attr(0640, mysqld, mysql) %config(noreplace) %verify(not md5 size mtime) %{_localstatedir}/log/mysqld.log

%files test
%defattr(-, root, root)
%{_datadir}/mysql-test/
%{_mandir}/man1/mysql_client_test.1*
%{_mandir}/man1/mysql-*test*.pl.1*
