Name: qt4
Version: 4.5.0
Release: 5ev
Summary: The Qt GUI toolkit
URL: http://www.trolltech.com/
Group: User Interface/Desktops
License: QPL
Vendor: GNyU-Linux
Source0: ftp://ftp.trolltech.com/qt/source/qt-x11-opensource-src-%{version}.tar.gz
Source1: %{name}-profile.sh
BuildRequires(build,install): make
BuildRequires(install): findutils
BuildRequires: libtiff, libjpeg, libpng, libmng, zlib
BuildRequires: glib2 >= 2.8.3, clucene-core, dbus
BuildRequires: fontconfig >= 2.0, freetype >= 1.7
BuildRequires: libXrender >= 0.9.0, libXrandr >= 1.0.2, libXcursor >= 1.1.4
BuildRequires: libXfixes >= 3.0.0, libXinerama
#BuildRequires: libXfixes >= 3.0.0, libXinerama >= 1.1.0
BuildRequires: libXi, libXt >= 0.99, libXext
#BuildRequires: libXi >= 1.3.0, libXt >= 0.99, libXext
#BuildRequires: libXi >= 1.3.0, libXt >= 0.99, libXext >= 6.4.3
#BuildRequires: libX11 >= 6.2.1, libSM >= 6.0.4, libICE >= 6.3.5
BuildRequires: libX11, libSM, libICE
BuildRequires: make >= 3.79.1, gcc-g++, libstdc++, openssl, cups, mesalib

%description
Qt is a complete and well-developed object-oriented framework for
developing graphical user interface (GUI) applications using C++.

This release is free only for development of free software for the X
Window System.  If you use Qt for developing commercial or other
non-free software, you must have a professional license.  Please see
http://www.trolltech.com/purchase.html for information on how to
obtain a professional license.


%package doc
Summary: Documentation, examples and demos for the Qt library
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
Qt based applications. It also includes the Qt Assistant and some demos and
examples.


%prep
%setup -q -n qt-x11-opensource-src-%{version}

# set correct FLAGS
%{__sed} -i \
	-e "s,\(QMAKE_CFLAGS_RELEASE[[:space:]]+=\).*$,\1 ${RPM_OPT_FLAGS},g" \
	-e "s,\(QMAKE_CC[[:space:]]=\).*$,\1 ${CC:-%{_target_platform}-gcc},g" \
	-e "s,\(QMAKE_CXX[[:space:]]*=\).*$,\1 ${CXX:-%{_target_platform}-g++},g" \
	mkspecs/common/g++.conf


%build
echo 'yes' | ./configure \
	-prefix '%{_libdir}/qt4' \
	-docdir '%{_docdir}/%{name}-%{version}' \
	-release \
	-iconv \
	-shared \
	-largefile \
	-qt3support \
	-qt-gif \
	-system-zlib \
	-no-exceptions \
	-no-nis \
	-cups \
	-fast \
	-system-libmng \
	-system-libjpeg \
	-system-libpng \
	-openssl \
	-no-nas-sound \
	-dbus \
	-no-separate-debug-info \
	-no-phonon \
	-plugin-sql-mysql \
	-webkit \
	-glib \
	-gtkstyle 
%{__make} %{?_smp_mflags}


%install
%{__make} install INSTALL_ROOT='%{buildroot}'

%{__mkdir_p} '%{buildroot}/%{_libdir}'
%{__cp} -R '%{buildroot}/%{_libdir}/qt4/lib/pkgconfig' \
	'%{buildroot}/%{_libdir}'

# Install Qt shell profile script
%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/profile.d'
%{__install} '%{SOURCE1}' '%{buildroot}/%{_sysconfdir}/profile.d/qt4.sh'

# Now, let's add a fine ldconfig file
%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/ld.so.conf.d'
echo '%{_libdir}/qt4/lib' \
	> '%{buildroot}/%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}'


%post -p %{__ldconfig}
%postun -p %{__ldconfig}


%files
%defattr(-, root, root)
%doc LGPL_EXCEPTION.txt LICENSE.* KNOWN.ISSUES README changes*
/etc/ld.so.conf.d/%{name}-%{_arch}
%attr(0755, root, root) %{_sysconfdir}/profile.d/qt4.sh
%dir %{_libdir}/qt4/
%dir %{_libdir}/qt4/bin
%{_libdir}/qt4/bin/designer
%{_libdir}/qt4/bin/linguist
%{_libdir}/qt4/bin/lconvert
%{_libdir}/qt4/bin/lrelease
%{_libdir}/qt4/bin/lupdate
%{_libdir}/qt4/bin/moc
%{_libdir}/qt4/bin/pixeltool
%{_libdir}/qt4/bin/qdbus
%{_libdir}/qt4/bin/qdbuscpp2xml
%{_libdir}/qt4/bin/qdbusviewer
%{_libdir}/qt4/bin/qdbusxml2cpp
%{_libdir}/qt4/bin/qhelpconverter
%{_libdir}/qt4/bin/qmake
%{_libdir}/qt4/bin/qt3to4
%{_libdir}/qt4/bin/qtconfig
%{_libdir}/qt4/bin/rcc
%{_libdir}/qt4/bin/uic
%{_libdir}/qt4/bin/uic3
%{_libdir}/qt4/include/
%dir %{_libdir}/qt4/lib
%{_libdir}/qt4/lib/libQt3Support.*
%{_libdir}/qt4/lib/libQtCLucene.*
%{_libdir}/qt4/lib/libQtCore.*
%{_libdir}/qt4/lib/libQtDBus.*
%{_libdir}/qt4/lib/libQtDesigner.*
%{_libdir}/qt4/lib/libQtDesignerComponents.*
%{_libdir}/qt4/lib/libQtGui.*
%{_libdir}/qt4/lib/libQtHelp.*
%{_libdir}/qt4/lib/libQtNetwork.*
%{_libdir}/qt4/lib/libQtOpenGL.*
%{_libdir}/qt4/lib/libQtScript.*
%{_libdir}/qt4/lib/libQtScriptTools.*
%{_libdir}/qt4/lib/libQtSvg.*
%{_libdir}/qt4/lib/libQtSql.*
%{_libdir}/qt4/lib/libQtTest.*
%{_libdir}/qt4/lib/libQtUiTools.*
%{_libdir}/qt4/lib/libQtWebKit.*
%{_libdir}/qt4/lib/libQtXml.*
#%{_libdir}/qt4/lib/libphonon.*
%dir %{_libdir}/qt4/lib/pkgconfig
#%{_libdir}/qt4/lib/pkgconfig/phonon.pc
%{_libdir}/qt4/lib/pkgconfig/Qt3Support.pc
%{_libdir}/qt4/lib/pkgconfig/QtCLucene.pc
%{_libdir}/qt4/lib/pkgconfig/QtCore.pc
%{_libdir}/qt4/lib/pkgconfig/QtDBus.pc
%{_libdir}/qt4/lib/pkgconfig/QtDesigner.pc
%{_libdir}/qt4/lib/pkgconfig/QtDesignerComponents.pc
%{_libdir}/qt4/lib/pkgconfig/QtGui.pc
%{_libdir}/qt4/lib/pkgconfig/QtHelp.pc
%{_libdir}/qt4/lib/pkgconfig/QtNetwork.pc
%{_libdir}/qt4/lib/pkgconfig/QtOpenGL.pc
%{_libdir}/qt4/lib/pkgconfig/QtScript.pc
%{_libdir}/qt4/lib/pkgconfig/QtScriptTools.pc
%{_libdir}/qt4/lib/pkgconfig/QtSql.pc
%{_libdir}/qt4/lib/pkgconfig/QtSvg.pc
%{_libdir}/qt4/lib/pkgconfig/QtTest.pc
%{_libdir}/qt4/lib/pkgconfig/QtUiTools.pc
%{_libdir}/qt4/lib/pkgconfig/QtWebKit.pc
%{_libdir}/qt4/lib/pkgconfig/QtXml.pc
%dir %{_libdir}/qt4/translations
%{_libdir}/qt4/translations/designer_*.qm
%{_libdir}/qt4/translations/linguist_*.qm
%{_libdir}/qt4/translations/qt_??.qm
%{_libdir}/qt4/translations/qt_??_??.qm
%{_libdir}/qt4/translations/qt_help_??.qm
%{_libdir}/qt4/translations/qt_help_??_??.qm
%{_libdir}/qt4/translations/qtconfig_*.qm
%{_libdir}/qt4/translations/qvfb*.qm
%{_libdir}/qt4/mkspecs/
%{_libdir}/qt4/plugins/
%{_libdir}/qt4/phrasebooks/
%{_libdir}/qt4/q3porting.xml
#%{_libdir}/pkgconfig/phonon.pc
%{_libdir}/pkgconfig/Qt3Support.pc
%{_libdir}/pkgconfig/QtCLucene.pc
%{_libdir}/pkgconfig/QtCore.pc
%{_libdir}/pkgconfig/QtDBus.pc
%{_libdir}/pkgconfig/QtDesigner.pc
%{_libdir}/pkgconfig/QtDesignerComponents.pc
%{_libdir}/pkgconfig/QtGui.pc
%{_libdir}/pkgconfig/QtHelp.pc
%{_libdir}/pkgconfig/QtNetwork.pc
%{_libdir}/pkgconfig/QtOpenGL.pc
%{_libdir}/pkgconfig/QtScript.pc
%{_libdir}/pkgconfig/QtScriptTools.pc
%{_libdir}/pkgconfig/QtSql.pc
%{_libdir}/pkgconfig/QtSvg.pc
%{_libdir}/pkgconfig/QtTest.pc
%{_libdir}/pkgconfig/QtUiTools.pc
%{_libdir}/pkgconfig/QtWebKit.pc
%{_libdir}/pkgconfig/QtXml.pc


%files doc
%defattr(-, root, root)
%doc doc/html doc/qch
%doc %{_libdir}/qt4/examples/
%doc %{_libdir}/qt4/demos/
%{_libdir}/qt4/bin/assistant*
%{_libdir}/qt4/bin/qhelpgenerator*
%{_libdir}/qt4/bin/qcollectiongenerator*
%{_libdir}/qt4/bin/qtdemo*
%{_libdir}/qt4/lib/libQtAssistantClient.*
%{_libdir}/qt4/lib/pkgconfig/QtAssistantClient.pc
%{_libdir}/pkgconfig/QtAssistantClient.pc
%{_libdir}/qt4/translations/assistant*.qm
