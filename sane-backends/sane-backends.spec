Name: sane-backends
Version: 1.0.20
Release: 4ev
Summary: Backend drivers for S.A.N.E. (Scanner Acess Now Easy)
License: GPL-2
Group: System Environment/Libraries
Source: ftp://ftp.sane-project.org/pub/sane/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1: %{name}-saned.i
URL: http://www.sane-project.org/
BuildRequires: pkg-config, make, gcc, gettext
BuildRequires: libjpeg, libtiff, libusb >= 0.1.8, libv4l
BuildRequires: ucspi-tcp
Requires: udev >= 0.90

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
Requires: ucspi-tcp, sane-backends = %{version}

%description -n saned
S.A.N.E. allows scanning over the network, implemented by a daemon called
"saned".


%prep
%setup -q
%configure


%build
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%find_lang sane-backends
%{__mkdir_p} '%{buildroot}/%{_datadir}/sane'

%{__cat} << __EOF__ > '%{buildroot}/%{_sysconfdir}/sane.d/net.rules'
# TCP rules file for saned
# For syntax documentation, see tcprules(1).

# Allow localhost to connect, but deny anybody else access to saned
127.0.0.1:allow
:deny
__EOF__
%{__touch} '%{buildroot}/%{_sysconfdir}/sane.d/net.rules.cdb' \
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


%preun -n saned
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
%doc AUTHORS ChangeLog* COPYING LICENSE PROBLEMS PROJECTS README*
%dir %attr(0750, root, scanner) %{_sysconfdir}/sane.d
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/abaton.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/agfafocus.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/apple.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/artec.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/artec_eplus48u.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/avision.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/bh.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/canon630u.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/canon.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/canon_dr.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/canon_pp.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/cardscan.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/coolscan2.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/coolscan3.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/coolscan.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/dc210.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/dc240.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/dc25.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/dell1600n_net.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/dll.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/dmc.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/epjitsu.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/epson2.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/epson.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/fujitsu.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/genesys.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/gt68xx.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/hp3900.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/hp4200.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/hp5400.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/hp.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/hpsj5s.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/hs2p.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/ibm.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/leo.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/lexmark.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/ma1509.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/matsushita.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/microtek2.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/microtek.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/mustek.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/mustek_pp.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/mustek_usb.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/nec.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/net.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/pie.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/pixma.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/plustek.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/plustek_pp.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/qcam.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/ricoh.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/rts8891.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/s9036.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/sceptre.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/sharp.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/sm3840.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/snapscan.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/sp15c.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/st400.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/stv680.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/tamarack.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/teco1.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/teco2.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/teco3.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/test.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/u12.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/umax1220u.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/umax.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/umax_pp.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/v4l.conf
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/xerox_mfp.conf
%dir %attr(0750, root, scanner) %{_sysconfdir}/sane.d/dll.d
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
%doc %{_mandir}/man1/sane-find-scanner.1*
%doc %{_mandir}/man1/gamma4scanimage.1*
%doc %{_mandir}/man1/scanimage.1*
%doc %{_mandir}/man1/sane-config.1*
%doc %{_mandir}/man5/sane-*.5*
%doc %{_mandir}/man7/sane.7*
%dir %{_docdir}/sane-%{version}
%doc %{_docdir}/sane-%{version}/*
%dir %{_datadir}/sane


%files -n saned
%defattr(-, root, root)
%doc AUTHORS ChangeLog* COPYING LICENSE PROBLEMS PROJECTS README*
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/net.rules
%attr(0640, root, scanner) %ghost %{_sysconfdir}/sane.d/net.rules.cdb
%attr(0640, root, scanner) %ghost %{_sysconfdir}/sane.d/net.rules.cdb.tmp
%attr(0640, root, scanner) %config(noreplace) %{_sysconfdir}/sane.d/saned.conf
%attr(0700, root, root) %{_sysconfdir}/initng/daemon/saned.i
%attr(0750, root, scanner) %{_sbindir}/saned
%doc %{_mandir}/man8/saned.8*
