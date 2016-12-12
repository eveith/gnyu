Name: make
Version: 3.82
Release: 1.0
Summary: A tool that makes building software easy
URL: http://www.gnu.org/software/make
Source: http://ftp.gnu.org/pub/gnu/make/make-%{version}.tar.bz2
License: GPL-2
Group: Development/Tools
BuildRequires: grep, sed, gettext-tools >= 0.14.1
BuildRequires: gcc
BuildRequires: eglibc-devel


%description
Make is a tool which controls the generation of executables and other
non-source files of a program from the program's source files. 
Make gets its knowledge of how to build your program from a file called the
makefile, which lists each of the non-source files and how to compute it from
other files. When you write a program, you should write a makefile for it, so
that it is possible to use Make to build and install the program.


%files -f make.lang
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS COPYING INSTALL NEWS README* 

%{_bindir}/make

%doc %{_infodir}/make.info*
%doc %{_mandir}/man1/make.1*


%post
if [ "$1" -eq 1 ]; then
    install-info --info-dir='%{_infodir}' %{_infodir}/make.info*
fi


%postun
if [ "$1" -eq 0 ]; then
    install-info --delete --info-dir='%{_infodir}' %{_infodir}/make.info*
fi



%prep
%setup -q


%build
%configure
sh ./build.sh


%install
./make DESTDIR="${RPM_BUILD_ROOT}" install
%{__rm} ${RPM_BUILD_ROOT}/%{_infodir}/dir
%find_lang make
