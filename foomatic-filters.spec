Name: foomatic-filters
Version: 3.0
%define reldate 20080511
Release: 2ev
Summary: Universal print filter to convert PS data into the printer's format
URL: http://www.linux-foundation.org/en/OpenPrinting/Database/Foomatic
Group: System Environment/Base
License: GPL-2
Vendor: GNyU-Linux
Source: http://www.openprinting.org/download/foomatic/%{name}-%{version}-%{reldate}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch
BuildRequires: coreutils, grep, sed, make, cups
Requires: cups, perl

%description
Filter scripts used by the printer spoolers to convert the incoming
PostScript data into the printer's native format using a
printer/driver specific, but spooler-independent PPD file.


%prep
%setup -q -n %{name}-%{version}-%{reldate}


%build
%configure
%{__make}

%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'

# Sorry, we don't support ppr. (http://ppr.sf.net/)
%{__rm} -rf '%{buildroot}/%{_libdir}/ppr'


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc COPYING README TODO ChangeLog USAGE
%dir %{_sysconfdir}/foomatic
%config(noreplace) %{_sysconfdir}/foomatic/filter.conf
%{_sysconfdir}/foomatic/filter.conf.sample
%{_bindir}/foomatic-rip
%{_bindir}/foomatic-gswrapper
%{_libdir}/cups/backend/beh
%{_libdir}/cups/filter/foomatic-rip
%{_mandir}/man1/foomatic-*.1*
