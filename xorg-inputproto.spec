Name: xorg-inputproto
%define _src_name %(echo %{name} | sed 's,^xorg-,,')
Version: 1.4.2.1
Release: 1ev
Summary: Protocol information and development headers for X11 input extension 
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
This package provides development headers describing the wire protocol for 
the Input extension, used to control all manner of options related to input 
device handling.


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
%{_includedir}/X11/extensions/XI.h
%{_includedir}/X11/extensions/XInput.h
%{_includedir}/X11/extensions/XIproto.h
%{_libdir}/pkgconfig/%{_src_name}.pc
