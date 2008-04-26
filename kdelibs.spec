Name: kdelibs
Version: 3.5.9
Release: 2ev
Summary: Base libraries for KDE-based applcations
URL: http://www.kde.org/
Group: User Interface/Desktops
License: GPL-2, LGPL-2, BSD
Vendor: GNyU-Linux
Source: http://download.kde.org/stable/%{version}/src/%{name}-%{version}.tar.bz2
Patch0: %{name}-post-kde-3.5.5-kinit.diff
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
BuildRequires: hicolor-icon-theme

%description
Libraries for the K Desktop Environment (KDE):
This package includes libraries that are central to the development and
execution of a KDE program, as well as internationalization files for these
libraries, misc HTML documentation, theme modules, and regression tests.


%prep
%setup -q
%patch0


%build
%configure \
	--disable-debug \
	--disable-warnings \
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
%{__make} %{?_smp_mflags}


%install
[[ "${RPM_BUILD_ROOT}" != "/" ]] && %{__rm} -rf "${RPM_BUILD_ROOT}"
%{__make_install} DESTDIR="${RPM_BUILD_ROOT}"

# This file is provided by hicolor-icon-theme, remove it here:
%{__rm} -f %{buildroot}/%{_datadir}/icons/hicolor/index.theme


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ "${RPM_BUILD_ROOT}" != "/" ]] && %{__rm} -rf "${RPM_BUILD_ROOT}"


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
