Name: python-sip
Version: 4.8.1
Release: 1ev
Summary: A tool to generate Python bindings to a C/C++ library
URL: http://www.riverbankcomputing.co.uk/software/sip/
Group: System Environment/Libraries
License: Python
Vendor: GNyU-Linux
Source: http://www.riverbankcomputing.co.uk/static/Downloads/sip4/sip-%{version}.tar.gz
BuildRequires: python, make, gcc, gcc-g++, libstdc++

%description
One of the features of Python that makes it so powerful is the ability to take
existing libraries, written in C or C++, and make them available as Python
extension modules. Such extension modules are often called bindings for the
library.  SIP is a tool that makes it very easy to create Python bindings for
C and C++ libraries. It was originally developed to create PyQt, the Python
bindings for the Qt toolkit, but can be used to create bindings for any C or
C++ library.  SIP comprises a code generator and a Python module. The code
generator processes a set of specification files and generates C or C++ code
which is then compiled to create the bindings extension module. The SIP Python
module provides support functions to the automatically generated code.  The
specification files contains a description of the interface of the C or C++
library, i.e. the classes, methods, functions and variables. The format of a
specification file is almost identical to a C or C++ header file, so much so
that the easiest way of creating a specification file is to edit the
corresponding header file.  SIP makes it easy to exploit existing C or C++
libraries in a productive interpretive programming environment. SIP also makes
it easy to take a Python application (maybe a prototype) and selectively
implement parts of the application (maybe for performance reasons) in C or
C++.


%prep
	%setup -q -n 'sip-%{version}'


%build
	%{__python} configure.py \
		CFLAGS="${CFLAGS:-%{optflags}}" \
		CXXFLAGS="${CXXFLAGS:-%{optflags}}" \
		CC="${CC:-%{_target_platform}-gcc}" \
		CXX="${CXX:-%{_target_platform}-g++}"
	%{__make} %{?_smp_mflags}


%install
	%{__make} install DESTDIR='%{buildroot}'
	%{__mkdir_p} '%{buildroot}/%{_datadir}/sip'


%files
	%defattr(-, root, root)
	%doc LICENSE NEWS README ChangeLog
	%{_bindir}/sip
	%{_includedir}/python*/sip.h
	%{python_sitelib}/sip.so
	%{python_sitelib}/sipconfig.py
	%{python_sitelib}/sipdistutils.py
	%dir %{_datadir}/sip
