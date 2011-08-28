Name: zypper
Version: 1.6.14
Release: 1.0
Summary: Command-line software manager
URL: http://en.opensuse.org/Zypper
Group: Package Management
License: GPL-2.0
Source: %{name}-%{version}.tar.xz
Patch0: cmake.patch
Patch1: rpm5-flag.patch
BuildRequires: cmake >= 2.4.6, make, grep, sed
BuildRequires: gcc-g++
BuildRequires: libstdc++-devel, rpm-devel >= 5.4.0
BuildRequires: boost-devel >= 1.33.1, readline-devel >= 5.1
BuildRequires: libzypp-devel >= 9.8.0, augeas-devel >= 0.5.0
BuildRequires: gettext-tools >= 0.17.0
Requires: procps, satsolver >= 0.17.0


%description
Zypper is a command line tool for managing software. It can be used to add
package repositories, search for packages, install, remove, or update packages,
install patches, hardware drivers, verify dependencies, and more.


%files -f zypper.lang
%defattr(-, root, root)
%doc COPYING HACKING
%{_sysconfdir}/bash_completion.d/zypper.sh

%{_sysconfdir}/logrotate.d/zypp-refresh.lr
%{_sysconfdir}/logrotate.d/zypper.lr

%dir %{_sysconfdir}/zypp
%config(noreplace) %{_sysconfdir}/zypp/zypper.conf

%{_bindir}/installation_sources
%{_bindir}/zypper

%{_sbindir}/zypp-refresh
%verify(not mode) %attr (755, root, root) %{_sbindir}/zypp-refresh-wrapper

%doc %{_mandir}/man8/zypper.8*

%dir %{_datadir}/zypper
%{_datadir}/zypper/zypper.aug
%dir %{_datadir}/zypper/xml
%{_datadir}/zypper/xml/xmlout.rnc

%ghost %config(noreplace) %{_localstatedir}/log/zypper.log


%package log
Summary: Zypper log file access CLI
Group: Package Management
License: GPL-2.0
Requires: python >= 2.6, python-argparse
Requires: %{name} = %{version}-%{release}


%description log
A helper utility for accessing Zypper's log files.


%files log
%defattr(-, root, root)
%doc COPYING HACKING
%{_sbindir}/zypper-log
%doc %{_mandir}/man8/zypper-log.8*


%prep
%setup -q
%patch0 -p1
%patch1 -p1


%build
%{__mkdir} build
pushd 'build'
%cmake \
    -DCMAKE_EXE_LINKER_FLAGS:STRING='-ltermcap' \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    ..
%{__make} %{?_smp_mflags}
%{__make} -C po %{?_smp_mflags} translations
popd


%install
pushd 'build'
%{__make} install DESTDIR='%{buildroot}'
popd

%find_lang zypper

%{__rm_rf} '%{buildroot}%{_datadir}/doc'

%{__install} -d -m755 '%{buildroot}%{_localstatedir}/log'
%{__touch} '%{buildroot}%{_localstatedir}/log/zypper.log'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'
