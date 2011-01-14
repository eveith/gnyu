Name: gdb
Version: 7.2
Release: 2.0ev
Summary: The GNU Project Debugger
URL: http://sourceware.org/gdb/
Group: Development/Debuggers
License: GPL-3, GPL-2, LGPL
Vendor: GNyU-Linux
Source: http://ftp.gnu.org/gnu/gdb/gdb-%{version}.tar.bz2
BuildRequires: sed, gawk, grep, make, bison, flex, perl
BuildRequires: m4, automake, autoconf, gcc, gcc-g++, gettext-tools
BuildRequires: elfutils-libelf, expat, ncurses

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
%configure \
	--enable-tui \
	--without-python
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

# Delete stuff already provided by other packages, e.g. binutils

%{__rm_rf} '%{buildroot}%{_datadir}/locale'
%{__rm_rf} '%{buildroot}%{_infodir}'/bfd*
%{__rm_rf} '%{buildroot}%{_infodir}'/standard*
%{__rm_rf} '%{buildroot}%{_infodir}'/mmalloc*
%{__rm_rf} '%{buildroot}%{_infodir}'/configure*
%{__rm_rf} '%{buildroot}%{_includedir}'
%{__rm_rf} '%{buildroot}%{_libdir}'/lib{bfd*,opcodes*,iberty*,mmalloc*}

[ -e "${RPM_BUILD_ROOT}%{_infodir}/dir" ] \
    && %{__rm} "${RPM_BUILD_ROOT}%{_infodir}/dir"


%post
update-info-dir


%postun
update-info-dir


%files 
%defattr(-, root, root)
%doc COPYING* README gdb/CONTRIBUTE gdb/ChangeLog* gdb/NEWS gdb/PROBLEMS
%doc gdb/README
%{_bindir}/gdb*
%{_libdir}/libinproctrace.so
%doc %{_infodir}/annotate.info*
%doc %{_infodir}/gdb*.info*
%doc %{_infodir}/stabs.info*
%doc %{_mandir}/man1/gdb*.1*
%dir %{_datadir}/gdb
%dir %{_datadir}/gdb/syscalls
%{_datadir}/gdb/syscalls/*.*
