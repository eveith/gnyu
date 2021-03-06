Name: xorg-xf86vidmodeproto
%define _src_name %(echo %{name} | sed 's,^xorg-,,')
Version: 2.2.2
Release: 1ev
Summary: Protocol information for X11 video mode extension
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
This package provides development headers describing the wire protocol for the
XFree86-VidMode extension, which provides access to detailed timings of video
modes currently in use, and a means to modify them.


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
%{_includedir}/X11/extensions/xf86vmode.h
%{_includedir}/X11/extensions/xf86vmstr.h
%{_libdir}/pkgconfig/%{_src_name}.pc
