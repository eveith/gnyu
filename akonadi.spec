Name: akonadi
Version: 1.1.1
Release: 1ev
Summary: KDE 4 PIM storage service
URL: http://pim.kde.org/akonadi/
Group: User Interface/Desktops
License: LGPL-2.1
Vendor: GNyU-Linux
Source: http://akonadi.omat.nl/akonadi-%{version}.tar.bz2
BuildRequires: cmake >= 2.4.5, make, gcc-g++, qt4 >= 4.2.0, automoc4 >= 0.8.86
BuildRequires: libX11, libXext, libICE, mysql-libs, shared-mime-info
BuildRequires: boost >= 1.33.1, pkg-config
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
%{_libdir}/libakonadi*.*
%{_libdir}/pkgconfig/akonadi.pc
%dir %{_datadir}/config/akonadi
%{_datadir}/config/akonadi/mysql-global.conf
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.*.xml
%{_datadir}/dbus-1/services/org.freedesktop.Akonadi.Control.service
%{_datadir}/mime/packages/akonadi-mime.xml
