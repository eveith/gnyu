Name: libdvdcss
Version: 1.2.10
Release: 1ev
Summary: A library to read and playback CSS-encrypted DVDs (most cinema DVDs)
URL: http://www.videolan.org/developers/libdvdcss.html
Group: System Environment/Libraries
License: GPL-2
Vendor: GNyU-Linux
Source: http://download.videolan.org/pub/%{name}/%{version}/%{name}-%{version}.tar.bz2
BuildRequires: make, gcc, doxygen

%description
libdvdcss is a free software library for accessing and unscrambling DVDs
encrypted with the Content Scramble System (CSS). libdvdcss is part of the
VideoLAN project and is used by VLC media player and other DVD player software
such as Ogle, xine-based players and MPlayer.


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
	%doc AUTHORS ChangeLog COPYING NEWS README
	%dir %{_includedir}/dvdcss
	%{_includedir}/dvdcss/dvdcss.h
	%{_libdir}/libdvdcss.*
	%{_libdir}/pkgconfig/libdvdcss.pc
