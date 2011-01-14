Name: openslp
Version: 1.2.1
Release: 1ev
Summary: An open-source implementation of the Service Location Protocol
URL: http://www.openslp.org/
Group: System Environment/Daemons
License: BSD
Vendor: GNyU-Linux
Source0: http://prdownloads.sourceforge.net/openslp/openslp-%{version}.tar.gz
Source1: %{name}-slpd.ii
BuildRequires: gcc, make, openssl
Requires: openssl
Provides: libtool(%{_libdir}/libslp.la)

%description
The OpenSLP project is an effort to develop an open-source implementation of
Service Location Protocol (RFC 2608) suitable for commercial and
non-commercial application. 
The Service Location Protocol (SLP, srvloc) is a service discovery protocol
that allows computers and other devices to find services in a local area
network without prior configuration. SLP has been designed to scale from
small, unmanaged networks to large enterprise networks. It has been defined in
RFC 2608 as Standards Track document.


%package -n libslp1
Summary: Client and server parts of the Service Location Protocol implementation
Group: System Environment/Libraries

%description -n libslp1
The Service Location Protocol (SLP, srvloc) is a service discovery protocol
that allows computers and other devices to find services in a local area
network without prior configuration. SLP has been designed to scale from
small, unmanaged networks to large enterprise networks. It has been defined in
RFC 2608 as Standards Track document.


%prep
%setup -q


%build
#libtoolize --force --copy
#autoheader
#aclocal
#automake --add-missing --copy
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR="${RPM_BUILD_ROOT}"

# Install service file
mkdir -p '%{buildroot}/%{_sysconfdir}/initng/daemon'
%{install_ifile '%{SOURCE1}' daemon/slpd.i}
	

%postun
if [[ "${1}" -eq 0 ]]
then
	ngc -d daemon/slpd
	ng-update remove slpd default
fi > /dev/null 2>&1


%post -n libslp1
%{__ldconfig}


%postun -n libslp1
%{__ldconfig}


%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog* FAQ NEWS README* THANKS doc/html doc/rfc
%config(noreplace) /etc/slp.*
%attr(0750, root, root) %{_sysconfdir}/initng/daemon/slpd.i
%{_bindir}/slptool
%{_sbindir}/slpd
%{_includedir}/slp.h


%files -n libslp1
%defattr(-, root, root)
%doc AUTHORS COPYING README NEWS FAQ
%{_libdir}/libslp*.*
