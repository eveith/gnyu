Name: pkg-config
Version: 0.23
Release: 2ev
Summary: A tool that transparently manages compile/link flags
URL: http://pkgconfig.freedesktop.org/wiki/
Group: Development/Tools
License: GPL
Vendor: GNyU-Linux
Source: http://pkgconfig.freedesktop.org/releases/%{name}-%{version}.tar.gz
BuildRequires: make >= 3.79.1, gcc
Provides: pkgconfig

%description
pkg-config is a helper tool used when compiling applications and libraries. It
helps you insert the correct compiler options on the command line so an
application can use  gcc -o test test.c `pkg-config --libs --cflags glib-2.0`
for instance, rather than hard-coding values on where to find glib (or other
libraries). It is language-agnostic, so it can be used for defining the
location of documentation tools, for instance.
It is often used by source distributions, and many libraries use it. It should
be installed on every system. :-)


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%{__mkdir_p} "${RPM_BUILD_ROOT}/%{_libdir}/pkgconfig"


%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog* INSTALL README* NEWS
%{_bindir}/pkg-config
%doc %{_mandir}/man1/pkg-config.1*
%{_datadir}/aclocal/pkg.m4
%dir %{_libdir}/pkgconfig
