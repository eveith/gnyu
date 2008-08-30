Name: xorg-xcb-proto
%define _src_name %(echo %{name} | sed 's,^xorg-,,')
Version: 1.1
Release: 3ev
Summary: XML-XCB protocol descriptions for libxcb
URL: http://xcb.freedesktop.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: ftp://xcb.freedesktop.org/dist/xcb-proto-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, libxml2, pkg-config
BuildArch: noarch
Requires: pkg-config

%description
The xcb-proto package provides the XML-XCB protocol descriptions that libxcb
uses to generate the majority of its code and API. 


%prep
%setup -q -n '%{_src_name}-%{version}'


%build
%configure
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc README COPYING*
%{_datadir}/xcb/
%{_libdir}/pkgconfig/%{_src_name}.pc
