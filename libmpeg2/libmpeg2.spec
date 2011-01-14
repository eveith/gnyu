Name: libmpeg2
Version: 0.5.1
Release: 1ev
Summary: A library for decoding MPEG-2 and MPEG-1 video streams
URL: http://libmpeg2.sourceforge.net
Group: System Environment/Libraries
License: GPL-2
Vendor: GNyU-Linux
Source: http://libmpeg2.sourceforge.net/files/%{name}-%{version}.tar.gz
BuildRequires: make, gcc, libsdl, libX11, libXext, libXv

%description
libmpeg2 is a library for decoding MPEG-1 and MPEG-2 video streams.


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
	%doc AUTHORS ChangeLog CodingStyle README COPYING NEWS TODO
	%{_bindir}/corrupt_mpeg2
	%{_bindir}/extract_mpeg2
	%{_bindir}/mpeg2dec
	%dir %{_includedir}/mpeg2dec
	%{_includedir}/mpeg2dec/*.h
	%{_libdir}/libmpeg2.*
	%{_libdir}/libmpeg2convert.*
	%{_libdir}/pkgconfig/libmpeg2.pc
	%{_libdir}/pkgconfig/libmpeg2convert.pc
	%doc %{_mandir}/man1/extract_mpeg2.1*
	%doc %{_mandir}/man1/mpeg2dec.1*
