Name: libXcomposite
Version: 0.4.0
Release: 2ev
Summary: X Composite Extension library
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: MSP Slackware
Source: http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: coreutils, grep, sed, make, gcc-core, pkg-config
BuildRequires: libX11, libXext, libXfixes

%description
The composite extension provides several related mechanisms:

Per-hierarchy storage
The rendering of an entire hierarchy of windows is redirected to
off-screen storage. The pixels of that hierarchy are available
whenever it is viewable. Storage is automatically reallocated
when the top level window changes size. Contents beyond the
geometry of the top window are not preserved.

Automatic shadow update
When a hierarchy is rendered off-screen, the X server provides
an automatic mechanism for presenting those contents within the
parent window. The implementation is free to make this update
lag behind actual rendering operations by an unspecified amount
of time. This automatic update mechanism may be disabled so that
the parent window contents can be completely determined by an
external application.

Composite Overlay Window
Version 0.3 of the protocol adds the Composite Overlay Window,
which provides compositing managers with a surface on which to
draw without interference. This window is always above normal
windows and is always below the screen saver window. It is an
InputOutput window whose width and height are the screen
dimensions. Its visual is the root visual and its border width
is zero. Attempts to redirect it using the composite extension
are ignored. This window does not appear in the reply of the
QueryTree request. It is also an override redirect window. These
last two features make it invisible to window managers and other
X11 clients. The only way to access the XID of this window is
via the CompositeGetOverlayWindow request. Initially, the
Composite Overlay Window is unmapped.

Per-hierarchy storage may be created for individual windows or for all
children of a window. Manual shadow update may be selected by only a
single application for each window; manual update may also be selected
on a per-window basis or for each child of a window. Detecting when to
update may be done with the Damage extension.
The off-screen storage includes the window contents, its borders and
the contents of all descendants.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc COPYING README AUTHORS
%{_includedir}/X11/extensions/Xcomposite.h
%{_libdir}/libXcomposite*.*
%{_libdir}/pkgconfig/xcomposite.pc
%{_mandir}/man3/X?omposite*.3*
