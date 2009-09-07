Name: xvidcore
Version: 1.2.2
Release: 2ev
Summary: A DivX-like MPEG-4 video codec
URL: http://www.xvid.org/
Group: System Environment/Libraries
License: GPL-2
Vendor: GNyU-Linux
Source: http://downloads.xvid.org/downloads/%{name}-%{version}.tar.bz2
BuildRequires: make, gcc, nasm
Provides: xvid = %{version}-%{release}

%description
Xvid (formerly "XviD") is a video codec library following the MPEG-4 standard.
Xvid features MPEG-4 Advanced Simple Profile features such as b-frames, global
and quarter pixel motion compensation, lumi masking, trellis quantization, and
H.263, MPEG and custom quantization matrices.
Xvid is a primary competitor of DivX (Xvid being DivX spelled backwards).
While DivX is proprietary software, Xvid is free and open source software and,
unlike DivX, can be used on many different platforms and operating systems.


%prep
%setup -q -n '%{name}'


%build
pushd 'build/generic'
%configure
%{__make} %{?_smp_mflags}
popd


%install
pushd 'build/generic'
%{__make} install DESTDIR="${RPM_BUILD_ROOT}"
popd


%post
%{__ldconfig}


%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc AUTHORS LICENSE ChangeLog* CodingStyle TODO doc README examples
%{_includedir}/xvid.h
%{_libdir}/libxvidcore*.*
