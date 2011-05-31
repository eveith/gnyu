Name: pcre
Version: 8.12
Release: 1.0
Summary: Perl5 compatible regular expressions for other programs
URL: http://www.pcre.org/
Group: System Environment/Libraries
License: BSD 
Vendor: GNyU-Linux
Source: ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/%{name}-%{version}.tar.bz2
Patch: pcre-pcreposix-glibc-conflict.patch
BuildRequires: grep, sed, make >= 3.79.1, gcc, gcc-g++
BuildRequires: eglibc-devel, libstdc++-devel
BuildRequires: bzip2-devel, zlib-devel, pkg-config

%description
The PCRE library is a set of functions that implement regular expression
pattern matching using the same syntax and semantics as Perl 5. PCRE has its
own native API, as well as a set of wrapper functions that correspond to the
POSIX regular expression API. The PCRE library is free, even for building
commercial software.
PCRE was originally written for the Exim MTA, but is now used by many
high-profile open source projects, including Apache, PHP, KDE, Postfix,
Analog, and Nmap. Some other interesting projects using PCRE include Ferite,
Onyx, Hypermail, Leafnode, and Askemos.


%package devel
Summary: Perl 5 Compatible Regular Expression Library
Group: Development/Languages
Requires: %{name} = %{version}-%{release}

%description devel
This is a library of functions to support regular expressions whose syntax and
semantics are as close as possible to those of the Perl 5 language.  This
package contains the development files, including headers, static libraries,
and documentation.


%package -n libpcre0
Summary: Perl 5 Compatible Regular Expression Library - development files
Group: System Environment/Libraries

%description -n libpcre0
This is a library of functions to support regular expressions whose syntax and
semantics are as close as possible to those of the Perl 5 language.
This package contains the runtime libraries.


%package -n libpcrecpp0
Summary: Perl 5 Compatible Regular Expression Library - C++ runtime
Group: System Environment/Libraries

%description -n libpcrecpp0
This is a C++ library of functions to support regular expressions whose syntax
and semantics are as close as possible to those of the Perl 5 language.
This package contains the C++ runtime library.


%prep
%setup -q
%patch0 -p1


%build
%configure \
	--enable-utf8 \
	--enable-unicode-properties \
	--enable-pcregrep-libz \
	--enable-pcregrep-libbz2
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'


%check
%{__make} check


%post -n libpcre0 -p %{__ldconfig}
%postun -n libpcre0 -p %{__ldconfig}
%post -n libpcrecpp0 -p %{__ldconfig}
%postun -n libpcrecpp0 -p %{__ldconfig}


%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog* NEWS README LICENCE NON-UNIX-USE
%{_bindir}/pcregrep
%{_bindir}/pcretest
%doc %{_mandir}/man1/pcregrep.1*
%doc %{_mandir}/man1/pcretest.1*


%files devel
%doc AUTHORS COPYING ChangeLog* NEWS README LICENCE NON-UNIX-USE
%doc doc/html
%{_bindir}/pcre-config
%{_includedir}/pcre.h
%{_includedir}/pcre_scanner.h
%{_includedir}/pcre_stringpiece.h
%{_includedir}/pcrecpp.h
%{_includedir}/pcrecpparg.h
%{_includedir}/pcreposix.h
%{_libdir}/libpcre.so
%{_libdir}/libpcre.la
%{_libdir}/libpcre.a
%{_libdir}/libpcreposix.so
%{_libdir}/libpcreposix.la
%{_libdir}/libpcreposix.a
%{_libdir}/libpcrecpp.so
%{_libdir}/libpcrecpp.la
%{_libdir}/libpcrecpp.a
%{_libdir}/pkgconfig/libpcre.pc
%{_libdir}/pkgconfig/libpcreposix.pc
%{_libdir}/pkgconfig/libpcrecpp.pc
%doc %{_mandir}/man1/pcre-config.1*
%doc %{_mandir}/man3/pcre*.3*
%dir %{_datadir}/doc/pcre
%doc %{_datadir}/doc/pcre/*


%files -n libpcre0
%doc AUTHORS COPYING ChangeLog* NEWS README LICENCE NON-UNIX-USE
%{_libdir}/libpcre.so.0*
%{_libdir}/libpcreposix.so.0*


%files -n libpcrecpp0
%doc AUTHORS COPYING ChangeLog* NEWS README LICENCE NON-UNIX-USE
%{_libdir}/libpcrecpp.so.0*
