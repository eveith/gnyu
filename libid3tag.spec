Name: libid3tag
Version: 0.15.1b
Release: 1ev
Summary: An ID3 tag manipulation library
URL: http://www.underbit.com/products/mad
Group: System Environment/Libraries
License: GPL-2
Vendor: GNyU-Linux
Source: ftp://ftp.mars.org/pub/mpeg/%{name}-%{version}.tar.gz
BuildRequires: make, gcc, zlib

%description
libid3tag is a library for reading and (eventually) writing ID3 tags, both
ID3v1 and the various versions of ID3v2.


%prep
	%setup -q


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
	%doc README COPYING COPYRIGHT TODO CHANGES
	%{_includedir}/id3tag.h
	%{_libdir}/libid3tag.*
