Name: lighttpd
Version: 1.4.18
Release: 1ev
Summary: A light httpd
URL: http://www.lighttpd.net/
Group: System Environment/Daemons
License: BSD
Vendor: MSP Slackware
Source0: http://www.lighttpd.net/download/lighttpd-%{version}.tar.bz2
Source1: %{name}-lighttpd.i
Source2: %{name}-lighttpd.conf
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, openssl, pcre, bzip2
%define _httpd_uid 500
%define _nogroup_gid 99

%description
lighttpd is a secure, fast, compliant, and very flexible Web server which has
been optimized for high-performance environments. It has a very low memory
footprint compared to other Web servers, and it takes care of CPU load. It has
an advanced feature set that includes FastCGI (load balanced), CGI, Auth,
Output-Compression, URL-Rewriting, SSL, and much more.


%prep
%setup -q


%build
%configure \
	--with-openssl \
	--with-pcre \
	--with-bzip2 \
	--without-fam \
	--with-webdav-props \
	--with-webdav-locks
%{__make} %{_smp_mflags}


%install
[[ -d '%{buildroot}' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'

# Install manual pages (why aren't they copied by make install?)
%{__mkdir_p} %{buildroot}/%{_mandir}/man1
%{__cp} doc/*.1 %{buildroot}/%{_mandir}/man1

pushd '%{buildroot}'

%{__mkdir_p} etc/initng/daemon var/log/lighttpd srv/htdocs/cgi-bin

# Install service file for InitNG
%{__cat} < %{SOURCE1} | sed 's,@lighttpd@,%{_sbindir}/lighttpd,' \
	> etc/initng/daemon/lighttpd.i

# Install our config file
cat < %{SOURCE2} > etc/lighttpd.conf

popd


%pre
useradd \
	-g %{_nogroup_gid} \
	-u %{_httpd_uid} \
	-c 'HTTP daemon user' \
	-d /srv/htdocs \
	-s /sbin/nologin \
	httpd > /dev/null 2>&1
exit 0

%preun
if [ $1 -eq 0 ]
then
	ngc -d daemon/lighttpd
	ng-update del lighttpd default
fi > /dev/null 2>&1
exit 0

%post
/sbin/ldconfig
ngc -r daemon/lighttpd > /dev/null 2>&1
exit 0

%postun
/sbin/ldconfig
if [ $1 -eq 0 ] 
then
	userdel httpd
fi > /dev/null 2>&1
exit 0



%clean
[[ -d '%{buildroot}' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc README doc/*.txt doc/*.conf doc/*.user
/etc/initng/daemon/lighttpd.i
%config(noreplace) /etc/lighttpd.conf
%dir /srv/htdocs
%dir /srv/htdocs/cgi-bin
%attr(775, httpd, root) /var/log/lighttpd
%{_sbindir}/lighttpd*
%{_bindir}/spawn-fcgi
%{_libdir}/mod_*.*
%{_mandir}/man1/*.1*
