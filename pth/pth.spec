Name: pth
Version: 2.0.7
Release: 1ev
Summary: GNU portable threads
URL: http://www.gnu.org/software/pth/
Group: System Environment/Libraries
License: LGPL
Vendor: GNyU-Linux
Source: ftp://ftp.ossp.org/pkg/lib/pth/pth-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires(prep,build,install): coreutils
BuildRequires(build,install): make
BuildRequires(build): gcc

%description
GNU Portable Threads (Pth) is a very portable POSIX/ANSI-C based library for
Unix platforms providing non-preemptive priority-based scheduling for multiple
threads of execution ("multithreading") inside server applications. All
threads run in the same address space, but each thread has its own individual
program-counter, run-time stack, signal mask and errno variable. The
scheduling is done in a cooperative way, i.e. the threads are dispatched based
on priority and pending events. The event facility allows threads to wait
until various types of events occur, including pending I/O on filedescriptors,
elapsed timers, pending I/O on message ports, thread and process termination,
and even customized callback functions. 


%prep
%setup -q


%build
%configure \
	--enable-optimize \
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc ANNOUNCE AUTHORS COPYING ChangeLog* HACKING HISTORY README NEWS PORTING
%doc SUPPORT TESTS THANKS
%{_bindir}/pth-config
%{_includedir}/pth.h
%{_libdir}/libpth.*
%doc %{_mandir}/man1/pth-config.1*
%doc %{_mandir}/man3/pth.3*
%{_datadir}/aclocal/pth.m4
