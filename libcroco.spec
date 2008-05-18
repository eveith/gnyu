Name: libcroco
Version: 0.6.1
Release: 2ev
Summary: A CSS parsing and manipulation library 
URL: http://www.freespiders.org/projects/libcroco/
Group: System Environment/Libraries
License: LGPL
Vendor: GNyU-Linux
Source: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/0.6/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: coreutils, grep, sed, make >= 3.79.1, gcc, glib2, libxml2

%description
Libcroco is a general CSS parsing and manipulation library written in C for
the GNOME project. It provides a CSS2 parser (SAC and CSSOM API), and a CSS2
selection engine. It uses Libxml2 as underlying XML platform and the GLib as a
portability layer.


%prep
%setup -q


%build
%configure \
	--enable-checks \
	--enable-gtk-doc
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
%doc ABOUT-NLS AUTHORS COPYING* HACKING README TODO NEWS
%{_libdir}/libcroco*.*
%{_libdir}/pkgconfig/libcroco*.pc
%{_includedir}/libcroco*/
%{_bindir}/csslint*
%{_bindir}/croco*-config
