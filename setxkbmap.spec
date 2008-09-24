Name: setxkbmap
Version: 1.0.4
Release: 1ev
Summary: X11 utility to set the keyboard map
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/archive/individual/app/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, xorg-proto, pkg-config, libX11, libxkbfile

%description
The setxkbmap command maps the keyboard to use the layout determined by
the options specified on the command line.


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
%{_bindir}/setxkbmap
%doc %{_mandir}/man1/setxkbmap.1*
