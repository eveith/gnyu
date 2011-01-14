Name: autoconf
Version: 2.65
Release: 2.0ev
Summary: A package of M4 macros to produce scripts to automatically configure sourcecode
URL: http://www.gnu.org/software/autoconf/
Group: Development/Tools
License: GPL-2
Vendor: GNyU-Linux
Source: http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.bz2
BuildRequires: perl >= 5.5, m4, automake >= 1.10, make,
BuildArch: noarch

%description
Autoconf is an extensible package of m4 macros that produce shell scripts to
automatically configure software source code packages. These scripts can adapt
the package to many kinds of UNIX-like systems without manual user
intervention.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR="${RPM_BUILD_ROOT}"
%{__rm_rf} "${RPM_BUILD_ROOT}/%{_infodir}/dir"

# Provided by binutils
%{__rm_rf} "${RPM_BUILD_ROOT}/%{_infodir}/"standards.info*


%post
update-info-dir


%postun
update-info-dir


%files
%defattr(-, root, root)
%doc AUTHORS BUGS COPYING ChangeLog* NEWS README THANKS TODO
%{_bindir}/autoconf
%{_bindir}/autoheader
%{_bindir}/autom4te
%{_bindir}/autoreconf
%{_bindir}/autoscan
%{_bindir}/autoupdate
%{_bindir}/ifnames
%{_datadir}/autoconf/*
%doc %{_mandir}/man1/autoconf.1*
%doc %{_mandir}/man1/autoheader.1*
%doc %{_mandir}/man1/autom4te.1*
%doc %{_mandir}/man1/autoreconf.1*
%doc %{_mandir}/man1/autoscan.1*
%doc %{_mandir}/man1/autoupdate.1*
%doc %{_mandir}/man1/config.guess.1*
%doc %{_mandir}/man1/config.sub.1*
%doc %{_mandir}/man1/ifnames.1*
%dir %{_datadir}/autoconf
%doc %{_infodir}/autoconf.info*
