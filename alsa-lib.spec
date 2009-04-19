Name: alsa-lib
Version: 1.0.19
Release: 4ev
Summary: Library for userspace access to the Advanced Linux Sound System
URL: http://www.alsa-project.org/
Group: System Environment/Libraries
License: LGPL-2
Vendor: GNyU-Linux
Source: ftp://ftp.alsa-project.org/pub/lib/%{name}-%{version}.tar.bz2
Patch0: %{name}-1.0.17-pcm-rewind-forward.patch
Patch1: %{name}-1.0.17-pcm-rewind-forward-return.patch
Patch2: %{name}-1.0.17-sframe-type.patch
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
	%{__make} install DESTDIR='%{buildroot}'
	%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/alsa'


%post
	%{__ldconfig}


%postun
	%{__ldconfig}


%files
	%defattr(-, root, root)
	%doc COPYING ChangeLog MEMORY-LEAK NOTES TODO doc/asoundrc.txt
	%doc doc/pictures/ doc/doxygen/
	%dir %{_sysconfdir}/alsa
	%{_bindir}/aserver
	%{_includedir}/alsa/
	%{_includedir}/sys/asoundlib.h
	%{_libdir}/alsa-lib/
	%{_libdir}/libasound.*
	%{_libdir}/pkgconfig/alsa.pc
	%{_datadir}/aclocal/alsa.m4
	%{_datadir}/alsa/
