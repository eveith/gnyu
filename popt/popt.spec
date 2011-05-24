Name: popt
Version: 1.16
Release: 1.0
Summary: A command-line parameters processing library
URL: http://rpm5.org
Group: System Environment/Libraries
License: MIT
Source: http://rpm5.org/files/popt/popt-%{version}.tar.gz
BuildRequires: grep, sed, make, gcc
BuildRequires: eglibc-devel
BuildRequires: gettext-tools
Requires: libpopt0 = %{version}-%{release}

%description
This is the popt(3) command line option parsing library. While it is similiar
to getopt(3), it contains a number of enhancements, including:
  - popt is fully reentrant
  - popt can parse arbitrary argv[] style arrays while
    getopt(3) makes this quite difficult
  - popt allows users to alias command line arguments
  - popt provides convience functions for parsing strings
    into argv[] style arrays
Complete documentation on popt(3) is available in popt.ps, which is excerpted
with permission from the book "Linux Application Development" by Michael K.
Johnson and Erik Troan (available from Addison Wesley in May, 1998).


%package devel
Summary: popt development headers
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This is the popt(3) command line option parsing library. This package contains
development headers, API documentation and a pkgconfig .pc file for
development with popt.


%package -n libpopt0
Summary: A command-line parameters processing library
Group: System Environment/Libraries

%description -n libpopt0
This is the popt(3) command line option parsing library. While it is similiar
to getopt(3), it contains a number of enhancements, including:
  - popt is fully reentrant
  - popt can parse arbitrary argv[] style arrays while
    getopt(3) makes this quite difficult
  - popt allows users to alias command line arguments
  - popt provides convience functions for parsing strings
    into argv[] style arrays
Complete documentation on popt(3) is available in popt.ps, which is excerpted
with permission from the book "Linux Application Development" by Michael K.
Johnson and Erik Troan (available from Addison Wesley in May, 1998).


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%find_lang popt


%post -n libpopt0 -p %{__ldconfig}
%postun -n libpopt0 -p %{__ldconfig}


%files
%defattr(-, root, root)
%doc README ABOUT-NLS CHANGES COPYING


%files -n libpopt0 -f popt.lang
%defattr(-, root, root)
%doc README ABOUT-NLS CHANGES COPYING
%{_libdir}/libpopt.so.0*


%files devel
%defattr(-, root, root)
%doc README ABOUT-NLS CHANGES COPYING popt.ps
%{_libdir}/libpopt.so
%{_libdir}/libpopt.la
%{_libdir}/libpopt.a
%{_libdir}/pkgconfig/popt.pc
%{_includedir}/popt.h
%doc %{_mandir}/man3/popt.3*
