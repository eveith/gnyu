Name: kdebindings4
Version: 4.3.0
Release: 2ev
Summary: Bindings for various languages to KDE
URL: http://www.kde.org/
Group: User Interface/Desktops
License: GPL-2/LGPL-2
Vendor: GNyU-Linux
Source: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdebindings-%{version}.tar.bz2
Patch0: %{name}-pykde4_sip-4.8.patch
BuildRequires: cmake >= 2.4.5, make, gcc-g++, qt4, automoc4 >= 0.9.76
BuildRequires: phonon, soprano, akonadi >= 1.1.1
BuildRequires: kdelibs4 = %{version}, kdepimlibs4 = %{version}
BuildRequires: kdebase4 = %{version}, kdegraphics4 = %{version}
BuildRequires: python, python-sip, python-PyQt4
BuildRequires: perl, ruby
Provides: PyKDE4, python-PyKDE4

%description
This package contains:
  * smoke: Language independent library for Qt and KDE bindings. Used by
    QtRuby, PerlQt and Qyoto.
  * kalyptus: a header parser and bindings generator for Qt/KDE. Used for
    Smoke.
  * qtruby: Qt bindings for Ruby
  * korundum: KDE bindings for ruby
  * PyKDE: KDE bindings for python, requires PyQt from
    riverbankcomputing.co.uk
  * KrossPython is the Python plugin for the kdelibs/kross scripting
    framework.
  * KrossRuby is the Ruby plugin for the kdelibs/kross scripting framework.
  * KrossJava is the Java plugin for the kdelibs/kross scripting framework.


%prep
	%setup -q -n 'kdebindings-%{version}'
	%patch0


%build
	%{cmake} \
		-DBUILD_ruby:BOOL=OFF \
		.
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
	%doc AUTHORS ChangeLog README COPYING* NEWS
	%{_includedir}/smoke.h
	%dir %{_includedir}/smoke
	%{_includedir}/smoke/*.h
	%{_libdir}/kde4/kpythonpluginfactory.so
	%{_libdir}/kde4/krosspython.so
	%{_libdir}/libsmokeakonadi.*
	%{_libdir}/libsmokekde.*
	%{_libdir}/libsmokekhtml.*
	%{_libdir}/libsmokektexteditor.*
	%{_libdir}/libsmokenepomuk.*
	%{_libdir}/libsmokeokular.*
	%{_libdir}/libsmokeplasma.*
	%{_libdir}/libsmokeqt.*
	%{_libdir}/libsmokeqtscript.*
	%{_libdir}/libsmokeqttest.*
	%{_libdir}/libsmokeqtuitools.*
	%{_libdir}/libsmokeqtwebkit.*
	%{_libdir}/libsmokesolid.*
	%{_libdir}/libsmokesoprano.*
	%dir %{python_sitelib}/PyKDE4
	%{python_sitelib}/PyKDE4/*
	%dir %{_datadir}/apps/pykde4
	%{_datadir}/apps/pykde4/*
	%dir %{_datadir}/sip/PyKDE4
	%{_datadir}/sip/PyKDE4/*
