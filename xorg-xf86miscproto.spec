Name: xorg-xf86miscproto
%define _src_name %(echo %{name} | sed 's,^xorg-,,')
Version: 0.9.2
Release: 1ev
Summary: Protocol information for X11 XFree86-Miscellaneous
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
This package provides the wire protocol for the XFree86-Misc extension, which provides 
a means to access input device configuration settings specific to the XFree86/Xorg DDX.


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
%{_includedir}/X11/extensions/xf86misc.h
%{_includedir}/X11/extensions/xf86mscstr.h
%{_libdir}/pkgconfig/%{_src_name}.pc
