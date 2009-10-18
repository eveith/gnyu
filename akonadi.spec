Name: akonadi
Version: 1.2.1
Release: 5.0ev
Summary: KDE 4 PIM storage service
URL: http://pim.kde.org/akonadi/
Group: User Interface/Desktops
License: LGPL-2.1
Vendor: GNyU-Linux
Source: http://download.akonadi-project.org/akonadi-%{version}.tar.bz2
BuildRequires: cmake >= 2.4.5, pkg-config >= 0.9.0, make, gcc-g++
BuildRequires: qt4 >= 4.5.0, libQtSql.so.4, automoc4, soprano
BuildRequires: shared-mime-info >= 0.20
BuildRequires: libxslt, boost, redland
Requires: shared-mime-info

%description
We intend to design an extensible cross-desktop storage service for PIM data 
and meta data providing concurrent read, write, and query access. It will 
provide unique desktop wide object identification and retrieval.


%prep
%setup -q


%build
%{cmake} \
	-DQT_QMAKE_EXECUTABLE:FILEPATH='%{_libdir}/qt4/bin/qmake' \
	.
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%{__mkdir_p} '%{buildroot}/%{_includedir}/akonadi/xml'
%{__mkdir_p} '%{buildroot}/%{_datadir}/akonadi/agents'
%{__mkdir_p} '%{buildroot}/%{_datadir}/apps/akonadi/firstrun'
%{__mkdir_p} '%{buildroot}/%{_datadir}/apps/akonadi/plugins/serializer'
%{__mkdir_p} '%{buildroot}/%{_datadir}/apps/akonadi_knut_resource'


%post
%{__ldconfig}
update-mime-database > /dev/null 2>&1
exit 0


%postun
%{__ldconfig}
update-mime-database > /dev/null 2>&1
exit 0


%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog lgpl-license NEWS README
%{_bindir}/akonadi_control
%{_bindir}/akonadictl
%{_bindir}/akonadiserver
%{_includedir}/akonadi/
%dir %{_libdir}/Akonadi
%dir %{_libdir}/Akonadi/cmake
%{_libdir}/Akonadi/cmake/AkonadiConfig.cmake
%{_libdir}/Akonadi/cmake/AkonadiConfigVersion.cmake
%{_libdir}/libakonadi*.*
%{_libdir}/pkgconfig/akonadi.pc
%dir %{_datadir}/akonadi
%dir %{_datadir}/akonadi/agents
%dir %{_datadir}/apps/akonadi
%dir %{_datadir}/apps/akonadi/firstrun
%dir %{_datadir}/apps/akonadi/plugins
%dir %{_datadir}/apps/akonadi/plugins/serializer
%dir %{_datadir}/apps/akonadi_knut_resource
%dir %{_datadir}/config/akonadi
%{_datadir}/config/akonadi/mysql-global.conf
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.*.xml
%{_datadir}/dbus-1/services/org.freedesktop.Akonadi.Control.service
%{_datadir}/mime/packages/akonadi-mime.xml
