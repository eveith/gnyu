Name: python2.6
Version: 2.6
Release: 2ev
Summary: A high-level scripting language
URL: http://www.python.org/
Group: Development/Languages
License: Modified CNRI Open Source License
Vendor: GNyU-Linux
Source: http://www.python.org/ftp/python/2.4.3/Python-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: gcc, gcc-g++, make >= 3.79.1, openssl, libX11
BuildRequires: zlib, ncurses, libstdc++, readline
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
%setup -q -n Python-%{version}


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
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'

#  fix the #! line in installed files
find '%{buildroot}' -type f -print0 |
      xargs -0 %{__grep} -l '/usr/local/bin/python' | while read file
do
   %{__sed} -i 's|^#!.*python|#!/usr/bin/env python|' "${file}"
done
find '%{buildroot}' -type f -print0 |
      xargs -0 %{__grep} -l '/usr/bin/env' | while read file
do
   %{__sed} -i 's|^#!.*python|#!/usr/bin/env python|' "${file}"
done

# Clean up the testsuite - we don't need compiled files for it
find '%{buildroot}/%{_libdir}/python*/test' \
    -name '*.pyc' -o -name '*.pyo' | xargs %{__rm} -f

find '%{buildroot}/%{_libdir}'/python* -type d | \
	%{__sed} 's|%{buildroot}|%dir |' >> dynfiles
find '%{buildroot}/%{_libdir}'/python* -type f | \
	%{__sed} 's|%{buildroot}||' >> dynfiles

%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files -f dynfiles
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
%{_includedir}/python?.?/
%doc %{_mandir}/man1/python.1*
