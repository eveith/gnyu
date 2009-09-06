Name: polkit-qt
Version: 0.9.2
Release: 1ev
Summary: Qt support for PolicyKit
URL: http://www.kde.org
Group: System Environment/Libraries
License: LGPL-2.1
Vendor: GNyU-Linux
Source: %{name}-%{version}.tar.bz2
BuildRequires: cmake >= 2.6.2, pkgconfig >= 0.9.0, make, gcc-g++
BuildRequires: qt4 >= 4.5.0, policykit >= 0.8, automoc4 >= 0.9.88
BuildRequires: libX11, libXext, libICE, libSM

%description
Polkit-qt aims to make it easy for Qt developers to take advantage of
PolicyKit API. It is a convenience wrapper around QAction and QAbstractButton
that lets you integrate those two components easily with PolicyKit.


%prep
	# polkit-qt needs to be checked out from SVN; the tarball here is made
	# manually.
	%setup -q 


%build
	%{__mkdir} '_Build'
	pushd '_Build'
	%{cmake} ..
	%{__make} %{?_smp_mflags}
	popd


%install
	pushd '_Build'
	%{__make} install DESTDIR='%{buildroot}'
	popd

	[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
		&& %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
	%{__ldconfig}


%postun
	%{__ldconfig}


%files
	%defattr(-, root, root)
	%doc COPYING
	%dir %{_includedir}/PolicyKit/polkit-qt
	%{_includedir}/PolicyKit/polkit-qt/*
	%{_libdir}/libpolkit-qt-core.so*
	%{_libdir}/libpolkit-qt-gui.so*
	%{_libdir}/pkgconfig/polkit-qt.pc
	%{_libdir}/pkgconfig/polkit-qt-core.pc
	%{_libdir}/pkgconfig/polkit-qt-gui.pc
