Name: enchant
Version: 1.5.0
Release: 1ev
Summary: An unified API to several spell checking engines
URL: http://www.abisource.com/projects/enchant/
Group: Applications/Text
License: LGPL-2.1
Vendor: GNyU-Linux
Source: http://www.abisource.com/downloads/enchant/%{version}/enchant-%{version}.tar.gz
BuildRequires: pkg-config, make, gcc, gcc-g++, libstdc++
BuildRequires: glib2 >= 2.6
BuildRequires: aspell >= 0.50.0

%description
Enchant is meant to provide a generic interface into various existing
spell checking libaries. These include, but are not limited to:
   * Aspell/Pspell
   * Ispell
   * Hspell
   * Uspell


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
	%doc AUTHORS BUGS ChangeLog COPYING.LIB HACKING MAINTAINERS NEWS README
	%doc TODO
	%{_bindir}/enchant
	%{_bindir}/enchant-lsmod
	%dir %{_includedir}/enchant
	%{_includedir}/enchant/enchant*.h
	%dir %{_libdir}/enchant
	%{_libdir}/enchant/libenchant_aspell.*
	%{_libdir}/enchant/libenchant_ispell.*
	%{_libdir}/enchant/libenchant_myspell.*
	%{_libdir}/enchant/libenchant_zemberek.*
	%{_libdir}/libenchant.*
	%{_libdir}/pkgconfig/enchant.pc
	%doc %{_mandir}/man1/enchant.1*
	%dir %{_datadir}/enchant
	%{_datadir}/enchant/enchant.ordering
