Name: make
Version: 3.81
Release: 2ev
Summary: A tool that makes building software easy
URL: http://www.gnu.org/software/make/
Source: http://ftp.gnu.org/pub/gnu/make/make-3.81.tar.bz2
License: GPL-2
Group: Development/Tools
Vendor: GNyU-Linux
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
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
${RPM_BUILD_DIR}/%{name}-%{version}/make DESTDIR="${RPM_BUILD_ROOT}" install
%{__rm} -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir
%find_lang make


%post
update-info-dir

%postun
update-info-dir


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files -f make.lang
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS COPYING INSTALL NEWS README* 
%{_bindir}/make
%{_infodir}/make.info*
%{_mandir}/man1/make.1*
