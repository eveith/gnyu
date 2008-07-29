Name: libxslt
Version: 1.1.22
Release: 2ev
Summary: Library providing the Gnome XSLT engine
URL: http://xmlsoft.org/XSLT/
Group: System Environment/Libraries
License: MIT
Vendor: GNyU-Linux
Source: ftp://xmlsoft.org/libxslt/%{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root
BuildRequires(build,prep,install): coreutils
BuildRequires(build,install): make, python, pkg-config
BuildRequires(build): gcc, libxml2 >= 2.6.17, libgcrypt

%description
This C library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism. To use it you need to have a version of libxml2 >= 2.6.27
installed. The xsltproc command is a command line interface to the XSLT engine


%package python
%define _python_version %(python -c "import sys; print sys.version[0:3]")
Summary: Python bindings for the libxslt library
Group: Development/Libraries
Requires: libxslt = %{version}
Requires: libxml2-python >= 2.6.17
Requires: %{_libdir}/python%{_python_version}

%description python
The libxslt-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libxslt library to apply XSLT transformations.

This library allows to parse sytlesheets, uses the libxml2-python
to load and save XML and HTML files. Direct access to XPath and
the XSLT transformation context are possible to extend the XSLT language
with XPath functions written in Python.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}
gzip -9 ChangeLog


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__make_install} \
	DESTDIR='%{buildroot}' \
	HTML_DIR='%{_docdir}' \
	DOCS_DIR='%{_docdir}/%{name}-python-%{version}'
%{__rm} -f ${RPM_BUILD_ROOT}/%{_infodir}/dir
%{__rm} -rf ${RPM_BUILD_ROOT}/%{_datadir}/doc


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog.gz NEWS README Copyright TODO FEATURES
%doc doc/*.html doc/html doc/tutorial doc/tutorial2 doc/*.gif
%doc doc/EXSLT
%doc doc/libxslt-api.xml
%doc doc/libxslt-refs.xml
%doc doc/EXSLT/libexslt-api.xml
%doc doc/EXSLT/libexslt-refs.xml
%doc %{_mandir}/man1/xsltproc.1*
%doc %{_mandir}/man3/libxslt.3*
%doc %{_mandir}/man3/libexslt.3*
%{_libdir}/libxslt-plugins
%{_bindir}/xsltproc
%{_datadir}/aclocal/libxslt.m4
%{_bindir}/xslt-config
%{_libdir}/libexslt.*
%{_libdir}/libxslt.*
%{_libdir}/xsltConf.sh
%{_libdir}/pkgconfig/libxslt.pc
%{_libdir}/pkgconfig/libexslt.pc
%{_includedir}/libexslt
%{_includedir}/libxslt

%files python
%defattr(-, root, root)
%doc AUTHORS ChangeLog.gz NEWS README Copyright FEATURES
%doc python/TODO
%doc python/libxsltclass.txt
%doc python/tests/*.py
%doc python/tests/*.xml
%doc python/tests/*.xsl
%{_libdir}/python*/site-packages/libxslt.py*
%{_libdir}/python*/site-packages/libxsltmod*
