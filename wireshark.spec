Name: wireshark
Version: 1.0.3
Release: 2ev
Summary: A network traffic analyzer ("sniffer") based on GTK+2
URL: http://www.wireshark.org/
Group: Applications/System
License: GPL-2
Vendor: GNyU-Linux
Source: http://www.wireshark.org/download/src/wireshark-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: make, gcc, flex >= 2.5.1, bison, gtk2, glib2
BuildRequires: perl, gettext, openssl, heimdal-libs, zlib, pcre
BuildRequires: libgcrypt, gnutls, libpcap

%description
Wireshark is a network traffic analyzer, or "sniffer", for Unix and
Unix-like operating systems.  It uses GTK+, a graphical user interface
library, and libpcap, a packet capture and filtering library.


%prep
%setup -q


%build
%configure \
	--enable-threads \
	--enable-wireshark \
	--enable-ipv6 \
	--with-ssl \
	--with-krb5 \
	--with-pcap \
	--with-pcre
%{__make} %{?_smp_mflags}


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} DESTDIR='%{buildroot}'


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc README* AUTHORS COPYING ChangeLog FAQ NEWS
%{_bindir}/capinfos
%{_bindir}/dftest
%{_bindir}/dumpcap
%{_bindir}/editcap
%{_bindir}/idl2wrs
%{_bindir}/mergecap
%{_bindir}/randpkt
%{_bindir}/rawshark
%{_bindir}/text2pcap
%{_bindir}/tshark
%{_bindir}/wireshark
%{_libdir}/libwireshark.*
%{_libdir}/libwiretap.*
%{_libdir}/wireshark/
%{_mandir}/man1/capinfos.1*
%{_mandir}/man1/dumpcap.1*
%{_mandir}/man1/editcap.1*
%{_mandir}/man1/idl2wrs.1*
%{_mandir}/man1/mergecap.1*
%{_mandir}/man1/rawshark.1*
%{_mandir}/man1/text2pcap.1*
%{_mandir}/man1/tshark.1*
%{_mandir}/man1/wireshark.1*
%{_mandir}/man4/wireshark-filter.4*
%{_datadir}/wireshark/
