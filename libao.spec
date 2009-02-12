Name: libao
Version: 0.8.6
Release: 1ev
Summary: Cross-Platform Audio Output Library
URL: http://www.xiph.org/
Group: System Environment/Libraries
License: GPL
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: http://www.xiph.org/ao/src/%{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc-core, alsa-lib, arts, perl
Requires: alsa-lib, arts

%description
Libao is a cross-platform audio output library.  It currently supports
ESD, aRts, ALSA, OSS, *BSD and Solaris.
This package provides plug-ins for OSS, ESD, aRts, and ALSA (0.9).  You will
need to install the supporting libraries for any plug-ins you want to use
in order for them to work.


%prep
%setup -q
perl -p -i -e "s/-O20/$RPM_OPT_FLAGS/" configure
perl -p -i -e "s/-ffast-math//" configure


%build
%configure --enable-arts --enable-alsa09 --disable-alsa --disable-esd


%install
%makeinstall
rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-, root, root)
%doc %{_datadir}/doc/%{name}-%{version}
%{_includedir}/ao.h
%{_includedir}/os_types.h
%{_includedir}/plugin.h
%{_libdir}/libalsa09.*
%{_libdir}/libao.*
%{_libdir}/libarts.*
%{_libdir}/liboss.*
%{_libdir}/pkgconfig/ao.pc
%{_mandir}/man5/libao.conf.5*
%{_datadir}/aclocal/ao.m4
