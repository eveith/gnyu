Name: make
Version: 3.81
Release: 2ev
Summary: A tool that makes building software easy
URL: http://www.gnu.org/software/make/
Source: http://ftp.gnu.org/pub/gnu/make/make-3.81.tar.bz2
License: GPL
Group: Development/Tools
Vendor: MSP Slackware
Packager: Eric MSP Veith <eveith@wwweb-library.net>
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: gcc-core
BuildRequires: /bin/sh
BuildRequires: sed

%description
Make is a tool which controls the generation of executables and other
non-source files of a program from the program's source files. 
Make gets its knowledge of how to build your program from a file called the
makefile, which lists each of the non-source files and how to compute it from
other files. When you write a program, you should write a makefile for it, so
that it is possible to use Make to build and install the program.


%prep
%setup -q


%build
%configure
sh ./build.sh


%install
${RPM_BUILD_DIR}/%{name}-%{version}/make DESTDIR="${RPM_BUILD_ROOT}" install
rm -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir


%clean
rm -vrf ${RPM_BUILD_ROOT}


%files
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS COPYING INSTALL NEWS README* 
%{_bindir}/make
%{_infodir}/make.info*
%{_mandir}/man1/make.1.gz
%{_datadir}/locale/be/LC_MESSAGES/make.mo
%{_datadir}/locale/da/LC_MESSAGES/make.mo
%{_datadir}/locale/de/LC_MESSAGES/make.mo
%{_datadir}/locale/es/LC_MESSAGES/make.mo
%{_datadir}/locale/fi/LC_MESSAGES/make.mo
%{_datadir}/locale/fr/LC_MESSAGES/make.mo
%{_datadir}/locale/ga/LC_MESSAGES/make.mo
%{_datadir}/locale/gl/LC_MESSAGES/make.mo
%{_datadir}/locale/he/LC_MESSAGES/make.mo
%{_datadir}/locale/hr/LC_MESSAGES/make.mo
%{_datadir}/locale/id/LC_MESSAGES/make.mo
%{_datadir}/locale/ja/LC_MESSAGES/make.mo
%{_datadir}/locale/ko/LC_MESSAGES/make.mo
%{_datadir}/locale/nl/LC_MESSAGES/make.mo
%{_datadir}/locale/pl/LC_MESSAGES/make.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/make.mo
%{_datadir}/locale/ru/LC_MESSAGES/make.mo
%{_datadir}/locale/rw/LC_MESSAGES/make.mo
%{_datadir}/locale/sv/LC_MESSAGES/make.mo
%{_datadir}/locale/tr/LC_MESSAGES/make.mo
%{_datadir}/locale/uk/LC_MESSAGES/make.mo
%{_datadir}/locale/vi/LC_MESSAGES/make.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/make.mo
