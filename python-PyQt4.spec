Name: python-PyQt4
Version: 4.5.1
Release: 1ev
Summary: Python bindings to the Qt GUI toolkit
URL: http://www.riverbankcomputing.co.uk/software/pyqt/
Group: System Environment/Libraries
License: GPL-2/GPL-3
Vendor: GNyU-Linux
Source: http://www.riverbankcomputing.co.uk/static/Downloads/PyQt4/PyQt-x11-gpl-%{version}.tar.gz
BuildRequires: python, make, gcc-g++, python-sip, qt4

%description
PyQt is a set of Python bindings for Nokia's Qt application framework and runs
on all platforms supported by Qt including Windows, MacOS/X and Linux.


%prep
	%setup -q -n 'PyQt-x11-gpl-%{version}'


%build
	echo 'yes' | %{__python} configure.py \
		CFLAGS="${CFLAGS:-%{optflags}}" \
		CXXFLAGS="${CXXFLAGS:-%{optflags}}" \
		CC="${CC:-%{_target_platform}-gcc}" \
		CXX="${CXX:-%{_target_platform}-g++}"
	%{__make} %{?_smp_mflags}


%install
	%{__make} install DESTDIR='%{buildroot}'



%files
	%defattr(-, root, root)
	%doc LICENSE* GPL* ChangeLog NEWS OPENSOURCE-NOTICE.TXT README THANKS
	%{_bindir}/pylupdate4
	%{_bindir}/pyrcc4
	%{_bindir}/pyuic4
	%{python_sitelib}/PyQt4/
	%dir %{_datadir}/sip/PyQt4
	%dir %{_datadir}/sip/PyQt4/Qt
	%dir %{_datadir}/sip/PyQt4/QtCore
	%dir %{_datadir}/sip/PyQt4/QtDesigner
	%dir %{_datadir}/sip/PyQt4/QtGui
	%dir %{_datadir}/sip/PyQt4/QtHelp
	%dir %{_datadir}/sip/PyQt4/QtNetwork
	%dir %{_datadir}/sip/PyQt4/QtOpenGL
	%dir %{_datadir}/sip/PyQt4/QtScript
	%dir %{_datadir}/sip/PyQt4/QtScriptTools
	%dir %{_datadir}/sip/PyQt4/QtSql
	%dir %{_datadir}/sip/PyQt4/QtSvg
	%dir %{_datadir}/sip/PyQt4/QtTest
	%dir %{_datadir}/sip/PyQt4/QtWebKit
	%dir %{_datadir}/sip/PyQt4/QtXml
	%{_datadir}/sip/PyQt4/*/*
