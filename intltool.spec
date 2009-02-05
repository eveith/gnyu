Name: intltool
Version: 0.9.5
Release: 1ev
Summary: Extracts translatable strings from various source files
URL: ftp://ftp.gnome.org/pub/gnome/sources/intltool/
Group: Development/Tools
License: GPL-2
Vendor: GNyU-Linux
Source: ftp://ftp.gnome.org/pub/gnome/sources/%{name}/0.9/%{name}-%{version}.tar.bz2
BuildRequires: make, perl, automake
BuildArch: noarch

%description
The intltool collection will do this steps:
 o Extract translatable strings from various source files (.xml.in,
   .glade, .desktop.in, oaf.in).
 o Collect the extracted strings together with messages from traditional
   source files (.c, .h) in po/$(PACKAGE).pot.
 o Merge back the translations from .po files into .xml, .desktop and
   .oaf files.  This merge step will happen at build resp. installation
   time.


%prep
%setup -q


%build
%configure
%{__make}


%install
%{__make} install DESTDIR='%{buildroot}'


%files
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/xml-i18n-extract
%{_bindir}/xml-i18n-merge
%{_bindir}/xml-i18n-prepare
%{_bindir}/xml-i18n-toolize
%{_bindir}/xml-i18n-unicodify
%{_bindir}/xml-i18n-update
%doc %{_mandir}/man8/xml-i18n-extract.8*
%doc %{_mandir}/man8/xml-i18n-merge.8*
%doc %{_mandir}/man8/xml-i18n-prepare.8*
%doc %{_mandir}/man8/xml-i18n-toolize.8*
%{_datadir}/aclocal/xml-i18n-tools.m4
%dir %{_datadir}/intltool
%{_datadir}/intltool/*.*
