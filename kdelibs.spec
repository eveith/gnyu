Name: kdelibs
Version: 3.5.8
Release: 1ev
Summary: Base libraries for KDE-based applcations
URL: http://www.kde.org/
Group: User Interface/Desktops
License: GPL, LGPL, BSD
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: http://download.kde.org/stable/%{version}/src/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc-g++, gcc-core, libstdc++, qt3 >= 3.3.2
BuildRequires: fontconfig, perl, bzip2, arts, zlib >= 1.1, libacl
BuildRequires: libxml2 >= 2.4.8, libxslt >= 1.0.7, cups >= 1.1.9, libattr
BuildRequires: sane-backends, openldap-libs, pcre, libntlm
BuildRequires: openssl >= 0.9.5a, mesalib, libpng, libjpeg, libmng, libtiff
BuildRequires: freetype >= 2.0.0, libart >= 2.3.8, libaudiofile, sudo
BuildRequires: alsa-lib, aspell, heimdal-libs, doxygen, openexr
BuildRequires: libSM, libX11, libICE, libXau, libXcursor, libXdmcp, libXext
BuildRequires: libXfixes, libXft, libXinerama, libXrandr, libXrender
Provides: libtool(%{_libdir}/libDCOP.la)
Provides: libtool(%{_libdir}/libkdeinit_dcopserver.la)
Provides: libtool(%{_libdir}/kde3/dcopserver.la)
Provides: libtool(%{_libdir}/kde3/kded_kdetrayproxy.la)
Provides: libtool(%{_libdir}/kde3/kded_kpasswdserver.la)
Provides: libtool(%{_libdir}/kde3/kio_uiserver.la)
Provides: libtool(%{_libdir}/kde3/kded_proxyscout.la)
Provides: libtool(%{_libdir}/kde3/kded_kssld.la)
Provides: libtool(%{_libdir}/kde3/kded_kwalletd.la)
Provides: libtool(%{_libdir}/kde3/knotify.la)
Provides: libtool(%{_libdir}/kde3/kconf_update.la)
Provides: libtool(%{_libdir}/kde3/kded.la)
Provides: libtool(%{_libdir}/kde3/kbuildsycoca.la)
Provides: libtool(%{_libdir}/kde3/kio_help.la)
Provides: libtool(%{_libdir}/kde3/kio_ghelp.la)
Provides: libtool(%{_libdir}/kde3/kimg_eps.la)
Provides: libtool(%{_libdir}/kde3/kimg_xview.la)
Provides: libtool(%{_libdir}/kde3/kimg_tiff.la)
Provides: libtool(%{_libdir}/kde3/kimg_ico.la)
Provides: libtool(%{_libdir}/kde3/kimg_pcx.la)
Provides: libtool(%{_libdir}/kde3/kimg_tga.la)
Provides: libtool(%{_libdir}/kde3/kimg_rgb.la)
Provides: libtool(%{_libdir}/kde3/kimg_xcf.la)
Provides: libtool(%{_libdir}/kde3/kimg_dds.la)
Provides: libtool(%{_libdir}/kde3/plugins/styles/plastik.la)
Provides: libtool(%{_libdir}/kde3/plugins/styles/highcolor.la)
Provides: libtool(%{_libdir}/kde3/plugins/styles/highcontrast.la)
Provides: libtool(%{_libdir}/kde3/plugins/styles/light.la)
Provides: libtool(%{_libdir}/kde3/plugins/styles/kthemestyle.la)
Provides: libtool(%{_libdir}/kde3/plugins/styles/keramik.la)
Provides: libtool(%{_libdir}/kde3/plugins/designer/kdewidgets.la)
Provides: libtool(%{_libdir}/kde3/kimg_psd.la)
Provides: libtool(%{_libdir}/kde3/kimg_hdr.la)
Provides: libtool(%{_libdir}/kde3/kio_file.la)
Provides: libtool(%{_libdir}/kde3/kded_kcookiejar.la)
Provides: libtool(%{_libdir}/kde3/kcookiejar.la)
Provides: libtool(%{_libdir}/kde3/kio_http.la)
Provides: libtool(%{_libdir}/kde3/kio_http_cache_cleaner.la)
Provides: libtool(%{_libdir}/kde3/kio_ftp.la)
Provides: libtool(%{_libdir}/kde3/kgzipfilter.la)
Provides: libtool(%{_libdir}/kde3/kbzip2filter.la)
Provides: libtool(%{_libdir}/kde3/kio_metainfo.la)
Provides: libtool(%{_libdir}/kde3/kcm_kresources.la)
Provides: libtool(%{_libdir}/kde3/kstyle_plastik_config.la)
Provides: libtool(%{_libdir}/kde3/kstyle_highcontrast_config.la)
Provides: libtool(%{_libdir}/kde3/libkcertpart.la)
Provides: libtool(%{_libdir}/kde3/klauncher.la)
Provides: libtool(%{_libdir}/kde3/kded_kdeprintd.la)
Provides: libtool(%{_libdir}/kde3/libkdeprint_management_module.la)
Provides: libtool(%{_libdir}/kde3/kaddprinterwizard.la)
Provides: libtool(%{_libdir}/kde3/kdeprint_lpdunix.la)
Provides: libtool(%{_libdir}/kde3/cupsdconf.la)
Provides: libtool(%{_libdir}/kde3/kdeprint_cups.la)
Provides: libtool(%{_libdir}/kde3/kdeprint_lpr.la)
Provides: libtool(%{_libdir}/kde3/kdeprint_rlpr.la)
Provides: libtool(%{_libdir}/kde3/kdeprint_ext.la)
Provides: libtool(%{_libdir}/kde3/kdeprint_tool_escputil.la)
Provides: libtool(%{_libdir}/kde3/kabcformat_binary.la)
Provides: libtool(%{_libdir}/kde3/kabc_file.la)
Provides: libtool(%{_libdir}/kde3/kabc_dir.la)
Provides: libtool(%{_libdir}/kde3/kabc_net.la)
Provides: libtool(%{_libdir}/kde3/kabc_ldapkio.la)
Provides: libtool(%{_libdir}/kde3/kspell_aspell.la)
Provides: libtool(%{_libdir}/kde3/kspell_ispell.la)
Provides: libtool(%{_libdir}/kde3/kcmshell.la)
Provides: libtool(%{_libdir}/kde3/kjavaappletviewer.la)
Provides: libtool(%{_libdir}/kde3/libkhtmlpart.la)
Provides: libtool(%{_libdir}/kde3/khtmlimagepart.la)
Provides: libtool(%{_libdir}/kde3/libkmultipart.la)
Provides: libtool(%{_libdir}/kde3/libshellscript.la)
Provides: libtool(%{_libdir}/kde3/kfileaudiopreview.la)
Provides: libtool(%{_libdir}/kde3/libkatepart.la)
Provides: libtool(%{_libdir}/kde3/ktexteditor_isearch.la)
Provides: libtool(%{_libdir}/kde3/ktexteditor_insertfile.la)
Provides: libtool(%{_libdir}/kde3/ktexteditor_kdatatool.la)
Provides: libtool(%{_libdir}/kde3/ktexteditor_docwordcompletion.la)
Provides: libtool(%{_libdir}/libkdefx.la)
Provides: libtool(%{_libdir}/libkdefakes.la)
Provides: libtool(%{_libdir}/libkdecore.la)
Provides: libtool(%{_libdir}/libkunittest.la)
Provides: libtool(%{_libdir}/libkdeui.la)
Provides: libtool(%{_libdir}/libkspell.la)
Provides: libtool(%{_libdir}/libkdesu.la)
Provides: libtool(%{_libdir}/libkjs.la)
Provides: libtool(%{_libdir}/libkwalletclient.la)
Provides: libtool(%{_libdir}/libkwalletbackend.la)
Provides: libtool(%{_libdir}/libkio.la)
Provides: libtool(%{_libdir}/libkdeinit_kio_uiserver.la)
Provides: libtool(%{_libdir}/libkdesasl.la)
Provides: libtool(%{_libdir}/libkntlm.la)
Provides: libtool(%{_libdir}/libartskde.la)
Provides: libtool(%{_libdir}/libkdnssd.la)
Provides: libtool(%{_libdir}/libkdeinit_kconf_update.la)
Provides: libtool(%{_libdir}/libkdeinit_kded.la)
Provides: libtool(%{_libdir}/libkdeinit_kbuildsycoca.la)
Provides: libtool(%{_libdir}/libkdeinit_kcookiejar.la)
Provides: libtool(%{_libdir}/libkdeinit_kio_http_cache_cleaner.la)
Provides: libtool(%{_libdir}/libknewstuff.la)
Provides: libtool(%{_libdir}/libkparts.la)
Provides: libtool(%{_libdir}/libkresources.la)
Provides: libtool(%{_libdir}/libkutils.la)
Provides: libtool(%{_libdir}/libkmid.la)
Provides: libtool(%{_libdir}/libkscreensaver.la)
Provides: libtool(%{_libdir}/libkdeinit_klauncher.la)
Provides: libtool(%{_libdir}/libkdeprint.la)
Provides: libtool(%{_libdir}/libkdeprint_management.la)
Provides: libtool(%{_libdir}/libkdeinit_kaddprinterwizard.la)
Provides: libtool(%{_libdir}/libkdeinit_cupsdconf.la)
Provides: libtool(%{_libdir}/libvcard.la)
Provides: libtool(%{_libdir}/libkabc.la)
Provides: libtool(%{_libdir}/libkabc_file.la)
Provides: libtool(%{_libdir}/libkabc_dir.la)
Provides: libtool(%{_libdir}/libkabc_net.la)
Provides: libtool(%{_libdir}/libkabc_ldapkio.la)
Provides: libtool(%{_libdir}/libkspell2.la)
Provides: libtool(%{_libdir}/libkmdi2.la)
Provides: libtool(%{_libdir}/libkmdi.la)
Provides: libtool(%{_libdir}/libkdeinit_kcmshell.la)
Provides: libtool(%{_libdir}/libkjava.la)
Provides: libtool(%{_libdir}/libkhtml.la)
Provides: libtool(%{_libdir}/libktexteditor.la)
Provides: libtool(%{_libdir}/libkscript.la)
Provides: libtool(%{_libdir}/libkmediaplayer.la)
Provides: libtool(%{_libdir}/libkimproxy.la)
Provides: libtool(%{_libdir}/libkatepartinterfaces.la)

%description
Libraries for the K Desktop Environment (KDE):
This package includes libraries that are central to the development and
execution of a KDE program, as well as internationalization files for these
libraries, misc HTML documentation, theme modules, and regression tests.


%prep
%setup -q


%build
%configure \
	--disable-debug \
	--disable-warnings \
	--enable-final \
	--enable-sendfile \
	--enable-mitshm \
	--enable-dnotify \
	--with-acl \
	--with-utempter \
	--with-libidn \
	--with-libart \
	--with-sudo-kdesu-backend \
	--with-tiff \
	--with-alsa \
	--with-aspell \
	--without-hspell 
make %{_smp_mflags}


%install
[[ "$RPM_BUILD_ROOT" != "/" ]] && rm -rf "$RPM_BUILD_ROOT"

make install DESTDIR="$RPM_BUILD_ROOT"
rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ "$RPM_BUILD_ROOT" != "/" ]] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc AUTHORS COPYING* KDE?PORTING* NAMING README TODO
%doc %{_datadir}/doc/HTML/en/
%dir %{_datadir}/doc/HTML
%dir %{_datadir}/doc/HTML/en
%{_libdir}/*
%{_libdir}/kde3/
%{_bindir}/*
%{_datadir}/apps/
%{_datadir}/config/
%{_datadir}/locale/all_languages
%{_datadir}/services/
%{_datadir}/servicetypes/
%{_datadir}/mimelnk/
%{_datadir}/icons/
%{_datadir}/applications/
%{_datadir}/emoticons/
%{_datadir}/autostart/
%{_includedir}/*.h
%{_includedir}/arts/*.h
%{_includedir}/kde.pot
%{_includedir}/kgenericfactory.tcc
%{_includedir}/kio/
%{_includedir}/kunittest/
%{_includedir}/kdesu/
%{_includedir}/kjs/
%{_includedir}/dnssd/
%{_includedir}/knewstuff/
%{_includedir}/kparts/
%{_includedir}/kresources/
%{_includedir}/ksettings/
%{_includedir}/libkmid/
%{_includedir}/kdeprint/
%{_includedir}/kabc/
%{_includedir}/kspell2/
%{_includedir}/kmdi/
%{_includedir}/dom/
%{_includedir}/ktexteditor/
%{_includedir}/kmediaplayer/
%{_includedir}/khexedit/
%{_includedir}/kate/
%dir /etc/xdg
%dir /etc/xdg/menus
/etc/xdg/menus/*
