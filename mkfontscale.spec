Name: mkfontscale
Version: 1.0.4
Release: 1ev
Summary: X11 console application that creates an index of scalable font files
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/archive/individual/app/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-g++

%description
For each directory argument, mkfontscale reads all of the scalable font
files in the directory. For every font file found, an X11 font name
(XLFD) is generated, and is written together with the file name to a
file fonts.scale in the directory.

%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/mkfontscale
%doc %{_mandir}/man1/mkfontscale.1*
