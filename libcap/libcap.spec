Name: libcap
Version: 2.21
Release: 1.0
Summary: Tools for getting/setting POSIX.1e capabilities
URL: http://www.kernel.org/pub/linux/libs/security/linux-privs
Group: System Environment/Libraries
License: BSD
Vendor: GNyU-Linux
Source: http://www.kernel.org/pub/linux/libs/security/linux-privs/libcap2/libcap-%{version}.tar.gz
BuildRequires: make, gcc
BuildRequires: eglibc-devel, linux-headers
BuildRequires: libpam, attr-devel

%description
These are tools for getting and setting POSIX.1e (formerly POSIX 6)
draft 15 capabilities.


%package devel
Summary: Development headers for libcap
Group: Development/Libraries
Requires: libcap = %{version}-%{release}

%description devel
libcap is a library for getting and setting POSIX.1e (formerly POSIX 6)
draft 15 capabilities.
This package contains header files and API documentation for development.


%package -n libcap2
Summary: A library for getting/setting POSIX.1e capabilities
Group: System Environment/Libraries

%description
This is a library for getting and setting POSIX.1e (formerly POSIX 6)
draft 15 capabilities.


%prep
%setup -q


%build
%{__make} %{?_smp_mflags} \
	CC="${CC:-%{__cc}}" \
	CFLAGS="${CFLAGS:-%{optflags}}"
	


%install
%{__make} install \
    DESTDIR='%{buildroot}' \
	MANDIR='%{buildroot}%{_mandir}' \
	SBINDIR='%{buildroot}/sbin' \
	LIBDIR='%{buildroot}/%{_lib}'


%post -n libcap2 -p %{__ldconfig}
%postun -n libcap2 -p %{__ldconfig}


%files
%defattr(-, root, root)
%doc CHANGELOG License README
%doc progs

%attr(0711, root, root) /%{_lib}/security/pam_cap.so

/sbin/capsh
/sbin/getcap
/sbin/getpcaps
/sbin/setcap

%doc %{_mandir}/man1/capsh.1*
%doc %{_mandir}/man8/getcap.8*
%doc %{_mandir}/man8/setcap.8*


%files -n libcap2
%defattr(-, root, root)
%doc CHANGELOG License README
/%{_lib}/libcap.so.2*


%files devel
%doc CHANGELOG License README

/%{_lib}/libcap.so
/%{_lib}/libcap.a

%{_includedir}/sys/capability.h

%doc %{_mandir}/man3/cap_*.3*
%doc %{_mandir}/man3/capgetp.3*
%doc %{_mandir}/man3/capsetp.3*
%doc %{_mandir}/man3/libcap.3*
