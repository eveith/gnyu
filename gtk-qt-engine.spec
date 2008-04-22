Name: gtk-qt-engine
Version: 0.8
Release: 1ev
Summary: A theme engine for GTK+ that makes applications use Qt styles.
URL: http://gtk-qt.ecs.soton.ac.uk
Group: User Interface/Desktops
License: GPL
Vendor: MSP Slackware
Source: http://gtk-qt.ecs.soton.ac.uk/files/0.7/gtk-qt-engine-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: gcc-core, gcc-g++, make >= 3.79.1, qt3, gtk2, cmake, gettext
Requires: qt3, gtk2

%description
Gtk-Qt Theme Engine is a GTK+ theme engine meant for GTK applications running
in KDE. It applies all Qt settings to the GTK application and uses Qt style
plugins directly.


%prep
%setup -q -n %{name}


%build
cmake \
	-DCMAKE_CXX_FLAGS_RELEASE:STRING="$RPM_OPT_FLAGS" \
	-DCMAKE_C_FLAGS_RELEASE:STRING="$RPM_OPT_FLAGS" \
	-DCMAKE_BUILD_TYPE:STRING='Release' \
	-DKDE3_ENABLE_FINAL:BOOL=ON \
	.	
make %{_smp_mflags}


%install
[ "$RPM_BUILD_ROOT" != '/' ] && rm -rf "${RPM_BUILD_ROOT}"
make install DESTDIR="$RPM_BUILD_ROOT"
rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir

%find_lang gtkqtengine


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != '/' ] && rm -rf "${RPM_BUILD_ROOT}"


%files -f gtkqtengine.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog* README NEWS TODO
%{_libdir}/gtk-2.0/2.10.0/engines/libqtengine.la
%{_libdir}/gtk-2.0/2.10.0/engines/libqtengine.so
%{_libdir}/kde3/kcm_kcmgtk.la
%{_libdir}/kde3/kcm_kcmgtk.so
%{_libdir}/menu/kcmgtk.menu
%{_datadir}/applications/kcmgtk-xdg.desktop
%{_datadir}/applnk/Settings/LookNFeel/kcmgtk.desktop
%{_datadir}/gtk-qt-engine/
%{_datadir}/themes/Qt/
