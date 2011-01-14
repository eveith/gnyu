Name: pcre
Version: 7.9
Release: 2ev
Summary: Perl5 compatible regular expressions for other programs
URL: http://www.pcre.org/
Group: System Environment/Libraries
License: BSD 
Vendor: GNyU-Linux
Source: ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/%{name}-%{version}.tar.bz2
BuildRequires: gcc, gcc-g++, make >= 3.79.1, bzip2, zlib, pkg-config, libstdc++

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


%prep
%setup -q


%build
%configure \
	--enable-utf8 \
	--enable-unicode-properties \
	--enable-pcregrep-libz \
	--enable-pcregrep-libbz2
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'


%post
%{__ldconfig}


%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog* NEWS README LICENCE NON-UNIX-USE
%doc doc/html
%{_bindir}/pcre-config
%{_bindir}/pcregrep
%{_bindir}/pcretest
%{_includedir}/pcre.h
%{_includedir}/pcre_scanner.h
%{_includedir}/pcre_stringpiece.h
%{_includedir}/pcrecpp.h
%{_includedir}/pcrecpparg.h
%{_includedir}/pcreposix.h
%{_libdir}/libpcre.*
%{_libdir}/libpcrecpp.*
%{_libdir}/libpcreposix.*
%{_libdir}/pkgconfig/libpcre.pc
%{_libdir}/pkgconfig/libpcrecpp.pc
%doc %{_mandir}/man1/pcre-config.1*
%doc %{_mandir}/man1/pcregrep.1*
%doc %{_mandir}/man1/pcretest.1*
%doc %{_mandir}/man3/pcre*.3*
%dir %{_datadir}/doc/pcre
%doc %{_datadir}/doc/pcre/*
