Name: xorg-xextproto
%define _src_name %(echo %{name} | sed 's,^xorg-,,')
Version: 7.0.2
Release: 1ev
Summary: Protocol information and development headers for various X11 extensions
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
This package provides the wire protocol for various extensions, the 
client-side libraries of which are provided in the Xext library. 


%prep
%setup -q -n '%{_src_name}-%{version}'


%build
%configure
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'

# Make sure %doc files are there, even if they're empty.
touch README COPYING ChangeLog TODO AUTHORS NEWS


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc README COPYING ChangeLog TODO AUTHORS NEWS
%{_includedir}/X11/extensions/MITMisc.h
%{_includedir}/X11/extensions/XEVI.h
%{_includedir}/X11/extensions/XEVIstr.h
%{_includedir}/X11/extensions/XLbx.h
%{_includedir}/X11/extensions/XShm.h
%{_includedir}/X11/extensions/XTest.h
%{_includedir}/X11/extensions/Xag.h
%{_includedir}/X11/extensions/Xagsrv.h
%{_includedir}/X11/extensions/Xagstr.h
%{_includedir}/X11/extensions/Xcup.h
%{_includedir}/X11/extensions/Xcupstr.h
%{_includedir}/X11/extensions/Xdbe.h
%{_includedir}/X11/extensions/Xdbeproto.h
%{_includedir}/X11/extensions/Xext.h
%{_includedir}/X11/extensions/dpms.h
%{_includedir}/X11/extensions/dpmsstr.h
%{_includedir}/X11/extensions/extutil.h
%{_includedir}/X11/extensions/lbxbuf.h
%{_includedir}/X11/extensions/lbxbufstr.h
%{_includedir}/X11/extensions/lbxdeltastr.h
%{_includedir}/X11/extensions/lbximage.h
%{_includedir}/X11/extensions/lbxopts.h
%{_includedir}/X11/extensions/lbxstr.h
%{_includedir}/X11/extensions/lbxzlib.h
%{_includedir}/X11/extensions/mitmiscstr.h
%{_includedir}/X11/extensions/multibuf.h
%{_includedir}/X11/extensions/multibufst.h
%{_includedir}/X11/extensions/security.h
%{_includedir}/X11/extensions/securstr.h
%{_includedir}/X11/extensions/shape.h
%{_includedir}/X11/extensions/shapestr.h
%{_includedir}/X11/extensions/shmstr.h
%{_includedir}/X11/extensions/sync.h
%{_includedir}/X11/extensions/syncstr.h
%{_includedir}/X11/extensions/xtestext1.h
%{_includedir}/X11/extensions/xteststr.h
%{_libdir}/pkgconfig/%{_src_name}.pc
