Name: qt4
Version: 4.3.4
Release: 1ev
Summary: The Qt GUI toolkit
URL: http://www.trolltech.com/
Group: User Interface/Desktops
License: QPL
Vendor: GNyU-Linux
Source0: ftp://ftp.trolltech.com/qt/source/qt-x11-opensource-src-%{version}.tar.gz
Source1: %{name}-profile.sh
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: libtiff, libjpeg, libpng, zlib, libstdc++
BuildRequires: fontconfig >= 2.0, freetype >= 1.7, libXext, libXinerama
BuildRequires: libSM, libICE, libX11, libXcursor,  libXrender, libXrandr
BuildRequires: make >= 3.79.1, gcc, gcc-g++, sed, findutils

%description
Qt is a complete and well-developed object-oriented framework for
developing graphical user interface (GUI) applications using C++.

This release is free only for development of free software for the X
Window System.  If you use Qt for developing commercial or other
non-free software, you must have a professional license.  Please see
http://www.trolltech.com/purchase.html for information on how to
obtain a professional license.


%package doc
Summary: Documentation for the Qt library
Group: User Interface/Desktops
Requires: qt4 = %{version}

%description doc
Qt is a complete and well-developed object-oriented framework for
developing graphical user interface (GUI) applications using C++.

This release is free only for development of free software for the X
Window System.  If you use Qt for developing commercial or other
non-free software, you must have a professional license.  Please see
http://www.trolltech.com/purchase.html for information on how to
obtain a professional license.

This package contains all documentation one will need when developing
Qt based applications. It also includes the Qt Assistant.


%prep
%setup -q -n qt-x11-opensource-src-%{version}

# set correct FLAGS
%{__sed} -i \
	-e "s,\(QMAKE_CFLAGS_RELEASE[[:space:]]+=\).*$,\1 ${RPM_OPT_FLAGS},g" \
	-e 's,\(QMAKE_CC[[:space:]]=\).*$,\1 %{_target_platform}-gcc,g' \
	-e 's,\(QMAKE_CXX[[:space:]]*=\).*$,\1 %{_target_platform}-g++,g' \
	mkspecs/common/g++.conf


%build
echo 'yes' | ./configure \
	-prefix %{_libdir}/qt4 \
	-docdir '%{_docdir}/%{name}-%{version}' \
	-release \
	-iconv \
	-release \
	-shared \
	-largefile \
	-qt3support \
	-qt-gif \
	-system-zlib \
	-no-g++-exceptions \
	-nis \
	-cups \
	-stl \
	-openssl \
	-system-libmng \
	-system-libjpeg \
	-system-libpng \
	-no-nas-sound \
	-sm \
	-xshape \
	-xinerama \
	-xcursor \
	-xrandr \
	-xrender \
	-no-tablet \
	-xkb \
	-qdbus
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} INSTALL_ROOT='%{buildroot}'

%{__mkdir_p} %{buildroot}/%{_libdir}
%{__cp} -R %{buildroot}/%{_libdir}/qt4/lib/pkgconfig %{buildroot}/%{_libdir}

# Install Qt shell profile script
%{__mkdir_p} %{buildroot}/etc/profile.d
%{__install} -m 0755 %{SOURCE1} %{buildroot}/etc/profile.d/qt4.sh

# Remove silly link
%{__find} %{buildroot}/%{_libdir}/qt/mkspecs/default/ -type l \
	-exec rm -f '{}' \; ||:

# Now, let's add a fine ldconfig file
%{__mkdir_p} %{buildroot}/etc/ld.so.conf.d
echo %{_libdir}/qt4/lib > %{buildroot}/etc/ld.so.conf.d/%{name}-%{_arch}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc GPL_*.TXT LICENSE.* OPENSOURCE-NOTICE.TXT README
/etc/ld.so.conf.d/%{name}-%{_arch}
%attr(0755, root, root) /etc/profile.d/qt4.sh
%{_libdir}/qt4/
%{_libdir}/pkgconfig/Qt*.pc
