Name: obby
Version: 0.4.5
Release: 1ev
Summary: A library providing synced document buffers
URL: http://releases.0x539.de/obby/
Group: System Environment/Libraries
License: GPL-2
Vendor: GNyU-Linux
Source: http://releases.0x539.de/obby/obby-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: coreutils, grep, sed, make, gcc-g++, libsigc++ >= 2.0
BuildRequires: net6 >= 1.3.3, gettext

%description
libobby is a library which provides synced document buffers. It supports
multiple documents in one session and is portable to both Windows and
Unix-like platforms.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%find_lang obby

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files -f obby.lang
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS ChangeLog COPYING README NEWS TODO
%{_includedir}/obby/
%{_libdir}/libobby-*.*
%{_libdir}/libobby.*
%{_libdir}/pkgconfig/obby-*.pc
