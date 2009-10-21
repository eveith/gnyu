Name: smart
Version: 1.2
Release: 3.0ev
Summary: A console-based package manager on top of RPM
URL: http://labix.org/smart/
Group: System Environment/Tools
License: GPL-2
Vendor: GNyU-Linux
Source: http://labix.org/download/smart/smart-%{version}.tar.bz2
BuildRequires: python >= 2.3, gcc, rpm5-python

%description
The Smart Package Manager project has the ambitious objective of creating 
smart and portable algorithms for solving adequately the problem of managing 
software upgrades and installation. This tool works in all major 
distributions and will bring notable advantages over native tools currently 
in use (APT, APT-RPM, YUM, URPMI, etc).
From The Free On-line Dictionary of Computing: 
	smart
		1. <programming> Said of a program that does the {Right Thing} 
		in a wide variety of complicated circumstances. (...)


%prep
	%setup -q


%build
	CFLAGS="${CFLAGS:-%{optflags}}"; export CFLAGS
	%{__python} ./setup.py build


%install
	%{__python} ./setup.py install \
		--prefix='%{_prefix}' \
		--root='%{buildroot}'
	%find_lang smart
	%{__mv} '%{buildroot}/%{_datadir}/man' '%{buildroot}/%{_mandir}' ||:

	# These are created by smart when running
	%{__mkdir_p} '%{buildroot}/%{_localstatedir}/lib/smart'


%files -f smart.lang
	%defattr(-, root, root)
	%doc HACKING IDEAS LICENSE PKG-INFO README TODO
	%attr(0700, root, root) %{_bindir}/smart
	%{python_sitelib}/smart-1.2-py2.6.egg-info
	%dir %{python_sitelib}/smart
	%dir %{python_sitelib}/smart/backends
	%dir %{python_sitelib}/smart/backends/deb
	%dir %{python_sitelib}/smart/backends/rpm
	%dir %{python_sitelib}/smart/backends/slack
	%dir %{python_sitelib}/smart/channels
	%dir %{python_sitelib}/smart/commands
	%dir %{python_sitelib}/smart/interfaces
	%dir %{python_sitelib}/smart/interfaces/gtk
	%dir %{python_sitelib}/smart/interfaces/images
	%dir %{python_sitelib}/smart/interfaces/text
	%dir %{python_sitelib}/smart/util
	%dir %{python_sitelib}/smart/plugins
	%{python_sitelib}/smart/*.*
	%{python_sitelib}/smart/*/*.*
	%{python_sitelib}/smart/*/*/*.*
	%doc %{_mandir}/man8/smart.8*
	%dir %attr(0700, root, root) %{_localstatedir}/lib/smart
