Name: k3b
Version: 1.0.5
Release: 1ev
Summary: A CD/DVD burning frontend for KDE
URL: http://www.k3b.org/
License: GPL-2
Group: User Interface/Desktops
Source: http://prdownloads.sourceforge.net/k3b/k3b-%{version}.tar.bz2
BuildRequires: coreutils, grep, sed, make, gcc-g++, gettext
BuildRequires: qt3, kdelibs >= 3.2, kdebase >= 3.2, hal, dbus, dbus-qt3-old
BuildRequires: alsa-lib, lame, libogg, libvorbis, libsndfile, ffmpeg, libmad
BuildRequires: libflac
Requires: cdrkit, dvd+rw-tools, cdrdao, normalize, sox, hal
BuildRoot: %{_tmppath}/%{name}-root

%description
K3b was created to be a feature-rich and easy to handle CD burning application. 
It consists of basicly three parts: 
 - The projects:
    Projects are created from the file menu and then filled with data to burn.
 - The Tools:
   The tools menu offers different tools like CD copy or DVD formatting.
 - Context sensitive media actions:
   When clicking on the Icon representing a CD/DVD drive K3b will present it's 
   contents and allow some further action. This is for example the way to rip 
   audio CDs.

%prep
%setup -q


%build
%configure \
	--disable-debug \
	--disable-warnings \
	--with-docdir=%{_docdir}/%{name}-%{version}
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR="${RPM_BUILD_ROOT}"


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc README AUTHORS FAQ KNOWNBUGS PERMISSIONS TODO ChangeLog
%doc %{_datadir}/doc/HTML/en/k3b/
%{_datadir}/apps/k3b/
%{_datadir}/apps/konqueror/servicemenus/k3b_*.desktop
%{_datadir}/apps/konqsidebartng/virtual_folders/services/videodvd.desktop
%{_datadir}/icons/hicolor/*/apps/k3b.png
%{_datadir}/mimelnk/application/x-k3b.desktop
%{_datadir}/sounds/k3b_*.wav
%{_datadir}/applnk/.hidden/k3b-*.desktop
%{_datadir}/applnk/Settings/System/k3bsetup2.desktop
%{_datadir}/applications/kde/k3b.desktop
%{_datadir}/services/kfile_k3b.desktop
%{_datadir}/services/videodvd.protocol
%{_libdir}/libk3b*.*
%{_libdir}/kde3/libk3b*.*
%{_libdir}/kde3/kcm_k3bsetup2.*
%{_libdir}/kde3/kfile_k3b.*
%{_libdir}/kde3/kio_videodvd.*
%{_includedir}/k3b*.h
%{_includedir}/kcutlabel.h
%{_bindir}/k3b
%{_bindir}/k3bsetup
