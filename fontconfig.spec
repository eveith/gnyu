Name: fontconfig
Version: 2.6.0
Release: 2ev
Summary: A font access configuration and customization library
URL: http://www.freedesktop.org/wiki/Software/fontconfig
Group: System Environment/Libraries
License: BSD
Vendor: GNyU-Linux
Source: http://fontconfig.org/release/fontconfig-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: make >= 3.79.1, gcc, pkg-config >= 0.9.0
BuildRequires: freetype, docbook-utils, expat, freetype

%description
Fontconfig can: 
 · discover new fonts when installed automatically, removing a common source of
   configuration problems. 
 · perform font name substitution, so that appropriate alternative fonts can be
   selected if fonts are missing. 
 · identify the set of fonts required to completely cover a set of languages. 
 · have GUI configuration tools built as it uses an XML-based configuration file
   (though with autodiscovery, we believe this need is minimized). 
 · efficiently and quickly find the fonts you need among the set of fonts you
   have installed, even if you have installed thousands of fonts, while 
   minimzing memory usage. 
 · be used in concert with the X Render Extension and FreeType to implement high
   quality, anti-aliased and subpixel rendered text on a display. 
Fontconfig does not: 
 · render the fonts themselves (this is left to FreeType or other rendering 
   mechanisms) 
 · depend on the X Window System in any fashion, so that printer only
   applications do not have such dependencies

%prep
	%setup -q


%build
	%configure \
		--with-cache-dir='%{_localstatedir}/cache/fontconfig' \
		--with-confdir='%{_sysconfdir}/fonts' \
		--with-docdir='%{_docdir}/%{name}-%{version}'
	%{__make} %{?_smp_mflags}


%install
	%{__make} install DESTDIR='%{buildroot}'
	%{__mkdir_p} '%{buildroot}/%{_localstatedir}/cache/fontconfig'
	%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/fonts'


%post
	%{_bindir}/fc-cache -r -f -v
	%{__ldconfig}


%postun
	%{__ldconfig}


%files
	%defattr(-, root, root)
	%doc AUTHORS COPYING ChangeLog NEWS README
	%doc doc/fontconfig-devel
	%dir %{_sysconfdir}/fonts
	%dir %{_sysconfdir}/fonts/conf.avail
	%config %{_sysconfdir}/fonts/conf.avail/*.conf
	%dir %{_sysconfdir}/fonts/conf.d
	%config %{_sysconfdir}/fonts/conf.d/*.conf
	%doc %{_sysconfdir}/fonts/conf.d/README
	%{_sysconfdir}/fonts/fonts.conf
	%{_sysconfdir}/fonts/fonts.dtd
	%dir %{_localstatedir}/cache/fontconfig
	%{_bindir}/fc-cache
	%{_bindir}/fc-cat
	%{_bindir}/fc-list
	%{_bindir}/fc-match
	%{_includedir}/fontconfig/
	%{_libdir}/libfontconfig.*
	%{_libdir}/pkgconfig/fontconfig.pc
	%doc %{_mandir}/man1/fc-*.1*
	%doc %{_mandir}/man3/Fc*.3*
	%doc %{_mandir}/man5/fonts-conf.5*
