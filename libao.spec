Name: libao
Version: 0.8.8
Release: 2ev
Summary: Cross-Platform Audio Output Library
URL: http://www.xiph.org/
Group: System Environment/Libraries
License: GPL
Vendor: GNyU-Linux
Source: http://www.xiph.org/ao/src/%{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc, alsa-lib

%description
Libao is a cross-platform audio output library.  It currently supports
ESD, aRts, ALSA, OSS, *BSD and Solaris.
This package provides plug-ins for OSS and ALSA (0.9).  You will
need to install the supporting libraries for any plug-ins you want to use
in order for them to work.


%prep
%setup -q


%build
%configure \
	--enable-alsa09 \
	--disable-esd \
	--disable-arts \
	--disable-nas \
	--disable-esd
%{__make} %{?_smp_mlfags}


%install
%{__make} install DESTDIR='%{buildroot}'
rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc %{_datadir}/doc/%{name}-%{version}
%{_includedir}/ao/
%{_libdir}/libao.*
%dir %{_libdir}/ao
%dir %{_libdir}/ao/plugins-2
%{_libdir}/ao/plugins-2/libalsa09.*
%{_libdir}/ao/plugins-2/liboss.*
%{_libdir}/pkgconfig/ao.pc
%doc %{_mandir}/man5/libao.conf.5*
%{_datadir}/aclocal/ao.m4
