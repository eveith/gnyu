Name: libvorbis
Version: 1.1.2
Release: 1ev
Summary: The Vorbis general audio (de-) compression codec
URL: http://www.xiph.org/
Group: System Environment/Libraries
License: BSD
Vendor: GNyU-Linux
Source: http://www.vorbis.com/files/1.0.1/unix/%{name}-%{version}.tar.gz
BuildRequires: make >= 3.79.1, gcc, libogg >= 1.1, pkg-config
Requires: pkg-config

%description
Ogg Vorbis is a fully open, non-proprietary, patent-and-royalty-free,
general-purpose compressed audio format for audio and music at fixed
and variable bitrates from 16 to 128 kbps/channel.


%prep
%setup -q


%build
%configure \
	--enable-static
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR="${RPM_BUILD_ROOT}"


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc AUTHORS COPYING README
%doc doc/*.html
%doc doc/*.png
%doc doc/*.txt
%doc doc/vorbisfile
%doc doc/vorbisenc
%doc %{_datadir}/doc/%{name}-%{version}
%{_datadir}/aclocal/vorbis.m4
%{_includedir}/vorbis/
%{_libdir}/libvorbis.*
%{_libdir}/libvorbisfile.*
%{_libdir}/libvorbisenc.*
%{_libdir}/pkgconfig/vorbis.pc
%{_libdir}/pkgconfig/vorbisfile.pc
%{_libdir}/pkgconfig/vorbisenc.pc
