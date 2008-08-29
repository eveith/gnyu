Name: applewmproto
Version: 1.0.3
Release: 1ev
Summary: Protocol information and development headers for Apple's WM extension
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/releases/individual/proto/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, pkg-config
Requires: x11-proto
BuildArch: noarch

%description
Contains headers for Apple's window manager extension API.


%prep
%setup -q


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
%{_includedir}/X11/extensions/applewm.h
%{_includedir}/X11/extensions/applewmstr.h
%{_libdir}/pkgconfig/%{name}.pc
