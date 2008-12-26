Name: hal-info
Version: 20071212
Release: 1ev
Summary: Device information for HAL
URL: http://www.freedesktop.org/wiki/Software/hal
Group: System Environment/Daemons
License: AFL-2.1/GPL-2
Vendor: MSP Slackware
Source: http://hal.freedesktop.org/releases/hal-info-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, coreutils, hal
BuildArch: noarch

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
[[ -d '%{buildroot}' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%clean
[[ -d '%{buildroot}' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING HACKING NEWS README
%{_datadir}/hal/fdi/
