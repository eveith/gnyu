Name: xorg-inputproto
%define src_name %(echo %{name} | sed 's,^xorg-,,')
Version: 1.5.0
Release: 2ev
Summary: Protocol information and development headers for X11 input extension 
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/releases/individual/proto/%{src_name}-%{version}.tar.bz2
BuildRequires: make, pkg-config
Requires: xorg-fslayout
BuildArch: noarch

%description
This package provides development headers describing the wire protocol for 
the Input extension, used to control all manner of options related to input 
device handling.


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
%{_includedir}/X11/extensions/XI.h
%{_includedir}/X11/extensions/XInput.h
%{_includedir}/X11/extensions/XIproto.h
%{_libdir}/pkgconfig/%{src_name}.pc
