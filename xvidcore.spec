Name: xvidcore
Version: 1.1.3
Release: 1ev
Summary: A DivX-like MPEG-4 video codec
URL: http://www.xvid.org/
Group: System Environment/Libraries
License: GPL
Vendor: MSP Slackware
Source: http://downloads.xvid.org/downloads/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, nasm

%description
Xvid (formerly "XviD") is a video codec library following the MPEG-4 standard.
Xvid features MPEG-4 Advanced Simple Profile features such as b-frames, global
and quarter pixel motion compensation, lumi masking, trellis quantization, and
H.263, MPEG and custom quantization matrices.
Xvid is a primary competitor of DivX (Xvid being DivX spelled backwards).
While DivX is proprietary software, Xvid is free and open source software and,
unlike DivX, can be used on many different platforms and operating systems.


%prep
%setup -q


%build
pushd 'build/generic'
%configure
make %{_smp_mflags}
popd


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
pushd 'build/generic'
make install DESTDIR="$RPM_BUILD_ROOT"
popd


[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc AUTHORS LICENSE ChangeLog* CodingStyle TODO doc README examples
%{_includedir}/xvid.h
%{_libdir}/libxvidcore*.*
