Name: docbook-style-dsssl
Version: 1.79
Release: 1ev
Summary: Norman Walsh's modular stylesheets for DocBook
URL: http://docbook.sourceforge.net/
Group: Applications/Text
License: Distributable
Vendor: GNyU-Linux
Source0: http://downloads.sourceforge.net/docbook/docbook-dsssl-1.79.tar.bz2
Source1: %{name}.Makefile
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make
BuildArch: noarch
%define openjadever 1.3.2
Requires: openjade = %{openjadever}, sgml-common >= 0.5, docbook-dtds >= 1.0-1ev
Conflicts: docbook-utils < 0.6.9

%description
These DSSSL stylesheets allow to convert any DocBook document to another
printed (for example, RTF or PostScript) or online (for example, HTML) format.
They are highly customizable.


%prep
%setup -q -n docbook-dsssl-%{version}


%build
exit 0


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__install} -d -m 0755 \
	%{buildroot}/{%{_bindir},%{_mandir}/man1} \
	%{buildroot}/%{_datadir}/sgml/docbook/%{name}-%{version}
%{__install} -m 0755 bin/collateindex.pl %{buildroot}/%{_bindir}
%{__install} -m 0644 bin/collateindex.pl.1 %{buildroot}/%{_mandir}/man1
%{__cp} -v -R * %{buildroot}/usr/share/sgml/docbook/%{name}-%{version}/
%{__mkdir_p} %{buildroot}/etc/sgml
touch %{buildroot}/%{_sysconfdir}/sgml/%{name}-%{version}.cat


%post
install-catalog --add %{_sysconfdir}/sgml/%{name}-%{version}.cat \
	%{_datadir}/sgml/docbook/%{name}-%{version}/catalog
install-catalog --add %{_sysconfdir}/sgml/%{name}-%{version}.cat \
	%{_datadir}/sgml/docbook/%{name}-%{version}/common/catalog

%postun
install-catalog --remove %{_sysconfdir}/sgml/%{name}-%{version}.cat \
	%{_datadir}/sgml/docbook/%{name}-%{version}/catalog
install-catalog --remove %{_sysconfdir}/sgml/%{name}-%{version}.cat \
	%{_datadir}/sgml/docbook/%{name}-%{version}/common/catalog

%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc BUGS README ChangeLog WhatsNew
%ghost %config /etc/sgml/%{name}-%{version}.cat
%{_bindir}/collateindex.pl
%{_mandir}/man1/collateindex.pl.1*
%{_datadir}/sgml/docbook/%{name}-%{version}/
