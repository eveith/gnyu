Name: xorg-xf86driproto
%define _src_name %(echo %{name} | sed 's,^xorg-,,')
Version: 2.0.3
Release: 1ev
Summary: Protocol information and development headers for X11 DRI extension
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/releases/individual/proto/%{_src_name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, pkg-config
Requires: xorg-proto
BuildArch: noarch

%description
This package provides the wire protocol for the XFree86-DRI extension, used to organise 
direct rendering support for 3D clients, and help arbiter the requests.


%prep
%setup -q -n '%{_src_name}-%{version}'


%build
%configure
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'

# Make sure %doc files are there, even if they're empty.
touch README COPYING ChangeLog TODO AUTHORS NEWS


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc README COPYING ChangeLog TODO AUTHORS NEWS
%{_includedir}/GL/internal/dri_interface.h
%{_includedir}/X11/dri/xf86dri.h
%{_includedir}/X11/dri/xf86dristr.h
%{_libdir}/pkgconfig/%{_src_name}.pc
