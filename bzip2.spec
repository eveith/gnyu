Name: bzip2
Version: 1.0.5
Release: 1ev
Summary: A high-quality data compressor
URL: http://www.bzip.org/
Group: Applications/Archiving
License: BSD
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: http://www.bzip.org/%{version}/%{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: gcc, make >= 3.79.1

%description
bzip2 is a freely available, patent free, high-quality data
compressor. It typically compresses files to within 10% to 15% of the best
available techniques (the PPM family of statistical compressors), whilst being
around twice as fast at compression and six times faster at decompression.

%prep
%setup -q


%build
%{__make} %{?_smp_mflags} \
	CFLAGS="-Wall -Winline -D_FILE_OFFSET_BITS=64 $RPM_OPT_FLAGS"


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} PREFIX="${RPM_BUILD_ROOT}/usr" 
%{__rm} -f ${RPM_BUILD_ROOT}/%{_infodir}/dir

# Move some binaries as expected
%{__mkdir_p} ${RPM_BUILD_ROOT}/bin
%{__mv} ${RPM_BUILD_ROOT}/%{_bindir}/{bunzip2,bzip2,bzip2recover} \
	${RPM_BUILD_ROOT}/bin

# Correct symlinks
pushd %{buildroot}/%{_bindir}
%{__rm} -f bzcmp bz[ef]grep bzless
%{__ln_s} bzdiff bzcmp
%{__ln_s} bzgrep bzegrep
%{__ln_s} bzgrep bzfgrep
%{__ln_s} bzmore bzless
popd


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


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
%{_includedir}/bzlib.h
%{_libdir}/libbz2.a
%{_mandir}/man1/bzcmp.1.gz
%{_mandir}/man1/bzdiff.1.gz
%{_mandir}/man1/bzegrep.1.gz
%{_mandir}/man1/bzfgrep.1.gz
%{_mandir}/man1/bzgrep.1.gz
%{_mandir}/man1/bzip2.1.gz
%{_mandir}/man1/bzless.1.gz
%{_mandir}/man1/bzmore.1.gz
