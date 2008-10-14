Name: lzma
Version: 4.32.7
Release: 1ev
Summary: Implementation of the Lempel-Ziv-Markov chain compression algorithm
URL: http://tukaani.org/lzma/
Group: System Environment/Base
License: GPL-2, GPL-3 and LGPL-2.1
Vendor: GNyU-Linux
Source: http://tukaani.org/lzma/lzma-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, gcc-g++, libstdc++

%description
LZMA provides very high compression ratio and fast decompression. The
core of the LZMA utils is Igor Pavlov\'s LZMA SDK containing the actual
LZMA encoder/decoder. LZMA utils add a few scripts which provide
gzip-like command line interface and a couple of other LZMA related
tools. Also provides:
- Average compression ratio 30% better than that of gzip and 15%
  better than that of bzip2.
- Decompression speed is only little slower than that of gzip, being
  two to five times faster than bzip2.
- In fast mode, compresses faster than bzip2 with a comparable
  compression ratio.
- Achieving the best compression ratios takes four to even twelve
  times longer than with bzip2. However. this doesn't affect
  decompressing speed.
- Very similar command line interface than what gzip and bzip2 have.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post

%postun


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc COPYING.* AUTHORS ChangeLog README NEWS THANKS
%{_bindir}/lzcat
%{_bindir}/lzcmp
%{_bindir}/lzdiff
%{_bindir}/lzegrep
%{_bindir}/lzfgrep
%{_bindir}/lzgrep
%{_bindir}/lzless
%{_bindir}/lzma
%{_bindir}/lzmadec
%{_bindir}/lzmainfo
%{_bindir}/lzmore
%{_bindir}/unlzma
%{_includedir}/lzmadec.h
%{_libdir}/liblzmadec.*
%doc %{_mandir}/man1/lzcat.1*
%doc %{_mandir}/man1/lzcmp.1*
%doc %{_mandir}/man1/lzdiff.1*
%doc %{_mandir}/man1/lzegrep.1*
%doc %{_mandir}/man1/lzfgrep.1*
%doc %{_mandir}/man1/lzgrep.1*
%doc %{_mandir}/man1/lzless.1*
%doc %{_mandir}/man1/lzma.1*
%doc %{_mandir}/man1/lzmadec.1*
%doc %{_mandir}/man1/lzmainfo.1*
%doc %{_mandir}/man1/lzmore.1*
%doc %{_mandir}/man1/unlzma.1*
