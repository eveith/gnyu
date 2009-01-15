Name: sane-backends
Version: 1.0.19
Release: 3ev
Summary: Backend drivers for S.A.N.E. (Scanner Acess Now Easy)
License: GPL-2
Group: System Environment/Libraries
Source: ftp://ftp.sane-project.org/pub/sane/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1: %{name}-saned.i
URL: http://www.sane-project.org/
Requires: udev >= 0.90, ucspi-tcp
BuildRequires: libusb >= 0.1.12, ucspi-tcp, libieee1284

%description
SANE (Scanner Access Now Easy) is a universal scanner
interface. SANE-BACKENDS comes complete with documentation,
several local backends, the network scanning backend, and the scanimage 
command line frontend. For other or graphical frontends take a look at 
XSane or KDE's kooka (in kdegraphics).


%package -n saned
Summary: SaneD network scanning daemon
Group: System Environment/Daemons
License: GPL-2
Requires: ucspi-tcp

%description -n saned
S.A.N.E. allows scanning over the network, implemented by a daemon called
"saned".



%prep
%setup -q
%configure \
	--with-docdir=%{_docdir}/%{name}-%{version}


%build
%{__make} %{?_smp_mflags}


%install
%{__make_install} DESTDIR='%{buildroot}'
%find_lang sane-backends
%{__mkdir_p} '%{buildroot}/%{_datadir}/sane'

%{__cat} << __EOF__ > '%{buildroot}/%{_sysconfdir}/sane.d/net.rules'
# TCP rules file for saned
# For syntax documentation, see tcprules(1).

# Allow localhost to connect, but deny anybody else access to saned
127.0.0.1:allow
:deny
__EOF__
touch '%{buildroot}/%{_sysconfdir}/sane.d/net.rules.cdb' \
	 '%{buildroot}/%{_sysconfdir}/sane.d/net.rules.cdb.tmp'

%{__mkdir_p} '%{buildroot}/%{_sysconfdir}/initng/daemon'
%{__cat} '%{SOURCE1}' | %{__sed} \
	-e 's,@sysconfdir@,%{_sysconfdir},g' \
	-e 's,@cat@,%{__cat},g' \
	-e 's,@tcprules@,%{_bindir}/tcprules,g' \
	-e 's,@tcpserver@,%{_bindir}/tcpserver,g' \
	-e 's,@saned@,%{_sbindir}/saned,g' \
	> '%{buildroot}/%{_sysconfdir}/initng/daemon/saned.i'


%pre
%{__ldconfig}

%preun
if [[ "${1}" -eq 0 ]]
then
	ngc -d daemon/saned
	ng-update del daemon/saned default
fi > /dev/null 2>&1
exit 0

%postun
%{__ldconfig}


%files -f sane-backends.lang
%defattr(-, root, root)
%dir %{_includedir}/sane
%{_includedir}/sane/sane.h
%{_includedir}/sane/saneopts.h
%dir %{_libdir}/sane
%{_libdir}/sane/libsane-*.*
%{_libdir}/libsane.*
%{_bindir}/scanimage
%{_bindir}/sane-config
%{_bindir}/sane-find-scanner
%{_bindir}/gamma4scanimage
%{_sbindir}/saned
%doc %{_mandir}/man1/sane-find-scanner.1*
%doc %{_mandir}/man1/gamma4scanimage.1*
%doc %{_mandir}/man1/scanimage.1*
%doc %{_mandir}/man1/sane-config.1*
%doc %{_mandir}/man5/sane-*.5*
%doc %{_mandir}/man7/sane.7*
%doc %{_mandir}/man8/saned.8*
%dir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/README
%doc %{_docdir}/%{name}-%{version}/AUTHORS
%doc %{_docdir}/%{name}-%{version}/COPYING
%doc %{_docdir}/%{name}-%{version}/ChangeLog
%doc %{_docdir}/%{name}-%{version}/LICENSE
%doc %{_docdir}/%{name}-%{version}/NEWS
%doc %{_docdir}/%{name}-%{version}/PROBLEMS
%doc %{_docdir}/%{name}-%{version}/PROJECTS
%doc %{_docdir}/%{name}-%{version}/README.aix
%doc %{_docdir}/%{name}-%{version}/README.beos
%doc %{_docdir}/%{name}-%{version}/README.darwin
%doc %{_docdir}/%{name}-%{version}/README.freebsd
%doc %{_docdir}/%{name}-%{version}/README.djpeg
%doc %{_docdir}/%{name}-%{version}/README.hp-ux
%doc %{_docdir}/%{name}-%{version}/README.linux
%doc %{_docdir}/%{name}-%{version}/README.netbsd
%doc %{_docdir}/%{name}-%{version}/README.openbsd
%doc %{_docdir}/%{name}-%{version}/README.os2
%doc %{_docdir}/%{name}-%{version}/README.solaris
%doc %{_docdir}/%{name}-%{version}/README.unixware2
%doc %{_docdir}/%{name}-%{version}/README.unixware7
%doc %{_docdir}/%{name}-%{version}/README.windows
%doc %{_docdir}/%{name}-%{version}/README.zeta
%dir %{_docdir}/%{name}-%{version}/canon
%doc %{_docdir}/%{name}-%{version}/canon/canon.changes
%doc %{_docdir}/%{name}-%{version}/canon/canon.install2700F.txt
%dir %{_docdir}/%{name}-%{version}/leo
%doc %{_docdir}/%{name}-%{version}/leo/leo.txt
%dir %{_docdir}/%{name}-%{version}/matsushita
%doc %{_docdir}/%{name}-%{version}/matsushita/matsushita.txt
%dir %{_docdir}/%{name}-%{version}/mustek
%doc %{_docdir}/%{name}-%{version}/mustek/mustek.CHANGES
%dir %{_docdir}/%{name}-%{version}/mustek_usb
%doc %{_docdir}/%{name}-%{version}/mustek_usb/mustek_usb.CHANGES
%doc %{_docdir}/%{name}-%{version}/mustek_usb/mustek_usb.TODO
%dir %{_docdir}/%{name}-%{version}/plustek
%doc %{_docdir}/%{name}-%{version}/plustek/FAQ
%doc %{_docdir}/%{name}-%{version}/plustek/MakeModule.sh
%doc %{_docdir}/%{name}-%{version}/plustek/Makefile.kernel24
%doc %{_docdir}/%{name}-%{version}/plustek/Makefile.kernel26
%doc %{_docdir}/%{name}-%{version}/plustek/Plustek-PARPORT-TODO.txt
%doc %{_docdir}/%{name}-%{version}/plustek/Plustek-PARPORT.changes
%doc %{_docdir}/%{name}-%{version}/plustek/Plustek-PARPORT.txt
%doc %{_docdir}/%{name}-%{version}/plustek/Plustek-USB-TODO.txt
%doc %{_docdir}/%{name}-%{version}/plustek/Plustek-USB.changes
%doc %{_docdir}/%{name}-%{version}/plustek/Plustek-USB.txt
%dir %{_docdir}/%{name}-%{version}/u12
%doc %{_docdir}/%{name}-%{version}/u12/U12.changes
%doc %{_docdir}/%{name}-%{version}/u12/U12.todo
%dir %{_docdir}/%{name}-%{version}/umax
%doc %{_docdir}/%{name}-%{version}/umax/negative-types.txt
%doc %{_docdir}/%{name}-%{version}/umax/sane-logo.jpg
%doc %{_docdir}/%{name}-%{version}/umax/sane-umax-advanced-options-doc.html
%doc %{_docdir}/%{name}-%{version}/umax/sane-umax-advanced.jpg
%doc %{_docdir}/%{name}-%{version}/umax/sane-umax-astra-doc.html
%doc %{_docdir}/%{name}-%{version}/umax/sane-umax-config-doc.html
%doc %{_docdir}/%{name}-%{version}/umax/sane-umax-doc.html
%doc %{_docdir}/%{name}-%{version}/umax/sane-umax-histogram.jpg
%doc %{_docdir}/%{name}-%{version}/umax/sane-umax-mirage-doc.html
%doc %{_docdir}/%{name}-%{version}/umax/sane-umax-not-listed-doc.html
%doc %{_docdir}/%{name}-%{version}/umax/sane-umax-others-doc.html
%doc %{_docdir}/%{name}-%{version}/umax/sane-umax-parport-doc.html
%doc %{_docdir}/%{name}-%{version}/umax/sane-umax-powerlook-doc.html
%doc %{_docdir}/%{name}-%{version}/umax/sane-umax-scanner-clones-doc.html
%doc %{_docdir}/%{name}-%{version}/umax/sane-umax-speed-doc.html
%doc %{_docdir}/%{name}-%{version}/umax/sane-umax-standard-options-doc.html
%doc %{_docdir}/%{name}-%{version}/umax/sane-umax-standard.jpg
%doc %{_docdir}/%{name}-%{version}/umax/sane-umax-text.jpg
%doc %{_docdir}/%{name}-%{version}/umax/sane-umax-text2.jpg
%doc %{_docdir}/%{name}-%{version}/umax/sane-umax-text4.jpg
%doc %{_docdir}/%{name}-%{version}/umax/sane-umax-uc-doc.html
%doc %{_docdir}/%{name}-%{version}/umax/sane-umax-vista-doc.html
%doc %{_docdir}/%{name}-%{version}/umax/sane-umax.jpg
%doc %{_docdir}/%{name}-%{version}/umax/umax.BUGS
%doc %{_docdir}/%{name}-%{version}/umax/umax.CHANGES
%doc %{_docdir}/%{name}-%{version}/umax/umax.FAQ
%doc %{_docdir}/%{name}-%{version}/umax/umax.TODO
%dir %{_docdir}/%{name}-%{version}/sceptre
%doc %{_docdir}/%{name}-%{version}/sceptre/s1200.txt
%dir %{_docdir}/%{name}-%{version}/teco
%doc %{_docdir}/%{name}-%{version}/teco/teco1.txt
%doc %{_docdir}/%{name}-%{version}/teco/teco2.txt
%doc %{_docdir}/%{name}-%{version}/teco/teco3.txt
%dir %{_docdir}/%{name}-%{version}/gt68xx
%doc %{_docdir}/%{name}-%{version}/gt68xx/gt68xx.CHANGES
%doc %{_docdir}/%{name}-%{version}/gt68xx/gt68xx.TODO
%dir %{_docdir}/%{name}-%{version}/niash
%doc %{_docdir}/%{name}-%{version}/niash/niash.TODO
%dir %{_docdir}/%{name}-%{version}/mustek_usb2
%doc %{_docdir}/%{name}-%{version}/mustek_usb2/mustek_usb2.CHANGES
%doc %{_docdir}/%{name}-%{version}/mustek_usb2/mustek_usb2.TODO
%doc %{_docdir}/%{name}-%{version}/backend-writing.txt
%doc %{_docdir}/%{name}-%{version}/sane-backends.html
%doc %{_docdir}/%{name}-%{version}/sane-backends-external.html
%doc %{_docdir}/%{name}-%{version}/sane-mfgs.html
%doc %{_docdir}/%{name}-%{version}/sane-mfgs-external.html
%dir %attr(0750, root, scanner) %{_sysconfdir}/sane.d
%attr(0640, root, scanner) %config %{_sysconfdir}/sane.d/*.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/net.rules
%attr(0640, root, scanner) %ghost %{_sysconfdir}/sane.d/net.rules.cdb
%attr(0640, root, scanner) %ghost %{_sysconfdir}/sane.d/net.rules.cdb.tmp
%attr(0700, root, root) %{_sysconfdir}/initng/daemon/saned.i
%dir %{_datadir}/sane
