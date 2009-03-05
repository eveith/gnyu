Name: xorg-xf86driproto
%define src_name %(echo %{name} | sed 's,^xorg-,,')
Version: 2.0.4
Release: 2ev
Summary: Protocol information and development headers for X11 DRI extension
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/releases/individual/proto/%{src_name}-%{version}.tar.bz2
BuildRequires: make, pkg-config
Requires: xorg-fslayout
BuildArch: noarch

%description
This package provides the wire protocol for the XFree86-DRI extension, used to organise 
direct rendering support for 3D clients, and help arbiter the requests.


%prep
%setup -q -n '%{src_name}-%{version}'


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

# Make sure %doc files are there, even if they're empty.
touch README COPYING ChangeLog TODO AUTHORS NEWS


%files
%defattr(-, root, root)
%doc README COPYING ChangeLog TODO AUTHORS NEWS
%{_includedir}/X11/dri/xf86dri.h
%{_includedir}/X11/dri/xf86dristr.h
%{_libdir}/pkgconfig/%{src_name}.pc
