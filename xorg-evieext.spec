Name: xorg-evieext
%define src_name %(echo %{name} | sed 's,^xorg-,,')
Version: 1.0.2
Release: 2ev
Summary: Protocol information and development headers for X11 EvIE extension
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/releases/individual/proto/%{src_name}-%{version}.tar.bz2
BuildRequires: make, pkg-config
Requires: xorg-fslayout
BuildArch: noarch

%description
This package provides the wire protocol for the EvIE extension, used to let 
arbitrary clients receive, filter, and potentially modify all events. 
More information about X.Org can be found at: 
<URL:http://xorg.freedesktop.org> 
<URL:http://lists.freedesktop.org/mailman/listinfo/xorg>


%prep
%setup -q -n '%{src_name}-%{version}'


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

# Make sure %doc files are there, even if they're empty.
touch README COPYING ChangeLog TODO AUTHORS NEWS


%files
%defattr(-, root, root)
%doc README COPYING ChangeLog TODO AUTHORS NEWS
%{_includedir}/X11/extensions/Xeviestr.h
%{_libdir}/pkgconfig/evieproto.pc
