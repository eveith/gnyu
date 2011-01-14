Name: mkfontdir
Version: 1.0.4
Release: 1ev
Summary: X11 console application that creates an index of X font files
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/archive/individual/app/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc-g++

%description
For each directory argument, mkfontdir reads all of the font files in
the directory searching for properties named "FONT", or (failing that)
the name of the file stripped of its suffix. These are converted to
lower case and used as font names, and, along with the name of the font
file, are written out to the file "fonts.dir" in the directory. The X
server and font server use "fonts.dir" to find font files.


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
%{_bindir}/mkfontdir
%doc %{_mandir}/man1/mkfontdir.1*
