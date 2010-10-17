Name: automake
Version: 1.11.1
Release: 1.0ev
Summary: A tool for generating Makefile.in
URL: http://www.gnu.org/software/automake
Group: Development/Tools
License: GPL-2
Source: http://ftp.gnu.org/gnu/automake/automake-%{version}.tar.bz2
BuildRequires: make >= 3.79.1, sed, autoconf >= 2.62, perl >= 5.8.2
Requires: perl >= 5.8.2
ExclusiveArch: noarch
BuildArch: noarch

%description
This is Automake, a Makefile generator.  It was inspired by the 4.4BSD
make and include files, but aims to be portable and to conform to the
GNU Coding Standards for Makefile variables and targets.
Automake is a Perl script.  The input files are called Makefile.am.
The output files are called Makefile.in; they are intended for use
with Autoconf.


%prep
%setup -q


%build
%configure
%{__make} %{_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%{__rm} '%{buildroot}%{_infodir}/dir' ||:
%{__mkdir_p} '%{buildroot}%{_datadir}/aclocal'


%post
update-info-dir
/sbin/ldconfig


%preun
update-info-dir
/sbin/ldconfig


%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog* INSTALL README THANKS NEWS TODO
%{_bindir}/automake
%{_bindir}/aclocal
%{_bindir}/automake-*
%{_bindir}/aclocal-*
%doc %{_mandir}/man1/automake*.1*
%doc %{_mandir}/man1/aclocal*.1*
%doc %{_infodir}/automake.info*
%dir %{_datadir}/aclocal
%dir %{_datadir}/aclocal-*
%{_datadir}/aclocal-*/*.m4
%dir %{_datadir}/automake-*
%{_datadir}/automake-*/*
%dir %{_datadir}/doc/automake
%doc %{_datadir}/doc/automake/*
