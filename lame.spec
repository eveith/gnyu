Name: lame
Version: 3.98.2
Release: 2ev
Summary: LAME Ain't An MP3 Encoder
URL: http://lame.sf.net/
Group: Applications/Multimedia
License: LGPL-2
Vendor: GNyU-Linux
Source: http://downloads.sourceforge.net/lame/lame-398-2.tar.gz
BuildRequires: make, gcc, nasm, ncurses

%description
LAME is an MPEG Audio Layer III (MP3) encoder licensed under the LGPL.


%prep
%setup -q -n 'lame-398-2'


%build
%configure \
	--enable-nasm \
	 --disable-debug
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR="${RPM_BUILD_ROOT}"


%post
%{__ldconfig}


%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc README* ACM API COPYING ChangeLog HACKING LICENSE STYLEGUIDE TODO USAGE 
%{_bindir}/lame
%dir %{_includedir}/lame
%{_includedir}/lame/lame.h
%{_libdir}/libmp3lame.*
%doc %{_mandir}/man1/lame.1*
%dir %{_datadir}/doc/lame
%dir %{_datadir}/doc/lame/html
%doc %{_datadir}/doc/lame/html/*.*
