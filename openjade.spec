Name: openjade
Version: 1.3.2
Release: 1ev
Summary: An implementation of DSSSL
URL: http://openjade.sf.net/
Group: Applications/Publishing
License: Freeware
Vendor: MSP Slackware
Source: http://downloads.sourceforge.net/openjade/openjade-1.3.2.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, gcc-g++, opensp, perl, grep, libstdc++, sgml-common
Requires: opensp, sgml-common

%description
OpenJade is a suite of tools for validating, processing, and applying DSSSL
(Document Style Semantics and Specification Language) stylesheets to SGML and
XML documents. It is a project undertaken by the DSSSL community to maintain
and extend Jade and the related SP suite of SGML/XML processing tools.


%prep
%setup -q


%build
%configure \
	--datadir=%{_datadir}/sgml/openjade-%{version} \
    --enable-default-catalog=%{_sysconfdir}/sgml/catalog \
    --enable-default-search-path=%{_datadir}/sgml \
	--enable-http
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%{__mkdir_p} %{buildroot}/%{_datadir}/sgml/openjade-%{version}
%{__install} -vm0644 dsssl/catalog \
	%{buildroot}/%{_datadir}/sgml/openjade-%{version}
%{__install} -vm0644 dsssl/*.{dtd,dsl,sgm} \
	%{buildroot}/%{_datadir}/sgml/openjade-%{version}

%{__mkdir_p} %{buildroot}/%{_sysconfdir}/sgml
touch %{buildroot}/%{_sysconfdir}/sgml/openjade-%{version}.cat

pushd '%{buildroot}/%{_bindir}'
%{__ln_s} openjade jade
popd


%post
/sbin/ldconfig
install-catalog --add %{_sysconfdir}/sgml/openjade-%{version}.cat \
	%{_datadir}/sgml/openjade-1.3.2/catalog
install-catalog --add %{_sysconfdir}/sgml/sgml-docbook.cat \
    %{_sysconfdir}/sgml/openjade-%{version}.cat

%postun
/sbin/ldconfig
install-catalog --remove %{_sysconfdir}/sgml/openjade-%{version}.cat \
	%{_datadir}/sgml/openjade-1.3.2/catalog
install-catalog --remove %{_sysconfdir}/sgml/sgml-docbook.cat \
    %{_sysconfdir}/sgml/openjade-%{version}.cat


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc doc/*.htm* README NEWS COPYING ChangeLog VERSION
%ghost %{_sysconfdir}/sgml/openjade-%{version}.cat
%{_libdir}/libo*.*
%{_bindir}/*jade
%{_datadir}/sgml/openjade-%{version}/
