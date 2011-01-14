Name: qimageblitz
Version: 0.0.4
Release: 1ev
Summary: A graphical effect and filter library for Qt/KDE 4
URL: http://qimageblitz.sourceforge.net/
Group: System Environment/Libraries
License: BSD
Vendor: GNyU-Linux
Source: http://downloads.sourceforge.net/qimageblitz/qimageblitz-%{version}.tar.bz2
BuildRequires: cmake >= 2.4.5, make, gcc-g++, qt4, libX11, libICE, libXext
BuildRequires: pkg-config

%description
Blitz is a graphical effect and filter library for KDE4.0 that contains many 
improvements over KDE 3.x's kdefx library including bugfixes, memory and speed 
improvements, and MMX/SSE support. 


%prep
%setup -q


%build
%{cmake} \
	-DQT_QMAKE_EXECUTABLE:FILEPATH='%{_libdir}/qt4/bin/qmake' \
	.
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc README* COPYING
%{_bindir}/blitztest
%{_includedir}/qimageblitz/
%{_libdir}/libqimageblitz.*
%{_libdir}/pkgconfig/qimageblitz.pc
