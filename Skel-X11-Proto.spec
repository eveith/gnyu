Name: xorg-Xproto
%define src_name %(echo %{name} | sed 's,^xorg-,,')
Version:
Release: 1ev
Summary: Protocol information and development headers for 
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/releases/individual/proto/%{src_name}-%{version}.tar.bz2
BuildRequires: make, pkg-config
Requires: xorg-fslayout
BuildArch: noarch

%description


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
%{_libdir}/pkgconfig/%{src_name}.pc
