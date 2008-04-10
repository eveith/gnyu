Name: subversion
Version: 1.4.6
Release: 2ev
Summary: A revision control system similar to CVS
URL: http://subversion.tigris.org/
Group: Development/Tools
License: Apache
Vendor: GNyU-Linux
Source0: http://subversion.tigris.org/downloads/subversion-%{version}.tar.bz2
Source1: %{name}-svnserve.i
Source2: %{name}-svnserve.conf.d
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc, gcc-g++, db >= 4.2, neon, zlib, apr, sun-jdk
%define _svnserve_uid 506
%define _svnserve_gid 99

%description
The goal of the Subversion project is to build a version control system that
is a compelling replacement for CVS in the open source community.


%package server
Summary: The subversion service
Group: System Environment/Daemons
License: Apache
Requires: ucspi-tcp

%description server
If you want to serve subversion repositories to your developers, you must
install the subversion-server package. 


%prep
%setup -q


%build
%configure \
	--enable-dso \
	--enable-javahl \
	--with-ssl 
%{__make} %{?_smp_mflags}


%install
[[ "%{buildroot}" != '/' ]] && %{__rm} -rf "%{buildroot}"
%{__make_install} DESTDIR='%{buildroot}'
%{__rm} -f %{buildroot}/%{_infodir}/dir
%find_lang subversion


# Change into install directory to perform some setup
pushd "$RPM_BUILD_ROOT"

%{__mkdir_p} srv/svn etc/initng/{daemon,iconfig}

# Create service file
%{__cat} < %{SOURCE1} | %{__sed} \
	-e 's,@_SVNSERVE_UID@,%{_svnserve_uid},g' \
	-e 's,@_SVNSERVE_GID@,%{_svnserve_gid},g' \
	-e 's,@svnserve@,%{_bindir}/svnserve,g' \
	> etc/initng/daemon/svnserve.i
%{__cat} < %{SOURCE2} > etc/initng/iconfig/svnserve

popd


%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%pre server
useradd \
	-u %{_svnserve_uid} \
	-g %{_svnserve_gid } \
	-d /srv/svn \
	-s /sbin/nologin \
	svnserve > /dev/null 2>&1 || :

%post server
ngc -r daemon/svnserve > /dev/null 2>&1 ||:

%preun server
[[ $1 -eq 0 ]] && /sbin/ngc -d daemon/svnserve >/dev/null 2>&1 || :

%postun server
if [[ $1 -eq 0 ]]
then
	ng-update del daemon/svnserve
	userdel svnserve
fi > /dev/null 2>&1
exit 0


%clean
[[ "%{buildroot}" != '/' ]] && %{__rm} -rf "%{buildroot}"


%files -f subversion.lang
%defattr(-, root, root)
%doc BUGS CHANGES COMMITTERS COPYING HACKING README TRANSLATING
%{_libdir}/libsvn*.*
%{_includedir}/subversion*/
%{_bindir}/svn
%{_bindir}/svnlook
%{_bindir}/svnsync
%{_bindir}/svnversion
%{_bindir}/svndumpfilter
%{_mandir}/man1/svn.1*
%{_mandir}/man1/svndumpfilter.1*
%{_mandir}/man1/svnlook.1*
%{_mandir}/man1/svnsync.1*
%{_mandir}/man1/svnversion.1*

%files server
%attr(0600, root, root) %config(noreplace) /etc/initng/iconfig/svnserve
/etc/initng/daemon/svnserve.i
%{_mandir}/man8/svnserve.8*
%{_mandir}/man5/svnserve.conf.5*
%{_mandir}/man1/svnadmin.1*
%{_bindir}/svnadmin
%{_bindir}/svnserve
%dir %attr(0775, svnserve, root) /srv/svn
