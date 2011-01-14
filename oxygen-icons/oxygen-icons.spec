Name: oxygen-icons
Version: 4.3.2
Release: 2.2ev
Summary: The Oxygen Icon Theme
URL: http://www.kde.org
Group: User Interface/Desktops
License: LGPL-3
Vendor: GNyU-Linux
Source: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires: cmake >= 2.4.5, make
BuildArch: noarch

%description
The Oxygen icon theme is mostly used by KDE 4, for which it was originally
developed. But it is an icon theme of its own, and one of the most complete.
It is unobstrusive and carfully designed for a coherent look and feel.


%prep
	%setup -q


%build
	%{cmake} .
	%{__make}


%install
	%{__make} install DESTDIR='%{buildroot}'
	
	# Create scalable dirs, even if just for reference
	for i in mimetypes intl animations apps emotes places categories emblems \
			actions devices status
	do
		for j in 128x128 16x16 22x22 256x256 32x32 42x42 48x48 64x64 8x8 \
			scalable
		do
			%{__mkdir_p} "%{buildroot}/%{_datadir}/icons/oxygen/${j}/${i}"
		done
	done


%files
	%defattr(-, root, root)
	%doc COPYING AUTHORS CONTRIBUTING
	%{_datadir}/icons/oxygen/
