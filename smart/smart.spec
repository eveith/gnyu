Name: smart
Version: 1.3
Release: 4.0ev
Summary: A console-based package manager on top of RPM
URL: http://labix.org/smart/
Group: System Environment/Tools
License: GPL-2
Vendor: GNyU-Linux
Source: http://edge.launchpad.net/smart/trunk/1.3/+download/smart-1.3.tar.bz2
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


%package gtk
Summary: GTK+2 frontend to smart
Group: System Environment/Tools
Requires: smart = %{version}, python-gtk

%description gtk
A GTK+2-based fronted to the Smart Package Manager.
The Smart Package Manager project has the ambitious objective of creating 
smart and portable algorithms for solving adequately the problem of managing 
software upgrades and installation. This tool works in all major 
distributions and will bring notable advantages over native tools currently 
in use (APT, APT-RPM, YUM, URPMI, etc).


%package qt
Summary: Qt frontend to smart
Group: System Environment/Tools
Requires: smart = %{version}, python-qt

%description qt
A Qt-based frontend to the Smart Package Manager.
The Smart Package Manager project has the ambitious objective of creating 
smart and portable algorithms for solving adequately the problem of managing 
software upgrades and installation. This tool works in all major 
distributions and will bring notable advantages over native tools currently 
in use (APT, APT-RPM, YUM, URPMI, etc).


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
%{python_sitelib}/smart-%{version}-py*.egg-info
%dir %{python_sitelib}/smart
%dir %{python_sitelib}/smart/backends
%dir %{python_sitelib}/smart/backends/arch
%dir %{python_sitelib}/smart/backends/deb
%dir %{python_sitelib}/smart/backends/rpm
%dir %{python_sitelib}/smart/backends/slack
%dir %{python_sitelib}/smart/channels
%dir %{python_sitelib}/smart/commands
%dir %{python_sitelib}/smart/interfaces
%dir %{python_sitelib}/smart/interfaces/images
%dir %{python_sitelib}/smart/interfaces/text
%dir %{python_sitelib}/smart/util
%dir %{python_sitelib}/smart/plugins
%{python_sitelib}/smart/ccache.so
%{python_sitelib}/smart/*.py*
%{python_sitelib}/smart/backends/*.py*
%{python_sitelib}/smart/backends/arch/*.py*
%{python_sitelib}/smart/backends/deb/*.py*
%{python_sitelib}/smart/backends/deb/cdebver.so
%{python_sitelib}/smart/backends/rpm/*.py*
%{python_sitelib}/smart/backends/rpm/crpmver.so
%{python_sitelib}/smart/backends/slack/*.py*
%{python_sitelib}/smart/channels/*.py*
%{python_sitelib}/smart/commands/*.py*
%{python_sitelib}/smart/interfaces/*.py*
%{python_sitelib}/smart/interfaces/text/*.py*
%{python_sitelib}/smart/interfaces/images/*.png
%{python_sitelib}/smart/interfaces/images/*.py*
%{python_sitelib}/smart/util/*.py*
%{python_sitelib}/smart/util/cdistance.so
%{python_sitelib}/smart/util/ctagfile.so
%{python_sitelib}/smart/plugins/*.py*
%doc %{_mandir}/man8/smart.8*
%dir %attr(0700, root, root) %{_localstatedir}/lib/smart


%files gtk
%defattr(-, root, root)
%doc HACKING IDEAS LICENSE PKG-INFO README TODO
%dir %{python_sitelib}/smart/interfaces/qt
%{python_sitelib}/smart/interfaces/qt/*.py*


%files qt
%defattr(-, root, root)
%doc HACKING IDEAS LICENSE PKG-INFO README TODO
%dir %{python_sitelib}/smart/interfaces/gtk
%{python_sitelib}/smart/interfaces/gtk/*.py*
