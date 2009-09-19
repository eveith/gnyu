Name: sed
Version: 4.1.5
Release: 1ev
Summary: The GNU Stream EDitor
URL: http://www.gnu.org/software/sed/
Group: System Environment/Base
License: GPL
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Source: http://www.gnu.org/software/sed/%{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: gcc-core, make >= 3.79.1
Requires: /sbin/install-info

%description
Sed (streams editor) isn't really a true text editor or text processor.
Instead, it is used to filter text, i.e., it takes text input and performs
some operation (or set of operations) on it and outputs the modified text. Sed
is typically used for extracting part of a file using pattern matching or
substituting multiple occurrences of a string within a file. 


%define _exec_prefix /

%prep
%setup -q


%build
%configure
make


%install
%makeinstall
rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir


%post
/sbin/install-info %{_infodir}/sed.info.gz %{_infodir}/dir

%preun
/sbin/install-info --delete %{_infodir}/sed.info.gz %{_infodir}/dir


%clean
rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS BUGS COPYING* ChangeLog README* NEWS THANKS
%{_datadir}/locale/af/LC_MESSAGES/sed.mo
%{_datadir}/locale/ca/LC_MESSAGES/sed.mo
%{_datadir}/locale/cs/LC_MESSAGES/sed.mo
%{_datadir}/locale/da/LC_MESSAGES/sed.mo
%{_datadir}/locale/de/LC_MESSAGES/sed.mo
%{_datadir}/locale/el/LC_MESSAGES/sed.mo
%{_datadir}/locale/eo/LC_MESSAGES/sed.mo
%{_datadir}/locale/es/LC_MESSAGES/sed.mo
%{_datadir}/locale/et/LC_MESSAGES/sed.mo
%{_datadir}/locale/fi/LC_MESSAGES/sed.mo
%{_datadir}/locale/fr/LC_MESSAGES/sed.mo
%{_datadir}/locale/ga/LC_MESSAGES/sed.mo
%{_datadir}/locale/gl/LC_MESSAGES/sed.mo
%{_datadir}/locale/he/LC_MESSAGES/sed.mo
%{_datadir}/locale/hr/LC_MESSAGES/sed.mo
%{_datadir}/locale/hu/LC_MESSAGES/sed.mo
%{_datadir}/locale/id/LC_MESSAGES/sed.mo
%{_datadir}/locale/it/LC_MESSAGES/sed.mo
%{_datadir}/locale/ja/LC_MESSAGES/sed.mo
%{_datadir}/locale/ko/LC_MESSAGES/sed.mo
%{_datadir}/locale/nl/LC_MESSAGES/sed.mo
%{_datadir}/locale/pl/LC_MESSAGES/sed.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/sed.mo
%{_datadir}/locale/ro/LC_MESSAGES/sed.mo
%{_datadir}/locale/ru/LC_MESSAGES/sed.mo
%{_datadir}/locale/sk/LC_MESSAGES/sed.mo
%{_datadir}/locale/sl/LC_MESSAGES/sed.mo
%{_datadir}/locale/sr/LC_MESSAGES/sed.mo
%{_datadir}/locale/sv/LC_MESSAGES/sed.mo
%{_datadir}/locale/tr/LC_MESSAGES/sed.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/sed.mo
%{_bindir}/sed
%{_infodir}/sed.info-2.gz
%{_infodir}/sed.info.gz
%{_infodir}/sed.info-1.gz
%{_mandir}/man1/sed.1.gz

