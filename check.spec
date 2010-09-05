Name: check
Version: 0.9.8
Release: 1.0ev
Summary: A unit testing framework for C
URL: http://check.sourceforge.net
Group: Development/Libraries
License: LGPL-2.1
Vendor: GNyU-Linux
Source: http://sourceforge.net/projects/check/files/check/%{version}/check-%{version}.tar.gz
BuildRequires: make, gcc
Requires: autoconf, pkg-config

%description
heck is a unit testing framework for C. It features a simple interface for
defining unit tests, putting little in the way of the developer. Tests are run
in a separate address space, so Check can catch both assertion failures and
code errors that cause segmentation faults or other signals. The output from
unit tests can be used within source code editors and IDEs.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%{__rm_rf} '%{buildroot}%{_datadir}/doc'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
	&& %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
%{__ldconfig}


%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc README NEWS AUTHORS THANKS *ChangeLog COPYING.LESSER doc/example/
%{_includedir}/check.h
%{_libdir}/libcheck.*
%{_libdir}/pkgconfig/check.pc
%{_datadir}/aclocal/check.m4
%doc %{_infodir}/check.info*
