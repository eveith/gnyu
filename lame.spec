Name: lame
Version: 3.97
Release: 1ev
Summary: LAME Ain't An MP3 Encoder
URL: http://lame.sf.net/
Group: Applications/Multimedia
License: LGPL
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: http://downloads.sourceforge.net/lame/lame-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: gcc-core, make >= 3.79.1, nasm
Provides: libtool(%{_libdir}/libmp3lame.la)

%description
LAME is an MPEG Audio Layer III (MP3) encoder licensed under the LGPL.


%prep
%setup -q


%build
%configure --enable-nasm --disable-mp3x --enable-mp3rtp --disable-debug \
	--with-fileio=lame
make


%install
make install DESTDIR="$RPM_BUILD_ROOT"
rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-, root, root)
%doc README* ACM API COPYING ChangeLog HACKING LICENSE STYLEGUIDE TODO USAGE 
%doc %{_datadir}/doc/%{name}/
%{_bindir}/lame
%{_bindir}/mp3rtp
%{_includedir}/lame/
%{_libdir}/libmp3lame.*
%{_mandir}/man1/lame.1*
