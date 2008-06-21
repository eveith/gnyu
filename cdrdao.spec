Name: cdrdao
Version: 1.2.2
Release: 1ev
Summary: Disk-At-Once Recording of Audio and Data CD-Rs/CD-RWs
URL: http://cdrdao.sf.net/
Group: Applications/System
License: GPL-2
Vendor: GNyU-Linux
Source: http://downloads.sourceforge.net/cdrdao/cdrdao-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: coreutils, grep, sed, make, gcc-g++, libstdc++

%description
Cdrdao records audio or data CD-Rs in disk-at-once (DAO) mode based on 
a textual description of the CD contents (toc-file).


%prep
%setup -q


%build
%configure \
	--without-lame \
	--without-xdao
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING CREDITS README* NEWS
%attr(4711, root, root) %{_bindir}/cdrdao
%{_bindir}/cue2toc
%{_bindir}/toc2cddb
%{_bindir}/toc2cue
%doc %{_mandir}/man1/cdrdao.1.gz
%doc %{_mandir}/man1/cue2toc.1.gz
%{_datadir}/cdrdao/
