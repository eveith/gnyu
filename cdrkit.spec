Name: cdrkit
Version: 1.1.8
Release: 1ev
Summary: A portable command-line CD/DVD recorder software
URL: http://www.cdrkit.org/
Group: Applications/System
License: GPL-2
Vendor: GNyU-Linux
Source: http://cdrkit.org/releases/cdrkit-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: coreutils, grep, sed, make, gcc, cmake, kernel-headers, libcap2
BuildRequires: perl, zlib, file
Obsoletes: cdrecord, cdrecord-devel, mkisofs

%description
cdrkit is a suite of programs for recording CDs and DVDs, blanking CD-RW 
media, creating ISO-9660 filesystem images, extracting audio CD data, and 
more. The programs included in the cdrkit package were originally derived 
from several sources, most notably mkisofs by Eric Youngdale and others, 
cdda2wav by Heiko Eissfeldt, and cdrecord by Jörg Schilling. However, cdrkit 
is not affiliated with any of these authors; it is now an independent project.


%prep
%setup -q
%{__sed} -i -e 's,#!/usr/local/bin/perl,%{__perl},' doc/icedax/tracknames.pl


%build
%{cmake} .
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'

%{__mv} '%{buildroot}/%{_prefix}/share/man' '%{buildroot}/%{_mandir}' ||:

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc doc/*
%doc ABOUT Changelog COPYING FAQ FORK START TODO VERSION
%{_bindir}/cdda2mp3
%{_bindir}/cdda2ogg
%{_bindir}/devdump
%{_bindir}/dirsplit
%{_bindir}/genisoimage
%{_bindir}/icedax
%{_bindir}/isodebug
%{_bindir}/isodump
%{_bindir}/isoinfo
%{_bindir}/isovfy
%{_bindir}/pitchplay
%{_bindir}/readmult
%{_bindir}/readom
%{_bindir}/wodim
%{_sbindir}/netscsid
%doc %{_mandir}/man1/cdda2ogg.1*
%doc %{_mandir}/man1/devdump.1*
%doc %{_mandir}/man1/dirsplit.1*
%doc %{_mandir}/man1/genisoimage.1*
%doc %{_mandir}/man1/icedax.1*
%doc %{_mandir}/man1/isodebug.1*
%doc %{_mandir}/man1/isodump.1*
%doc %{_mandir}/man1/isoinfo.1*
%doc %{_mandir}/man1/isovfy.1*
%doc %{_mandir}/man1/list_audio_tracks.1*
%doc %{_mandir}/man1/pitchplay.1*
%doc %{_mandir}/man1/readmult.1*
%doc %{_mandir}/man1/readom.1*
%doc %{_mandir}/man1/wodim.1*
%doc %{_mandir}/man5/genisoimagerc.5*
