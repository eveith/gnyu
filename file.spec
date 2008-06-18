Name: file
Version: 4.24
Release: 2ev
Summary: File type identification utility
URL: http://www.darwinsys.com/file/
Group: System Environment/Base
License: BSD
Vendor: GNyU-Linux
Source: ftp://ftp.astron.com/pub/file/file-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: coreutils, grep, sed, make >= 3.79.1, gcc

%description
The file command is "a file type guesser", that is, a command-line tool that
tells you in words what kind of data a file contains. Unlike most GUI systems,
command-line UNIX systems - with this program leading the charge - don't rely
on filename extentions to tell you the type of a file, but look at the file's
actual contents. This is, of course, more reliable, but requires a bit of I/O.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'
%{__rm} -vf ${RPM_BUILD_ROOT}/%{_infodir}/dir


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc ChangeLog* COPYING MAINT AUTHORS README 
%{_bindir}/file
%{_includedir}/magic.h
%{_libdir}/libmagic.*
%doc %{_mandir}/man1/file.1*
%doc %{_mandir}/man3/libmagic.3*
%doc %{_mandir}/man4/magic.4*
%{_datadir}/file/
