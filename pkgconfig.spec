Name: pkg-config
Version: 0.21
Release: 1ev
Summary: A tool that transparently manages compile/link flags
URL: http://pkgconfig.freedesktop.org/wiki/
Group: Development/Tools
License: GPL
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: http://pkgconfig.freedesktop.org/releases/%{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1
BuildRequires: gcc-core

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
make


%install
%makeinstall
mkdir -p ${RPM_BUILD_ROOT}/%{_libdir}/pkgconfig


%clean
rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog* INSTALL README* NEWS
%{_bindir}/pkg-config
%{_mandir}/man1/pkg-config.1.gz
%{_datadir}/aclocal/pkg.m4
%dir %{_libdir}/pkgconfig
