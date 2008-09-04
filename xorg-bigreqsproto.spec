Name: xorg-bigreqsproto
%define _src_name %(echo %{name} | sed 's,^xorg-,,')
Version: 1.0.2
Release: 1ev
Summary: Protocol information and development headers for X11 big requests
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/releases/individual/proto/%{_src_name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, pkg-config
Requires: xorg-fslayout
BuildArch: noarch

%description
This package provides the wire protocol for the BIG-REQUESTS extension, used to send larger requests than usual in order to avoid fragmentation.


%prep
%setup -q -n '%{_src_name}-%{version}'


%build
%configure
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'

# Make sure %doc files are there, even if they're empty.
touch README COPYING ChangeLog TODO


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc README COPYING ChangeLog TODO
%{_includedir}/X11/extensions/bigreqstr.h
%{_libdir}/pkgconfig/%{_src_name}.pc
