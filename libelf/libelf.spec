Name: libelf
Version: 0.8.13
Release: 1.0
Summary: A library for reading, modifying and creating ELF files
URL: http://www.mr511.de/software
Group: System Environment/Libraries
License: LGPL-2
Source: http://www.mr511.de/software/libelf-0.8.13.tar.gz
BuildRequires: grep, sed, make, gcc
BuildRequires: eglibc-devel, kernel-headers
BuildRequires: gettext-tools
Requires: libelf0 = %{version}-%{release}

%description
'Libelf' lets you read, modify or create ELF files in an
architecture-independent way. The library takes care of size and endian
issues, e.g. you can process a file for SPARC processors on an Intel-based
system. 


%package -n libelf0
Summary: A library for reading, modifying and creating ELF files
Group: System Environment/Libraries

%description -n libelf0
'Libelf' lets you read, modify or create ELF files in an
architecture-independent way. The library takes care of size and endian
issues, e.g. you can process a file for SPARC processors on an Intel-based
system. 


%package devel
Summary: Development headers for libelf
Group: Development/Libraries
Requires: pkg-config, libelf = %{version}-%{release}

%description devel
'Libelf' lets you read, modify or create ELF files in an
architecture-independent way. The library takes care of size and endian
issues, e.g. you can process a file for SPARC processors on an Intel-based
system. 
The file contains the headers and pkg-config files which are needed to make
actual use of libelf in a program.


%prep
%setup -q


%build
%configure \
    --libdir='/%{_lib}' \
    --enable-compat
%{__make} %{?_smp_mflags}



%install
%{__make} install instroot='%{buildroot}'

%{__mkdir_p} '%{buildroot}%{_libdir}'
%{__mv} '%{buildroot}/%{_lib}/pkgconfig' '%{buildroot}%{_libdir}'

%find_lang libelf

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%check
%{__make} check


%post -n libelf0 -p %{__ldconfig}
%postun -n libelf0 -p %{__ldconfig}


%files -f libelf.lang
%defattr(-, root, root)
%doc COPYING.LIB ChangeLog MANIFEST README VERSION


%files -n libelf0
/%{_lib}/libelf.so.0*


%files devel
%defattr(-, root, root)
%doc COPYING.LIB ChangeLog MANIFEST README VERSION
/%{_lib}/libelf.so
/%{_lib}/libelf.a
%{_libdir}/pkgconfig/libelf.pc
%dir %{_includedir}/libelf
%{_includedir}/libelf/libelf.h
%{_includedir}/libelf/nlist.h
%{_includedir}/libelf/gelf.h
%{_includedir}/libelf/sys_elf.h
%{_includedir}/libelf/elf_repl.h
%{_includedir}/libelf.h
%{_includedir}/nlist.h
%{_includedir}/gelf.h
