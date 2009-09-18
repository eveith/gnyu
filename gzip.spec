Name: gzip
Version: 1.3.3
Release: 1ev
Summary: The GNU zip compression utility
URL: http://www.gzip.org/
Group: Applications/Archiving
License: GPL
Vendor: MSP Slackware
Source: http://www.gzip.org/%{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: zlib, gcc-core, make >= 3.79.1

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
	--libdir=/%{_lib}
%{__make} %{_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%{__rm} -f %{buildroot}/%{_infodir}/dir


%post
update-info-dir

%preun
update-info-dir


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


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
%{_infodir}/gzip.info.gz
%{_mandir}/man1/gunzip.1.gz
%{_mandir}/man1/gzexe.1.gz
%{_mandir}/man1/gzip.1.gz
%{_mandir}/man1/zcat.1.gz
%{_mandir}/man1/zcmp.1.gz
%{_mandir}/man1/zdiff.1.gz
%{_mandir}/man1/zforce.1.gz
%{_mandir}/man1/zgrep.1.gz
%{_mandir}/man1/zless.1.gz
%{_mandir}/man1/zmore.1.gz
%{_mandir}/man1/znew.1.gz
