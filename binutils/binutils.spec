Name: binutils
Version: 2.19.1
Release: 3ev
Summary: A collection of binary tools
Group: Development/Tools
License: GPL-2, GPL-3, LGPL-2
Source: http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.bz2
Vendor: GNyU-Linux
BuildRequires: make, gcc, bison, flex, perl, gettext, texinfo
BuildRequires: zlib, gmp, mpfr

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
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%{__rm} -f %{buildroot}/%{_infodir}/dir

%find_lang binutils
for lang in bfd gas gprof opcodes ld 
do
	%find_lang "${lang}"
	%{__cat} "${lang}.lang" >> binutils.lang
done


%post
%{__ldconfig}
update-info-dir


%postun
%{__ldconfig}
update-info-dir


%files -f binutils.lang
%defattr(-, root, root)
%doc README COPYING* ChangeLog
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
%dir %{_prefix}/%{_target_platform}
%dir %{_prefix}/%{_target_platform}/bin
%{_prefix}/%{_target_platform}/bin/ar
%{_prefix}/%{_target_platform}/bin/as
%{_prefix}/%{_target_platform}/bin/ld
%{_prefix}/%{_target_platform}/bin/nm
%{_prefix}/%{_target_platform}/bin/objcopy
%{_prefix}/%{_target_platform}/bin/objdump
%{_prefix}/%{_target_platform}/bin/ranlib
%{_prefix}/%{_target_platform}/bin/strip
%dir %{_prefix}/%{_target_platform}/lib
%dir %{_prefix}/%{_target_platform}/lib/ldscripts
%{_prefix}/%{_target_platform}/lib/ldscripts/*%{_build_arch}*
%{_libdir}/libbfd.*
%{_libdir}/libiberty.a
%{_libdir}/libopcodes.*
%{_includedir}/ansidecl.h
%{_includedir}/bfd.h
%{_includedir}/bfdlink.h
%{_includedir}/dis-asm.h
%{_includedir}/symcat.h
%doc %{_infodir}/as.info*
%doc %{_infodir}/bfd.info*
%doc %{_infodir}/binutils.info*
%doc %{_infodir}/configure.info*
%doc %{_infodir}/gprof.info*
%doc %{_infodir}/ld.info*
%doc %{_infodir}/standards.info*
%doc %{_mandir}/man1/addr2line.1*
%doc %{_mandir}/man1/ar.1*
%doc %{_mandir}/man1/as.1*
%doc %{_mandir}/man1/c++filt.1*
%doc %{_mandir}/man1/dlltool.1*
%doc %{_mandir}/man1/gprof.1*
%doc %{_mandir}/man1/ld.1*
%doc %{_mandir}/man1/nlmconv.1*
%doc %{_mandir}/man1/nm.1*
%doc %{_mandir}/man1/objcopy.1*
%doc %{_mandir}/man1/objdump.1*
%doc %{_mandir}/man1/ranlib.1*
%doc %{_mandir}/man1/readelf.1*
%doc %{_mandir}/man1/size.1*
%doc %{_mandir}/man1/strings.1*
%doc %{_mandir}/man1/strip.1*
%doc %{_mandir}/man1/windmc.1*
%doc %{_mandir}/man1/windres.1*
