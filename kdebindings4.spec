Name: kdebindings4
Version: 4.3.2
Release: 3.0ev
Summary: Bindings for various languages to KDE
URL: http://www.kde.org/
Group: User Interface/Desktops
License: GPL-2/LGPL-2
Vendor: GNyU-Linux
Source: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdebindings-%{version}.tar.bz2
Patch0: %{name}-pykde4_sip-4.8.patch
BuildRequires: cmake >= 2.6.2, make, flex, bison, gcc-g++, perl, gettext
BuildRequires: libX11, libSM, libICE, libXrender, libXt, libxkbfile
BuildRequires: qt4 >= 4.5.0, automoc4 >= 0.9.88, polkit-qt >= 0.9.0
BuildRequires: qimageblitz
BuildRequires: kdelibs4 = %{version}, kdepimlibs4 = %{version}
BuildRequires: kdebase4 = %{version}, kdegraphics4 = %{version}
BuildRequires: soprano >= 2.0, akonadi >= 1.1.1, phonon >= 4.3.0
BuildRequires: python, python-sip, python-PyQt4
BuildRequires: perl, ruby
Provides: PyKDE4, python-PyKDE4
Requires: ruby = %{_ruby_version}

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
	%{__find} ruby -type f -name CMakeLists.txt \
		-exec %{__sed} -i \
			's,${RUBY_INCLUDE_PATH},${RUBY_INCLUDE_PATH} %{_includedir}/ruby-%{_ruby_version}/%{_target},' \
			'{}' \; \
		-print


%build
	%{cmake} \
		-DRUBY_INCLUDE_PATH='%{_includedir}/ruby-%{_ruby_version}' \
		-DBUILD_KROSSRUBY:BOOL=OFF \
		-DENABLE_KROSSRUBY:BOOL=OFF \
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
	%{_bindir}/krubyapplication
	%{_bindir}/pykdeuic4
	%{_bindir}/rbkconfig_compiler4
	%{_bindir}/rbqtapi
	%{_bindir}/rbrcc
	%{_bindir}/rbuic4
	%dir %{_includedir}/qtruby
	%{_includedir}/qtruby/marshall.h
	%{_includedir}/qtruby/marshall_basetypes.h
	%{_includedir}/qtruby/marshall_complex.h
	%{_includedir}/qtruby/marshall_macros.h
	%{_includedir}/qtruby/marshall_primitives.h
	%{_includedir}/qtruby/marshall_types.h
	%{_includedir}/qtruby/qtruby.h
	%{_includedir}/qtruby/smokeruby.h
	%{_includedir}/smoke.h
	%dir %{_includedir}/smoke
	%{_includedir}/smoke/*.h
	%{_libdir}/kde4/kpythonpluginfactory.so
	%{_libdir}/kde4/krosspython.so
	%{_libdir}/kde4/krubypluginfactory.so
	%{_libdir}/libqtruby4shared.*
	%{_libdir}/libsmokeakonadi.*
	%{_libdir}/libsmokekde.*
	%{_libdir}/libsmokekhtml.*
	%{_libdir}/libsmokektexteditor.*
	%{_libdir}/libsmokenepomuk.*
	%{_libdir}/libsmokeokular.*
	%{_libdir}/libsmokeplasma.*
	%{_libdir}/libsmokeqimageblitz.*
	%{_libdir}/libsmokeqt.*
	%{_libdir}/libsmokeqtscript.*
	%{_libdir}/libsmokeqttest.*
	%{_libdir}/libsmokeqtuitools.*
	%{_libdir}/libsmokeqtwebkit.*
	%{_libdir}/libsmokesolid.*
	%{_libdir}/libsmokesoprano.*
	%dir %{python_sitelib}/PyKDE4
	%{python_sitelib}/PyKDE4/*
	%dir %{python_sitelib}/PyQt4
	%{python_sitelib}/PyQt4/*
	%dir %{_libdir}/ruby/site_ruby/%{_ruby_version}/KDE
	%dir %{_libdir}/ruby/site_ruby/%{_ruby_version}/Qt
	%dir %{_libdir}/ruby/site_ruby/%{_ruby_version}/akonadi
	%{_libdir}/ruby/site_ruby/%{_ruby_version}/%{_target}/*.so
	%dir %{_libdir}/ruby/site_ruby/%{_ruby_version}/khtml
	%dir %{_libdir}/ruby/site_ruby/%{_ruby_version}/ktexteditor
	%dir %{_libdir}/ruby/site_ruby/%{_ruby_version}/nepomuk
	%dir %{_libdir}/ruby/site_ruby/%{_ruby_version}/okular
	%dir %{_libdir}/ruby/site_ruby/%{_ruby_version}/qtscript
	%dir %{_libdir}/ruby/site_ruby/%{_ruby_version}/qttest
	%dir %{_libdir}/ruby/site_ruby/%{_ruby_version}/qtuitools
	%dir %{_libdir}/ruby/site_ruby/%{_ruby_version}/qtwebkit
	%dir %{_libdir}/ruby/site_ruby/%{_ruby_version}/solid
	%dir %{_libdir}/ruby/site_ruby/%{_ruby_version}/soprano
	%dir %{_libdir}/ruby/site_ruby/%{_ruby_version}/*.rb
	%dir %{_libdir}/ruby/site_ruby/%{_ruby_version}/*/*.rb
	%dir %{_datadir}/apps/pykde4
	%{_datadir}/applications/kde4/dbpedia_references.desktop
	%dir %{_datadir}/apps/dbpedia_references
	%{_datadir}/apps/dbpedia_references/dbpedia_references.rb
	%{_datadir}/apps/pykde4/*
	%dir %{_datadir}/sip/PyKDE4
	%{_datadir}/sip/PyKDE4/*
