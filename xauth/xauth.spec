Name: xauth
Version: 1.0.3
Release: 1ev
Summary: Utility to edit X authority files
URL: http://www.x.org/
Group: User Interface/X
License: MIT
Vendor: GNyU-Linux
Source: http://xorg.freedesktop.org/archive/individual/app/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, libX11, libXau, libXext, libXmu, xorg-proto

%description
The xauth program is used to edit and display the authorization
information used in connecting to the X server. This program is usually
used to extract authorization records from one machine and merge them
in on another (as is the case when using remote logins or granting
access to other users). Commands (described below) may be entered
interactively, on the xauth command line, or in scripts. Note that
this program does not contact the X server except when the generate
command is used. Normally xauth is not used to create the authority
file entry in the first place; xdm does that.


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
%{_bindir}/xauth
%doc %{_mandir}/man1/xauth.1*
