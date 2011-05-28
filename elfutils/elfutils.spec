Name: elfutils
Version: 0.152
Release: 1.0
Summary: A collection of utilities and DSOs to handle compiled objects
URL: http://www.fedorahosted.org/elfutils
Group: Development/Tools
License: GPL-2
Source: https://fedorahosted.org/releases/e/l/elfutils/%{version}/elfutils-%{version}.tar.bz2
Patch0: elfutils-portability.patch
Patch1: elfutils-robustify.patch
BuildRequires: grep, make, gcc
BuildRequires: bison >= 1.875, flex >= 2.5.4a, gettext-tools
BuildRequires: eglibc-devel >= 2.7
BuildRequires: xz-devel, zlib-devel, bzip2-devel

%description
Elfutils is a collection of utilities, including ld (a linker), nm (for
listing symbols from object files), size (for listing the section sizes of an
object or archive file), strip (for discarding symbols), readelf (to see the
raw ELF file structures), and elflint (to check for well-formed ELF files).
Also included are numerous helper libraries which implement DWARF, ELF, and
machine-specific ELF handling.


%package devel
Summary: Development libraries to handle compiled objects
Group: Development/Tools
Requires: elfutils = %{version}-%{release}
Requires: elfutils-libelf-devel = %{version}-%{release}

%description devel
The elfutils-devel package contains the libraries to create
applications for handling compiled objects.  libebl provides some
higher-level ELF access functionality.  libdw provides access to
the DWARF debugging information.  libasm provides a programmable
assembler interface.


%package libelf
Summary: Library to read and write ELF files
Group: Development/Tools

%description libelf
The elfutils-libelf package provides a DSO which allows reading and
writing ELF files on a high level.  Third party programs depend on
this package to read internals of ELF files.  The programs of the
elfutils package use it also to generate new ELF files.


%package libelf-devel
Summary: Development support for libelf
Group: Development/Tools
Requires: elfutils-libelf = %{version}-%{release}
Conflicts: libelf-devel

%description libelf-devel
The elfutils-libelf-devel package contains the libraries to create
applications for handling compiled objects.  libelf allows you to
access the internals of the ELF object file format, so you can see the
different sections of an ELF file.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%{__find} . \
    \( -name Makefile\* -or -name configure\* \) \
    -exec %{__touch} '{}' \;


%build
%configure \
    --program-prefix='eu-'
%{__make} -k %{?_smp_mflags} ||:


%install
%{__make} install DESTDIR='%{buildroot}'
%find_lang elfutils

# Nuke unpackaged files
{
    pushd '%{buildroot}'
    %{__rm} -f '.%{_bindir}/eu-ld' \
        '.%{_includedir}/elfutils/libasm.h' \
        '.%{_libdir}/libasm.so' \
        '.%{_libdir}/libasm.a'
}

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%check
%{__make} check ||:


%post libelf -p %{__ldconfig}
%postun libelf -p %{__ldconfig}


%files
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS COPYING ChangeLog EXCEPTION README NEWS NOTES THANKS TODO
%{_bindir}/eu-addr2line
%{_bindir}/eu-ar
%{_bindir}/eu-elfcmp
%{_bindir}/eu-elflint
%{_bindir}/eu-findtextrel
%{_bindir}/eu-nm
%{_bindir}/eu-objdump
%{_bindir}/eu-ranlib
%{_bindir}/eu-readelf
%{_bindir}/eu-size
%{_bindir}/eu-strings
%{_bindir}/eu-strip
%{_bindir}/eu-unstrip
%{_bindir}/eu-make-debug-archive
%dir %{_libdir}/elfutils
%{_libdir}/elfutils/lib*.so
%{_libdir}/libdw-%{version}.so
%{_libdir}/libdw.so.*
%{_libdir}/libasm-%{version}.so
%{_libdir}/libasm.so.*


%files devel
%defattr(-,root,root)
%{_includedir}/dwarf.h
%dir %{_includedir}/elfutils
%{_includedir}/elfutils/elf-knowledge.h
%{_includedir}/elfutils/libebl.h
%{_includedir}/elfutils/libdw.h
%{_includedir}/elfutils/libdwfl.h
%{_libdir}/libebl.a
%{_libdir}/libdw.so
%{_libdir}/libdw.a


%files libelf -f elfutils.lang
%defattr(-,root,root)
%{_libdir}/libelf-%{version}.so
%{_libdir}/libelf.so.*


%files libelf-devel
%defattr(-,root,root)
%{_includedir}/libelf.h
%{_includedir}/gelf.h
%{_includedir}/nlist.h
%{_includedir}/elfutils/version.h
%{_libdir}/libelf.so
%{_libdir}/libelf.a
