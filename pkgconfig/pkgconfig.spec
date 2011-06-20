Name: pkg-config
Version: 0.26
Release: 1.0
Summary: A tool that transparently manages compile/link flags
URL: http://pkgconfig.freedesktop.org/wiki
Group: Development/Tools
License: GPL
Source: http://pkgconfig.freedesktop.org/releases/%{name}-%{version}.tar.gz
BuildRequires: grep, sed, make >= 3.79.1, gcc
BuildRequires: pkg-config
BuildRequires: eglibc-devel
BuildRequires: glib-devel >= 2.0, popt-devel
Provides: pkgconfig = %{version}-%{release}

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
%configure \
    --with-installed-popt
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

for i in '%{_libdir}' '%{_datadir}'; do
    %{__mkdir_p} "%{buildroot}${i}/pkgconfig"
done

%{__rm_rf} '%{buildroot}%{_datadir}/doc'


%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog* INSTALL README* NEWS
%doc pkg-config-guide.html

%{_bindir}/pkg-config

%doc %{_mandir}/man1/pkg-config.1*

%{_datadir}/aclocal/pkg.m4

%dir %{_libdir}/pkgconfig
%dir %{_datadir}/pkgconfig
