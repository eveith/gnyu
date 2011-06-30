Name: libtool
Version: 2.4
Release: 1.0
Summary: A tool helping to build shared libraries
URL: http://www.gnu.org/software/libtool
Group: Development/Tools
License: GPL-3
Source: http://ftp.gnu.org/gnu/libtool/libtool-%{version}.tar.xz
BuildRequires: grep, sed, make
BuildRequires: gcc
BuildRequires: zlib-devel
Requires: tar, automake >= 1.4
Provides: libltdl-devel = %{version}-%{release}

%description
GNU libtool is a set of shell scripts to automatically configure UNIX
architectures to build shared libraries in a generic fashion.


%post
if [ "$1" -eq 1 ]; then
    install-info %{_infodir}/libtool.info* '%{_infodir}/dir'
fi


%preun
if [ "$1" -eq 1 ]; then
    install-info --delete %{_infodir}/libtool.info* '%{_infodir}/dir'
fi


%files
%defattr(-, root, root)
%doc README COPYING AUTHORS NEWS THANKS TODO ChangeLog*

%{_bindir}/libtool
%{_bindir}/libtoolize
%{_includedir}/libltdl
%{_includedir}/ltdl.h

%{_libdir}/libltdl.a
%attr(644, root, root) %{_libdir}/libltdl.la
%{_libdir}/libltdl.so

%{_datadir}/aclocal/*.m4
%{_datadir}/libtool/

%doc %{_infodir}/libtool.info*
%doc %{_mandir}/man1/libtool.1*
%doc %{_mandir}/man1/libtoolize.1*

 
%package -n libltdl7
Summary: Libtool Runtime Library
License: LGPL-2.1
Group: Development/Libraries
 
%description -n libltdl7
Library needed by programs that use the ltdl interface of GNU libtool.


%post -n libltdl7 -p %{__ldconfig}
%postun -n libltdl7 -p %{__ldconfig}


%files -n libltdl7
%defattr(-, root, root)
%doc libltdl/README libltdl/COPYING.LIB
%{_libdir}/libltdl.so.7*


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'
