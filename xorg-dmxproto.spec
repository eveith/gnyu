Name: xorg-dmxproto
%define _src_name %(echo %{name} | sed 's,^xorg-,,')
Version: 2.2.2
Release: 1ev
Summary: Protocol information and development headers for X11 DMX extension
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/releases/individual/proto/%{_src_name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, pkg-config
Requires: x11-proto
BuildArch: noarch

%description
DMX is short for "Distributed Multihead X", meaning an X-Server distributing
more than one screen. This package contains protocol information and header
files for that extension.


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
%{_includedir}/X11/extensions/dmxext.h
%{_includedir}/X11/extensions/dmxproto.h
%{_libdir}/pkgconfig/%{_src_name}.pc
