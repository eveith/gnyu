Name: zlib
Version: 1.2.5
Release: 1.0
Summary: A data compression library
URL: http://zlib.net
Group: System Environment/Libraries
License: BSD
Source: http://zlib.net/zlib-%{version}.tar.gz
BuildRequires: grep, sed, make, gcc
BuildRequires: eglibc-devel
Requires: zlib1 = %{version}-%{release}

%description
zlib is designed to be a free, general-purpose, legally unencumbered -- that
is, not covered by any patents -- lossless data-compression library for use on
virtually any computer hardware and operating system. The zlib data format is
itself portable across platforms. Unlike the LZW compression method used in
Unix compress(1) and in the GIF image format, the compression method currently
used in zlib essentially never expands the data. (LZW can double or triple the
file size in extreme cases.) zlib's memory footprint is also independent of
the input data and can be reduced, if necessary, at some cost in compression.


%package -n libz1
Summary: The gzip/deflate compression library
Group: System Environment/Libraries

%description -n libz1
zlib is designed to be a free, general-purpose, legally unencumbered -- that
is, not covered by any patents -- lossless data-compression library for use on
virtually any computer hardware and operating system. The zlib data format is
itself portable across platforms. Unlike the LZW compression method used in
Unix compress(1) and in the GIF image format, the compression method currently
used in zlib essentially never expands the data. (LZW can double or triple the
file size in extreme cases.) zlib's memory footprint is also independent of
the input data and can be reduced, if necessary, at some cost in compression.


%package devel
Summary: Development headers for zlib
Group: Development/Libraries

%description devel
zlib is designed to be a free, general-purpose, legally unencumbered -- that
is, not covered by any patents -- lossless data-compression library for use on
virtually any computer hardware and operating system. 
Many applications make use of zlib. If you want to develop applications that
use the gzip compression yourself, or if you want to compile source code that
makes use of zlib, you will need to install this package.


%prep
%setup -q


%build
export CFLAGS="${CFLAGS:-%{optflags}}"
export CXXFLAGS="${CXXFLAGS:-%{optflags}}"
./configure \
    --prefix='%{_prefix}' \
    --eprefix='%{_exec_prefix}' \
    --libdir='/%{_lib}' \
    --sharedlibdir='/%{_lib}'
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}' \
    mandir='%{_mandir}'

%{__mkdir_p} '%{buildroot}%{_libdir}'
%{__mv} '%{buildroot}/%{_lib}/pkgconfig' '%{buildroot}%{_libdir}'


%check
%{__make} test


%post -n libz1 -p %{__ldconfig}
%postun -n libz1 -p %{__ldconfig}


%files
%defattr(-, root, root)
%doc README FAQ INDEX ChangeLog


%files -n libz1
%defattr(-, root, root)
%doc README FAQ INDEX ChangeLog
/%{_lib}/libz.so.1*


%files devel
%defattr(-, root, root)
%doc README FAQ INDEX ChangeLog
%doc zlib.3.pdf doc/*.txt
/%{_lib}/libz.a
/%{_lib}/libz.so
%{_includedir}/zlib.h
%{_includedir}/zconf.h
%{_libdir}/pkgconfig/zlib.pc
%doc %{_mandir}/man3/zlib.3*
