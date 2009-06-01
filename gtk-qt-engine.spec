Name: gtk-qt-engine
Version: 1.1svn20090601
Release: 6ev
Summary: A theme engine for GTK+ that makes applications use Qt styles
URL: http://gtk-qt.ecs.soton.ac.uk
Group: User Interface/Desktops
License: GPL-2
Vendor: GNyU-Linux
Source: http://gtk-qt-engine.googlecode.com/files/gtk-qt-engine-%{version}.tar.bz2
BuildRequires: gcc, gcc-g++, make >= 3.79.1, pkg-config, gettext
BuildRequires: gtk2
BuildRequires: automoc4, phonon >= 4.3.0, qt4, kdelibs4, kdebase4-runtime

%description
Gtk-Qt Theme Engine is a GTK+ theme engine meant for GTK applications running
in KDE. It applies all Qt settings to the GTK application and uses Qt style
plugins directly.


%prep
	%setup -q


%build
	%{cmake} \
		-DQT_QMAKE_EXECUTABLE:FILEPATH='%{_libdir}/qt4/bin/qmake' \
		.
	%{__make} %{?_smp_mflags}


%install
	%{__make} install DESTDIR='%{buildroot}'
	%find_lang gtkqtengine


%post
	%{__ldconfig}


%postun
	%{__ldconfig}


%files -f gtkqtengine.lang
	%defattr(-, root, root)
	%doc AUTHORS COPYING ChangeLog*
	%{_libdir}/gtk-?.?/*/engines/libqt4engine.so
	%{_libdir}/kde4/kcm_gtk4.so
	%{_datadir}/applications/kde4/kcmgtk4.desktop
	%{_datadir}/icons/kcmgtk.png
	%{_datadir}/themes/Qt4/
