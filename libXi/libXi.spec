Name: libXi
Version: 1.2.1
Release: 3ev
Summary: X Input Extension Library
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
BuildRequires: make, gcc, pkg-config >= 0.9.0
BuildRequires: xorg-xproto, xorg-xextproto, xorg-inputproto >= 1.5
BuildRequires: libXext, libX11

%description
libXi provides an X Window System client interface to the X Input Extension,
an extension to the X protocol. 


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
%doc COPYING README AUTHORS
%{_libdir}/libXi*.*
%{_libdir}/pkgconfig/xi.pc
%doc %{_mandir}/man3/X*.3*
