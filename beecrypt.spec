Name: beecrypt
Version: 4.1.2
Release: 1.1ev
Summary: A strong and fast cryptography toolkit
URL: http://beecrypt.sf.net/
Group: System Environment/Libraries
License:  GPL-2, LGPL-2.1
Vendor: GNyU-Linux
Source: http://downloads.sourceforge.net/beecrypt/beecrypt-%{version}.tar.gz
BuildRequires: grep, awk, libtool, make, gcc, gcc-g++, libstdc++
BuildRequires: python
Requires: libbeecrypt6 = %{version}-%{release}

%description
BeeCrypt is an ongoing project to provide a strong and fast cryptography
toolkit. Includes entropy sources, random generators, block ciphers, hash
functions, message authentication codes, multiprecision integer routines, and
public key primitives.


%package -n libbeecrypt6
Summary: A strong and fast cryptography toolkit
Group: System Environment/Libraries

%description
BeeCrypt is an ongoing project to provide a strong and fast cryptography
toolkit. Includes entropy sources, random generators, block ciphers, hash
functions, message authentication codes, multiprecision integer routines, and
public key primitives.


%package -n libbeecrypt_java0
Summary: Java glue for libbeecrypt
Group: System Environment/Libraries
Provides: beecrypt-java = %{version}-%{release}

%description -n libbeecrypt_java0
This package contains the glue code to use the BeeCrypt C/C++ functions from
Java.


%package devel
Summary: Development headers for beecrypt
Group: Development/Libraries
Requires: beecrypt = %{version}-%{release}

%description devel
Contains development headers needed when compiling applications that use
beecrypt.


%package python
Summary: Python bindings to beecrypt
Group: Development/Libraries
Requires: beecrypt = %{version}-%{release}

%description python
This package contains the necessary python binding code that allows using
beecrypt's functions from python scripts.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%{__rm} '%{buildroot}/%{_libdir}'/libbeecrypt*.so


%post -n libbeecrypt6
%{__ldconfig}


%postun -n libbeecrypt6
%{__ldconfig}


%post -n libbeecrypt_java0
%{__ldconfig}


%postun -n libbeecrypt_java0
%{__ldconfig}


%files
%defattr(-, root, root)
%doc AUTHORS BENCHMARKS BUGS CONTRIBUTORS COPYING* NEWS README*


%files -n libbeecrypt6
%defattr(-, root, root)
%{_libdir}/libbeecrypt.so.6*


%files -n libbeecrypt_java0
%defattr(-, root, root)
%{_libdir}/libbeecrypt_java.so.0*


%files devel
%defattr(-, root, root)
%dir %{_includedir}/beecrypt
%{_includedir}/beecrypt/*.h
%{_libdir}/libbeecrypt*.a
%{_libdir}/libbeecrypt*.la


%files python
%defattr(-, root, root)
%{python_sitelib}/_bc.*
