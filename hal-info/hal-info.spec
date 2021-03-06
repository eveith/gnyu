Name: hal-info
Version: 20090716
Release: 3ev
Summary: Device information for HAL
URL: http://www.freedesktop.org/wiki/Software/hal
Group: System Environment/Daemons
License: AFL-2.1/GPL-2
Vendor: GNyU-Linux
Source: http://hal.freedesktop.org/releases/hal-info-%{version}.tar.gz
BuildRequires: make
BuildArch: noarch
Conflicts: hal < 0.5.11

%description
FDI files a basically XML-based device information files. They are used to
recocnize hardware, like cameras or storage media, and to set the device 
parameters accordingly.


%prep
%setup -q


%build
%configure
%{__make}


%install
%{__make_install} DESTDIR='%{buildroot}'


%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING HACKING NEWS README
%{_datadir}/hal/fdi/
