Name: libtasn1
Version: 2.7
Release: 1.0ev
Summary: A library implementing ASN.1
URL: http://www.gnu.org/software/libtasn1
Group: System Environment/Libraries
License: LGPL-2.1
Vendor: GNyU-Linux
Source: http://ftp.gnu.org/gnu/libtasn1/libtasn1-%{version}.tar.gz
BuildRequires: make, gcc, perl >= 5.6

%description
Libtasn1 is the ASN.1 library used by GnuTLS, GNU Shishi and some other
packages. It was written by Fabio Fiorina, and has been shipped as part of
GnuTLS for some time but is now a proper GNU package.
The goal of this implementation is to be highly portable, and only require an
ANSI C89 platform.


%package devel
Summary: Development headers and documentation for libtasn1
Group: Development/Libraries
Requires: pkg-config

%description devel
This package contains the libtasn1 development headers as well as the API
documentation in both info and man format.


%prep
%setup -q


%build
%configure \
	--libdir='/%{_lib}'
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

%{__mkdir_p} '%{buildroot}/%{_libdir}'
%{__mv} '%{buildroot}/%{_lib}/pkgconfig' '%{buildroot}/%{_libdir}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
	&& %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
%{__ldconfig}


%postun
%{__ldconfig}


%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING* NEWS README THANKS
/%{_lib}/libtasn1.so*
%{_bindir}/asn1*
%doc %{_mandir}/man1/asn1*.1*


%files devel
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING* NEWS README THANKS
%doc %{_mandir}/man3/*asn1*.3*
%doc %{_infodir}/libtasn1.info*
/%{_lib}/libtasn1.a
/%{_lib}/libtasn1.la
%{_libdir}/pkgconfig/libtasn1.pc
%{_includedir}/libtasn1.h
