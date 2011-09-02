Name: tcl
Version: 8.5.10
Release: 1.0
Summary: The Tool Command Language, a programming language
URL: http://www.tcl.tk
Group: Development/TCL
License: BSD
Source: http://prdownloads.sourceforge.net/%{name}/%{name}%{version}-src.tar.gz
Patch0: tcl-unload.patch
Patch1: tcl-stack.patch
Patch2: tcl.patch
BuildRequires: autoconf, patch
BuildRequires: grep, sed, gawk, make
BuildRequires: gcc
BuildRequires: eglibc-devel
Requires: libtcl%{version} = %{version}-%{release}

%description
Tcl (Tool Command Language) is a very powerful but easy to learn
dynamic programming language, suitable for a very wide range of uses,
including web and desktop applications, networking, administration,
testing and many more. Open source and business-friendly, Tcl is a
mature yet evolving language that is truly cross platform, easily
deployed and highly extensible.

For more information on Tcl see http://www.tcl.tk and
http://wiki.tcl.tk.


%files
%defattr(-, root, root)
%doc ChangeLog* README changes license.terms
%{_bindir}/tclsh8.5

%doc %{_mandir}/man1/tclsh.1*
%doc %{_mandir}/mann/Tcl.n*
%doc %{_mandir}/mann/msgcat.n*
%doc %{_mandir}/mann/after.n*
%doc %{_mandir}/mann/memory.n*
%doc %{_mandir}/mann/append.n*
%doc %{_mandir}/mann/refchan.n*
%doc %{_mandir}/mann/apply.n*
%doc %{_mandir}/mann/regexp.n*
%doc %{_mandir}/mann/array.n*
%doc %{_mandir}/mann/registry.n*
%doc %{_mandir}/mann/bgerror.n*
%doc %{_mandir}/mann/regsub.n*
%doc %{_mandir}/mann/binary.n*
%doc %{_mandir}/mann/rename.n*
%doc %{_mandir}/mann/break.n*
%doc %{_mandir}/mann/return.n*
%doc %{_mandir}/mann/case.n*
%doc %{_mandir}/mann/SafeBase.n*
%doc %{_mandir}/mann/catch.n*
%doc %{_mandir}/mann/cd.n*
%doc %{_mandir}/mann/scan.n*
%doc %{_mandir}/mann/chan.n*
%doc %{_mandir}/mann/seek.n*
%doc %{_mandir}/mann/clock.n*
%doc %{_mandir}/mann/set.n*
%doc %{_mandir}/mann/close.n*
%doc %{_mandir}/mann/socket.n*
%doc %{_mandir}/mann/concat.n*
%doc %{_mandir}/mann/source.n*
%doc %{_mandir}/mann/continue.n*
%doc %{_mandir}/mann/dde.n*
%doc %{_mandir}/mann/split.n*
%doc %{_mandir}/mann/dict.n*
%doc %{_mandir}/mann/string.n*
%doc %{_mandir}/mann/encoding.n*
%doc %{_mandir}/mann/eof.n*
%doc %{_mandir}/mann/subst.n*
%doc %{_mandir}/mann/error.n*
%doc %{_mandir}/mann/switch.n*
%doc %{_mandir}/mann/eval.n*
%doc %{_mandir}/mann/tcltest.n*
%doc %{_mandir}/mann/exec.n*
%doc %{_mandir}/mann/tclvars.n*
%doc %{_mandir}/mann/exit.n*
%doc %{_mandir}/mann/tell.n*
%doc %{_mandir}/mann/expr.n*
%doc %{_mandir}/mann/time.n*
%doc %{_mandir}/mann/fblocked.n*
%doc %{_mandir}/mann/tm.n*
%doc %{_mandir}/mann/fconfigure.n*
%doc %{_mandir}/mann/trace.n*
%doc %{_mandir}/mann/fcopy.n*
%doc %{_mandir}/mann/unknown.n*
%doc %{_mandir}/mann/file.n*
%doc %{_mandir}/mann/unload.n*
%doc %{_mandir}/mann/fileevent.n*
%doc %{_mandir}/mann/unset.n*
%doc %{_mandir}/mann/filename.n*
%doc %{_mandir}/mann/update.n*
%doc %{_mandir}/mann/flush.n*
%doc %{_mandir}/mann/for.n*
%doc %{_mandir}/mann/uplevel.n*
%doc %{_mandir}/mann/foreach.n*
%doc %{_mandir}/mann/upvar.n*
%doc %{_mandir}/mann/format.n*
%doc %{_mandir}/mann/variable.n*
%doc %{_mandir}/mann/gets.n*
%doc %{_mandir}/mann/vwait.n*
%doc %{_mandir}/mann/glob.n*
%doc %{_mandir}/mann/while.n*
%doc %{_mandir}/mann/global.n*
%doc %{_mandir}/mann/history.n*
%doc %{_mandir}/mann/http.n*
%doc %{_mandir}/mann/if.n*
%doc %{_mandir}/mann/incr.n*
%doc %{_mandir}/mann/info.n*
%doc %{_mandir}/mann/interp.n*
%doc %{_mandir}/mann/join.n*
%doc %{_mandir}/mann/lappend.n*
%doc %{_mandir}/mann/lassign.n*
%doc %{_mandir}/mann/auto_execok.n*
%doc %{_mandir}/mann/lindex.n*
%doc %{_mandir}/mann/linsert.n*
%doc %{_mandir}/mann/list.n*
%doc %{_mandir}/mann/llength.n*
%doc %{_mandir}/mann/load.n*
%doc %{_mandir}/mann/lrange.n*
%doc %{_mandir}/mann/lrepeat.n*
%doc %{_mandir}/mann/lreplace.n*
%doc %{_mandir}/mann/lreverse.n*
%doc %{_mandir}/mann/lsearch.n*
%doc %{_mandir}/mann/lset.n*
%doc %{_mandir}/mann/lsort.n*
%doc %{_mandir}/mann/mathfunc.n*
%doc %{_mandir}/mann/mathop.n*
%doc %{_mandir}/mann/namespace.n*
%doc %{_mandir}/mann/open.n*
%doc %{_mandir}/mann/package.n*
%doc %{_mandir}/mann/pkg::create.n*
%doc %{_mandir}/mann/pid.n*
%doc %{_mandir}/mann/pkg_mkIndex.n*
%doc %{_mandir}/mann/platform.n*
%doc %{_mandir}/mann/platform::shell.n*
%doc %{_mandir}/mann/proc.n*
%doc %{_mandir}/mann/puts.n*
%doc %{_mandir}/mann/pwd.n*
%doc %{_mandir}/mann/re_syntax.n*
%doc %{_mandir}/mann/read.n*
%doc %{_mandir}/mann/auto_import.n.gz
%doc %{_mandir}/mann/auto_load.n.gz
%doc %{_mandir}/mann/auto_mkindex.n.gz
%doc %{_mandir}/mann/auto_mkindex_old.n.gz
%doc %{_mandir}/mann/auto_qualify.n.gz
%doc %{_mandir}/mann/auto_reset.n.gz
%doc %{_mandir}/mann/parray.n.gz
%doc %{_mandir}/mann/tcl_endOfWord.n.gz
%doc %{_mandir}/mann/tcl_findLibrary.n.gz
%doc %{_mandir}/mann/tcl_startOfNextWord.n.gz
%doc %{_mandir}/mann/tcl_startOfPreviousWord.n.gz
%doc %{_mandir}/mann/tcl_wordBreakAfter.n.gz
%doc %{_mandir}/mann/tcl_wordBreakBefore.n.gz


%package devel
Group: Development/TCL
License: BSD3
Summary: Header Files and C API Documentation for Tcl
Requires: tcl = %{version}-%{release}
 

%description devel
This package contains header files and documentation needed for writing
Tcl extensions in compiled languages like C, C++, etc., or for
embedding the Tcl interpreter in programs written in such languages.
This package is not needed for writing extensions or applications in
the Tcl language itself.


%files devel
%defattr(-, root, root)
%doc ChangeLog* README changes license.terms

%{_libdir}/tclConfig.sh
%{_libdir}/libtclstub8.5.a
%{_libdir}/tcl8.5/tclAppInit.c

%{_includedir}/tcl*.h

%doc %{_mandir}/man3/attemptckalloc.3.gz
%doc %{_mandir}/man3/attemptckrealloc.3.gz
%doc %{_mandir}/man3/ckalloc.3.gz
%doc %{_mandir}/man3/ckfree.3.gz
%doc %{_mandir}/man3/ckrealloc.3.gz
%doc %{_mandir}/man3/TCL_MEM_DEBUG.3*
%doc %{_mandir}/man3/Tcl_*.3*


%package -n libtcl8.5
Summary: Tool Command Language runtime library
Group: Development/Tcl


%description -n libtcl8.5
Tcl (Tool Command Language) is a very powerful but easy to learn
dynamic programming language, suitable for a very wide range of uses,
including web and desktop applications, networking, administration,
testing and many more. 
The language basis is included in this package. It contains the shared runtime
library as well as other files needed for Tcl scripts to run, such as timezone
data.


%files -n libtcl8.5
%defattr(-, root, root)

%{_libdir}/libtcl8.5.so

%dir %{_libdir}/tcl8

%dir %{_libdir}/tcl8/8.4
%{_libdir}/tcl8/8.4/http-2.7.6.tm
%{_libdir}/tcl8/8.4/platform-1.0.10.tm
%{_libdir}/tcl8/8.4/platform/shell-1.1.4.tm

%dir %{_libdir}/tcl8/8.5
%{_libdir}/tcl8/8.5/msgcat-1.4.4.tm
%{_libdir}/tcl8/8.5/tcltest-2.3.3.tm

%dir %{_libdir}/tcl8.5
%{_libdir}/tcl8.5/tzdata
%{_libdir}/tcl8.5/msgs
%{_libdir}/tcl8.5/opt0.4
%{_libdir}/tcl8.5/http1.0
%{_libdir}/tcl8.5/encoding
%{_libdir}/tcl8.5/auto.tcl
%{_libdir}/tcl8.5/clock.tcl
%{_libdir}/tcl8.5/history.tcl
%{_libdir}/tcl8.5/init.tcl
%{_libdir}/tcl8.5/package.tcl
%{_libdir}/tcl8.5/parray.tcl
%{_libdir}/tcl8.5/safe.tcl
%{_libdir}/tcl8.5/tm.tcl
%{_libdir}/tcl8.5/word.tcl
%{_libdir}/tcl8.5/tclIndex


%prep
%setup -q -n '%{name}%{version}'
%patch0 -p0
%patch1 -p0
%patch2 -p0


%build
pushd unix
%{__autoconf}
%configure \
    --enable-man-symlinks \
    --enable-man-compression=gzip
%{__make} %{?_smp_mflags}
popd


%install
%{__make} -C unix \
    install install-private-headers \
    DESTDIR='%{buildroot}' \
    INSTALL_ROOT='%{buildroot}'

[[ -e '%{buildroot}%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}%{_infodir}/dir'


%check
%{__make} -C unix test ||:
