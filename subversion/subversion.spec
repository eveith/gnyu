Name: subversion
Version: 1.5.1
Release: 3ev
Summary: A revision control system similar to CVS
URL: http://subversion.tigris.org/
Group: Development/Tools
License: Apache
Vendor: GNyU-Linux
Source0: http://subversion.tigris.org/downloads/subversion-%{version}.tar.bz2
Source1: %{name}-svnserve.i
Source2: %{name}-svnserve.conf.d
Buildroot: %{_tmppath}/%{name}-root
BuildRequires(build,install): make, gettext
BuildRequires(build): gcc, gcc-g++, db >= 4.2, neon >= 0.24.0, zlib, apr >= 1.1, sun-jdk
BuildRequires(build): cyrus-sasl
Requires: %{name}-libs = %{version}-%{release}
%define _svnserve_uid 506
%define _svnserve_gid 99

%description
The goal of the Subversion project is to build a version control system that
is a compelling replacement for CVS in the open source community.


%package libs
Summary: Common librarires shared between SVN applications
Group: System Environment/Libraries

%description libs
Programs using the subversion API will need to link against these common
libraries. 


%package server
Summary: The subversion service
Group: System Environment/Daemons
Requires: ucspi-tcp, %{name}-libs = %{version}-%{release}

%description server
If you want to serve subversion repositories to your developers, you must
install the subversion-server package. 


%package java
Summary: Java bindings for SVN
Group: System Environment/Libraries
Requires: java-jdk, %{name}-libs = %{version}-%{release}

%description java
Native java bindings for Subversion. Allows Java programs like the popular
Eclipse IDE to use SVN.


%prep
%setup -q


%build
%configure \
	--disable-mod-activation \
	--enable-javahl
%{__make} %{?_smp_mflags}


%install
[[ "%{buildroot}" != '/' ]] && %{__rm} -rf "%{buildroot}"
%{__make_install} install-javahl DESTDIR='%{buildroot}'
%find_lang subversion


# Change into install directory to perform some setup
pushd '%{buildroot}'

# SVN service file
%{__mkdir_p} srv/svn ./%{_sysconfdir}/initng/{daemon,iconfig}
%{__cat} < %{SOURCE1} | %{__sed} \
	-e 's,@_SVNSERVE_UID@,%{_svnserve_uid},g' \
	-e 's,@_SVNSERVE_GID@,%{_svnserve_gid},g' \
	-e 's,@svnserve@,%{_bindir}/svnserve,g' \
	> ./%{_sysconfdir}/initng/daemon/svnserve.i
%{__cat} < %{SOURCE2} > etc/initng/iconfig/svnserve

%{__mkdir_p} ./%{_sysconfdir}/profile.d
%{__cat} <<__EOF__> ./%{_sysconfdir}/profile.d/svn-javahl.sh
#!/bin/bash
if [[ -z "\${CLASSPATH}" ]]
then
	export CLASSPATH='%{_libdir}/svn-javahl/svn-javahl.jar'
else
	export CLASSPATH="\${CLASSPATH}:%{_libdir}/svn-javahl/svn-javahl.jar"
fi
__EOF__

popd


%post libs
/sbin/ldconfig

%postun libs
/sbin/ldconfig

%pre server
if [[ "${1}" -eq 1 ]] 
then
	userdel 'svnserve' > /dev/null 2>&1
	useradd \
		-u '%{_svnserve_uid}' \
		-g '%{_svnserve_gid }' \
		-d /srv/svn \
		-s /sbin/nologin \
		svnserve > /dev/null
fi > /dev/null 2>&1
exit 0

%preun server
[[ "${1}" -eq 0 ]] && /sbin/ngc -d daemon/svnserve >/dev/null 2>&1 || :

%postun server
if [[ "${1}" -eq 0 ]]
then
	ng-update del daemon/svnserve default
	userdel svnserve
fi > /dev/null 2>&1
exit 0


%clean
[[ "%{buildroot}" != '/' ]] && %{__rm} -rf "%{buildroot}"


%files
%defattr(-, root, root)
%doc BUGS CHANGES COMMITTERS COPYING HACKING README TRANSLATING
%{_bindir}/svn
%{_bindir}/svnlook
%{_bindir}/svnsync
%{_bindir}/svnversion
%{_bindir}/svndumpfilter
%doc %{_mandir}/man1/svn.1*
%doc %{_mandir}/man1/svndumpfilter.1*
%doc %{_mandir}/man1/svnlook.1*
%doc %{_mandir}/man1/svnsync.1*
%doc %{_mandir}/man1/svnversion.1*

%files libs -f subversion.lang
%defattr(-, root, root)
%{_includedir}/subversion-1/
%{_libdir}/libsvn_*.*

%files java
%defattr(-, root, root)
%dir %{_libdir}/svn-javahl
%dir %{_libdir}/svn-javahl/include
%{_libdir}/svn-javahl/svn-javahl.jar
%{_libdir}/libsvnjavahl-1.*
%attr(0755, root, root) %{_sysconfdir}/profile.d/svn-javahl.sh

%files server
%defattr(-, root, root)
%attr(0600, root, root) %config(noreplace) %{_sysconfdir}/initng/iconfig/svnserve
%{_sysconfdir}/initng/daemon/svnserve.i
%doc %{_mandir}/man8/svnserve.8*
%doc %{_mandir}/man5/svnserve.conf.5*
%doc %{_mandir}/man1/svnadmin.1*
%{_bindir}/svnadmin
%{_bindir}/svnserve
%dir %attr(0775, svnserve, root) /srv/svn
