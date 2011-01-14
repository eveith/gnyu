Name: xkbcomp
Version: 1.0.5
Release: 1ev
Summary: Compiles X keyboard descriptions
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/archive/individual/app/%{name}-%{version}.tar.bz2
BuildRequires: pkg-config, make, gcc, libX11, libxkbfile

%description
The xkbcomp keymap compiler converts a description of a XKB keymap into one of
several output formats. The most common use for xkbcomp is to create a
compiled keymap file which can be read directly by XKB-capable X servers or
utilites.


%prep
	%setup -q


%build
	%configure
	%{__make} %{?_smp_mflags}


%install
	%{__make} install DESTDIR='%{buildroot}'



%files
	%defattr(-, root, root)
	%doc AUTHORS ChangeLog COPYING README* NEWS
	%{_bindir}/xkbcomp
	%doc %{_mandir}/man1/xkbcomp.1*
