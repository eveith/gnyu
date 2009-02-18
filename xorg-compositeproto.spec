Name: xorg-compositeproto
%define _src_name %(echo %{name} | %{__sed} 's,^xorg-,,')
Version: 0.4
Release: 1ev
Summary: Protocol information and development headers for X composite
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/releases/individual/proto/%{_src_name}-%{version}.tar.bz2
BuildRequires: make, gcc, pkg-config
Requires: xorg-fslayout, pkg-config
BuildArch: noarch

%description
This package contains header files and documentation for the composite
extension.


%prep
%setup -q -n '%{_src_name}-%{version}'


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%{__rm} -rf '%{buildroot}/%{_datadir}'

# Make sure %doc files are there, even if they're empty.
touch README COPYING ChangeLog TODO NEWS AUTHORS


%files
%defattr(-, root, root)
%doc README COPYING ChangeLog TODO NEWS AUTHORS compositeproto.txt
%{_includedir}/X11/extensions/composite.h
%{_includedir}/X11/extensions/compositeproto.h
%{_libdir}/pkgconfig/%{_src_name}.pc
