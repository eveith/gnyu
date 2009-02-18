Name: xorg-damageproto
%define _src_name %(echo %{name} | %{__sed} 's,^xorg-,,')
Version: 1.1.0
Release: 1ev
Summary: Protocol information and development headers for X damage extension
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/releases/individual/proto/%{_src_name}-%{version}.tar.bz2
BuildRequires: make, gcc, pkg-config
Requires: xorg-fslayout, pkg-config
BuildArch: noarch

%description
This package contains header files and documentation for the X Damage
extension. The damage extension notifies the server when a window is
"damaged", i. e. influenced by another window, allowing only parts of the
window to be redrawn instead of the whole.


%prep
%setup -q -n '%{_src_name}-%{version}'


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%{__rm} -rf '%{buildroot}/%{_datadir}'

# Make sure %doc files are there, even if they're empty.
touch README COPYING ChangeLog TODO AUTHORS NEWS


%files
%defattr(-, root, root)
%doc README COPYING ChangeLog TODO AUTHORS NEWS damageproto.txt
%{_includedir}/X11/extensions/damageproto.h
%{_includedir}/X11/extensions/damagewire.h
%{_libdir}/pkgconfig/%{_src_name}.pc
