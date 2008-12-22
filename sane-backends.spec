Name: sane-backends
Version: 1.0.18
Release: 1ev
Summary: Backend drivers for S.A.N.E. (Scanner Acess Now Easy)
License: GPL
Group: System Environment/Libraries
Source: ftp://ftp.sane-project.org/pub/sane/%{name}-%{version}/%{name}-%{version}.tar.gz
URL: http://www.sane-project.org/
Requires: libusb >= 0.1.12
Requires: udev >= 0.90
BuildRequires: libusb >= 0.1.12
BuildRoot: %{_tmppath}/%{name}-root
%define scanner_gid 103

%description
SANE (Scanner Access Now Easy) is a universal scanner
interface. SANE-BACKENDS comes complete with documentation,
several backends, scanimage command line frontend, and
networking support. For other/graphical frontends take a look
at sane-frontends and XSane.


%prep
%setup -q
%configure \
	--with-docdir=%{_docdir}/%{name}-%{version}


%build
make %{_smp_mflags}


%install
[ "$RPM_BUILD_ROOT" != '/' ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR=${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/%{_sysconfdir}/udev/rules.d
cp -v ${RPM_BUILD_DIR}/%{name}-%{version}/tools/udev/libsane.rules \
	 ${RPM_BUILD_ROOT}/%{_sysconfdir}/udev/rules.d/90-sane-backends.rules


%pre
# Add the hald user and group
/usr/sbin/groupadd -g %{scanner_gid} scanner
exit 0


%postun
groupdel scanner >/dev/null 2>&1
exit 0


%clean
[ "$RPM_BUILD_ROOT" != '/' ] && rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)
%{_includedir}/sane/sane.h
%{_includedir}/sane/saneopts.h
%{_libdir}/sane/libsane-abaton.so.1.0.18
%{_libdir}/sane/libsane-abaton.so.1
%{_libdir}/sane/libsane-abaton.so
%{_libdir}/sane/libsane-abaton.la
%{_libdir}/sane/libsane-agfafocus.so.1.0.18
%{_libdir}/sane/libsane-agfafocus.so.1
%{_libdir}/sane/libsane-agfafocus.so
%{_libdir}/sane/libsane-agfafocus.la
%{_libdir}/sane/libsane-apple.so.1.0.18
%{_libdir}/sane/libsane-apple.so.1
%{_libdir}/sane/libsane-apple.so
%{_libdir}/sane/libsane-apple.la
%{_libdir}/sane/libsane-artec.so.1.0.18
%{_libdir}/sane/libsane-artec.so.1
%{_libdir}/sane/libsane-artec.so
%{_libdir}/sane/libsane-artec.la
%{_libdir}/sane/libsane-as6e.so.1.0.18
%{_libdir}/sane/libsane-as6e.so.1
%{_libdir}/sane/libsane-as6e.so
%{_libdir}/sane/libsane-as6e.la
%{_libdir}/sane/libsane-avision.so.1.0.18
%{_libdir}/sane/libsane-avision.so.1
%{_libdir}/sane/libsane-avision.so
%{_libdir}/sane/libsane-avision.la
%{_libdir}/sane/libsane-bh.so.1.0.18
%{_libdir}/sane/libsane-bh.so.1
%{_libdir}/sane/libsane-bh.so
%{_libdir}/sane/libsane-bh.la
%{_libdir}/sane/libsane-canon.so.1.0.18
%{_libdir}/sane/libsane-canon.so.1
%{_libdir}/sane/libsane-canon.so
%{_libdir}/sane/libsane-canon.la
%{_libdir}/sane/libsane-canon630u.so.1.0.18
%{_libdir}/sane/libsane-canon630u.so.1
%{_libdir}/sane/libsane-canon630u.so
%{_libdir}/sane/libsane-canon630u.la
%{_libdir}/sane/libsane-coolscan.so.1.0.18
%{_libdir}/sane/libsane-coolscan.so.1
%{_libdir}/sane/libsane-coolscan.so
%{_libdir}/sane/libsane-coolscan.la
%{_libdir}/sane/libsane-coolscan2.so.1.0.18
%{_libdir}/sane/libsane-coolscan2.so.1
%{_libdir}/sane/libsane-coolscan2.so
%{_libdir}/sane/libsane-coolscan2.la
%{_libdir}/sane/libsane-dc25.so.1.0.18
%{_libdir}/sane/libsane-dc25.so.1
%{_libdir}/sane/libsane-dc25.so
%{_libdir}/sane/libsane-dc25.la
%{_libdir}/sane/libsane-dmc.so.1.0.18
%{_libdir}/sane/libsane-dmc.so.1
%{_libdir}/sane/libsane-dmc.so
%{_libdir}/sane/libsane-dmc.la
%{_libdir}/sane/libsane-epson.so.1.0.18
%{_libdir}/sane/libsane-epson.so.1
%{_libdir}/sane/libsane-epson.so
%{_libdir}/sane/libsane-epson.la
%{_libdir}/sane/libsane-fujitsu.so.1.0.18
%{_libdir}/sane/libsane-fujitsu.so.1
%{_libdir}/sane/libsane-fujitsu.so
%{_libdir}/sane/libsane-fujitsu.la
%{_libdir}/sane/libsane-genesys.so.1.0.18
%{_libdir}/sane/libsane-genesys.so.1
%{_libdir}/sane/libsane-genesys.so
%{_libdir}/sane/libsane-genesys.la
%{_libdir}/sane/libsane-gt68xx.so.1.0.18
%{_libdir}/sane/libsane-gt68xx.so.1
%{_libdir}/sane/libsane-gt68xx.so
%{_libdir}/sane/libsane-gt68xx.la
%{_libdir}/sane/libsane-hp.so.1.0.18
%{_libdir}/sane/libsane-hp.so.1
%{_libdir}/sane/libsane-hp.so
%{_libdir}/sane/libsane-hp.la
%{_libdir}/sane/libsane-leo.so.1.0.18
%{_libdir}/sane/libsane-leo.so.1
%{_libdir}/sane/libsane-leo.so
%{_libdir}/sane/libsane-leo.la
%{_libdir}/sane/libsane-lexmark.so.1.0.18
%{_libdir}/sane/libsane-lexmark.so.1
%{_libdir}/sane/libsane-lexmark.so
%{_libdir}/sane/libsane-lexmark.la
%{_libdir}/sane/libsane-matsushita.so.1.0.18
%{_libdir}/sane/libsane-matsushita.so.1
%{_libdir}/sane/libsane-matsushita.so
%{_libdir}/sane/libsane-matsushita.la
%{_libdir}/sane/libsane-microtek.so.1.0.18
%{_libdir}/sane/libsane-microtek.so.1
%{_libdir}/sane/libsane-microtek.so
%{_libdir}/sane/libsane-microtek.la
%{_libdir}/sane/libsane-microtek2.so.1.0.18
%{_libdir}/sane/libsane-microtek2.so.1
%{_libdir}/sane/libsane-microtek2.so
%{_libdir}/sane/libsane-microtek2.la
%{_libdir}/sane/libsane-mustek.so.1.0.18
%{_libdir}/sane/libsane-mustek.so.1
%{_libdir}/sane/libsane-mustek.so
%{_libdir}/sane/libsane-mustek.la
%{_libdir}/sane/libsane-mustek_usb.so.1.0.18
%{_libdir}/sane/libsane-mustek_usb.so.1
%{_libdir}/sane/libsane-mustek_usb.so
%{_libdir}/sane/libsane-mustek_usb.la
%{_libdir}/sane/libsane-nec.so.1.0.18
%{_libdir}/sane/libsane-nec.so.1
%{_libdir}/sane/libsane-nec.so
%{_libdir}/sane/libsane-nec.la
%{_libdir}/sane/libsane-pie.so.1.0.18
%{_libdir}/sane/libsane-pie.so.1
%{_libdir}/sane/libsane-pie.so
%{_libdir}/sane/libsane-pie.la
%{_libdir}/sane/libsane-pixma.so.1.0.18
%{_libdir}/sane/libsane-pixma.so.1
%{_libdir}/sane/libsane-pixma.so
%{_libdir}/sane/libsane-pixma.la
%{_libdir}/sane/libsane-plustek.so.1.0.18
%{_libdir}/sane/libsane-plustek.so.1
%{_libdir}/sane/libsane-plustek.so
%{_libdir}/sane/libsane-plustek.la
%{_libdir}/sane/libsane-plustek_pp.so.1.0.18
%{_libdir}/sane/libsane-plustek_pp.so.1
%{_libdir}/sane/libsane-plustek_pp.so
%{_libdir}/sane/libsane-plustek_pp.la
%{_libdir}/sane/libsane-ricoh.so.1.0.18
%{_libdir}/sane/libsane-ricoh.so.1
%{_libdir}/sane/libsane-ricoh.so
%{_libdir}/sane/libsane-ricoh.la
%{_libdir}/sane/libsane-s9036.so.1.0.18
%{_libdir}/sane/libsane-s9036.so.1
%{_libdir}/sane/libsane-s9036.so
%{_libdir}/sane/libsane-s9036.la
%{_libdir}/sane/libsane-sceptre.so.1.0.18
%{_libdir}/sane/libsane-sceptre.so.1
%{_libdir}/sane/libsane-sceptre.so
%{_libdir}/sane/libsane-sceptre.la
%{_libdir}/sane/libsane-sharp.so.1.0.18
%{_libdir}/sane/libsane-sharp.so.1
%{_libdir}/sane/libsane-sharp.so
%{_libdir}/sane/libsane-sharp.la
%{_libdir}/sane/libsane-sp15c.so.1.0.18
%{_libdir}/sane/libsane-sp15c.so.1
%{_libdir}/sane/libsane-sp15c.so
%{_libdir}/sane/libsane-sp15c.la
%{_libdir}/sane/libsane-st400.so.1.0.18
%{_libdir}/sane/libsane-st400.so.1
%{_libdir}/sane/libsane-st400.so
%{_libdir}/sane/libsane-st400.la
%{_libdir}/sane/libsane-tamarack.so.1.0.18
%{_libdir}/sane/libsane-tamarack.so.1
%{_libdir}/sane/libsane-tamarack.so
%{_libdir}/sane/libsane-tamarack.la
%{_libdir}/sane/libsane-test.so.1.0.18
%{_libdir}/sane/libsane-test.so.1
%{_libdir}/sane/libsane-test.so
%{_libdir}/sane/libsane-test.la
%{_libdir}/sane/libsane-teco1.so.1.0.18
%{_libdir}/sane/libsane-teco1.so.1
%{_libdir}/sane/libsane-teco1.so
%{_libdir}/sane/libsane-teco1.la
%{_libdir}/sane/libsane-teco2.so.1.0.18
%{_libdir}/sane/libsane-teco2.so.1
%{_libdir}/sane/libsane-teco2.so
%{_libdir}/sane/libsane-teco2.la
%{_libdir}/sane/libsane-teco3.so.1.0.18
%{_libdir}/sane/libsane-teco3.so.1
%{_libdir}/sane/libsane-teco3.so
%{_libdir}/sane/libsane-teco3.la
%{_libdir}/sane/libsane-umax.so.1.0.18
%{_libdir}/sane/libsane-umax.so.1
%{_libdir}/sane/libsane-umax.so
%{_libdir}/sane/libsane-umax.la
%{_libdir}/sane/libsane-umax_pp.so.1.0.18
%{_libdir}/sane/libsane-umax_pp.so.1
%{_libdir}/sane/libsane-umax_pp.so
%{_libdir}/sane/libsane-umax_pp.la
%{_libdir}/sane/libsane-umax1220u.so.1.0.18
%{_libdir}/sane/libsane-umax1220u.so.1
%{_libdir}/sane/libsane-umax1220u.so
%{_libdir}/sane/libsane-umax1220u.la
%{_libdir}/sane/libsane-artec_eplus48u.so.1.0.18
%{_libdir}/sane/libsane-artec_eplus48u.so.1
%{_libdir}/sane/libsane-artec_eplus48u.so
%{_libdir}/sane/libsane-artec_eplus48u.la
%{_libdir}/sane/libsane-ma1509.so.1.0.18
%{_libdir}/sane/libsane-ma1509.so.1
%{_libdir}/sane/libsane-ma1509.so
%{_libdir}/sane/libsane-ma1509.la
%{_libdir}/sane/libsane-ibm.so.1.0.18
%{_libdir}/sane/libsane-ibm.so.1
%{_libdir}/sane/libsane-ibm.so
%{_libdir}/sane/libsane-ibm.la
%{_libdir}/sane/libsane-hp5400.so.1.0.18
%{_libdir}/sane/libsane-hp5400.so.1
%{_libdir}/sane/libsane-hp5400.so
%{_libdir}/sane/libsane-hp5400.la
%{_libdir}/sane/libsane-u12.so.1.0.18
%{_libdir}/sane/libsane-u12.so.1
%{_libdir}/sane/libsane-u12.so
%{_libdir}/sane/libsane-u12.la
%{_libdir}/sane/libsane-snapscan.so.1.0.18
%{_libdir}/sane/libsane-snapscan.so.1
%{_libdir}/sane/libsane-snapscan.so
%{_libdir}/sane/libsane-snapscan.la
%{_libdir}/sane/libsane-niash.so.1.0.18
%{_libdir}/sane/libsane-niash.so.1
%{_libdir}/sane/libsane-niash.so
%{_libdir}/sane/libsane-niash.la
%{_libdir}/sane/libsane-sm3840.so.1.0.18
%{_libdir}/sane/libsane-sm3840.so.1
%{_libdir}/sane/libsane-sm3840.so
%{_libdir}/sane/libsane-sm3840.la
%{_libdir}/sane/libsane-hp4200.so.1.0.18
%{_libdir}/sane/libsane-hp4200.so.1
%{_libdir}/sane/libsane-hp4200.so
%{_libdir}/sane/libsane-hp4200.la
%{_libdir}/sane/libsane-sm3600.so.1.0.18
%{_libdir}/sane/libsane-sm3600.so.1
%{_libdir}/sane/libsane-sm3600.so
%{_libdir}/sane/libsane-sm3600.la
%{_libdir}/sane/libsane-hp3500.so.1.0.18
%{_libdir}/sane/libsane-hp3500.so.1
%{_libdir}/sane/libsane-hp3500.so
%{_libdir}/sane/libsane-hp3500.la
%{_libdir}/sane/libsane-stv680.so.1.0.18
%{_libdir}/sane/libsane-stv680.so.1
%{_libdir}/sane/libsane-stv680.so
%{_libdir}/sane/libsane-stv680.la
%{_libdir}/sane/libsane-dc210.so.1.0.18
%{_libdir}/sane/libsane-dc210.so.1
%{_libdir}/sane/libsane-dc210.so
%{_libdir}/sane/libsane-dc210.la
%{_libdir}/sane/libsane-dc240.so.1.0.18
%{_libdir}/sane/libsane-dc240.so.1
%{_libdir}/sane/libsane-dc240.so
%{_libdir}/sane/libsane-dc240.la
%{_libdir}/sane/libsane-canon_pp.so.1.0.18
%{_libdir}/sane/libsane-canon_pp.so.1
%{_libdir}/sane/libsane-canon_pp.so
%{_libdir}/sane/libsane-canon_pp.la
%{_libdir}/sane/libsane-hpsj5s.so.1.0.18
%{_libdir}/sane/libsane-hpsj5s.so.1
%{_libdir}/sane/libsane-hpsj5s.so
%{_libdir}/sane/libsane-hpsj5s.la
%{_libdir}/sane/libsane-mustek_pp.so.1.0.18
%{_libdir}/sane/libsane-mustek_pp.so.1
%{_libdir}/sane/libsane-mustek_pp.so
%{_libdir}/sane/libsane-mustek_pp.la
%{_libdir}/sane/libsane-dell1600n_net.so.1.0.18
%{_libdir}/sane/libsane-qcam.so.1
%{_libdir}/sane/libsane-dell1600n_net.so.1
%{_libdir}/sane/libsane-dell1600n_net.so
%{_libdir}/sane/libsane-dell1600n_net.la
%{_libdir}/sane/libsane-qcam.so.1.0.18
%{_libdir}/sane/libsane-qcam.so
%{_libdir}/sane/libsane-qcam.la
%{_libdir}/sane/libsane-v4l.so.1.0.18
%{_libdir}/sane/libsane-v4l.so.1
%{_libdir}/sane/libsane-v4l.so
%{_libdir}/sane/libsane-v4l.la
%{_libdir}/sane/libsane-net.so.1.0.18
%{_libdir}/sane/libsane-net.so.1
%{_libdir}/sane/libsane-net.so
%{_libdir}/sane/libsane-net.la
%{_libdir}/sane/libsane-mustek_usb2.so.1.0.18
%{_libdir}/sane/libsane-mustek_usb2.so.1
%{_libdir}/sane/libsane-mustek_usb2.so
%{_libdir}/sane/libsane-mustek_usb2.la
%{_libdir}/sane/libsane-dll.so.1.0.18
%{_libdir}/sane/libsane-dll.so.1
%{_libdir}/sane/libsane-dll.so
%{_libdir}/sane/libsane-dll.la
%{_libdir}/libsane.so.1.0.18
%{_libdir}/libsane.so.1
%{_libdir}/libsane.so
%{_libdir}/libsane.la
%{_datadir}/locale/bg/LC_MESSAGES/sane-backends.mo
%{_datadir}/locale/cs/LC_MESSAGES/sane-backends.mo
%{_datadir}/locale/da/LC_MESSAGES/sane-backends.mo
%{_datadir}/locale/de/LC_MESSAGES/sane-backends.mo
%{_datadir}/locale/es/LC_MESSAGES/sane-backends.mo
%{_datadir}/locale/fi/LC_MESSAGES/sane-backends.mo
%{_datadir}/locale/fr/LC_MESSAGES/sane-backends.mo
%{_datadir}/locale/it/LC_MESSAGES/sane-backends.mo
%{_datadir}/locale/nl/LC_MESSAGES/sane-backends.mo
%{_datadir}/locale/no/LC_MESSAGES/sane-backends.mo
%{_datadir}/locale/pl/LC_MESSAGES/sane-backends.mo
%{_datadir}/locale/pt/LC_MESSAGES/sane-backends.mo
%{_datadir}/locale/ru/LC_MESSAGES/sane-backends.mo
%{_datadir}/locale/sv/LC_MESSAGES/sane-backends.mo
%{_bindir}/scanimage
%{_bindir}/sane-config
%{_bindir}/sane-find-scanner
%{_bindir}/gamma4scanimage
%{_sbindir}/saned
%{_mandir}/man1/sane-find-scanner.1.gz
%{_mandir}/man1/gamma4scanimage.1.gz
%{_mandir}/man1/scanimage.1.gz
%{_mandir}/man1/sane-config.1.gz
%{_mandir}/man5/sane-apple.5.gz
%{_mandir}/man5/sane-as6e.5.gz
%{_mandir}/man5/sane-dll.5.gz
%{_mandir}/man5/sane-dc25.5.gz
%{_mandir}/man5/sane-dmc.5.gz
%{_mandir}/man5/sane-epson.5.gz
%{_mandir}/man5/sane-hp.5.gz
%{_mandir}/man5/sane-leo.5.gz
%{_mandir}/man5/sane-lexmark.5.gz
%{_mandir}/man5/sane-matsushita.5.gz
%{_mandir}/man5/sane-microtek.5.gz
%{_mandir}/man5/sane-microtek2.5.gz
%{_mandir}/man5/sane-mustek.5.gz
%{_mandir}/man5/sane-nec.5.gz
%{_mandir}/man5/sane-net.5.gz
%{_mandir}/man5/sane-pie.5.gz
%{_mandir}/man5/sane-pnm.5.gz
%{_mandir}/man5/sane-umax.5.gz
%{_mandir}/man5/sane-qcam.5.gz
%{_mandir}/man5/sane-scsi.5.gz
%{_mandir}/man5/sane-artec.5.gz
%{_mandir}/man5/sane-sharp.5.gz
%{_mandir}/man5/sane-s9036.5.gz
%{_mandir}/man5/sane-tamarack.5.gz
%{_mandir}/man5/sane-ricoh.5.gz
%{_mandir}/man5/sane-avision.5.gz
%{_mandir}/man5/sane-st400.5.gz
%{_mandir}/man5/sane-mustek_pp.5.gz
%{_mandir}/man5/sane-dc210.5.gz
%{_mandir}/man5/sane-v4l.5.gz
%{_mandir}/man5/sane-snapscan.5.gz
%{_mandir}/man5/sane-canon.5.gz
%{_mandir}/man5/sane-bh.5.gz
%{_mandir}/man5/sane-dc240.5.gz
%{_mandir}/man5/sane-umax_pp.5.gz
%{_mandir}/man5/sane-umax1220u.5.gz
%{_mandir}/man5/sane-sm3600.5.gz
%{_mandir}/man5/sane-usb.5.gz
%{_mandir}/man5/sane-sceptre.5.gz
%{_mandir}/man5/sane-mustek_usb.5.gz
%{_mandir}/man5/sane-canon_pp.5.gz
%{_mandir}/man5/sane-teco1.5.gz
%{_mandir}/man5/sane-teco2.5.gz
%{_mandir}/man5/sane-teco3.5.gz
%{_mandir}/man5/sane-test.5.gz
%{_mandir}/man5/sane-sp15c.5.gz
%{_mandir}/man5/sane-coolscan2.5.gz
%{_mandir}/man5/sane-hpsj5s.5.gz
%{_mandir}/man5/sane-gt68xx.5.gz
%{_mandir}/man5/sane-ma1509.5.gz
%{_mandir}/man5/sane-ibm.5.gz
%{_mandir}/man5/sane-hp5400.5.gz
%{_mandir}/man5/sane-plustek_pp.5.gz
%{_mandir}/man5/sane-u12.5.gz
%{_mandir}/man5/sane-niash.5.gz
%{_mandir}/man5/sane-sm3840.5.gz
%{_mandir}/man5/sane-genesys.5.gz
%{_mandir}/man5/sane-hp4200.5.gz
%{_mandir}/man5/sane-mustek_usb2.5.gz
%{_mandir}/man5/sane-hp3500.5.gz
%{_mandir}/man5/sane-pixma.5.gz
%{_mandir}/man5/sane-stv680.5.gz
%{_mandir}/man5/sane-abaton.5.gz
%{_mandir}/man5/sane-agfafocus.5.gz
%{_mandir}/man5/sane-gphoto2.5.gz
%{_mandir}/man5/sane-pint.5.gz
%{_mandir}/man5/sane-fujitsu.5.gz
%{_mandir}/man5/sane-plustek.5.gz
%{_mandir}/man5/sane-coolscan.5.gz
%{_mandir}/man5/sane-canon630u.5.gz
%{_mandir}/man5/sane-artec_eplus48u.5.gz
%{_mandir}/man7/sane.7.gz
%{_mandir}/man8/saned.8.gz
%{_docdir}/%{name}-%{version}/README
%{_docdir}/%{name}-%{version}/AUTHORS
%{_docdir}/%{name}-%{version}/COPYING
%{_docdir}/%{name}-%{version}/ChangeLog
%{_docdir}/%{name}-%{version}/LICENSE
%{_docdir}/%{name}-%{version}/NEWS
%{_docdir}/%{name}-%{version}/PROBLEMS
%{_docdir}/%{name}-%{version}/PROJECTS
%{_docdir}/%{name}-%{version}/README.aix
%{_docdir}/%{name}-%{version}/README.beos
%{_docdir}/%{name}-%{version}/README.darwin
%{_docdir}/%{name}-%{version}/README.freebsd
%{_docdir}/%{name}-%{version}/README.djpeg
%{_docdir}/%{name}-%{version}/README.hp-ux
%{_docdir}/%{name}-%{version}/README.linux
%{_docdir}/%{name}-%{version}/README.netbsd
%{_docdir}/%{name}-%{version}/README.openbsd
%{_docdir}/%{name}-%{version}/README.os2
%{_docdir}/%{name}-%{version}/README.solaris
%{_docdir}/%{name}-%{version}/README.unixware2
%{_docdir}/%{name}-%{version}/README.unixware7
%{_docdir}/%{name}-%{version}/README.windows
%{_docdir}/%{name}-%{version}/README.zeta
%{_docdir}/%{name}-%{version}/canon/canon.changes
%{_docdir}/%{name}-%{version}/canon/canon.install2700F.txt
%{_docdir}/%{name}-%{version}/leo/leo.txt
%{_docdir}/%{name}-%{version}/matsushita/matsushita.txt
%{_docdir}/%{name}-%{version}/mustek/mustek.CHANGES
%{_docdir}/%{name}-%{version}/mustek_usb/mustek_usb.CHANGES
%{_docdir}/%{name}-%{version}/mustek_usb/mustek_usb.TODO
%{_docdir}/%{name}-%{version}/plustek/FAQ
%{_docdir}/%{name}-%{version}/plustek/MakeModule.sh
%{_docdir}/%{name}-%{version}/plustek/Makefile.kernel24
%{_docdir}/%{name}-%{version}/plustek/Makefile.kernel26
%{_docdir}/%{name}-%{version}/plustek/Plustek-PARPORT-TODO.txt
%{_docdir}/%{name}-%{version}/plustek/Plustek-PARPORT.changes
%{_docdir}/%{name}-%{version}/plustek/Plustek-PARPORT.txt
%{_docdir}/%{name}-%{version}/plustek/Plustek-USB-TODO.txt
%{_docdir}/%{name}-%{version}/plustek/Plustek-USB.changes
%{_docdir}/%{name}-%{version}/plustek/Plustek-USB.txt
%{_docdir}/%{name}-%{version}/u12/U12.changes
%{_docdir}/%{name}-%{version}/u12/U12.todo
%{_docdir}/%{name}-%{version}/umax/negative-types.txt
%{_docdir}/%{name}-%{version}/umax/sane-logo.jpg
%{_docdir}/%{name}-%{version}/umax/sane-umax-advanced-options-doc.html
%{_docdir}/%{name}-%{version}/umax/sane-umax-advanced.jpg
%{_docdir}/%{name}-%{version}/umax/sane-umax-astra-doc.html
%{_docdir}/%{name}-%{version}/umax/sane-umax-config-doc.html
%{_docdir}/%{name}-%{version}/umax/sane-umax-doc.html
%{_docdir}/%{name}-%{version}/umax/sane-umax-histogram.jpg
%{_docdir}/%{name}-%{version}/umax/sane-umax-mirage-doc.html
%{_docdir}/%{name}-%{version}/umax/sane-umax-not-listed-doc.html
%{_docdir}/%{name}-%{version}/umax/sane-umax-others-doc.html
%{_docdir}/%{name}-%{version}/umax/sane-umax-parport-doc.html
%{_docdir}/%{name}-%{version}/umax/sane-umax-powerlook-doc.html
%{_docdir}/%{name}-%{version}/umax/sane-umax-scanner-clones-doc.html
%{_docdir}/%{name}-%{version}/umax/sane-umax-speed-doc.html
%{_docdir}/%{name}-%{version}/umax/sane-umax-standard-options-doc.html
%{_docdir}/%{name}-%{version}/umax/sane-umax-standard.jpg
%{_docdir}/%{name}-%{version}/umax/sane-umax-text.jpg
%{_docdir}/%{name}-%{version}/umax/sane-umax-text2.jpg
%{_docdir}/%{name}-%{version}/umax/sane-umax-text4.jpg
%{_docdir}/%{name}-%{version}/umax/sane-umax-uc-doc.html
%{_docdir}/%{name}-%{version}/umax/sane-umax-vista-doc.html
%{_docdir}/%{name}-%{version}/umax/sane-umax.jpg
%{_docdir}/%{name}-%{version}/umax/umax.BUGS
%{_docdir}/%{name}-%{version}/umax/umax.CHANGES
%{_docdir}/%{name}-%{version}/umax/umax.FAQ
%{_docdir}/%{name}-%{version}/umax/umax.TODO
%{_docdir}/%{name}-%{version}/sceptre/s1200.txt
%{_docdir}/%{name}-%{version}/teco/teco1.txt
%{_docdir}/%{name}-%{version}/teco/teco2.txt
%{_docdir}/%{name}-%{version}/teco/teco3.txt
%{_docdir}/%{name}-%{version}/gt68xx/gt68xx.CHANGES
%{_docdir}/%{name}-%{version}/gt68xx/gt68xx.TODO
%{_docdir}/%{name}-%{version}/niash/niash.TODO
%{_docdir}/%{name}-%{version}/mustek_usb2/mustek_usb2.CHANGES
%{_docdir}/%{name}-%{version}/mustek_usb2/mustek_usb2.TODO
%{_docdir}/%{name}-%{version}/backend-writing.txt
%{_docdir}/%{name}-%{version}/sane.ps
%{_docdir}/%{name}-%{version}/sane.dvi
%{_docdir}/%{name}-%{version}/sane-backends.html
%{_docdir}/%{name}-%{version}/sane-backends-external.html
%{_docdir}/%{name}-%{version}/sane-mfgs.html
%{_docdir}/%{name}-%{version}/sane-mfgs-external.html
%{_sysconfdir}/udev/rules.d/90-sane-backends.rules
%config %{_sysconfdir}/sane.d/abaton.conf
%config %{_sysconfdir}/sane.d/agfafocus.conf
%config %{_sysconfdir}/sane.d/apple.conf
%config %{_sysconfdir}/sane.d/artec.conf
%config %{_sysconfdir}/sane.d/avision.conf
%config %{_sysconfdir}/sane.d/bh.conf
%config %{_sysconfdir}/sane.d/canon.conf
%config %{_sysconfdir}/sane.d/canon630u.conf
%config %{_sysconfdir}/sane.d/coolscan.conf
%config %{_sysconfdir}/sane.d/coolscan2.conf
%config %{_sysconfdir}/sane.d/dc25.conf
%config %{_sysconfdir}/sane.d/dmc.conf
%config %{_sysconfdir}/sane.d/epson.conf
%config %{_sysconfdir}/sane.d/fujitsu.conf
%config %{_sysconfdir}/sane.d/genesys.conf
%config %{_sysconfdir}/sane.d/gt68xx.conf
%config %{_sysconfdir}/sane.d/hp.conf
%config %{_sysconfdir}/sane.d/leo.conf
%config %{_sysconfdir}/sane.d/lexmark.conf
%config %{_sysconfdir}/sane.d/matsushita.conf
%config %{_sysconfdir}/sane.d/microtek.conf
%config %{_sysconfdir}/sane.d/microtek2.conf
%config %{_sysconfdir}/sane.d/mustek.conf
%config %{_sysconfdir}/sane.d/mustek_usb.conf
%config %{_sysconfdir}/sane.d/nec.conf
%config %{_sysconfdir}/sane.d/pie.conf
%config %{_sysconfdir}/sane.d/plustek.conf
%config %{_sysconfdir}/sane.d/plustek_pp.conf
%config %{_sysconfdir}/sane.d/ricoh.conf
%config %{_sysconfdir}/sane.d/s9036.conf
%config %{_sysconfdir}/sane.d/sceptre.conf
%config %{_sysconfdir}/sane.d/sharp.conf
%config %{_sysconfdir}/sane.d/sp15c.conf
%config %{_sysconfdir}/sane.d/st400.conf
%config %{_sysconfdir}/sane.d/tamarack.conf
%config %{_sysconfdir}/sane.d/test.conf
%config %{_sysconfdir}/sane.d/teco1.conf
%config %{_sysconfdir}/sane.d/teco2.conf
%config %{_sysconfdir}/sane.d/teco3.conf
%config %{_sysconfdir}/sane.d/umax.conf
%config %{_sysconfdir}/sane.d/umax_pp.conf
%config %{_sysconfdir}/sane.d/umax1220u.conf
%config %{_sysconfdir}/sane.d/artec_eplus48u.conf
%config %{_sysconfdir}/sane.d/ma1509.conf
%config %{_sysconfdir}/sane.d/ibm.conf
%config %{_sysconfdir}/sane.d/hp5400.conf
%config %{_sysconfdir}/sane.d/u12.conf
%config %{_sysconfdir}/sane.d/snapscan.conf
%config %{_sysconfdir}/sane.d/v4l.conf
%config %{_sysconfdir}/sane.d/sm3840.conf
%config %{_sysconfdir}/sane.d/hp4200.conf
%config %{_sysconfdir}/sane.d/stv680.conf
%config %{_sysconfdir}/sane.d/dc210.conf
%config %{_sysconfdir}/sane.d/dc240.conf
%config %{_sysconfdir}/sane.d/canon_pp.conf
%config %{_sysconfdir}/sane.d/hpsj5s.conf
%config %{_sysconfdir}/sane.d/mustek_pp.conf
%config %{_sysconfdir}/sane.d/qcam.conf
%config %{_sysconfdir}/sane.d/net.conf
%config %{_sysconfdir}/sane.d/dll.conf
%config %{_sysconfdir}/sane.d/saned.conf
