Name: gzip
Version: 1.3.3
Release: 2ev
Summary: The GNU zip compression utility
URL: http://www.gzip.org/
Group: Applications/Archiving
License: GPL-2
Vendor: GNyU-Linux
Source: http://www.gzip.org/%{name}-%{version}.tar.gz
BuildRequires: make, gcc, zlib

%description
gzip (GNU zip) is a compression utility designed to be a replacement for
compress. Its main advantages over compress are much better compression and
freedom from patented algorithms. It has been adopted by the  GNU project and
is now relatively popular on the Internet. gzip was written by Jean-loup
Gailly (jloup@gzip.org), and Mark Adler for the decompression code. 
gzip produces files with a .gz extension. gunzip can decompress files created
by gzip, compress or pack. The detection of the input format is automatic.


%prep
%setup -q


%build
%configure \
	--bindir=/bin \
	--sbindir=/sbin \
	--libdir='/%{_lib}'
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%{__rm} -f %{buildroot}/%{_infodir}/dir


%post
update-info-dir


%preun
update-info-dir


%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog* README* NEWS THANKS TODO
/bin/gunzip
/bin/gzexe
/bin/gzip
/bin/zcat
/bin/zcmp
/bin/zdiff
/bin/zegrep
/bin/zfgrep
/bin/zforce
/bin/zgrep
/bin/zless
/bin/zmore
/bin/znew
%doc %{_infodir}/gzip.info*
%doc %{_mandir}/man1/gunzip.1*
%doc %{_mandir}/man1/gzexe.1*
%doc %{_mandir}/man1/gzip.1*
%doc %{_mandir}/man1/zcat.1*
%doc %{_mandir}/man1/zcmp.1*
%doc %{_mandir}/man1/zdiff.1*
%doc %{_mandir}/man1/zforce.1*
%doc %{_mandir}/man1/zgrep.1*
%doc %{_mandir}/man1/zless.1*
%doc %{_mandir}/man1/zmore.1*
%doc %{_mandir}/man1/znew.1*
