Name: libxklavier
Version: 3.8
Release: 1ev
Summary: A high-level API for the X Keyboard Extension
URL: http://freedesktop.org/wiki/Software/LibXklavier
Group: User Interface/X
License: LGPL-2
Vendor: GNyU-Linux
Source: http://downloads.sourceforge.net/gswitchit/libxklavier-%{version}.tar.bz2
BuildRequires: make, gcc, pkg-config, libICE, libXi, libxkbfile, x11-apps
BuildRequires: glib2, libxml2, iso-codes

%description
libxklavier is a library providing high-level API for X Keyboard Extension known as 
XKB. This library is indended to support XFree86 and other commercial X servers. 
It is useful for creating XKB-related software (layout indicators etc). 
The current features are:
- Reading XKB configuration registry information (for XFree86) 
- Configuring XKB 
- Application-defined callbacks for many XKB-related events 
- Support for per-window switching etc.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc NEWS README COPYING* CREDITS ChangeLog
%doc %{_datadir}/gtk-doc/html/libxklavier
%{_includedir}/libxklavier/
%{_libdir}/libxklavier.*
%{_libdir}/pkgconfig/libxklavier.pc
