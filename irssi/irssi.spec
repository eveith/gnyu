Name: irssi
Version: 0.8.12
Release: 1ev
Summary: A command-line IRC client
URL: http://www.irssi.org/
Group: Applications/Communications
License: GPL-2
Vendor: GNyU-Linux
Source: http://www.irssi.org/files/irssi-%{version}.tar.bz2
BuildRequires: make, gcc, pkg-config >= 0.7, glib2 >= 2.0.0, openssl

%description
Irssi is a terminal based IRC client for UNIX systems. It also supports SILC
and ICB protocols via plugins.


%prep
%setup -q


%build
%configure \
	--with-proxy \
	--enable-ipv6 \
	--with-perl-lib=vendor
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%{__rm} -rf '%{buildroot}/%{_libdir}/perl5/%{_perl_version}'
%{__rm} -rf '%{buildroot}/%{_datadir}/doc'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post

%postun


%files
%defattr(-, root, root)
%doc README COPYING NEWS TODO AUTHORS ChangeLog
%config %{_sysconfdir}/irssi.conf
%{_bindir}/irssi
%{_includedir}/irssi/
%{_libdir}/irssi/
%{perl_vendorarch}/Irssi.pm
%{perl_vendorarch}/Irssi/
%{perl_vendorarch}/auto/*
%dir %{_datadir}/irssi
%{_datadir}/irssi/*
%doc %{_mandir}/man1/irssi.1*
