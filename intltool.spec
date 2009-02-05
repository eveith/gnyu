Name: intltool
Version: 0.40.5
Release: 1ev
Summary: Extracts translatable strings from various source files
URL: ftp://ftp.gnome.org/pub/gnome/sources/intltool/
Group: Development/Tools
License: GPL-2
Vendor: GNyU-Linux
Source: ftp://ftp.gnome.org/pub/gnome/sources/%{name}/0.40/%{name}-%{version}.tar.bz2
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
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/intltool-extract
%{_bindir}/intltool-merge
%{_bindir}/intltool-prepare
%{_bindir}/intltool-update
%{_bindir}/intltoolize
%doc %{_mandir}/man8/intltool-extract.8*
%doc %{_mandir}/man8/intltool-merge.8*
%doc %{_mandir}/man8/intltool-prepare.8*
%doc %{_mandir}/man8/intltool-update.8*
%doc %{_mandir}/man8/intltoolize.8*
%{_datadir}/aclocal/intltool.m4
%dir %{_datadir}/intltool
%{_datadir}/intltool/*.*
