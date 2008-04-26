Name: libX11
Version: 1.1.4
Release: 2ev
Summary: X11 client-side library
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: MSP Slackware
Source: http://xorg.freedesktop.org/releases/individual/lib/libX11-%{version}.tar.bz2
Patch: %{name}-1.1.2-badargs-1.patch
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: coreutils, grep, sed, make, gcc, pkg-config
BuildRequires: x11-proto, libxcb, xtrans

%description
This package provides the main client interface to the X Window System, 
and is otherwise known as 'Xlib'. It provides a complete API for the basic 
functions of the window system. 


%prep
%setup -q
%{__sed} -i 's/_XGet/XGet/' modules/im/ximcp/imDefLkup.c


%build
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
%doc COPYING README AUTHORS
%{_includedir}/X11/*.h
%{_libdir}/libX11*.*
%dir %{_libdir}/X11
%{_libdir}/X11/Xcms.txt
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*.3*
%{_datadir}/X11/
