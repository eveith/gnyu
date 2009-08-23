Name: kdelibs4-experimental
Version: 4.3.0
Release: 1ev
Summary: Experimental KDE modules intended for internal use only
URL: http://www.kde.org/
Group: User Interface/Desktops
License: GPL-2, LGPL-2.1
Vendor: GNyU-Linux
Source: ftp://ftp.kde.org/pub/kde/stable/4.3.0/src/kdelibs-experimental-%{version}.tar.bz2
BuildRequires: cmake >= 2.4.5, pkg-config >= 0.9.0, make, gcc-g++
BuildRequires: kdelibs4 = %{version}

%description
This package contains KDE modules which are used internally by the KDE
project. They are not intended to be part of any external project since they
are still considered to be experimental.


%prep
	%setup -q -n 'kdelibs-experimental-%{version}'


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
	%doc COPYING*
	%dir %{_includedir}/knotificationitem-1
	%{_includedir}/knotificationitem-1/knotificationitem*.h
	%{_libdir}/libknotificationitem-1.*
	%{_datadir}/dbus-1/interfaces/org.kde.NotificationItem*.xml
