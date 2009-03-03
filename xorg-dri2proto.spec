Name: xorg-dri2proto
%define src_name %(echo %{name} | sed 's,^xorg-,,')
Version: 1.1
Release: 1ev
Summary: Protocol information and development headers for DRI2 extension
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/releases/individual/proto/%{src_name}-%{version}.tar.bz2
BuildRequires: make, pkg-config
Requires: xorg-fslayout
BuildArch: noarch

%description
The DRI2 extension is designed to associate and access auxillary
rendering buffers with an X drawable.
DRI2 is a essentially a helper extension to support implementation of
direct rendering drivers/libraries/technologies.
The main consumer of this extension will be a direct rendering OpenGL
driver, but the DRI2 extension is not designed to be OpenGL specific.
Direct rendering implementations of OpenVG, Xv, cairo and other
graphics APIs should find the functionality exposed by this extension
helpful and hopefully sufficient.


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
%{_includedir}/X11/extensions/dri2proto.h
%{_libdir}/pkgconfig/%{src_name}.pc
