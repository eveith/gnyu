Name: scons
Version: 1.0.0
Release: 1ev
Summary: A software construction tool, similar to GNU autotools/GNU make
URL: http://www.scons.org
Group: Development/Tools
License: BSD
Vendor: GNyU-Linux
Source: http://prdownloads.sourceforge.net/scons/scons-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-buildroot
BuildRequires: python >= 1.6
BuildArch: noarch

%description
This is SCons, a tool for building software (and other files).  SCons is
implemented in Python, and its "configuration files" are actually Python
scripts, allowing you to use the full power of a real scripting language
to solve build problems.  You do not, however, need to know Python to
use SCons effectively.


%prep
%setup -q


%build
%{__python} ./setup.py build


%install
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'
%{__python} ./setup.py install \
	--prefix '%{_prefix}' \
	--root '%{buildroot}'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'


%clean
[[ '%{buildroot}' != '/' ]] && %{__rm} -rf '%{buildroot}'


%files
%defattr(-, root, root)
%doc CHANGES.txt LICENSE.txt MANIFEST PKG-INFO README.txt RELEASE.txt
%{_bindir}/scons
%{_bindir}/scons-1.0.0
%{_bindir}/scons-time
%{_bindir}/scons-time-1.0.0
%{_bindir}/sconsign
%{_bindir}/sconsign-1.0.0
%{_libdir}/scons-%{version}/
%doc %{_mandir}/man1/scons-time.1*
%doc %{_mandir}/man1/scons.1*
%doc %{_mandir}/man1/sconsign.1*
