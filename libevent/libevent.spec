Name: libevent
Version: 1.4.12
Release: 1ev
Summary: An event notification library
URL: http://www.monkey.org/~provos/libevent
Group: System Environment/Libraries
License: BSD
Vendor: GNyU-Linux
Source: http://www.monkey.org/~provos/%{name}-%{version}-stable.tar.gz
BuildRequires: make, gcc

%description
The libevent API provides a mechanism to execute a callback function when a
specific event occurs on a file descriptor or after a timeout has been
reached. Furthermore, libevent also support callbacks due to signals or
regular timeouts. 
libevent is meant to replace the event loop found in event driven network
servers. An application just needs to call event_dispatch() and then add or
remove events dynamically without having to change the event loop.


%prep
	%setup -q -n '%{name}-%{version}-stable'


%build
	%configure
	%{__make} %{?_smp_mflags}


%check
	%{__make} verify


%install
	%{__make} install DESTDIR='%{buildroot}'


%post
	%{__ldconfig}


%postun
	%{__ldconfig}


%files
	%defattr(-, root, root)
	%doc README ChangeLog
	%{_bindir}/event_rpcgen.py
	%{_includedir}/evdns.h
	%{_includedir}/event-config.h
	%{_includedir}/event.h
	%{_includedir}/evhttp.h
	%{_includedir}/evrpc.h
	%{_includedir}/evutil.h
	%{_libdir}/libevent-1.4.*
	%{_libdir}/libevent.*
	%{_libdir}/libevent_core*.*
	%{_libdir}/libevent_extra*.*
	%doc %{_mandir}/man3/evdns.3*
	%doc %{_mandir}/man3/event.3*
