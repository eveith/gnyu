Name: popt
Version: 1.15
Release: 1ev
Summary: A command-line parameters processing library
URL: http://rpm5.org/
Group: System Environment/Libraries
License: MIT
Vendor: GNyU-Linux
Source: http://rpm5.org/files/popt/popt-%{version}.tar.gz
BuildRequires: make, gcc, gettext

%description
This is the popt(3) command line option parsing library. While it is similiar
to getopt(3), it contains a number of enhancements, including:

        1) popt is fully reentrant
        2) popt can parse arbitrary argv[] style arrays while
           getopt(3) makes this quite difficult
        3) popt allows users to alias command line arguments
        4) popt provides convience functions for parsing strings
           into argv[] style arrays

Complete documentation on popt(3) is available in popt.ps (included in this
tarball), which is excerpted with permission from the book "Linux
Application Development" by Michael K. Johnson and Erik Troan (available
from Addison Wesley in May, 1998).


%prep
	%setup -q


%build
	%configure
	%{__make} %{?_smp_mflags}


%install
	%{__make} install DESTDIR='%{buildroot}'
	%find_lang popt

	[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
		&& %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
	%{__ldconfig}


%postun
	%{__ldconfig}


%files -f popt.lang
	%defattr(-, root, root)
	%doc README ABOUT-NLS ChangeLog CHANGES COPYING popt.ps
	%{_includedir}/popt.h
	%{_libdir}/libpopt.*
	%doc %{_mandir}/man3/popt.3*
