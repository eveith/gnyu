Name: xcb-proto
Version: 1.4
Release: 4ev
Summary: XML-XCB protocol descriptions for libxcb
URL: http://xcb.freedesktop.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: ftp://xcb.freedesktop.org/dist/xcb-proto-%{version}.tar.bz2
BuildRequires: make, python >= 2.5, libxml2, pkg-config
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
%{__make} install DESTDIR='%{buildroot}'


%files
%defattr(-, root, root)
%doc README COPYING*
%{_libdir}/pkgconfig/xcb-proto.pc
%{_libdir}/python*.*/site-packages/xcbgen/
%dir %{_datadir}/xcb
%{_datadir}/xcb/*.x[sm][dl]
