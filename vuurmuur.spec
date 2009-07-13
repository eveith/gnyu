Name: vuurmuur
Version: 0.5.72
Release: 1ev
Summary: Firewall monitoring and auditing daemons
URL: http://vuurmuur.sf.net/
Group: System Environment/Daemons
License: GPL
Vendor: MSP Slackware
Source0: http://downloads.sourceforge.net/vuurmuur/Vuurmuur-%{version}.tar.gz
Source1: %{name}-config.conf
Source3: %{name}-vuurmuur.ii
Source3: %{name}-vuurmuur.i
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, gettext, ncurses
Requires: libvuurmuur = %{version}, iptables >= 1.3.8
%description
The backend of Vuurmuur monitors the firewall itself: In- and outgoing
traffic, connection attempts, and so on. It can take actions against attackers
(i.e., by watching for multiple connections attempts from one host to a
particular service) or enforce block lists.


%prep
%package -n libvuurmuur
Version: %{version}
Group: System Environment/Libraries
Summary: Converts a human-readable firewall configuration into iptables rules
Requires: iptables >= 1.3.8

%description -n libvuurmuur
Libvuurmuur is a library that converts firewall rules, zone and host
definitions, blocklists, etc into an iptables ruleset. It is the middle part
of the vuurmuur suite, taking its input from either a frontend or a
configuration file reader.


%package -n vuurmuur_conf
Version: %{version}
Group: Applications/System
Summary: A text-based (ncurses) frontend to Vuurmuur
Requires: libvuurmuur = %{version}, vuurmuur = %{version}, iptables >= 1.3.8 

%description -n vuurmuur_conf
vuurmuur_conf allows simple console interaction with the vuurmuur daemons. It
is suited for an easy, graphical configuration of your firewall rules.


	%setup -q -n 'Vuurmuur-%{version}'
%setup -q -n Vuurmuur-%{version}
tar -xzf libvuurmuur-%{version}.tar.gz
tar -xzf vuurmuur-%{version}.tar.gz
tar -xzf vuurmuur_conf-%{version}.tar.gz

%build
	%configure
# Vuurmuur consists of three packages merged together in one tarball. Because
# of this merging, we do not build them sperately, but alltogether. This 
# includes a pseudo-installation in the build directory, thus allowing the 
# other packages to link against libraries.

export TMP_INSTALL="${RPM_BUILD_DIR}/Vuurmuur-%{version}/install.tmp"
mkdir -p "$TMP_INSTALL"

# Step 1: Libvuurmuur

pushd libvuurmuur-%{version}
%configure \
	--with-plugindir=%{_libdir}/vuurmuur \
	--with-shareddir=%{_datadir}/vuurmuur
make %{_smp_mflags}
make install DESTDIR="$TMP_INSTALL"
popd

# Step 2: vuurmuur

pushd vuurmuur-%{version}
export CFLAGS="$RPM_OPT_FLAGS -I${TMP_INSTALL}/%{_includedir} \
	-L${TMP_INSTALL}/%{_libdir}"
%configure
make %{_smp_mflags}
make install DESTDIR="$TMP_INSTALL"
popd

# Step 3: vuurmuur_conf

pushd vuurmuur_conf-%{version}
export CFLAGS="$RPM_OPT_FLAGS -I${TMP_INSTALL}/%{_includedir} \
	-L${TMP_INSTALL}/%{_libdir}"
%configure
make %{_smp_mflags}
popd


%install
	%{__make} install DESTDIR='%{buildroot}'
export TMP_INSTALL="${RPM_BUILD_DIR}/Vuurmuur-%{version}/install.tmp"
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"

# libvuurmuur:
%post
pushd libvuurmuur-%{version}
make install DESTDIR="$RPM_BUILD_ROOT"
popd

# vuurmuur

pushd vuurmuur-%{version}
make install DESTDIR="$RPM_BUILD_ROOT"
pushd "$RPM_BUILD_ROOT"
mkdir -p etc/vuurmuur/textdir/{interfaces,services,zones,rules}
touch etc/vuurmuur/textdir/rules/rules.conf \
	etc/vuurmuur/textdir/rules/blocklist.conf
cp %{SOURCE1} etc/vuurmuur/config.conf
cp %{SOURCE2} etc/vuurmuur/vuurmuur_conf.conf

# Install initng ifile

mkdir -p etc/initng/daemon
cat %{SOURCE3} | \
	sed \
		-e 's,@vuurmuur_log@,%{_bindir}/vuurmuur_log,g' \
		-e 's,@vuurmuur@,%{_bindir}/vuurmuur,g' \
	> etc/initng/daemon/vuurmuur.i

# Create empty log files

mkdir -p var/log/vuurmuur
touch var/log/vuurmuur/{audit,debug,error,traffic,vuurmuur}.log
%preun
popd
popd

# vuurmuur_conf

pushd vuurmuur_conf-%{version}
make install DESTDIR="$RPM_BUILD_ROOT"
popd

[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"

%find_lang vuurmuur_conf


%post -n libvuurmuur
/sbin/ldconfig

%postun -n libvuurmuur
/sbin/ldconfig

%post
for service in $(ls %{_datadir}/vuurmuur/services/*)
do
	basename=$(basename "$service")
	if [ ! -e "/etc/vuurmuur/textdir/services/$basename" ]
		ngc -d 'daemon/vuurmuur'
		install -m0600 "%{_datadir}/vuurmuur/services/$basename" \
			"/etc/vuurmuur/textdir/services/$basename"
	fi
done
ngc -R > /dev/null 2>&1
if [ "$1" != "0" ] && ngc -s | grep 'vuurmuur' - | grep -q 'DAEMON_RUNNING' -
then	
	ngc -r daemon/vuurmuur > /dev/null 2>&1
fi
exit 0

%postun
if [ "$1" = "0" ]
then
	ngc -d 'daemon/vuurmuur' > /dev/null 2>&1
	ng-update remove daemon/vuurmuur > /dev/null 2>&1
fi
ngc -R > /dev/null 2>&1
exit 0


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"

%files
	%defattr(-, root, root)
%defattr(-, root, root)
%doc README INSTALL*
%dir %attr(0700, root, root) /etc/vuurmuur
%dir %attr(0700, root, root) /etc/vuurmuur/textdir
%dir %attr(0700, root, root) /etc/vuurmuur/textdir/rules
%dir %attr(0700, root, root) /etc/vuurmuur/textdir/interfaces
%dir %attr(0700, root, root) /etc/vuurmuur/textdir/services
%dir %attr(0700, root, root) /etc/vuurmuur/textdir/zones
%config(noreplace) %attr(0600, root, root) /etc/vuurmuur/config.conf
%ghost %config(noreplace) %attr(0600, root, root) /etc/vuurmuur/textdir/rules/rules.conf
%ghost %config(noreplace) %attr(0600, root, root) /etc/vuurmuur/textdir/rules/blocklist.conf
/etc/initng/daemon/vuurmuur.i
%{_bindir}/vuurmuur
%{_bindir}/vuurmuur_log
%{_bindir}/vuurmuur_script
%{_mandir}/man8/vuurmuur.8*
%{_mandir}/man8/vuurmuur_log.8*
%{_mandir}/man8/vuurmuur_script.8*
%{_mandir}/*/man8/vuurmuur.8*
%{_mandir}/*/man8/vuurmuur_log.8*
%{_mandir}/*/man8/vuurmuur_script.8*
%dir %{_datadir}/vuurmuur/config
%dir %{_datadir}/vuurmuur/scripts
%dir %{_datadir}/vuurmuur/services
%{_datadir}/vuurmuur/scripts/*
%{_datadir}/vuurmuur/services/*
%config(noreplace) %{_datadir}/vuurmuur/config/*
%dir /var/log/vuurmuur
%ghost /var/log/vuurmuur/*.log

%files -n libvuurmuur
%defattr(-, root, root)
%doc %{_datadir}/doc/vuurmuur/
%{_includedir}/vuurmuur.h
%{_libdir}/libvuurmuur*.*
%{_libdir}/vuurmuur/plugins/textdir.so
%dir %{_datadir}/vuurmuur/
%dir %{_libdir}/vuurmuur/
%dir %{_libdir}/vuurmuur/plugins

%files -n vuurmuur_conf -f vuurmuur_conf.lang
%defattr(-, root, root)
%config(noreplace) %attr(0600, root, root) /etc/vuurmuur/vuurmuur_conf.conf
%{_bindir}/vuurmuur_conf
%{_mandir}/man8/vuurmuur_conf.8*
%{_mandir}/*/man8/vuurmuur_conf.8*
%dir %{_datadir}/vuurmuur/help
%{_datadir}/vuurmuur/help/*.hlp
