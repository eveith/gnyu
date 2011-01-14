Name: libwmf
Version: 0.2.8.4
Release: 2ev
Summary: A library to read and write WMF files
URL: http://wvware.sourceforge.net
Group: System Environment/Libraries
License: LGPL
Vendor: GNyU-Linux
Source: http://downloads.sourceforge.net/wvware/libwmf-%{version}.tar.gz
BuildRequires: make >= 3.79.1, gcc
BuildRequires: libX11, expat, freetype >= 2.0.0, gtk2
BuildRequires: zlib, libpng, libjpeg, libXpm

%description
libwmf is a library to convert Microsoft's WMF (Windows Metafile) format to
something useful. Bindings exist to convert them to onscreen X graphics, to
the png format, and to fig and eps.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR="${RPM_BUILD_ROOT}"


%post
%{__ldconfig}


%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc AUTHORS COPYING CREDITS ChangeLog* README NEWS TODO
%dir %{_datadir}/doc/libwmf
%doc %{_datadir}/doc/libwmf/*
%{_bindir}/libwmf-config
%{_bindir}/wmf2eps
%{_bindir}/wmf2fig
%{_bindir}/wmf2svg
%{_bindir}/wmf2gd
%{_bindir}/wmf2x
%{_bindir}/libwmf-fontmap
%{_includedir}/libwmf/
%{_libdir}/libwmf*.*
%{_libdir}/gtk-2.0/2.10.0/loaders/io-wmf.*
%{_datadir}/libwmf/
