Name: libffi
Version: 3.0.9
Release: 1.0
Summary: A library to allow code calls to other programing languages
URL: http://www.sourceware.org/libffi
Group: System Environment/Libraries
License: BSD
Source: ftp://sourceware.org/pub/libffi/libffi-%{version}.tar.gz
BuildRequires: grep, sed, gawk, make
BuildRequires: gcc
BuildRequires: eglibc-devel
Requires: libffi5 = %{version}-%{release}

%description
A foreign function interface is the popular name for the interface that allows
code written in one language to call code written in another language.


%files
%defattr(-, root, root)
%doc README LICENSE ChangeLog*


%package -n libffi5
Summary: A library to allow code calls to other programing languages
Group: System Environment/Libraries
License: BSD

%description -n libffi5
A foreign function interface is the popular name for the interface that allows
code written in one language to call code written in another language.


%files -n libffi5
%defattr(-, root, root)
%doc README LICENSE ChangeLog*
%{_libdir}/libffi.so.5*


%post -n libffi5 -p %{__ldconfig}
%postun -n libffi5 -p %{__ldconfig}


%package devel
Summary: A library to allow code calls to other programing languages
Group: Development/Libraries
License: BSD
Requires: %{name} = %{version}-%{release}
Requires: info

%description devel
A foreign function interface is the popular name for the interface that allows
code written in one language to call code written in another language.
This package contains files necessary for developing and compiling
applications that use libffi.


%files devel
%defattr(-, root, root)
%doc README LICENSE ChangeLog*
%{_libdir}/libffi.so
%{_libdir}/libffi.a
%{_libdir}/libffi.la

%dir %{_libdir}/libffi-%{version}
%dir %{_libdir}/libffi-%{version}/include
%{_libdir}/libffi-%{version}/include/ffi.h
%{_libdir}/libffi-%{version}/include/ffitarget.h

%{_libdir}/pkgconfig/libffi.pc

%doc %{_infodir}/libffi.info*
%doc %{_mandir}/man3/ffi*.3*


%post devel
if [ "$1" -eq 1 ]; then
    install-info %{_infodir}/libffi.info* '%{_infodir}/dir'
fi


%preun devel
if [ "$1" -eq 1 ]; then
    install-info --delete %{_infodir}/libffi.info* '%{_infodir}/dir'
fi


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%check
%{__make} check ||:
