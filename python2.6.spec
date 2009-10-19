Name: python2.6
Version: 2.6.3
Release: 3.0ev
Summary: A high-level scripting language
URL: http://www.python.org/
Group: Development/Languages
License: Modified CNRI Open Source License
Vendor: GNyU-Linux
Source: http://www.python.org/ftp/python/%{version}/Python-%{version}.tar.bz2
BuildRequires: pkg-config, make, gcc, gcc-g++, 
BuildRequires: zlib, bzip2, gmp, readline, ncurses, openssl, expat
BuildRequires: libX11, bluez, sqlite, gdbm, libstdc++
Provides: python(abi) = 2.6, python-abi = 2.6, python = %{version}
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


%prep 
%setup -q -n 'Python-%{version}'


%build
%configure \
	--enable-shared \
	--enable-ipv6 \
	--with-threads \
	--with-fpectl \
	--with-signal-module \
	--with-cxx='%{_target_platform}-g++'
%{__make} %{?_smp_mflags} BASECFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"


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


%post
%{__ldconfig}


%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc LICENSE README 
%{_bindir}/python
%{_bindir}/python?.?
%{_bindir}/python-config
%{_bindir}/python?.?-config
%{_bindir}/pydoc
%{_bindir}/idle
%{_bindir}/2to3
%{_bindir}/smtpd.py
%{_libdir}/libpython?.?.*
%dir %{_libdir}/python?.?
%{_libdir}/python?.?/*
%dir %{_includedir}/python?.?
%{_includedir}/python?.?/*.h
%doc %{_mandir}/man1/python.1*
