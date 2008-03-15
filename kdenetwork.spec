Name: kdenetwork
Version: 3.5.6
Release: 1ev
Summary: Network related utilities for the K Desktop Environment (KDE)
URL: http://www.kde.org/
Group: Applications/Communications
License: GPL
Vendor: MSP Slackware
Source: http://download.kde.org/stable/%{version}/src/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, gcc-g++, qt3 >= 3.3.2, kdelibs, kdebase
BuildRequires: openslp, zlib >= 1.1, fontconfig, libxml2 >= 2.4.8, glib2 >= 2.4
BuildRequires: libxslt >= 1.0.7, openssl >= 0.9.6, freetype >= 2.0.0
Requires: qt3 >= 3.3.2, kdelibs, kdebase, zlib >= 1.1, libxml2 >= 2.4.8
Requires: glib2 >= 2.4, libxslt >= 1.0.7, openssl >= 0.9.6, freetype >= 2.0.0
Provides: libtool(%{_libdir}/kde3/kcm_kcmsambaconf.la)
Provides: libtool(%{_libdir}/kde3/fileshare_propsdlgplugin.la)
Provides: libtool(%{_libdir}/kde3/kcm_fileshare.la)
Provides: libtool(%{_libdir}/kde3/kdict_panelapplet.la)
Provides: libtool(%{_libdir}/kde3/kdict.la)
Provides: libtool(%{_libdir}/kde3/kio_zeroconf.la)
Provides: libtool(%{_libdir}/kde3/kded_dnssdwatcher.la)
Provides: libtool(%{_libdir}/kde3/kfile_torrent.la)
Provides: libtool(%{_libdir}/kde3/khtml_kget.la)
Provides: libtool(%{_libdir}/kde3/libkrichtexteditpart.la)
Provides: libtool(%{_libdir}/kde3/kopete_chatwindow.la)
Provides: libtool(%{_libdir}/kde3/kopete_emailwindow.la)
Provides: libtool(%{_libdir}/kde3/kcm_kopete_accountconfig.la)
Provides: libtool(%{_libdir}/kde3/kcm_kopete_behaviorconfig.la)
Provides: libtool(%{_libdir}/kde3/kcm_kopete_appearanceconfig.la)
Provides: libtool(%{_libdir}/kde3/kcm_kopete_identityconfig.la)
Provides: libtool(%{_libdir}/kde3/kcm_kopete_avdeviceconfig.la)
Provides: libtool(%{_libdir}/kde3/kopete_testbed.la)
Provides: libtool(%{_libdir}/kde3/kopete_groupwise.la)
Provides: libtool(%{_libdir}/kde3/kopete_msn.la)
Provides: libtool(%{_libdir}/kde3/kcm_kopete_msn.la)
Provides: libtool(%{_libdir}/kde3/kopete_irc.la)
Provides: libtool(%{_libdir}/kde3/kopete_aim.la)
Provides: libtool(%{_libdir}/kde3/kopete_icq.la)
Provides: libtool(%{_libdir}/kde3/kopete_yahoo.la)
Provides: libtool(%{_libdir}/kde3/kopete_wp.la)
Provides: libtool(%{_libdir}/kde3/kopete_jabber.la)
Provides: libtool(%{_libdir}/kde3/kio_jabberdisco.la)
Provides: libtool(%{_libdir}/kde3/kopete_gadu.la)
Provides: libtool(%{_libdir}/kde3/kopete_latex.la)
Provides: libtool(%{_libdir}/kde3/kcm_kopete_latex.la)
Provides: libtool(%{_libdir}/kde3/kopete_autoreplace.la)
Provides: libtool(%{_libdir}/kde3/kcm_kopete_autoreplace.la)
Provides: libtool(%{_libdir}/kde3/kopete_history.la)
Provides: libtool(%{_libdir}/kde3/kcm_kopete_history.la)
Provides: libtool(%{_libdir}/kde3/kopete_contactnotes.la)
Provides: libtool(%{_libdir}/kde3/kopete_cryptography.la)
Provides: libtool(%{_libdir}/kde3/kcm_kopete_cryptography.la)
Provides: libtool(%{_libdir}/kde3/kopete_connectionstatus.la)
Provides: libtool(%{_libdir}/kde3/kopete_translator.la)
Provides: libtool(%{_libdir}/kde3/kcm_kopete_translator.la)
Provides: libtool(%{_libdir}/kde3/kopete_nowlistening.la)
Provides: libtool(%{_libdir}/kde3/kcm_kopete_nowlistening.la)
Provides: libtool(%{_libdir}/kde3/kopete_webpresence.la)
Provides: libtool(%{_libdir}/kde3/kcm_kopete_webpresence.la)
Provides: libtool(%{_libdir}/kde3/kopete_texteffect.la)
Provides: libtool(%{_libdir}/kde3/kcm_kopete_texteffect.la)
Provides: libtool(%{_libdir}/kde3/kopete_highlight.la)
Provides: libtool(%{_libdir}/kde3/kcm_kopete_highlight.la)
Provides: libtool(%{_libdir}/kde3/kopete_alias.la)
Provides: libtool(%{_libdir}/kde3/kcm_kopete_alias.la)
Provides: libtool(%{_libdir}/kde3/kopete_netmeeting.la)
Provides: libtool(%{_libdir}/kde3/kcm_kopete_netmeeting.la)
Provides: libtool(%{_libdir}/kde3/kopete_addbookmarks.la)
Provides: libtool(%{_libdir}/kde3/kcm_kopete_addbookmarks.la)
Provides: libtool(%{_libdir}/kde3/kopete_statistics.la)
Provides: libtool(%{_libdir}/kde3/kpf_panelapplet.la)
Provides: libtool(%{_libdir}/kde3/kpfpropertiesdialog.la)
Provides: libtool(%{_libdir}/kde3/kded_kinetd.la)
Provides: libtool(%{_libdir}/kde3/kcm_krfb.la)
Provides: libtool(%{_libdir}/kde3/ksirc.la)
Provides: libtool(%{_libdir}/kde3/kcm_ktalkd.la)
Provides: libtool(%{_libdir}/kde3/kcm_lanbrowser.la)
Provides: libtool(%{_libdir}/kde3/kio_lan.la)
Provides: libtool(%{_libdir}/kde3/libkntsrcfilepropsdlg.la)
Provides: libtool(%{_libdir}/kde3/knewsticker_panelapplet.la)
Provides: libtool(%{_libdir}/libkdeinit_kdict.la)
Provides: libtool(%{_libdir}/libkopete.la)
Provides: libtool(%{_libdir}/libkopete_videodevice.la)
Provides: libtool(%{_libdir}/libkopete_msn_shared.la)
Provides: libtool(%{_libdir}/libkopete_oscar.la)
Provides: libtool(%{_libdir}/libkdeinit_ksirc.la)
Provides: libtool(%{_libdir}/librss.la)

%description
* kdict: graphical client for the DICT protocol.
* kit: AOL instant messenger client, using the TOC protocol
* knewsticker: RDF newsticker applet
* kpf: public fileserver applet
* kppp: dialer and front end for pppd
* ksirc: IRC client
* ktalkd: talk daemon
* kxmlrpc: KDE XmlRpc Daemon
* lanbrowsing: lan browsing kio slave
* krfb: Desktop Sharing server, allow others to access your desktop via VNC
* krdc: a client for Desktop Sharing and other VNC servers
* wifi: Wireless LAN tools


%prep
%setup -q


%build
%configure \
    --disable-debug \
	--disable-warnings \
    --enable-pch \
	--enable-new-ldflags \
	--enable-final
make %{_smp_mflags}


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"


[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc AUTHORS COPYING* README
%doc %{_datadir}/doc/HTML/en/*
%{_datadir}/config/*rc
%{_datadir}/icons/*/*/*/*
%{_datadir}/applications/kde/*.desktop
%{_datadir}/services/*.*
%{_datadir}/services/*/*.*
%{_datadir}/servicetypes/*.desktop
%{_datadir}/sounds/*.*
%{_datadir}/apps/kicker/applets/*.desktop
%{_datadir}/apps/kdict/
%{_datadir}/apps/remoteview/*.desktop
%{_datadir}/apps/zeroconf/
%{_datadir}/apps/kget/
%{_datadir}/apps/konqueror/*/*.*
%{_datadir}/apps/khtml/*/*.*
%{_datadir}/apps/kopete/
%{_datadir}/apps/kopeterichtexteditpart/
%{_datadir}/apps/kopete_*/
%{_datadir}/apps/kconf_update/*.*
%{_datadir}/apps/knewsticker/
%{_datadir}/apps/kppp/
%{_datadir}/apps/krdc/
%{_datadir}/apps/kinetd/
%{_datadir}/apps/krfb/
%{_datadir}/apps/ksirc/
%{_datadir}/apps/lisa/
%{_datadir}/apps/konqsidebartng/virtual_folders/services/*.desktop
%{_datadir}/apps/konqueror/dirtree/remote/*.desktop
%{_datadir}/applnk/.hidden/*.desktop
%{_datadir}/mimelnk/*/*.desktop
%{_datadir}/config.kcfg/*.kcfg
%{_libdir}/*.*
%{_libdir}/kde3/*.*
%{_libdir}/kconf_update_bin/*-kconf_update
%{_includedir}/kopete/
%{_includedir}/rss/
%{_bindir}/*
