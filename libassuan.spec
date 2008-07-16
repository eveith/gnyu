Name: libassuan
Version: 1.0.1
Release: 1ev
Summary: The IPC library used by GnuPG and related projects
URL: http://www.gnupg.org/related_software/assuan/
Group: System Environment/Libraries
License: LGPL
Vendor: MSP Slackware
Source: ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, pth

%description
Libassuan is a small library implementing the so-called Assuan protocol. This
protocol is used for IPC between most newer GnuPG components. Both, server and
client side functions are provided.


%prep
%setup -q


%build
%configure
make


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"


[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
/sbin/install-info --info-dir=%{_infodir} %{_infodir}/assuan.info*

%postun
/sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/assuan.info*


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc README* AUTHORS COPYING* ChangeLog* NEWS THANKS TODO VERSION
%{_bindir}/libassuan-config
%{_libdir}/libassuan*.*
%{_includedir}/assuan.h
%{_infodir}/assuan.info*
%{_datadir}/aclocal/libassuan.m4
