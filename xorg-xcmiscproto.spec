Name: xorg-xcmiscproto
%define _src_name %(echo %{name} | sed 's,^xorg-,,')
Version: 1.1.2
Release: 1ev
Summary: Protocol information and for X11 XC-Miscellaneous extension
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
This package provides the wire protocol for the XC-MISC extension, used to 
get details of XID allocation within the server.


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
%{_includedir}/X11/extensions/xcmiscstr.h
%{_libdir}/pkgconfig/%{_src_name}.pc
