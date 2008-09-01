Name: xorg-renderproto
%define _src_name %(echo %{name} | sed 's,^xorg-,,')
Version: 0.9.3
Release: 1ev
Summary: Protocol information and development headers for X11 render extension
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
This package provides the wire protocol for the Render extension, used to 
implement Porter-Duff operations within X.


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
%doc README COPYING ChangeLog TODO AUTHORS NEWS renderproto.txt
%{_includedir}/X11/extensions/render.h
%{_includedir}/X11/extensions/renderproto.h
%{_libdir}/pkgconfig/%{_src_name}.pc
