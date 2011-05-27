Name: file
Version: 5.07
Release: 1.0
Summary: A file type identification utility
URL: http://www.darwinsys.com/file
Group: System Environment/Base
License: BSD
Source: ftp://ftp.astron.com/pub/file/file-%{version}.tar.gz
BuildRequires: grep, sed, make >= 3.79.1, gcc

%description
The file command is "a file type guesser", that is, a command-line tool that
tells you in words what kind of data a file contains. Unlike most GUI systems,
command-line UNIX systems - with this program leading the charge - don't rely
on filename extentions to tell you the type of a file, but look at the file's
actual contents. This is, of course, more reliable, but requires a bit of I/O.


%package devel
Summary: Development headers for file
Group: Development/Libraries

%description devel
The file command is "a file type guesser", that is, a command-line tool that
tells you in words what kind of data a file contains. 
To access file's database in a programatic way, you will need to install these
header files.


%package -n libmagic1
Summary: A file type identification library
Group: System Environment/Libraries

%description -n libmagic1
The magic library is a "file type guesser," a library that reads a file and
identifies its type.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%{__rm} '${RPM_BUILD_ROOT}%{_infodir}/dir' ||:


%post -n libmagic1 -p %{__ldconfig}
%postun -n libmagic1 -p %{__ldconfig}


%files
%defattr(-, root, root)
%doc ChangeLog* COPYING MAINT AUTHORS README NEWS TODO
%{_bindir}/file
%doc %{_mandir}/man1/file.1*
%{_datadir}/misc/magic.mgc


%files -n libmagic1
%defattr(-, root, root)
%doc ChangeLog* COPYING MAINT AUTHORS README NEWS TODO
%{_libdir}/libmagic.so.1*
%doc %{_mandir}/man4/magic.4*


%files devel
%defattr(-, root, root)
%doc ChangeLog* COPYING MAINT AUTHORS README NEWS TODO
%{_libdir}/libmagic.so
%{_libdir}/libmagic.la
%{_libdir}/libmagic.a
%{_includedir}/magic.h
%doc %{_mandir}/man3/libmagic.3*
