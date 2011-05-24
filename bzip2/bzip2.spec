Name: bzip2
Version: 1.0.6
Release: 1.0
Summary: A high-quality data compressor
URL: http://www.bzip.org
Group: Applications/Archiving
License: BSD
Source: http://www.bzip.org/%{version}/%{name}-%{version}.tar.gz
BuildRequires: gcc, make >= 3.79.1

%description
bzip2 is a freely available, patent free, high-quality data compressor. It
typically compresses files to within 10% to 15% of the best available
techniques (the PPM family of statistical compressors), whilst being around
twice as fast at compression and six times faster at decompression.


%package devel
Summary: BZIP2 development headers
Group: Development/Libraries
Requires: libbz21 = %{version}-%{release}

%description devel
bzip2 is a freely available, patent free, high-quality data compressor. This
package contains the header file and static library for using bzip2
compression in applications.


%package -n libbz21
Summary: A high-quality data compression shared library
Group: System Environment/Libraries

%description -n libbz21
bzip2 is a freely available, patent free, high-quality data compressor. It
typically compresses files to within 10% to 15% of the best available
techniques (the PPM family of statistical compressors), whilst being around
twice as fast at compression and six times faster at decompression.
This package contains the bz2 shared library.

%prep
%setup -q


%build
%{__make} %{?_smp_mflags} \
	CFLAGS="-Wall -Winline -D_FILE_OFFSET_BITS=64 $RPM_OPT_FLAGS"
%{__make} %{?_smp_mflags} -f Makefile-libbz2_so \
	CFLAGS="-Wall -Winline -D_FILE_OFFSET_BITS=64 $RPM_OPT_FLAGS"


%check
%{__make} check


%install
%{__make} install PREFIX="${RPM_BUILD_ROOT}/usr" 
%{__install} -oroot -groot libbz2.so* '%{buildroot}%{_libdir}'

# Move some binaries as expected
%{__mkdir_p} '%{buildroot}/bin'
%{__mv} "${RPM_BUILD_ROOT}%{_bindir}"/{bunzip2,bzip2,bzip2recover} \
	"${RPM_BUILD_ROOT}/bin"

# Correct symlinks
pushd '%{buildroot}%{_bindir}'
%{__rm} -f bzcmp bz[ef]grep bzless
%{__ln_s} bzdiff bzcmp
%{__ln_s} bzgrep bzegrep
%{__ln_s} bzgrep bzfgrep
%{__ln_s} bzmore bzless
popd


%files
%defattr(-, root, root)
%doc CHANGES LICENSE README
/bin/bunzip2
%{_bindir}/bzcat
%{_bindir}/bzcmp
%{_bindir}/bzdiff
%{_bindir}/bzegrep
%{_bindir}/bzfgrep
%{_bindir}/bzgrep
/bin/bzip2
/bin/bzip2recover
%{_bindir}/bzless
%{_bindir}/bzmore
%doc %{_mandir}/man1/bzcmp.1*
%doc %{_mandir}/man1/bzdiff.1*
%doc %{_mandir}/man1/bzegrep.1*
%doc %{_mandir}/man1/bzfgrep.1*
%doc %{_mandir}/man1/bzgrep.1*
%doc %{_mandir}/man1/bzip2.1*
%doc %{_mandir}/man1/bzless.1*
%doc %{_mandir}/man1/bzmore.1*


%files devel
%defattr(-, root, root)
%doc CHANGES LICENSE README
%{_includedir}/bzlib.h
%{_libdir}/libbz2.a


%files -n libbz21
%defattr(-, root, root)
%doc CHANGES LICENSE README
%{_libdir}/libbz2.so.1*
