Name: foomatic-db
Version: 20090620
Release: 2ev
Summary: A huge printer-driver database in XML format
URL: http://www.linux-foundation.org/en/OpenPrinting/Database/Foomatic
Group: Applications/Publishing
License: GPL-2
Vendor: GNyU-Linux
Source: http://www.openprinting.org/download/foomatic/%{name}-current.tar.gz
BuildArch: noarch
BuildRequires: make, cups, gzip
Requires: cups

%description
The collected knowledge about printers, drivers, and driver options in
XML files, used by foomatic-db-engine to generate PPD files.


%prep
	%setup -q


%build
	%configure \
		--with-drivers=NOOBSOLETES
	%{__make} %{?_smp_mflags}


%install
	%{__make} install DESTDIR="$RPM_BUILD_ROOT"


%files
	%defattr(-, root, root)
	%doc COPYING README USAGE ChangeLog
	%{_datadir}/foomatic
	%{_datadir}/cups/model/foomatic-db-ppds
