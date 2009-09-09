Name: faad2
Version: 2.7
Release: 2ev
Summary: An HE, LC, MAIN and LTP profile, MPEG2 and MPEG-4 AAC decoder
URL: http://faac.sf.net/
Group: System Environment/Libraries
License: GPL-2
Vendor: GNyU-Linux
Source: http://downloads.sourceforge.net/faac/faad2-%{version}.tar.bz2
BuildRequires: autoconf, make, gcc-core

%description
FAAC and FAAD2 stand for Freeware Advanced Audio Coder and Decoder 2
respectively, collectively make up an open source implementation of AAC.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR="${RPM_BUILD_ROOT}"
%{__mv} '%{buildroot}/%{_mandir}/manm' '%{buildroot}/%{_mandir}/man1'
%{__mv} '%{buildroot}/%{_mandir}/man1/faad.man' \
	'%{buildroot}/%{_mandir}/man1/faad.1'


%post
%{__ldconfig}


%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog README* TODO NEWS
%{_bindir}/faad
%{_includedir}/faad.h
%{_includedir}/mp4ff.h
%{_includedir}/mp4ffint.h
%{_includedir}/neaacdec.h
%{_libdir}/libfaad.*
%{_libdir}/libmp4ff.*
%doc %{_mandir}/man1/faad.1*
