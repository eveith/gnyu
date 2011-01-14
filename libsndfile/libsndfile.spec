Name: libsndfile
Version: 1.0.17
Release: 1ev
Summary: A library for reading and writing sound files
URL: http://www.mega-nerd.com/libsndfile/
Group: System Environment/Libraries
License: LGPL
Vendor: GNyU-Linux
Source: http://www.mega-nerd.com/%{name}/%{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: coreutils, grep, sed, make >= 3.79.1, gcc, alsa-lib, sqlite

%description
libsndfile is a C library for reading and writing sound files such as AIFF,
AU, WAV, and others through one standard interface. It can currently
read/write 8, 16, 24 and 32-bit PCM files as well as 32 and 64-bit floating
point WAV files and a number of compressed formats. It compiles and runs on
*nix, MacOS, and Win32.


%prep
%setup -q


%build
export LDFLAGS=-ldl
%configure
%{__make} %{?_smp_mflags}


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
%doc AUTHORS COPYING ChangeLog* README NEWS TODO
%doc %{_datadir}/doc/%{name}1-dev
%{_bindir}/sndfile-convert
%{_bindir}/sndfile-info
%{_bindir}/sndfile-play
%{_bindir}/sndfile-regtest
%{_includedir}/sndfile.h
%{_includedir}/sndfile.hh
%{_libdir}/libsndfile.*
%{_libdir}/pkgconfig/sndfile.pc
%doc %{_mandir}/man1/sndfile-convert.1*
%doc %{_mandir}/man1/sndfile-info.1*
%doc %{_mandir}/man1/sndfile-play.1*
%{_datadir}/octave/
