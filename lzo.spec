Name: lzo
Version: 2.03
Release: 1ev
Summary: LZO compression/decompression library
URL: http://www.oberhumer.com/opensource/lzo
Group: System Environment/Libraries
License: GPL-2
Vendor: GNyU-Linux
Source: http://www.oberhumer.com/opensource/lzo/download/lzo-%{version}.tar.gz
BuildRequires: make, gcc

%description
LZO is a data compression library which is suitable for data de-/compression in 
real-time. This means it favours speed over compression ratio. 
LZO is written in ANSI C. Both the source code and the compressed data format 
are designed to be portable across platforms.
LZO implements a number of algorithms with the following features:
   * Decompression is simple and *very* fast.
   * Requires no memory for decompression.
   * Compression is pretty fast.
   * Requires 64 kB of memory for compression.
   * Allows you to dial up extra compression at a speed cost in the compressor.
     The speed of the decompressor is not reduced.
   * Includes compression levels for generating pre-compressed data which 
     achieve a quite competitive compression ratio.
   * There is also a compression level which needs only 8 kB for compression.
   * Algorithm is thread safe.
   * Algorithm is lossless.
LZO supports overlapping compression and in-place decompression.


%prep
%setup -q


%build
%configure \
	--enable-shared
%{__make} %{?_smp_mflags}
%{__make} check


%install
%{__make} install DESTDIR='%{buildroot}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc AUTHORS BUGS COPYING NEWS README THANKS
%{_includedir}/lzo/
%{_libdir}/liblzo2.*
