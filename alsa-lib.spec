Name: alsa-lib
Version: 1.0.14a
Release: 1ev
Summary: Library for userspace access to the Advanced Linux Sound System
URL: http://www.alsa-project.org/
Group: System Environment/Libraries
License: LGPL
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: ftp://ftp.alsa-project.org/pub/lib/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc-core, doxygen
Provides: libtool(%{_libdir}/libasound.la)
Provides: libtool(%{_libdir}/alsa-lib/smixer/smixer-ac97.la)
Provides: libtool(%{_libdir}/alsa-lib/smixer/smixer-hda.la)
Provides: libtool(%{_libdir}/alsa-lib/smixer/smixer-sbase.la)

%description
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system. This the userspace library that
simplifies programing and provides higher level functionality.


%prep
%setup -q


%build
%configure
make %{_smp_mflags}
make doc


%install
[ "$RPM_BUILD_ROOT" != '/' ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"
rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != '/' ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc COPYING ChangeLog MEMORY-LEAK NOTES TODO doc/asoundrc.txt
%doc doc/pictures/ doc/doxygen/
%{_bindir}/aserver
%{_includedir}/alsa/
%{_includedir}/sys/asoundlib.h
%{_libdir}/alsa-lib/
%{_libdir}/libasound.*
%{_libdir}/pkgconfig/alsa.pc
%{_datadir}/aclocal/alsa.m4
%{_datadir}/alsa/
