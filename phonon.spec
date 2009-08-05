Name: phonon
Version: 4.3.0
Release: 2ev
Summary: KDE Multimedia backend
URL: http://phonon.kde.org/
Group: User Interface/Desktops
License: LGPL-2.1
Vendor: GNyU-Linux
Source: ftp://ftp.kde.org/pub/kde/stable/phonon/%{version}/%{name}-%{version}.tar.bz2
BuildRequires: cmake >= 2.4.5, make, gcc-g++, qt4 >= 4.4.0, automoc4 >= 0.9.86
BuildRequires: kdelibs4, xine-lib, gstreamer, glib2, mesalib, pkg-config, libxml2
BuildRequires: libX11, libSM, libICE, libXxf86misc, libXv, libXt
BuildRequires: libXrender, libXScrnSaver, alsa-lib, gst-plugins-base

%description
Phonon is KDE's multimedia backend. It replaces aRts, but also provides an
improved API and the possibility to use different backends, such as Xine or
GStreamer.


%prep
%setup -q


%build
%{cmake} \
	.
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc COPYING.LIB
%{_includedir}/phonon
%{_includedir}/KDE/Phonon
%dir %{_libdir}/kde4/plugins/phonon_backend
%{_libdir}/kde4/plugins/phonon_backend/phonon_xine.so
%{_libdir}/kde4/plugins/phonon_backend/phonon_gstreamer.so
%{_libdir}/libphonon*.so*
%{_libdir}/pkgconfig/phonon.pc
%{_datadir}/dbus-1/interfaces/org.kde.Phonon.AudioOutput.xml
%{_datadir}/icons/oxygen/*/*/*.*
%dir %{_datadir}/kde4/services/phononbackends
%{_datadir}/kde4/services/phononbackends/gstreamer.desktop
%{_datadir}/kde4/services/phononbackends/xine.desktop
