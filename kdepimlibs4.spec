Name: kdepimlibs4
Version: 4.2.4
Release: 4ev
Summary: Libraries common to all KDE 4 PIM applications
URL: http://www.kde.org/
Group: System Environment/Libraries
License: LGPL-2.1, GPL-2, BSD
Vendor: GNyU-Linux
Source: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdepimlibs-%{version}.tar.bz2
BuildRequires: cmake >= 2.4.5, make, gcc-g++, qt4 >= 4.2.0, automoc4 >= 0.8.86
BuildRequires: kdelibs4 = %{version}, phonon >= 4.3.0, boost >= 1.33.1
BuildRequires: cyrus-sasl, gpgme >= 1.1.8, akonadi >= 0.80, libical >= 0.33
BuildRequires: openldap-libs, pkg-config

%description
This module includes libraries that are central to the development and
execution of a KDE-PIM application.
The KDE-PIM project aims to bring together those who wish to help design,
implement, test, etc. anything that's to do with personal information
management.
This rather broad scope encompasses mail clients, addressbooks, usenet news,
scheduling and even sticky notes.



%prep
	%setup -q -n 'kdepimlibs-%{version}'
	

%build
	%{cmake} \
		-DQT_QMAKE_EXECUTABLE:FILEPATH='%{_libdir}/qt4/bin/qmake' \
		.
	%{__make} %{?_smp_mflags}


%install
	%{__make} install DESTDIR='%{buildroot}'


%post
	%{__ldconfig}


%postun
	%{__ldconfig}


%files
	%defattr(-, root, root)
	%doc README COPYING* HACKING DEBUG KDE4PORTING.html MAINTAINERS PLAN POLICIES
	%doc %{_datadir}/doc/HTML/en/*
	%{_libdir}/libgpgme++*.so*
	%{_libdir}/libqgpgme.so*
	%{_libdir}/libkmime.so*
	%{_libdir}/libakonadi-*.so*
	%{_libdir}/libkabc*.so*
	%{_libdir}/libkblog.so*
	%{_libdir}/libkcal.so*
	%{_libdir}/libkimap.so*
	%{_libdir}/libkldap.so*
	%{_libdir}/libkpimidentities.so*
	%{_libdir}/libkpimutils.so*
	%{_libdir}/libkresources.so*
	%{_libdir}/libktnef.so*
	%{_libdir}/libkxmlrpcclient.so*
	%{_libdir}/libmailtransport.so*
	%{_libdir}/libsyndication.so*
	%dir %{_libdir}/KdepimLibs-%{version}
	%dir %{_libdir}/KdepimLibs-%{version}/cmake
	%{_libdir}/KdepimLibs-%{version}/cmake/*.cmake
	%dir %{_libdir}/gpgmepp
	%{_libdir}/gpgmepp/*.cmake
	%{_libdir}/kde4/*.so
	%dir %{_datadir}/apps/akonadi-kde
	%{_datadir}/apps/akonadi-kde/kcfg2dbus.xsl
	%dir %{_datadir}/apps/kabc
	%{_datadir}/apps/kabc/countrytransl.map
	%dir %{_datadir}/apps/kabc/formats
	%{_datadir}/apps/kabc/formats/binary.desktop
	%{_datadir}/apps/kconf_update/mailtransports.upd
	%{_datadir}/apps/kconf_update/migrate-transports.pl
	%dir %{_datadir}/kde4/services/kresources
	%dir %{_datadir}/kde4/services/kresources/kabc
	%dir %{_datadir}/kde4/services/kresources/kcal
	%dir %{_includedir}/gpgme++
	%dir %{_includedir}/gpgme++/interfaces
	%{_includedir}/gpgme++/*.h
	%{_includedir}/gpgme++/*/*.h
	%dir %{_includedir}/kmime
	%{_includedir}/kmime/*.h
	%dir %{_includedir}/kabc
	%{_includedir}/kabc/*.h
	%dir %{_includedir}/akonadi/kabc
	%dir %{_includedir}/akonadi/kmime
	%{_includedir}/akonadi/*.h
	%{_includedir}/akonadi/*/*.h
	%dir %{_includedir}/kblog
	%{_includedir}/kblog/*.h
	%dir %{_includedir}/kcal
	%{_includedir}/kcal/*.h
	%dir %{_includedir}/kimap
	%{_includedir}/kimap/*.h
	%dir %{_includedir}/kldap
	%{_includedir}/kldap/*.h
	%dir %{_includedir}/kpimidentities
	%{_includedir}/kpimidentities/*.h
	%dir %{_includedir}/kpimutils
	%{_includedir}/kpimutils/*.h
	%dir %{_includedir}/kresources
	%{_includedir}/kresources/*.h
	%dir %{_includedir}/kxmlrpcclient
	%{_includedir}/kxmlrpcclient/*.h
	%dir %{_includedir}/mailtransport
	%{_includedir}/mailtransport/*.h
	%dir %{_includedir}/qgpgme
	%{_includedir}/qgpgme/*.h
	%dir %{_includedir}/syndication
	%dir %{_includedir}/syndication/atom
	%dir %{_includedir}/syndication/rdf
	%dir %{_includedir}/syndication/rss2
	%{_includedir}/syndication/*.h
	%{_includedir}/syndication/*/*.h
	%dir %{_includedir}/ktnef
	%{_includedir}/ktnef/*.h
	%{_datadir}/apps/cmake/modules/*.cmake
	%{_datadir}/config.kcfg/mailtransport.kcfg
	%{_datadir}/dbus-1/interfaces/org.kde.KResourcesManager.xml
	%{_datadir}/dbus-1/interfaces/org.kde.pim.IdentityManager.xml
	%{_datadir}/kde4/services/*.*
	%{_datadir}/kde4/services/kresources/*.*
	%{_datadir}/kde4/services/kresources/*/*.desktop
	%{_datadir}/kde4/servicetypes/*.*
