Name: foomatic-filters
Version: 4.0.1
Release: 3ev
Summary: Universal print filter to convert PS data into the printer's format
URL: http://www.linux-foundation.org/en/OpenPrinting/Database/Foomatic
Group: System Environment/Base
License: GPL-2
Vendor: GNyU-Linux
Source: http://www.openprinting.org/download/foomatic/%{name}-%{version}.tar.gz
BuildRequires: make, gcc, cups, enscript
Requires: cups

%description
Filter scripts used by the printer spoolers to convert the incoming
PostScript data into the printer's native format using a
printer/driver specific, but spooler-independent PPD file.


%prep
	%setup -q


%build
	%configure
	%{__make} %{?_smp_mflags}

%install
	%{__make} install DESTDIR='%{buildroot}'

	# Sorry, we don't support ppr. (http://ppr.sf.net/)
	%{__rm} -rf '%{buildroot}/%{_libdir}/ppr'


%files
	%defattr(-, root, root)
	%doc COPYING README TODO ChangeLog USAGE
	%dir %{_sysconfdir}/foomatic
	%config(noreplace) %{_sysconfdir}/foomatic/filter.conf
	%{_sysconfdir}/foomatic/filter.conf.sample
	%{_bindir}/foomatic-rip
	%{_libdir}/cups/backend/beh
	%{_libdir}/cups/filter/foomatic-rip
	%doc %{_mandir}/man1/foomatic-*.1*
