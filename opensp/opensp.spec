Name: opensp
Version: 1.5.1
Release: 1ev
Summary: A SGML parser
URL: http://openjade.sf.net/
Group: Development/Languages
License: Freeware
Vendor: GNyU-Linux
Source: http://prdownloads.sourceforge.net/openjade/OpenSP-%{version}.tar.gz
Patch0: %{name}-include_constant.patch
Patch1: %{name}-1.5.1-gcc41.patch
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, perl, gcc-g++, libstdc++
Requires: sgml-common

%description
OpenSP is a SGML parser conforming to international standard ISO 8879.


%prep
%setup -q -n OpenSP-%{version}
%patch0 -p1
%patch1 -p1
%{__sed} -i 's:32,:253,:' lib/Syntax.cxx
%{__sed} -i 's:LITLEN          240 :LITLEN          8092:' \
	unicode/{gensyntax.pl,unicode.syn}


%build
%configure \
	--enable-http \
	--enable-xml-messages \
	--enable-default-catalog=%{_sysconfdir}/sgml/catalog \
	--enable-default-search-path=%{_datadir}/sgml
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} \
	pkgdatadir=%{_datadir}/sgml/OpenSP-%{version} \
	DESTDIR='%{buildroot}'
%find_lang sp4

# We include docs manually at a better place, so delete them for now.
%{__rm} -rf '%{buildroot}/%{_datadir}/doc'

pushd '%{buildroot}/%{_bindir}'
%{__ln_s} -v onsgmls nsgmls
%{__ln_s} -v osgmlnorm sgmlnorm
%{__ln_s} -v ospam spam
%{__ln_s} -v ospcat spcat
%{__ln_s} -v ospent spent
%{__ln_s} -v osx sx
%{__ln_s} -v osx sgml2xml
popd



%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
%{__make_install} DESTDIR='%{buildroot}'


%files -f sp4.lang
%defattr(-, root, root)
%doc README doc/*.htm* ABOUT-NLS AUTHORS BUGS COPYING ChangeLog NEWS
%{_datadir}/sgml/OpenSP-%{version}/
%{_includedir}/OpenSP/
%{_mandir}/*/*
%{_bindir}/osgmlnorm
%{_bindir}/sgmlnorm
%{_bindir}/ospam
%{_bindir}/spam
%{_bindir}/ospcat
%{_bindir}/spcat
%{_bindir}/ospent
%{_bindir}/spent
%{_bindir}/osx
%{_bindir}/sx
%{_bindir}/osx
%{_bindir}/sgml2xml
%{_bindir}/nsgmls
%{_bindir}/onsgmls
%{_libdir}/libosp.*
