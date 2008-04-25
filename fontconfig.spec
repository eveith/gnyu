Name: fontconfig
Version: 2.4.2
Release: 2ev
Summary: A font access configuration and customization library
URL: http://www.freedesktop.org/wiki/Software/fontconfig
Group: System Environment/Libraries
License: Public Domain
Vendor: GNyU-Linux
Source: http://fontconfig.org/release/fontconfig-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: gcc, make >= 3.79.1, docbook-utils, expat

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
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'

pushd '%{buildroot}'
%{__mkdir_p} -m 0755 \
	'./%{_localstatedir}/cache/fontconfig' \
	'./%{_datadir}/fonts'
%{__rm} -f './%{_infodir}/dir'
popd


%post
%{_bindir}/fc-cache -r -f -v
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%dir %{_datadir}/fonts
%dir %{_sysconfdir}/fonts
%{_sysconfdir}/fonts/conf.avail/
%{_sysconfdir}/fonts/conf.d/
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
%{_mandir}/man1/fc-*.1.gz
%{_mandir}/man3/Fc*.3*
%{_mandir}/man5/fonts-conf.5.gz
