Name: etc
Version: 1.0
Release: 1ev
Summary: Basic system configuration files
Group: System Environment/Base
License: various
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source0: http://www.sethwklein.net/projects/iana-etc/downloads/iana-etc-2.20.tar.bz2
BuildRequires: gawk, make >= 3.79.1
BuildArch: noarch

%description
The etc package populates your /etc directory with some very basic files that
are needed by the system to funtion correctly. Although they are configuration
files, they aren't changed, though.


%prep
%prep -qa0


%build
cd iana-etc*
%{__make}
cd -


%install
%{__mkdir_p} "${RPM_BUILD_ROOT}"

# IANA /etc files
pushd iana-etc*
%{__make_install} DESTDIR="${RPM_BUILD_ROOT}"

%{__mkdir_p} '%{buildroot}/etc'/cron.{hourly,daily,weekly}


%files
%defattr(-, root, root)
%config %attr(0644, root, root) /etc/protocols
%config %attr(0644, root, root) /etc/services
%dir /etc/cron.*
