Name: xorg-randrproto
%define _src_name %(echo %{name} | sed 's,^xorg-,,')
Version: 1.2.1
Release: 1ev
Summary: Protocol information and development headers for X11 RandR extenstion
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
This package provides the wire protocol for the RandR extension, used to 
change display properties such as resolution, rotation, reflection, et al, 
on the fly.


%prep
%setup -q -n '%{_src_name}-%{version}'


%build
%configure
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%{__rm} -rf '%{buildroot}/%{_datadir}'

# Make sure %doc files are there, even if they're empty.
touch README COPYING ChangeLog TODO AUTHORS NEWS


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc README COPYING ChangeLog TODO AUTHORS NEWS randrproto.txt
%{_libdir}/pkgconfig/%{_src_name}.pc
%{_includedir}/X11/extensions/randr.h
%{_includedir}/X11/extensions/randrproto.h
