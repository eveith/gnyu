Name: compositeproto
Version: 0.4
Release: 1ev
Summary: Protocol information and development headers for X composite
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
This package contains header files and documentation for the composite
extension.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%{__rm} -rf '%{buildroot}/%{_datadir}'

# Make sure %doc files are there, even if they're empty.
touch README COPYING ChangeLog TODO NEWS AUTHORS


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc README COPYING ChangeLog TODO NEWS AUTHORS compositeproto.txt
%{_includedir}/X11/extensions/composite.h
%{_includedir}/X11/extensions/compositeproto.h
%{_libdir}/pkgconfig/%{name}.pc
