Name: xorg-applewmproto
%define _src_name %(echo %{name} | %{__sed} 's,^xorg-,,')
Version: 1.1.1
Release: 2ev
Summary: Protocol information and development headers for Apple's WM extension
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/releases/individual/proto/%{_src_name}-%{version}.tar.bz2
BuildRequires: make, gcc, pkg-config
Requires: xorg-fslayout, pkg-config
BuildArch: noarch

%description
Contains headers for Apple's window manager extension API.


%prep
%setup -q -n '%{_src_name}-%{version}'


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

# Make sure %doc files are there, even if they're empty.
touch README COPYING ChangeLog TODO


%files
%defattr(-, root, root)
%doc README COPYING ChangeLog TODO
%{_includedir}/X11/extensions/applewm.h
%{_includedir}/X11/extensions/applewmstr.h
%{_libdir}/pkgconfig/%{_src_name}.pc
