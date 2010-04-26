Name: beecrypt
Version: 4.1.2
Release: 1ev
Summary: A strong and fast cryptography toolkit
URL: http://beecrypt.sf.net/
Group: System Environment/Libraries
License:  GPL/LGPL
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: http://downloads.sourceforge.net/beecrypt/beecrypt-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root
%define py_version %(echo $(python -c "import sys; print sys.version[0:3]"))
BuildRequires: make >= 3.79.1, gcc-core, gcc-g++, libstdc++, gcc-java, libgcj
BuildRequires: python >= %py_version

%description
BeeCrypt is an ongoing project to provide a strong and fast cryptography
toolkit. Includes entropy sources, random generators, block ciphers, hash
functions, message authentication codes, multiprecision integer routines, and
public key primitives.


%prep
%setup -q


%build
%configure --with-cplusplus --with-java --with-python
make


%install
%makeinstall
rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%clean
rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-, root, root)
%doc AUTHORS BENCHMARKS BUGS CONTRIBUTORS COPYING* NEWS README*
%{_includedir}/beecrypt/
%{_libdir}/libbeecrypt.*
%{_libdir}/libbeecrypt_java.*
