Name: binutils
Version: 2.18
Release: 2ev
Summary: A collection of binary tools
Group: Development/Tools
License: GPL
Source: http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.bz2
Vendor: MSP Slackware
BuildRequires: make, gcc-core
Buildroot: %{_tmppath}/%{name}-root

%description
The GNU Binutils are a collection of binary tools. The main ones are:
    ld - the GNU linker.
    as - the GNU assembler.
But they also include:
    addr2line - Converts addresses into filenames and line numbers.
    ar - A utility for creating, modifying and extracting from archives.
    c++filt - Filter to demangle encoded C++ symbols.
    gprof - Displays profiling information.
    nlmconv - Converts object code into an NLM.
    nm - Lists symbols from object files.
    objcopy - Copys and translates object files.
    objdump - Displays information from object files.
    ranlib - Generates an index to the contents of an archive.
    readelf - Displays information from any ELF format object file.
    size - Lists the section sizes of an object or archive file.
    strings - Lists printable strings from files.
    strip - Discards symbols.
    windres - A compiler for Windows resource files.
Most of these programs use BFD, the Binary File Descriptor library, to do
low-level manipulation. Many of them also use the opcodes library to assemble
and disassemble machine instructions.


%prep
%setup -q


%build
%configure
%{__make} %{_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%{__rm} -f %{buildroot}/%{_infodir}/dir

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
%doc README COPYING*
%{_bindir}/addr2line
%{_bindir}/ar
%{_bindir}/as
%{_bindir}/c++filt
%{_bindir}/gprof
%{_bindir}/ld
%{_bindir}/nm
%{_bindir}/objcopy
%{_bindir}/objdump
%{_bindir}/ranlib
%{_bindir}/readelf
%{_bindir}/size
%{_bindir}/strings
%{_bindir}/strip
%{_prefix}/%{_target_platform}/
%{_includedir}/*.h
%{_infodir}/as.info.gz
%{_infodir}/bfd.info.gz
%{_infodir}/binutils.info.gz
%{_infodir}/configure.info.gz
%{_infodir}/gprof.info.gz
%{_infodir}/ld.info.gz
%{_infodir}/standards.info.gz
%{_libdir}/libbfd.*
%{_libdir}/libiberty.a
%{_libdir}/libopcodes.*
%{_mandir}/man1/*.1*
%{_datadir}/locale/*/*/*.mo
