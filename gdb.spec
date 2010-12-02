Name: gdb
Version: 6.7
Release: 1ev
Summary: The GNU Project Debugger
URL: http://sourceware.org/gdb/
Group: Development/Debuggers
License: GPL-3, GPL-2, LGPL
Vendor: MSP Slackware
Source: http://ftp.gnu.org/gnu/gdb/gdb-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, expat, ncurses
Requires: %{_libdir}/libiberty.a, %{_libdir}/libbfd.a, %{_libdir}/libopcodes.a

%description
GDB, the GNU Project debugger, allows you to see what is going on `inside'
another program while it executes -- or what another program was doing at the
moment it crashed. 
GDB can do four main kinds of things (plus other things in support of these)
to help you catch bugs in the act: 
- Start your program, specifying anything that might affect its behavior. 
- Make your program stop on specified conditions. 
- Examine what has happened, when your program has stopped. 
- Change things in your program, so you can experiment with correcting the
  effects of one bug and go on to learn about another. 
The program being debugged can be written in Ada, C, C++, Objective-C, Pascal
(and many other languages). Those programs might be executing on the same
machine as GDB (native) or on another machine (remote). 


%prep
%setup -q


%build
%configure
make %{_smp_mflags}


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"
rm -rf "${RPM_BUILD_ROOT}"/{%{_libdir},%{_includedir}}

[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
/sbin/regen-info-dir

%postun
/sbin/regen-info-dir


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc COPYING* README gdb/CONTRIBUTE gdb/ChangeLog* gdb/NEWS gdb/PROBLEMS
%doc gdb/README
%{_bindir}/gdb*
%{_infodir}/annotate.info*
%{_infodir}/bfd.info*
%{_infodir}/configure.info*
%{_infodir}/gdb*.info*
%{_infodir}/stabs.info*
%{_infodir}/standards.info*
%{_mandir}/man1/gdb*.1*
%{_datadir}/locale/*/LC_MESSAGES/*.mo
