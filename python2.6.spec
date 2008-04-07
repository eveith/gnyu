Name: python
Version: 2.4.3
Release: 1ev
Summary: A high-level scripting language
URL: http://www.python.org/
Group: Development/Languages
License: Modified CNRI Open Source License
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: http://www.python.org/ftp/python/2.4.3/Python-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: gcc-core, make >= 3.79.1, sed, findutils
Provides: python = %{version}
Provides: python(abi) = 2.4, python-abi = 2.4
AutoReq: 0
AutoProv: 0

%description
Python is an interpreted, interactive, object-oriented programming
language.  It incorporates modules, exceptions, dynamic typing, very high
level dynamic data types, and classes. Python combines remarkable power
with very clear syntax. It has interfaces to many system calls and
libraries, as well as to various window systems, and is extensible in C or
C++. It is also usable as an extension language for applications that need
a programmable interface.  Finally, Python is portable: it runs on many
brands of UNIX, on PCs under Windows, MS-DOS, and OS/2, and on the
Mac.


%prep 
%setup -q -n Python-%{version}


%build
%configure --enable-shared --enable-ipv6
make BASECFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"


%install
%makeinstall
rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir

#  fix the #! line in installed files
find "$RPM_BUILD_ROOT" -type f -print0 |
      xargs -0 grep -l /usr/local/bin/python | while read file
do
   sed -i 's|^#!.*python|#!/bin/env python|' "$file"
done
find "$RPM_BUILD_ROOT" -type f -print0 |
      xargs -0 grep -l /usr/bin/env | while read file
do
   sed -i 's|^#!.*python|#!/bin/env python|' "$file"
done

# Clean up the testsuite - we don't need compiled files for it
find ${RPM_BUILD_ROOT}/%{_libdir}/python*/test \
    -name "*.pyc" -o -name "*.pyo" | xargs rm -f

find ${RPM_BUILD_ROOT}/%{_libdir}/python* -type d | \
	sed "s|$RPM_BUILD_ROOT|%dir |" >> dynfiles
find ${RPM_BUILD_ROOT}/%{_libdir}/python* -type f | \
	sed "s|$RPM_BUILD_ROOT||" >> dynfiles

%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
rm -rf ${RPM_BUILD_ROOT}


%files -f dynfiles
%defattr(-, root, root)
%doc LICENSE README 
%{_bindir}/python2.4
%{_bindir}/pydoc
%{_bindir}/idle
%{_bindir}/smtpd.py
%{_bindir}/python
%{_libdir}/libpython2.4.*
%{_includedir}/python2.4/
%dir %{_libdir}/python2.4
