Name: check
Version: 0.9.8
Release: 1.0
Summary: A unit testing framework for C
URL: http://check.sourceforge.net
Group: Development/Libraries
License: LGPL-2.1
Vendor: GNyU-Linux
Source: http://sourceforge.net/projects/check/files/check/%{version}/check-%{version}.tar.gz
BuildRequires: grep, sed, make, gcc
BuildRequires: eglibc-devel
Requires: libcheck0


%description
heck is a unit testing framework for C. It features a simple interface for
defining unit tests, putting little in the way of the developer. Tests are run
in a separate address space, so Check can catch both assertion failures and
code errors that cause segmentation faults or other signals. The output from
unit tests can be used within source code editors and IDEs.


%files
%defattr(-, root, root)
%doc README NEWS AUTHORS THANKS *ChangeLog COPYING.LESSER


%package -n libcheck0
Summary: A unit testing library in C
Group: Development/Libraries


%description -n libcheck0
heck is a unit test framework for C. It features a simple interface for
defining unit tests, putting little in the way of the developer.  Tests are
run in a separate address space, so Check can catch both assertion failures
and code errors that cause segmentation faults or other signals. The output
from unit tests can be used within source code editors and IDEs.


%files -n libcheck0
%defattr(-, root, root)
%{_libdir}/libcheck.so.0*


%post -n libcheck0 -p %{__ldconfig}
%postun -n libcheck0 -p %{__ldconfig}


%package devel
Summary: A unit testing framework for C
Group: Development/Libraries
Requires: autoconf, pkg-config
Requires: check = %{version}-%{release}


%description devel
heck is a unit test framework for C. It features a simple interface for
defining unit tests, putting little in the way of the developer.  Tests are
run in a separate address space, so Check can catch both assertion failures
and code errors that cause segmentation faults or other signals. The output
from unit tests can be used within source code editors and IDEs.


%files devel
%defattr(-, root root)
%doc README NEWS AUTHORS THANKS *ChangeLog COPYING.LESSER doc/example/

%{_libdir}/libcheck.a
%{_libdir}/libcheck.la
%{_libdir}/libcheck.so

%doc %{_infodir}/check.info*
%{_includedir}/check.h
%{_libdir}/pkgconfig/check.pc
%{_datadir}/aclocal/check.m4


%post devel
if [ "$1" -eq 1 ]; then
    install-info --infodir='%{_infodir}' %{_infodir}/check.info*
fi


%preun devel
if [ "$1" -eq 0 ]; then
    install-info --delete --infodir='%{_infodir}' %{_infodir}/check.info*
fi


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


%check
%{__make} check
