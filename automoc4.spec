Name: automoc4
Version: 0.9.84
Release: 1ev
Summary: CMake automatic MOC generation
URL: http://www.kde.org/
Group: Development/Tools
License: BSD
Vendor: GNyU-Linux
Source: ftp://ftp.kde.org/pub/kde/unstable/%{name}/%{version}/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires(build): cmake >= 2.4.5, qt4, make, gcc-g++
BuildRequires(install): make
Requires: cmake >= 2.4.5

%description
automoc4 is a tool to add rules for generating Qt moc files
automatically to projects that use CMake as the buildsystem.


%prep
%setup -q


%build
%{cmake} .
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%{_bindir}/automoc4
%{_libdir}/automoc4/
