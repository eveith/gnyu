Name: libvuurmuur0
Version: 0.7
Release: 3.0ev
Summary: Converts a human-readable firewall configuration into iptables rules
URL: http://www.vuurmuur.org/
Group: System Environment/Libraries
License: GPL-2
Vendor: GNyU-Linux
Source: ftp://ftp.vuurmuur.org/releases/0.7/Vuurmuur-%{version}.tar.gz
BuildRequires: make, gcc, libtool
Provides: libvuurmuur = %{version}
Conflicts: vuurmuur < 0.7

%description
Libvuurmuur is a library that converts human-readable firewall rules, zone and
host definitions, blocklists, etc from Vuurmuur into an iptables ruleset. It
is the middle part of the vuurmuur suite, taking its input from either a
frontend or a configuration file reader.


%package devel
Summary: Development headers for libvuurmuur0
Group: Development/Libraries
Requires: libvuurmuur0 = %{version}-%{release}
Provides: libvuurmuur-devel = %{version}-%{release}

%description
This package contains header files needed for developing or compiling
applications that use libvuurmuur.


%prep
%setup -q -n 'Vuurmuur-%{version}'
%{__gzip} -dc 'libvuurmuur-%{version}.tar.gz' | %{__tar} -x
%setup -D -T -n 'Vuurmuur-%{version}/libvuurmuur-%{version}'


%build
%configure \
	--with-plugindir='%{_libdir}/vuurmuur' \
	--with-shareddir='%{_datadir}/vuurmuur'
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%{__mkdir_p} '%{buildroot}/%{_datadir}/vuurmuur'

# We can take care of the documentation ourselves, thanks. :-)
%{__rm_rf} '%{buildroot}/%{_datadir}/doc'
[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
	&& %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
%{__ldconfig}


%postun
%{__ldconfig}


%clean
%{__rm_rf} '%{_builddir}/Vuurmuur-%{version}'


%files
%defattr(-, root, root)
%doc COPYING AUTHORS ChangeLog NEWS README TODO
%{_libdir}/libvuurmuur.so*
%dir %{_libdir}/vuurmuur
%dir %{_libdir}/vuurmuur/plugins
%{_libdir}/vuurmuur/plugins/libtextdir.*
%dir %{_datadir}/vuurmuur


%files devel
%defattr(-, root, root)
%{_includedir}/vuurmuur.h
%{_libdir}/libvuurmuur.a
%{_libdir}/libvuurmuur.la
