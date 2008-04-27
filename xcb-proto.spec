Name: xcb-proto
Version: 1.1
Release: 2ev
Summary: XML-XCB protocol descriptions for libxcb
URL: http://xcb.freedesktop.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: ftp://xcb.freedesktop.org/dist/xcb-proto-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: coreutils, gawk, make, gcc, libxml2, pkg-config
BuildArch: noarch
Requires: pkg-config

%description
The xcb-proto package provides the XML-XCB protocol descriptions that libxcb
uses to generate the majority of its code and API. 


%prep
%setup -q


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
%{_libdir}/pkgconfig/xcb-proto.pc
