Name: arts
Version: 1.5.6
Release: 1ev
Summary: Analogue Realtime Synthesizer - KDE's sound server
URL: http://www.arts-project.org/
Group: Applications/Multimedia
License: LGPL, Artistic
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: http://download.kde.org/stable/3.5.6/src/arts-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: zlib, gcc-core, gcc-g++, make >= 3.79.1, libxml2 >= 2.4.8,
BuildRequires: libstdc++
BuildRequires: glib2 >= 2.4, libxslt >= 1.0.7, libogg, libaudiofile, alsa-lib
Requires: zlib, libxml2 >= 2.4.8, libxslt >= 1.0.7, libogg, glib2 >= 2.4
Requires: libaudiofile, alsa-lib, libstdc++
Provides: libtool(/usr/lib/libartsc.la)
Provides: libtool(/usr/lib/libartscbackend.la)
Provides: libtool(/usr/lib/libartsdsp.la)
Provides: libtool(/usr/lib/libartsdsp_st.la)
Provides: libtool(/usr/lib/libartsflow.la)
Provides: libtool(/usr/lib/libartsflow_idl.la)
Provides: libtool(/usr/lib/libartsgslplayobject.la)
Provides: libtool(/usr/lib/libartswavplayobject.la)
Provides: libtool(/usr/lib/libgmcop.la)
Provides: libtool(/usr/lib/libkmedia2.la)
Provides: libtool(/usr/lib/libkmedia2_idl.la)
Provides: libtool(/usr/lib/libmcop.la)
Provides: libtool(/usr/lib/libmcop_mt.la)
Provides: libtool(/usr/lib/libqtmcop.la)
Provides: libtool(/usr/lib/libsoundserver_idl.la)
Provides: libtool(/usr/lib/libx11globalcomm.la)


%description
aRts simulates a complete "modular analog synthesizer" on your - digital -
computer. Create sounds & music using small modules like oscillators for
creating waveforms, various filters, modules for playing data on your
speakers, mixers, faders,... You can build your complete setup with the GUI of
the system, using the modules - generators, effects and output - connected to
each other.
New synthesis modules can easily be written and integrated in the aRts
system. The artsd sound server mixes audio from several sources in real time,
allowing multiple sound applications to transparently share access to sound
hardware.
Using MCOP, the Multimedia Communication Protocol, multimedia applications
can be network transparent, authenticated for security, and cross-platform
using interfaces defined in a language-independent way using IDL. As a core
component of the KDE 3 desktop environment, aRts provides the basis for the
KDE multimedia. It can also be used independently of KDE (i.e. uses no Qt- or
KDE-libs for most things).


%prep
%setup -q


%build
%configure \
	--with-alsa \
	--with-audiofile \
	--enable-final \
	--enable-pch \
	--disable-warnings \
	--disable-debug
make


%install
make install DESTDIR="$RPM_BUILD_ROOT"
rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-, root, root)
%doc COPYING* doc/{NEWS,README,TODO}
%{_bindir}/artsc-config
%{_bindir}/artscat
%{_bindir}/artsd
%{_bindir}/artsdsp
%{_bindir}/artsplay
%{_bindir}/artsrec
%{_bindir}/artsshell
%{_bindir}/artswrapper
%{_bindir}/mcopidl
%{_includedir}/arts/
%{_includedir}/artsc/
%{_libdir}/libartsc.*
%{_libdir}/libartscbackend.*
%{_libdir}/libartsdsp.*
%{_libdir}/libartsdsp_st.*
%{_libdir}/libartsflow.*
%{_libdir}/libartsflow_idl.*
%{_libdir}/libartsgslplayobject.*
%{_libdir}/libartswavplayobject.*
%{_libdir}/libgmcop.*
%{_libdir}/libkmedia2.*
%{_libdir}/libkmedia2_idl.*
%{_libdir}/libmcop.*
%{_libdir}/libmcop_mt.*
%{_libdir}/libqtmcop.*
%{_libdir}/libsoundserver_idl.*
%{_libdir}/libx11globalcomm.*
%dir %{_libdir}/mcop
%{_libdir}/mcop/Arts/
%{_libdir}/mcop/artsflow.mcopclass
%{_libdir}/mcop/artsflow.mcoptype
%{_libdir}/mcop/kmedia2.mcopclass
%{_libdir}/mcop/kmedia2.mcoptype
%{_libdir}/mcop/soundserver.mcopclass
%{_libdir}/mcop/soundserver.mcoptype
%{_libdir}/mcop/x11globalcomm.mcopclass
%{_libdir}/mcop/x11globalcomm.mcoptype
