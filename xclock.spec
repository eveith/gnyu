Name: xclock
Version: 1.0.3
Release: 1ev
Summary: Small and simple clock for X11
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/archive/individual/app/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, xorg-proto, xorg-libs

%description
The xclock binary provides what the name suggests: A simple clock for the X
Window System. It has three modi (analogue, digital and colloquial) and 
some options to modify its appereance.


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
%{_bindir}/xclock
%{_datadir}/X11/app-defaults/XClock
%{_datadir}/X11/app-defaults/XClock-color
%doc %{_mandir}/man1/xclock.1*
