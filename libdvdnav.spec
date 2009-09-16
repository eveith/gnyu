Name: libdvdnav
Version: 0.1.10
Release: 1ev
Summary: A library for displaying and handling all kinds of DVD menus
URL: http://dvd.sourceforge.net
Group: System Environment/Libraries
License: GPL-2
Vendor: GNyU-Linux
Source: http://downloads.sourceforge.net/dvd/%{name}-%{version}.tar.gz
BuildRequires: make, gcc, doxygen

%description
libdvdnav is a library that allows easy use of sophisticated DVD navigation
features such as DVD menus, multiangle playback and even interactive DVD
games.
All this functionality is provided through a simple API which provides the
DVD playback as a single logical stream of blocks, intermitted by special
dvdnav events to report certain conditions. The main usage of libdvdnav is a
loop regularly calling a function to get the next block, surrounded by
additional calls to tell the library of user interaction.
The whole DVD virtual machine and internal playback states are completely
encapsulated.


%prep
	%setup -q


%build
	%configure
	%{__make} %{?_smp_mflags}


%install
	%{__make} install DESTDIR='%{buildroot}'

	[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
		&& %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%post
	%{__ldconfig}


%postun
	%{__ldconfig}


%files
	%defattr(-, root, root)
	%doc AUTHORS ChangeLog COPYING NEWS README TODO
	%{_bindir}/dvdnav-config
	%dir %{_includedir}/dvdnav
	%{_includedir}/dvdnav/*.h
	%{_libdir}/libdvdnav.*
	%{_datadir}/aclocal/dvdnav.m4
