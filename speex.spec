Name: speex
Version: 1.2rc1
Release: 2ev
Summary: An audio codec especially for speech
URL: http://www.speex.org/
Group: System Environment/Libraries
License: BSD
Vendor: GNyU-Linux
Source: http://downloads.us.xiph.org/releases/speex/speex-%{version}.tar.gz
BuildRequires: pkg-config >= 0.9.0, make, gcc, libogg

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
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR="${RPM_BUILD_ROOT}"


%post
%{__ldconfig}

%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc README* AUTHORS COPYING ChangeLog NEWS TODO doc/*.pdf
%{_bindir}/speexdec
%{_bindir}/speexenc
%dir %{_includedir}/speex
%{_includedir}/speex/*.h
%{_libdir}/libspeex*.*
%{_libdir}/pkgconfig/speex.pc
%{_libdir}/pkgconfig/speexdsp.pc
%{_datadir}/aclocal/speex.m4
%doc %{_mandir}/man1/speex*.1*
%dir %{_datadir}/doc/speex
%doc %{_datadir}/doc/speex/manual.pdf
