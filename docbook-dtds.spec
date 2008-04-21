Name: docbook-dtds
Version: 1.0
Release: 1ev
Summary: SGML and XML document type definitions for DocBook
URL: http://www.oasis-open.org/docbook/
Group: Applications/Text
License: Distributable
Vendor: GNyU-Linux
Source0: http://www.oasis-open.org/docbook/sgml/3.0/docbk30.zip
Source1: http://www.oasis-open.org/docbook/sgml/3.1/docbk31.zip
Source2: http://www.oasis-open.org/docbook/sgml/4.0/docbk40.zip
Source3: http://www.oasis-open.org/docbook/sgml/4.1/docbk41.zip
Source4: http://www.oasis-open.org/docbook/xml/4.1.2/docbkx412.zip
Source5: http://www.oasis-open.org/docbook/sgml/4.2/docbook-4.2.zip
Source6: http://www.oasis-open.org/docbook/xml/4.2/docbook-xml-4.2.zip
Source7: http://www.docbook.org/sgml/4.3/docbook-4.3.zip
Source8: http://www.docbook.org/xml/4.3/docbook-xml-4.3.zip
Source9: http://www.docbook.org/sgml/4.4/docbook-4.4.zip
Source10: http://www.docbook.org/xml/4.4/docbook-xml-4.4.zip
Patch0: docbook-dtd30-sgml-1.0.catalog.patch
Patch1: docbook-dtd31-sgml-1.0.catalog.patch
Patch2: docbook-dtd40-sgml-1.0.catalog.patch
Patch3: docbook-dtd41-sgml-1.0.catalog.patch
Patch4: docbook-dtd42-sgml-1.0.catalog.patch
Patch5: docbook-4.2-euro.patch
Patch6: docbook-dtds-ents.patch
BuildArch: noarch
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: unzip, findutils, coreutils
%define openjadever 1.3.2
Requires: libxml2, sgml-common, perl, openjade = %{openjadever}
Provides: docbook-dtd-xml docbook-dtd-sgml
Provides: docbook-dtd30-sgml docbook-dtd31-sgml
Provides: docbook-dtd40-sgml docbook-dtd41-sgml
Provides: docbook-dtd412-xml
Provides: docbook-dtd42-sgml docbook-dtd42-xml
Provides: docbook-dtd43-sgml docbook-dtd43-xml
Provides: docbook-dtd44-sgml docbook-dtd44-xml

%description
The DocBook Document Type Definition (DTD) describes the syntax of
technical documentation texts (articles, books and manual pages).
This syntax is XML-compliant and is developed by the OASIS consortium.
This package contains SGML and XML versions of the DocBook DTD.


%prep
%setup -c -T

# DocBook V3.0
%{__mkdir} 3.0-sgml
cd 3.0-sgml
%{__unzip} %{SOURCE0}
patch -b docbook.cat %{PATCH0}
cd ..

# DocBook V3.1
%{__mkdir} 3.1-sgml
cd 3.1-sgml
%{__unzip} %{SOURCE1}
patch -b docbook.cat %{PATCH1}
cd ..

# DocBook V4.0
%{__mkdir} 4.0-sgml
cd 4.0-sgml
%{__unzip} %{SOURCE2}
patch -b docbook.cat %{PATCH2}
cd ..

# DocBook V4.1
%{__mkdir} 4.1-sgml
cd 4.1-sgml
%{__unzip} %{SOURCE3}
patch -b docbook.cat %{PATCH3}
cd ..

# DocBook XML V4.1.2
%{__mkdir} 4.1.2-xml
cd 4.1.2-xml
%{__unzip} %{SOURCE4}
cd ..

# DocBook V4.2
%{__mkdir} 4.2-sgml
cd 4.2-sgml
%{__unzip} %{SOURCE5}
patch -b docbook.cat %{PATCH4}
cd ..

# DocBook XML V4.2
%{__mkdir} 4.2-xml
cd 4.2-xml
%{__unzip} %{SOURCE6}
cd ..

# DocBook V4.3
%{__mkdir} 4.3-sgml
cd 4.3-sgml
%{__unzip} %{SOURCE7}
cd ..

# DocBook XML V4.3
%{__mkdir} 4.3-xml
cd 4.3-xml
%{__unzip} %{SOURCE8}
cd ..

# DocBook V4.4
%{__mkdir} 4.4-sgml
cd 4.4-sgml
%{__unzip} %{SOURCE9}
cd ..

# DocBook XML V4.4
%{__mkdir} 4.4-xml
cd 4.4-xml
%{__unzip} %{SOURCE10}
cd ..

# Fix &euro; in SGML.
%patch5 -p1

# Fix ISO entities in 4.3/4.4 SGML
%patch6 -p1

# Increase NAMELEN (bug #36058, bug #159382).
%{__sed} -e 's,\(NAMELEN\s\+\)44\(\s\*\)\?,\1256,' -i.namelen */docbook.dcl

if [[ $(id -u) -eq 0 ]]
then
	%{__chown} -R root:root .
	%{__chmod} -R a+rX,g-w,o-w .
fi


%build


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'

for dir in $(ls -1)
do
	pushd "${dir}"
	DESTDIR="%{buildroot}/%{_datadir}/sgml/docbook/${dir/*-/}-dtd-${dir/-*/}-%{version}-%{release}"
	%{__mkdir_p} "$DESTDIR"
	for file in $(find . -maxdepth 1 -type f \( -name '*.dcl' -or -name '*.dtd' -or -name '*.mod' \))
	do
		%{__install} "${file}" "${DESTDIR}"
	done
	%{__install} docbook.cat "${DESTDIR}/catalog" ||:
	if [[ -d ent ]]
	then
		%{__mkdir_p} "${DESTDIR}/ent"
		%{__install} ent/* "${DESTDIR}/ent"
	fi
	popd
done


%post
#
# SGML catalog
#

# Update the centralized catalog corresponding to this version of the DTD
for dir in %{_datadir}/sgml/docbook/sgml-dtd-*-%{version}-%{release} \
		%{_datadir}/sgml/docbook/xml-dtd-*-%{version}-%{release}
do
	install-catalog --add "%{_sysconfdir}/sgml/${dir/*\//}" "${dir}/catalog"
done

#
# XML catalog
#
CATALOG=%{_datadir}/sgml/docbook/xmlcatalog

[[ ! -e "${CATALOG}" ]] && xmlcatalog --create > "${CATALOG}"
if [[ -w "${CATALOG}" ]]
then
    # DocBook XML V4.1.2
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Publishing//EN" \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-pub.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Greek Letters//EN" \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-grk1.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//ELEMENTS DocBook XML Information Pool V4.1.2//EN" \
        "xml-dtd-4.1.2-%{version}-%{release}/dbpoolx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Box and Line Drawing//EN" \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-box.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//DTD DocBook XML V4.1.2//EN" \
        "xml-dtd-4.1.2-%{version}-%{release}/docbookx.dtd" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Greek Symbols//EN" \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-grk3.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Math Symbols: Negated Relations//EN" \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-amsn.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Numeric and Special Graphic//EN" \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-num.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//ENTITIES DocBook XML Character Entities V4.1.2//EN" \
        "xml-dtd-4.1.2-%{version}-%{release}/dbcentx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Alternative Greek Symbols//EN" \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-grk4.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//ENTITIES DocBook XML Notations V4.1.2//EN" \
        "xml-dtd-4.1.2-%{version}-%{release}/dbnotnx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Diacritical Marks//EN" \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-dia.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Monotoniko Greek//EN" \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-grk2.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//ENTITIES DocBook XML Additional General Entities V4.1.2//EN" \
        "xml-dtd-4.1.2-%{version}-%{release}/dbgenent.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//ELEMENTS DocBook XML Document Hierarchy V4.1.2//EN" \
        "xml-dtd-4.1.2-%{version}-%{release}/dbhierx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Math Symbols: Arrow Relations//EN" \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-amsa.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Math Symbols: Ordinary//EN" \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-amso.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Russian Cyrillic//EN" \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-cyrl.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES General Technical//EN" \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-tech.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Math Symbols: Delimiters//EN" \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-amsc.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//DTD XML Exchange Table Model 19990315//EN" \
        "xml-dtd-4.1.2-%{version}-%{release}/soextblx.dtd" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//DTD DocBook XML CALS Table Model V4.1.2//EN" \
        "xml-dtd-4.1.2-%{version}-%{release}/calstblx.dtd" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Latin 1//EN" \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-lat1.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Math Symbols: Binary Operators//EN" \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-amsb.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Latin 2//EN" \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-lat2.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Math Symbols: Relations//EN" \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-amsr.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Non-Russian Cyrillic//EN" \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-cyr2.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "rewriteSystem" \
        "http://www.oasis-open.org/docbook/xml/4.1.2" \
        "xml-dtd-4.1.2-%{version}-%{release}" $CATALOG
    /usr/bin/xmlcatalog --noout --add "rewriteURI" \
        "http://www.oasis-open.org/docbook/xml/4.1.2" \
        "xml-dtd-4.1.2-%{version}-%{release}" $CATALOG

    # DocBook XML V4.2
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Publishing//EN" \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-pub.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Greek Letters//EN" \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-grk1.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//ELEMENTS DocBook XML Information Pool V4.2//EN" \
        "xml-dtd-4.2-%{version}-%{release}/dbpoolx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Box and Line Drawing//EN" \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-box.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//DTD DocBook XML V4.2//EN" \
        "xml-dtd-4.2-%{version}-%{release}/docbookx.dtd" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Greek Symbols//EN" \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-grk3.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Math Symbols: Negated Relations//EN" \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-amsn.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Numeric and Special Graphic//EN" \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-num.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//ENTITIES DocBook XML Character Entities V4.2//EN" \
        "xml-dtd-4.2-%{version}-%{release}/dbcentx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Alternative Greek Symbols//EN" \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-grk4.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//ENTITIES DocBook XML Notations V4.2//EN" \
        "xml-dtd-4.2-%{version}-%{release}/dbnotnx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Diacritical Marks//EN" \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-dia.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Monotoniko Greek//EN" \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-grk2.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//ENTITIES DocBook XML Additional General Entities V4.2//EN" \
        "xml-dtd-4.2-%{version}-%{release}/dbgenent.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//ELEMENTS DocBook XML Document Hierarchy V4.2//EN" \
        "xml-dtd-4.2-%{version}-%{release}/dbhierx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Math Symbols: Arrow Relations//EN" \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-amsa.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Math Symbols: Ordinary//EN" \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-amso.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Russian Cyrillic//EN" \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-cyrl.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES General Technical//EN" \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-tech.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Math Symbols: Delimiters//EN" \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-amsc.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//DTD XML Exchange Table Model 19990315//EN" \
        "xml-dtd-4.2-%{version}-%{release}/soextblx.dtd" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//DTD DocBook XML CALS Table Model V4.2//EN" \
        "xml-dtd-4.2-%{version}-%{release}/calstblx.dtd" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Latin 1//EN" \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-lat1.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Math Symbols: Binary Operators//EN" \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-amsb.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Latin 2//EN" \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-lat2.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Math Symbols: Relations//EN" \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-amsr.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Non-Russian Cyrillic//EN" \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-cyr2.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "rewriteSystem" \
        "http://www.oasis-open.org/docbook/xml/4.2" \
        "xml-dtd-4.2-%{version}-%{release}" $CATALOG
    /usr/bin/xmlcatalog --noout --add "rewriteURI" \
        "http://www.oasis-open.org/docbook/xml/4.2" \
        "xml-dtd-4.2-%{version}-%{release}" $CATALOG

    # DocBook XML V4.3
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Publishing//EN" \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-pub.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Greek Letters//EN" \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-grk1.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//ELEMENTS DocBook XML Information Pool V4.3//EN" \
        "xml-dtd-4.3-%{version}-%{release}/dbpoolx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Box and Line Drawing//EN" \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-box.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//DTD DocBook XML V4.3//EN" \
        "xml-dtd-4.3-%{version}-%{release}/docbookx.dtd" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Greek Symbols//EN" \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-grk3.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Math Symbols: Negated Relations//EN" \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-amsn.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Numeric and Special Graphic//EN" \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-num.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//ENTITIES DocBook XML Character Entities V4.3//EN" \
        "xml-dtd-4.3-%{version}-%{release}/dbcentx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Alternative Greek Symbols//EN" \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-grk4.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//ENTITIES DocBook XML Notations V4.3//EN" \
        "xml-dtd-4.3-%{version}-%{release}/dbnotnx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Diacritical Marks//EN" \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-dia.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Monotoniko Greek//EN" \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-grk2.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//ENTITIES DocBook XML Additional General Entities V4.3//EN" \
        "xml-dtd-4.3-%{version}-%{release}/dbgenent.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//ELEMENTS DocBook XML Document Hierarchy V4.3//EN" \
        "xml-dtd-4.3-%{version}-%{release}/dbhierx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Math Symbols: Arrow Relations//EN" \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-amsa.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Math Symbols: Ordinary//EN" \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-amso.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Russian Cyrillic//EN" \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-cyrl.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES General Technical//EN" \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-tech.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Math Symbols: Delimiters//EN" \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-amsc.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//DTD XML Exchange Table Model 19990315//EN" \
        "xml-dtd-4.3-%{version}-%{release}/soextblx.dtd" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//DTD DocBook XML CALS Table Model V4.3//EN" \
        "xml-dtd-4.3-%{version}-%{release}/calstblx.dtd" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Latin 1//EN" \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-lat1.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Math Symbols: Binary Operators//EN" \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-amsb.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Latin 2//EN" \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-lat2.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Math Symbols: Relations//EN" \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-amsr.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Non-Russian Cyrillic//EN" \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-cyr2.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "rewriteSystem" \
        "http://www.oasis-open.org/docbook/xml/4.3" \
        "xml-dtd-4.3-%{version}-%{release}" $CATALOG
    /usr/bin/xmlcatalog --noout --add "rewriteURI" \
        "http://www.oasis-open.org/docbook/xml/4.3" \
        "xml-dtd-4.3-%{version}-%{release}" $CATALOG

    # DocBook XML V4.4
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Publishing//EN" \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-pub.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Greek Letters//EN" \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-grk1.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//ELEMENTS DocBook XML Information Pool V4.4//EN" \
        "xml-dtd-4.4-%{version}-%{release}/dbpoolx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Box and Line Drawing//EN" \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-box.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//DTD DocBook XML V4.4//EN" \
        "xml-dtd-4.4-%{version}-%{release}/docbookx.dtd" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Greek Symbols//EN" \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-grk3.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Math Symbols: Negated Relations//EN" \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-amsn.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Numeric and Special Graphic//EN" \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-num.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//ENTITIES DocBook XML Character Entities V4.4//EN" \
        "xml-dtd-4.4-%{version}-%{release}/dbcentx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Alternative Greek Symbols//EN" \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-grk4.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//ENTITIES DocBook XML Notations V4.4//EN" \
        "xml-dtd-4.4-%{version}-%{release}/dbnotnx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Diacritical Marks//EN" \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-dia.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Monotoniko Greek//EN" \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-grk2.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//ENTITIES DocBook XML Additional General Entities V4.4//EN" \
        "xml-dtd-4.4-%{version}-%{release}/dbgenent.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//ELEMENTS DocBook XML Document Hierarchy V4.4//EN" \
        "xml-dtd-4.4-%{version}-%{release}/dbhierx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Math Symbols: Arrow Relations//EN" \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-amsa.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Math Symbols: Ordinary//EN" \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-amso.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Russian Cyrillic//EN" \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-cyrl.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES General Technical//EN" \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-tech.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Math Symbols: Delimiters//EN" \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-amsc.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//DTD XML Exchange Table Model 19990315//EN" \
        "xml-dtd-4.4-%{version}-%{release}/soextblx.dtd" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "-//OASIS//DTD DocBook XML CALS Table Model V4.4//EN" \
        "xml-dtd-4.4-%{version}-%{release}/calstblx.dtd" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Latin 1//EN" \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-lat1.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Math Symbols: Binary Operators//EN" \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-amsb.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Latin 2//EN" \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-lat2.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Added Math Symbols: Relations//EN" \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-amsr.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "public" \
        "ISO 8879:1986//ENTITIES Non-Russian Cyrillic//EN" \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-cyr2.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --add "rewriteSystem" \
        "http://www.oasis-open.org/docbook/xml/4.4" \
        "xml-dtd-4.4-%{version}-%{release}" $CATALOG
    /usr/bin/xmlcatalog --noout --add "rewriteURI" \
        "http://www.oasis-open.org/docbook/xml/4.4" \
        "xml-dtd-4.4-%{version}-%{release}" $CATALOG
fi

# Finally, make sure everything in /etc/sgml is readable!
%{__chmod} 0644 %{_sysconfdir}/sgml/*


%postun
#
# SGML catalog
#

# Update the centralized catalog corresponding to this version of the DTD
for dir in %{_datadir}/sgml/docbook/sgml-dtd-*-%{version}-%{release} \
		%{_datadir}/sgml/docbook/xml-dtd-*-%{version}-%{release}
do
	install-catalog --remove "%{_sysconfdir}/sgml/${dir/*\//}" "${dir}/catalog"
done

#
# XML catalog
#
CATALOG=%{_datadir}/sgml/docbook/xmlcatalog

if [[ -w "${CATALOG}" ]]
then
    # DocBook XML V4.1.2
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-pub.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-grk1.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.1.2-%{version}-%{release}/dbpoolx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-box.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.1.2-%{version}-%{release}/docbookx.dtd" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-grk3.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-amsn.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-num.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.1.2-%{version}-%{release}/dbcentx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-grk4.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.1.2-%{version}-%{release}/dbnotnx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-dia.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-grk2.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.1.2-%{version}-%{release}/dbgenent.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.1.2-%{version}-%{release}/dbhierx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-amsa.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-amso.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-cyrl.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-tech.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-amsc.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.1.2-%{version}-%{release}/soextblx.dtd" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.1.2-%{version}-%{release}/calstblx.dtd" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-lat1.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-amsb.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-lat2.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-amsr.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.1.2-%{version}-%{release}/ent/iso-cyr2.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.1.2-%{version}-%{release}" $CATALOG

    # DocBook XML V4.2
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-pub.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-grk1.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.2-%{version}-%{release}/dbpoolx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-box.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.2-%{version}-%{release}/docbookx.dtd" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-grk3.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-amsn.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-num.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.2-%{version}-%{release}/dbcentx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-grk4.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.2-%{version}-%{release}/dbnotnx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-dia.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-grk2.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.2-%{version}-%{release}/dbgenent.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.2-%{version}-%{release}/dbhierx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-amsa.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-amso.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-cyrl.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-tech.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-amsc.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.2-%{version}-%{release}/soextblx.dtd" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.2-%{version}-%{release}/calstblx.dtd" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-lat1.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-amsb.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-lat2.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-amsr.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.2-%{version}-%{release}/ent/iso-cyr2.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.2-%{version}-%{release}" $CATALOG

    # DocBook XML V4.3
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-pub.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-grk1.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.3-%{version}-%{release}/dbpoolx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-box.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.3-%{version}-%{release}/docbookx.dtd" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-grk3.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-amsn.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-num.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.3-%{version}-%{release}/dbcentx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-grk4.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.3-%{version}-%{release}/dbnotnx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-dia.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-grk2.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.3-%{version}-%{release}/dbgenent.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.3-%{version}-%{release}/dbhierx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-amsa.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-amso.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-cyrl.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-tech.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-amsc.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.3-%{version}-%{release}/soextblx.dtd" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.3-%{version}-%{release}/calstblx.dtd" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-lat1.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-amsb.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-lat2.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-amsr.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.3-%{version}-%{release}/ent/iso-cyr2.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.3-%{version}-%{release}" $CATALOG

    # DocBook XML V4.4
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-pub.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-grk1.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.4-%{version}-%{release}/dbpoolx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-box.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.4-%{version}-%{release}/docbookx.dtd" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-grk3.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-amsn.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-num.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.4-%{version}-%{release}/dbcentx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-grk4.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.4-%{version}-%{release}/dbnotnx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-dia.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-grk2.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.4-%{version}-%{release}/dbgenent.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.4-%{version}-%{release}/dbhierx.mod" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-amsa.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-amso.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-cyrl.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-tech.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-amsc.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.4-%{version}-%{release}/soextblx.dtd" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.4-%{version}-%{release}/calstblx.dtd" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-lat1.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-amsb.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-lat2.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-amsr.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.4-%{version}-%{release}/ent/iso-cyr2.ent" $CATALOG
    /usr/bin/xmlcatalog --noout --del \
        "xml-dtd-4.4-%{version}-%{release}" $CATALOG
fi


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc --parents 3.1-sgml/ChangeLog
%doc --parents 4.1-sgml/ChangeLog
%doc --parents */*.txt
%{_datadir}/sgml/docbook/sgml-dtd-3.0-%{version}-%{release}
%{_datadir}/sgml/docbook/sgml-dtd-3.1-%{version}-%{release}
%{_datadir}/sgml/docbook/sgml-dtd-4.0-%{version}-%{release}
%{_datadir}/sgml/docbook/sgml-dtd-4.1-%{version}-%{release}
%{_datadir}/sgml/docbook/sgml-dtd-4.2-%{version}-%{release}
%{_datadir}/sgml/docbook/sgml-dtd-4.3-%{version}-%{release}
%{_datadir}/sgml/docbook/sgml-dtd-4.4-%{version}-%{release}
%{_datadir}/sgml/docbook/xml-dtd-4.1.2-%{version}-%{release}
%{_datadir}/sgml/docbook/xml-dtd-4.2-%{version}-%{release}
%{_datadir}/sgml/docbook/xml-dtd-4.3-%{version}-%{release}
%{_datadir}/sgml/docbook/xml-dtd-4.4-%{version}-%{release}
