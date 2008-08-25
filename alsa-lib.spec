Name: alsa-lib
Version: 1.0.17a
Release: 3ev
Summary: Library for userspace access to the Advanced Linux Sound System
URL: http://www.alsa-project.org/
Group: System Environment/Libraries
License: LGPL-2
Vendor: GNyU-Linux
Source: ftp://ftp.alsa-project.org/pub/lib/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc, doxygen, pkg-config

%description
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system. This the userspace library that
simplifies programing and provides higher level functionality.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}
%{__make} doc


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


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
