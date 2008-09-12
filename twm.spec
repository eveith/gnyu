Name: twm
Version: 1.0.4
Release: 1ev
Summary: A very basic window manager
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/archive/individual/app/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, xorg-proto, xorg-libs

%description
Twm is a window manager for the X Window System. It provides title-
bars, shaped windows, several forms of icon management, user-defined
macro functions, click-to-type and pointer-driven keyboard focus, and
user-specified key and pointer button bindings.



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
%{_bindir}/twm
%dir %{_datadir}/X11/twm
%{_datadir}/X11/twm/system.twmrc
%doc %{_mandir}/man1/twm.1*
