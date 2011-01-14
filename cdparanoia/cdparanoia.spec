Name: cdparanoia
%define ver 9.8
Version: alpha%{ver}
Release: 2ev
Summary: A CD ripping application
URL: http://www.xiph.org/paranoia/
Group: Applications/Multimedia
License: GPL-2
Vendor: GNyU-Linux
Source: http://downloads.xiph.org/releases/%{name}/%{name}-III-%{version}.src.tgz
Patch0: cdparanoia-III-alpha9.8.nostrip.patch
Patch1: cdparanoia-III-alpha9.8.labels.patch
Patch2: cdparanoia-III-alpha9.8.O_EXCL.patch
Patch3: cdparanoia-III-alpha9.8.cflags.patch
Patch4: cdparanoia-III-alpha9.8.sgio.patch
Patch5: cdparanoia-III-alpha9.8.verbose.patch
Patch6: cdparanoia-III-alpha9.8.louder.patch
Patch7: cdparanoia-III-alpha9.8.verbosity3.patch
Patch8: cdparanoia-III-alpha9.8.env.patch
Patch9: cdparanoia-III-alpha9.8.smalldma.patch
Patch10: cdparanoia-III-alpha9.8.lm.patch
BuildRequires: make >= 3.79.1, gcc

%description
cdparanoia reads audio from the CDROM directly as data, with no analog step
between, and writes the data to a file or pipe in WAV, AIFC or raw 16 bit
linear PCM. Cdparanoia will read correct, rock-solid audio data from
inexpensive drives prone to misalignment, frame jitter and loss of streaming
during atomic reads. cdparanoia will also read and repair data from CDs that
have been damaged in some way.


%prep
%setup -q -n %{name}-III-%{version}
%patch4 -p1 -b .sgio
%patch0 -p1 -b .nostrip
%patch1 -p1 -b .labels
%patch2 -p1 -b .O_EXCL
%patch3 -p1 -b .cflags
%patch5 -p1 -b .verbose
%patch6 -p1 -b .louder
%patch7 -p1 -b .verbosity3
%patch8 -p1 -b .env
%patch9 -p1 -b .smalldma
%patch10 -p1 -b .lm


%build
%configure \
	--includedir='%{_includedir}/cdda'
%{__make} %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"


%install
%{__install} -d "${RPM_BUILD_ROOT}/%{_bindir}"
%{__install} -d "${RPM_BUILD_ROOT}/%{_includedir}/cdda"
%{__install} -d "${RPM_BUILD_ROOT}/%{_libdir}"
%{__install} -d "${RPM_BUILD_ROOT}/%{_mandir}/man1"
%{__install} -m 0755 cdparanoia "${RPM_BUILD_ROOT}/%{_bindir}"
%{__install} -m 0644 cdparanoia.1 "${RPM_BUILD_ROOT}/%{_mandir}/man1"
%{__install} -m 0644 utils.h paranoia/cdda_paranoia.h \
	interface/cdda_interface.h \
    "${RPM_BUILD_ROOT}/%{_includedir}/cdda"
%{__install} -m 0755 "paranoia/libcdda_paranoia.so.0.%{ver}" \
    "interface/libcdda_interface.so.0.%{ver}" \
    "${RPM_BUILD_ROOT}/%{_libdir}"
%{__install} -m 0755 paranoia/libcdda_paranoia.a interface/libcdda_interface.a \
    "${RPM_BUILD_ROOT}/%{_libdir}"

%{__ldconfig} -n "$RPM_BUILD_ROOT/%{_libdir}"

pushd "$RPM_BUILD_ROOT/%{_libdir}"
%{__ln_s} "libcdda_paranoia.so.0.%{ver}" libcdda_paranoia.so
%{__ln_s} "libcdda_interface.so.0.%{ver}" libcdda_interface.so
popd


%post
%{__ldconfig}


%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc FAQ* GPL README
%{_bindir}/cdparanoia
%doc %{_mandir}/man1/cdparanoia.1*
%{_libdir}/libcdda_*.*
%dir %{_includedir}/cdda
%{_includedir}/cdda/*.h
