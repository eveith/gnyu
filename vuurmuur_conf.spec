Name: vuurmuur_conf
Version: 0.7
Release: 3.0ev
Summary: A ncurses-based text user interface to Vuurmuur
URL: http://www.vuurmuur.org/
Group: Applications/Internet
License: GPL-2
Vendor: GNyU-Linux
Source0: ftp://ftp.vuurmuur.org/releases/0.7/Vuurmuur-%{version}.tar.gz
Source1: %{name}-vuurmuur_conf.conf
BuildRequires: make, gcc, gettext
BuildRequires: ncurses, libvuurmuur-devel = %{version}

%description
vuurmuur_conf allows simple console interaction with the vuurmuur daemons. It
is suited for an easy, graphical configuration of your firewall rules.


%prep
%setup -q -n 'Vuurmuur-%{version}'
%{__gzip} -dc 'vuurmuur_conf-%{version}.tar.gz' | %{__tar} -x
%setup -D -T -n 'Vuurmuur-%{version}/vuurmuur_conf-%{version}'


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR='%{buildroot}'
%find_lang vuurmuur_conf

%{__mkdir_p} '%{buildroot}%{_sysconfdir}'
%{__cp} '%{SOURCE1}' '%{buildroot}%{_sysconfdir}/vuurmuur_conf.conf'


%files -f vuurmuur_conf.lang
%defattr(-, root, root)
%doc ABOUT-NLS AUTHORS ChangeLog COPYING NEWS README TODO
%attr(0640, root, root) %config(noreplace) 	%{_sysconfdir}/vuurmuur_conf.conf
%attr(0750, root, root) %{_bindir}/vuurmuur_conf
%doc %{_mandir}/man8/vuurmuur_conf.8*
%doc %{_mandir}/*/man8/vuurmuur_conf.8*
%dir %{_datadir}/vuurmuur/help
%doc %{_datadir}/vuurmuur/help/*.hlp 
%{_datadir}/vuurmuur/config/vuurmuur_conf.conf.sample
%{_datadir}/vuurmuur/scripts/vuurmuur-searchlog.sh
