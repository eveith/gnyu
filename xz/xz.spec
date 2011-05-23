Name: xz
Version: 5.0.3
Release: 1.0
Summary: A general-pourpose data compression format (LZMA2)
URL: http://tukaani.org/xz
Group: System Environment/Base
License: Public Domain, GPL-2
Source: http://tukaani.org/xz/xz-%{version}.tar.bz2
BuildRequires: grep, sed, make, gcc
BuildRequires: gettext-tools

%description
XZ Utils is free general-purpose data compression software with high
compression ratio. XZ Utils are the successor to LZMA Utils.
This package contains the command line tools for working with .xz archives.
Many of them have been adapted from their GZip counterparts, such as xzgrep,
xzdiff, etc.


%package devel
Summary: Development headers for XZ/LZMA
Group: Development/Libraries
Requires: liblzma5 = %{version}-%{release}, pkgconfig

%description devel
This package includes the API headers, static library, and other development
files related to liblzma.


%package lzma
Summary: LZMA compatibility programs
Group: System Environment/Base

%description lzma
This package includes executables and symlinks to make XZ Utils emulate lzma,
unlzma, lzcat, and other command line tools found from the legacy LZMA Utils
4.32.x package.


%package -n liblzma5
Summary: A general-pourpose data compression library (XZ/LZMA2)
Group: System Environment/Libraries

%description -n liblzma5
liblzma is a general purpose data compression library with an API similar to
that of zlib. liblzma supports multiple algorithms, of which LZMA2 is
currently the primary algorithm.  The native file format is .xz, but also the
legacy .lzma format and raw streams (no headers at all) are supported.
This package includes the shared library.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%{__rm_rf} '%{buildroot}%{_datadir}/doc' ||:
%find_lang xz

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post -n liblzma5 -p %{__ldconfig}
%postun -n liblzma5 -p %{__ldconfig}


%files -f xz.lang
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS ChangeLog COPYING* NEWS README THANKS TODO
%{_bindir}/xzcat
%{_bindir}/xzcmp
%{_bindir}/xzdiff
%{_bindir}/xzegrep
%{_bindir}/xzfgrep
%{_bindir}/xzgrep
%{_bindir}/xzless
%{_bindir}/xz
%{_bindir}/xzdec
%{_bindir}/xzmore
%{_bindir}/unxz
%doc %{_mandir}/man1/xzcat.1*
%doc %{_mandir}/man1/xzcmp.1*
%doc %{_mandir}/man1/xzdiff.1*
%doc %{_mandir}/man1/xzegrep.1*
%doc %{_mandir}/man1/xzfgrep.1*
%doc %{_mandir}/man1/xzgrep.1*
%doc %{_mandir}/man1/xzless.1*
%doc %{_mandir}/man1/xz.1*
%doc %{_mandir}/man1/xzdec.1*
%doc %{_mandir}/man1/xzmore.1*
%doc %{_mandir}/man1/unxz.1*


%files devel
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS ChangeLog COPYING* NEWS README THANKS TODO
%doc doc/*.txt doc/examples
%{_libdir}/liblzma.so
%{_libdir}/liblzma.la
%{_libdir}/liblzma.a
%{_libdir}/pkgconfig/liblzma.pc
%{_includedir}/lzma.h
%dir %{_includedir}/lzma
%{_includedir}/lzma/*.h


%files lzma
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS ChangeLog COPYING* NEWS README THANKS TODO
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


%files -n liblzma5
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS ChangeLog COPYING* NEWS README THANKS TODO
%{_libdir}/liblzma.so.5*
