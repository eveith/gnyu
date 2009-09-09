Name: speex
Version: 1.2beta2
Release: 1ev
Summary: An audio codec especially for speech
URL: http://www.speex.org/
Group: System Environment/Libraries
License: BSD
Vendor: MSP Slackware
Source: http://downloads.us.xiph.org/releases/speex/speex-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-core, libogg

%description
Speex is an Open Source/Free Software patent-free audio compression format
designed for speech. The Speex Project aims to lower the barrier of entry for
voice applications by providing a free alternative to expensive proprietary
speech codecs. Moreover, Speex is well-adapted to Internet applications and
provides useful features that are not present in most other codecs.


%prep
%setup -q


%build
%configure
make %{_smp_mflags}


%install
[ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT" mandir="%{_mandir}"
rm -rf "$RPM_BUILD_ROOT/%{_datadir}/doc"

[ -e "${RPM_BUILD_ROOT}/%{_infodir}/dir" ] \
    && rm -f "${RPM_BUILD_ROOT}/%{_infodir}/dir"


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%doc README* AUTHORS COPYING ChangeLog NEWS TODO doc/*.pdf
%{_bindir}/speexdec
%{_bindir}/speexenc
%{_includedir}/speex/
%{_libdir}/libspeex*.*
%{_libdir}/pkgconfig/speex.pc
%{_datadir}/aclocal/speex.m4
%{_mandir}/man1/speex*.1*
