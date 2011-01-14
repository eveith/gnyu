Name: liba52
Version: 0.7.4
Release: 1ev
Summary: An ATSC A/52 (AC-3) stream decoder
URL: http://liba52.sourceforge.net
Group: System Environmet/Libraries
License: GPL-2
Vendor: GNyU-Linux
Source: http://liba52.sourceforge.net/files/a52dec-%{version}.tar.gz
BuildRequires: make, gcc
Provides: a52dec = %{version}-%{release}

%description
liba52 is a free library for decoding ATSC A/52 streams, also known as AC-3.


%prep
	%setup -q -n 'a52dec-%{version}'


%build
	%configure
	%{__make} %{?_smp_mflags}


%install
	%{__make} install DESTDIR='%{buildroot}'

	[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
		&& %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
	%{__ldconfig}


%postun
	%{__ldconfig}


%files
	%defattr(-, root, root)
	%doc ChangeLog COPYING HISTORY NEWS README TODO
	%{_bindir}/a52dec
	%{_bindir}/extract_a52
	%dir %{_includedir}/a52dec
	%{_includedir}/a52dec/*.h
	%{_libdir}/liba52.*a
	%doc %{_mandir}/man1/a52dec.1*
	%doc %{_mandir}/man1/extract_a52.1*
