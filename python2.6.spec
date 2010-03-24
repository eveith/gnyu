Name: python
Version: 2.6.5
Release: 4.0ev
Summary: A high-level scripting language
URL: http://www.python.org/
Group: Development/Languages
License: Modified CNRI Open Source License
Vendor: GNyU-Linux
Source: http://www.python.org/ftp/python/%{version}/Python-%{version}.tar.bz2
BuildRequires: sed, pkg-config, make, gcc, gcc-g++
BuildRequires: net6, zlib, bzip2, gmp, readline >= 2.1, ncurses, openssl, expat
BuildRequires: libX11, bluez, sqlite, gdbm, libstdc++
Provides: python(abi) = 2.6, python-abi = 2.6, python = %{version}
Requires: python2.6 = %{version}-%{release}
%define __python_requires %nil

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


%package -n python2.6
Summary: Versioned Python executables and paths
Group: Development/Languages

%description -n python2.6
The python2.6 package contains the very core of a Python installation. It is
stripped out into a versioned package to allow different Python major versions
to co-exist happily.


%package -n libpython2.6
Summary: Python interpreter library
Group: System Environment/Libraries

%description -n libpython2.6
The Python library contains not only the core of the interpreter, but also a
lot of C binding code. Software that embedds Python does not neccesarily need
the interpreter executable, but this library.


%package devel
Summary: Python development headers
Group: Development/Languages
Requires: python2.6 = %{version}-%{release}

%description devel
This package contains the development headers needed for compiling software
that uses Python internally.


%prep 
%setup -q -n 'Python-%{version}'


%build
%configure \
	--enable-shared \
	--enable-ipv6 \
	--with-fpectl \
	--with-signal-module \
	--with-cxx="${CXX:-%{_target_platform}-g++}"
%{__make} %{?_smp_mflags}
%{__make} test


%install
%{__make} install DESTDIR='%{buildroot}'

#  fix the #! line in installed files
%{__find} '%{buildroot}' -type f -print0 |
      xargs -0 %{__grep} -l '/usr/local/bin/python' | while read file
do
   %{__sed} -i 's|^#!.*python|#!/usr/bin/env python|' "${file}"
done
%{__find} '%{buildroot}' -type f -print0 |
      xargs -0 %{__grep} -l '/usr/bin/env' | while read file
do
   %{__sed} -i 's|^#!.*python|#!/usr/bin/env python|' "${file}"
done

# Clean up the testsuite - we don't need compiled files for it
%{__find} '%{buildroot}/%{_libdir}/python*/test' \
    -name '*.pyc' -o -name '*.pyo' | xargs %{__rm} -f


%post -n libpython2.6
%{__ldconfig}


%postun -n libpython2.6
%{__ldconfig}


%files
%defattr(-, root, root)
%doc LICENSE README 
%{_bindir}/python
%{_bindir}/pydoc
%{_bindir}/idle
%{_bindir}/2to3
%{_bindir}/smtpd.py
%doc %{_mandir}/man1/python.1*


%files devel
%defattr(-, root, root)
%doc LICENSE README 
%{_bindir}/python-config
%{_bindir}/python?.?-config
%dir %{_includedir}/python?.?
%{_includedir}/python?.?/*.h


%files -n python2.6
%defattr(-, root, root)
%doc LICENSE README 
%{_bindir}/python?.?
%dir %{_libdir}/python?.?
%{_libdir}/python?.?/*


%files -n libpython2.6
%defattr(-, root, root)
%doc LICENSE README 
%{_libdir}/libpython?.?.*
