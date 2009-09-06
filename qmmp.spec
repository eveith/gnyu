Name: qmmp
Version: 0.3.0
Release: 1ev
Summary: A WinAmp-like audio player based on Qt
URL: http://code.google.com/p/qmmp
Group: Applications/Multimedia
License: GPL-2
Vendor: GNyU-Linux
Source: http://qmmp.googlecode.com/files/qmmp-%{version}.tar.bz2
BuildRequires: cmake >= 2.4.8, pkg-config >= 0.9.0, make, gcc-g++
BuildRequires: qt4 >= 4.3
BuildRequires: alsa-lib >= 1.0.1, libogg, libvorbis, libmad >= 0.15.1b-3ev
BuildRequires: taglib >= 1.4, curl >= 7.16, libsndfile >= 1.0.17

%description


%prep
	%setup -q


%build
	%{cmake} .
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
	%doc README COPYING
	%{_bindir}/qmmp
	%dir %{_includedir}/qmmp
	%dir %{_includedir}/qmmpui
	%{_includedir}/qmmp*/*.h
	%{_libdir}/qmmp/
	%{_libdir}/libqmmp.so*
	%{_libdir}/libqmmpui.so*
	%{_datadir}/applications/qmmp*.desktop
	%{_datadir}/icons/hicolor/*/apps/qmmp.png
