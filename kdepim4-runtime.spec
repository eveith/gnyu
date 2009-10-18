Name: kdepim4-runtime
Version: 4.3.2
Release: 1.0ev
Summary: KDE 4 PIM runtime environment
URL: http://www.kde.org
Group: User Interface/Desktop
License: GPL-2, LGPL-2.1
Vendor: GNyU-Linux
Source: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdepim-runtime-%{version}.tar.bz2
BuildRequires: cmake >= 2.6.2, make, flex, bison, gcc-g++, perl, gettext
BuildRequires: libX11, libSM, libICE, libXrender, libXt, libxkbfile
BuildRequires: qt4 >= 4.5.0, automoc4 >= 0.9.88
BuildRequires: kdelibs4 = %{version}, kdelibs4-experimental = %{version}
BuildRequires: kdepimlibs4 = %{version}, kdebase4 = %{version}
BuildRequires: boost >= 1.33.1, shared-mime-info >= 0.30, libxml2, libxslt
BuildRequires: akonadi >= 1.1.1

%description
This package contains akonadi agents written using kdelibs.


%prep
	%setup -q -n 'kdepim-runtime-%{version}'


%build
	%{cmake} .
	%{__make} %{?_smp_mflags}


%install
	%{__make} install DESTDIR='%{buildroot}'


%post


%postun


%files
	%defattr(-, root, root)
	%doc COPYING*
	%config %{_sysconfdir}/kde4/kres-migratorrc
	%{_bindir}/akonadi2xml
	%{_bindir}/akonadi_birthdays_resource
	%{_bindir}/akonadi_distlist_resource
	%{_bindir}/akonadi_ical_resource
	%{_bindir}/akonadi_imap_resource
	%{_bindir}/akonadi_kabc_resource
	%{_bindir}/akonadi_kcal_resource
	%{_bindir}/akonadi_knut_resource
	%{_bindir}/akonadi_kolabproxy_resource
	%{_bindir}/akonadi_localbookmarks_resource
	%{_bindir}/akonadi_maildir_resource
	%{_bindir}/akonadi_microblog_resource
	%{_bindir}/akonadi_nepomuk_contact_feeder
	%{_bindir}/akonadi_nepomuk_email_feeder
	%{_bindir}/akonadi_nepomuktag_resource
	%{_bindir}/akonadi_nntp_resource
	%{_bindir}/akonadi_strigi_feeder
	%{_bindir}/akonadi_vcard_resource
	%{_bindir}/akonadi_vcarddir_resource
	%{_bindir}/akonadiconsole
	%{_bindir}/akonaditray
	%{_bindir}/kres-migrator
	%{_includedir}/akonadi/xml/*xml*.h
	%{_libdir}/kde4/akonadi_serializer_addressee.so
	%{_libdir}/kde4/akonadi_serializer_bookmark.so
	%{_libdir}/kde4/akonadi_serializer_contactgroup.so
	%{_libdir}/kde4/akonadi_serializer_kcal.so
	%{_libdir}/kde4/akonadi_serializer_mail.so
	%{_libdir}/kde4/akonadi_serializer_microblog.so
	%{_libdir}/kde4/kabc_akonadi.so
	%{_libdir}/kde4/kcal_akonadi.so
	%{_libdir}/kde4/kcm_akonadi.so
	%{_libdir}/kde4/kcm_akonadi_resources.so
	%{_libdir}/kde4/kcm_akonadi_server.so
	%{_libdir}/kde4/kio_akonadi.so
	%{_libdir}/libakonadi-kabccommon.so*
	%{_libdir}/libakonadi-kcal.so*
	%{_libdir}/libakonadi-xml.so*
	%{_libdir}/libakonadi_next.so*
	%{_libdir}/libkdepim-copy.so*
	%{_libdir}/libmaildir.so*
	%{_datadir}/akonadi/agents/*.desktop
	%{_datadir}/applications/kde4/akonadiconsole.desktop
	%{_datadir}/applications/kde4/akonaditray.desktop
	%{_datadir}/apps/akonadi/akonadi-xml.xsd
	%{_datadir}/apps/akonadi/firstrun/defaultaddressbook
	%{_datadir}/apps/akonadi/firstrun/defaultcalendar
	%{_datadir}/apps/akonadi/plugins/serializer/akonadi_serializer_*.desktop
	%{_datadir}/apps/akonadi_knut_resource/knut-template.xml
	%dir %{_datadir}/apps/akonadiconsole
	%{_datadir}/apps/akonadiconsole/akonadiconsoleui.rc
	%{_datadir}/dbus-1/interfaces/org.kde.Akonadi.Maildir.Settings.xml
	%{_datadir}/icons/hicolor/64x64/apps/kolab.png
	%{_datadir}/kde4/services/*.*
	%{_datadir}/kde4/services/kresources/*/*.desktop
	%{_datadir}/mime/packages/kdepim-mime.xml

