Name: libassuan
Version: 1.0.5
Release: 2ev
Summary: The IPC library used by GnuPG and related projects
URL: http://www.gnupg.org/related_software/assuan/
Group: System Environment/Libraries
License: GPL-3
Vendor: GNyU-Linux
Source: ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires(prep,build,install): coreutils
BuildRequires(build,install): make
BuildRequires(build): gcc, pth

%description
Libassuan is a small library implementing the so-called Assuan protocol. This
protocol is used for IPC between most newer GnuPG components. Both, server and
client side functions are provided.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'

[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
/sbin/ldconfig
update-info-dir

%postun
/sbin/ldconfig
update-info-dir


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc README* AUTHORS COPYING* ChangeLog* NEWS THANKS TODO VERSION
%{_bindir}/libassuan-config
%{_libdir}/libassuan*.*
%{_includedir}/assuan.h
%doc %{_infodir}/assuan.info*
%{_datadir}/aclocal/libassuan.m4
