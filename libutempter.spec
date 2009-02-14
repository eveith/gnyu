Name: libutempter
Version: 1.1.5
Release: 1ev
Summary: A library to record user sessions to utmp and wtmp files
URL: ftp://ftp.altlinux.org/pub/people/ldv/utempter
Group: System Environment/Libraries
License: LGPL-2.1
Vendor: GNyU-Linux
Source: ftp://ftp.altlinux.org/pub/people/ldv/utempter/%{name}-%{version}.tar.bz2
BuildRequires: make, gcc

%description
The libutempter library provides interface for terminal emulators such as
screen and xterm to record user sessions to utmp and wtmp files.
The utempter is a privileged helper used by libutempter library to manipulate
utmp and wtmp files.


%prep
%setup -q


%build
%{__make} %{?_smp_mflags} \
	libdir='%{_libdir}' \
	libexecdir='%{_libexecdir}' \
	includedir='%{_includedir}' \
	CFLAGS="${CFLAGS:-%{optflags}}"
	


%install
%{__make} install \
	DESTDIR='%{buildroot}' \
	libdir='%{_libdir}' \
	libexecdir='%{_libexecdir}' \
	includedir='%{_includedir}' 


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc README COPYING
%{_includedir}/utempter.h
%{_libdir}/libutempter.*
%dir %{_libexecdir}/utempter
%attr(2711, root, root) %{_libexecdir}/utempter/utempter
