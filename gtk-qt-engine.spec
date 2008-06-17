Name: gtk-qt-engine
Version: 0.8
Release: 3ev
Summary: A theme engine for GTK+ that makes applications use Qt styles
URL: http://gtk-qt.ecs.soton.ac.uk
Group: User Interface/Desktops
License: GPL
Vendor: GNyU-Linux
Source: http://gtk-qt.ecs.soton.ac.uk/files/0.7/gtk-qt-engine-%{version}.tar.bz2
Patch: %{name}-flashplugin.patch
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: gcc, gcc-g++, make >= 3.79.1, qt3, gtk2, cmake >= 2.4, gettext
BuildRequires: libX11, libICE, libXext, libSM, coreutils, grep, sed

%description
Gtk-Qt Theme Engine is a GTK+ theme engine meant for GTK applications running
in KDE. It applies all Qt settings to the GTK application and uses Qt style
plugins directly.


%prep
%setup -q -n %{name}
%patch0 -p1


%build
cmake \
	-DCMAKE_INSTALL_PREFIX:PATH='%{_prefix}' \
	-DCMAKE_CXX_FLAGS_RELEASE:STRING="$RPM_OPT_FLAGS" \
	-DCMAKE_C_FLAGS_RELEASE:STRING="$RPM_OPT_FLAGS" \
	-DCMAKE_BUILD_TYPE:STRING='Release' \
	.	
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%find_lang gtkqtengine


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files -f gtkqtengine.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog* README NEWS TODO
%{_libdir}/gtk-2.0/2.10.0/engines/libqtengine.so
%{_libdir}/kde3/kcm_kcmgtk.la
%{_libdir}/kde3/kcm_kcmgtk.so
%{_datadir}/applications/kcmgtk.desktop
%{_datadir}/themes/Qt/
