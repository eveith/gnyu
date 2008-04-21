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
cp %{SOURCE1} Makefile


%build
exit 0


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__install} -d -m 0755 \
	%{buildroot}/{%{_bindir},%{_mandir}/man1} \
	%{buildroot}/usr/share/sgml/docbook/%{name}-%{version}}
%{__install} -m 0755 bin/collateindex.pl %{buildroot}/%{_bindir}
%{__install} -m 0644 bin/collateindex.pl.1 %{buildroot}/%{_mandir}/man1
%{__cp} -v -R * %{buildroot}/usr/share/sgml/%{name}-%{version}/
%{__mkdir} %{buildroot}/etc/sgml
touch %{buildroot}/etc/sgml/%{name}-%{version}.cat


%post
rel=$(find /etc/sgml -type f -name 'sgml-docbook-3.0-*.cat'|head -n1)
rel=${rel##*-}
rel=${rel%.cat}
for centralized in /etc/sgml/*-docbook-*.cat
do
    /usr/bin/install-catalog --remove $centralized \
        /usr/share/sgml/docbook/dsssl-stylesheets-*/catalog \
        >/dev/null 2>/dev/null
done

for centralized in /etc/sgml/*-docbook-*$rel.cat
do
    /usr/bin/install-catalog --add $centralized \
        /usr/share/sgml/openjade-%{openjadever}/catalog \
        > /dev/null 2>/dev/null
    /usr/bin/install-catalog --add $centralized \
        /usr/share/sgml/docbook/dsssl-stylesheets-%{version}/catalog \
        > /dev/null 2>/dev/null
done

%postun
if [ "$1" = "0" ]
then
	for centralized in /etc/sgml/*-docbook-*.cat
	do
		/usr/bin/install-catalog --remove $centralized \
			/usr/share/sgml/openjade-%{openjadever}/catalog > /dev/null 2>/dev/null
		/usr/bin/install-catalog --remove $centralized \
			/usr/share/sgml/docbook/dsssl-stylesheets-%{version}/catalog \
			> /dev/null 2>/dev/null
	done
fi
exit 0


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc BUGS README ChangeLog WhatsNew
%ghost %config /etc/sgml/%{name}-%{version}.cat
%{_bindir}/collateindex.pl
%{_mandir}/man1/collateindex.1*
/usr/share/sgml/docbook/%{name}-%{version}/
