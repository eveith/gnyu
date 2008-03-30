Name: foomatic-filters
Version: 3.0
%define reldate 20071023
Release: 1ev
Summary: Universal print filter to convert PS data into the printer's format
URL: http://www.linux-foundation.org/en/OpenPrinting/Database/Foomatic
Group: System Environment/Base
License: GPL-2
Vendor: MSP Slackware
Source: http://www.openprinting.org/download/foomatic/%{name}-%{version}-%{reldate}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch
BuildRequires: make
Requires: cups, perl

%description
Filter scripts used by the printer spoolers to convert the incoming
PostScript data into the printer's native format using a
printer/driver specific, but spooler-independent PPD file.


%prep
%setup -q -n %{name}-%{version}-%{reldate}


%build
%configure
make

%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"

# Sorry, we don't support ppr. (http://ppr.sf.net/)
rm -rf "${RPM_BUILD_ROOT}/%{_libdir}/ppr"


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc COPYING README TODO ChangeLog USAGE
%dir /etc/foomatic
%config(noreplace) /etc/foomatic/filter.conf
/etc/foomatic/filter.conf.sample
%{_bindir}/foomatic-rip
%{_bindir}/foomatic-gswrapper
%{_libdir}/cups/backend/beh
%{_libdir}/cups/filter/foomatic-rip
%{_mandir}/man1/foomatic-*.1*
