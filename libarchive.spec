Name: libarchive
Version: 2.7.0
Release: 1ev
Summary: A library and command line tools for reading/writing archives
URL: http://code.google.com/p/libarchive/
Group: System Environment/Libraries
License: BSD
Vendor: GNyU-Linux
Source: http://libarchive.googlecode.com/files/libarchive-%{version}.tar.gz
BuildRequires: make, gcc, bison, zlib, bzip2, lzma, openssl, libattr

%description
Libarchive is a reusable C library for reading and writing a variety of
streaming archive formats. It features: 
   - Supports a variety of archive and compression formats. 
   - Robust automatic format detection, including archive/compression
     combinations such as tar.gz. 
   - Zero-copy internal architecture for high performance. 
   - Streaming architecture eliminates all limits on size of archive, limits
     on entry sizes depend on particular formats. 
   - Growing test suite to verify correctness of new ports. 
   - Works on all POSIX-like systems; is regularly tested on both FreeBSD and
     Linux. 
   - Supports Windows, including Cygwin and Visual Studio.


%prep
	%setup -q


%build
	%configure
	%{__make} %{?_smp_mflags}


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
	%doc COPYING NEWS PROJECTS README
	%{_bindir}/bsdcpio
	%{_bindir}/bsdtar
	%{_includedir}/archive.h
	%{_includedir}/archive_entry.h
	%{_libdir}/libarchive.*
	%doc %{_mandir}/man1/bsdcpio.1*
	%doc %{_mandir}/man1/bsdtar.1*
	%doc %{_mandir}/man3/archive_entry.3*
	%doc %{_mandir}/man3/archive_read.3*
	%doc %{_mandir}/man3/archive_read_disk.3*
	%doc %{_mandir}/man3/archive_util.3*
	%doc %{_mandir}/man3/archive_write.3*
	%doc %{_mandir}/man3/archive_write_disk.3*
	%doc %{_mandir}/man3/libarchive.3*
	%doc %{_mandir}/man3/libarchive_internals.3*
	%doc %{_mandir}/man5/cpio.5*
	%doc %{_mandir}/man5/libarchive-formats.5*
	%doc %{_mandir}/man5/mtree.5*
	%doc %{_mandir}/man5/tar.5*
