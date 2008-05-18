Name: net6
Version: 1.3.6
Release: 1ev
Summary: A library for network-based applications
URL: http://releases.0x539.de/net6/
Group: System Environment/Libraries
License: LGPL-2.0
Vendor: GNyU-Linux
Source: http://releases.0x539.de/net6/net6-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: coreutils, grep, sed, make, gcc-g++, libsigc++ >= 2.0, gnutls
BuildRequires: gettext, pkg-config

%description
net6 is a library which eases the development of network-based applications
as it provides a TCP protocol abstraction for C++. It is portable to both
the Windows and Unix-like platforms.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%{find_lang} net6


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files -f net6.lang
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS README NEWS ChangeLog NEWS
%{_includedir}/net6/
%{_libdir}/libnet6*.*
%{_libdir}/pkgconfig/net6-*.pc
