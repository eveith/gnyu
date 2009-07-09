Name: openslp
Version: 1.2.1
Release: 1ev
Summary: An open-source implementation of the Service Location Protocol
URL: http://www.openslp.org/
Group: System Environment/Daemons
License: BSD
Vendor: MSP Slackware
Source0: http://prdownloads.sourceforge.net/openslp/openslp-%{version}.tar.gz
Source1: openslp.i
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: gcc-core, make, openssl
Requires: openssl
Provides: libtool(%{_libdir}/libslp.la)

%description
The OpenSLP project is an effort to develop an open-source implementation of
Service Location Protocol (RFC 2608) suitable for commercial and
non-commercial application. 


%prep
%setup -q


%build
libtoolize --force --copy
autoheader
aclocal
automake --add-missing --copy
%configure
make


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"

# Install service file

mkdir -p "$RPM_BUILD_ROOT"/etc/initng/daemon
cat %{SOURCE1} | sed 's,@slpd@,%{_sbindir}/slpd,' \
	> "$RPM_BUILD_ROOT"/etc/initng/daemon/slpd.i
	

[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
/sbin/ldconfig
if /sbin/ngc -s | grep -q slpd
then
	/sbin/ngc -r daemon/slpd > /dev/null 2>&1
fi

%postun
/sbin/ldconfig
if [ "$1" = 0 ] && /sbin/ngc -s | grep -q slpd
then
	/sbin/ngc -d daemon/slpd > /dev/null 2>&1
fi


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog* FAQ NEWS README* THANKS doc/html doc/rfc
%config(noreplace) /etc/slp.*
/etc/initng/daemon/slpd.i
%{_bindir}/slptool
%{_sbindir}/slpd
%{_libdir}/libslp*.*
%{_includedir}/slp.h
